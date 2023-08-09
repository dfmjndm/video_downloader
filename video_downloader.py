import datetime
import typing
import yt_dlp as youtube_download
from aiocqhttp.message import MessageSegment
from hoshino import Service
from moviepy.editor import *
import asyncio

cool_down = datetime.timedelta(minutes=1)  # 冷却时间
expire = datetime.timedelta(minutes=2)

temp = {}
last_check = {}

opt_path = '/youtube/' # 你的视频下载地址
aria2c = '/usr/bin/aria2c'  # 你的aria2文件位置
sv = Service('下载视频', help_='''
发送"下视频 网页地址",支持知乎微博油管twitch蓝鸟等平台
'''.strip())

async def search_youtube(youtube_link):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': f'{opt_path}%(id)s.%(ext)s',
        'proxy': 'http://127.0.0.1:20172' # 你的代理地址
    }

    with youtube_download.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(youtube_link, download=True)
        if 'entries' in result:
            return 0
        else:
            return result

async def download_video(url, ydl_opts, retry_count=3):
    for _ in range(retry_count):
        with youtube_download.YoutubeDL(ydl_opts) as ydl:
            try:
                result = ydl.extract_info(url, download=True)
                if 'entries' in result:
                    # 播放清单
                    video = result['entries'][0]
                else:
                    # 单个视频
                    video = result
                return video
            except Exception as e:
                print(f"Error downloading video: {e}")
                await asyncio.sleep(1)  # 休眠1秒
    return None

@sv.on_prefix(('下视频'))
async def fetch_info(bot, ev):
    try:
        youtube_link = [msg_seg.data['text'].strip() for msg_seg in ev.message if msg_seg.type == 'text' and msg_seg.data['text']]
        
        if not youtube_link:
            await bot.send(ev, '你想下什么呀?', at_sender=True)
        else:
            youtube_link = ''.join(youtube_link)
            video_info = await search_youtube(youtube_link)
            
            if video_info == 0:
                await bot.send(ev, '暂时不支持下载多个视频呀', at_sender=True)
            else:
                extractor = video_info['extractor']
                await bot.send(ev, f'获取{extractor}视频信息中！')
                
                id = video_info['id']
                title = video_info['title']
                uploader = video_info.get('uploader') or video_info.get('creator')
                
                msg = '标题：' + str(title) + '\n作者：' + str(uploader) +'\n请回复"音乐下载","QQ下载"'
                key = f'{ev.group_id}-{ev.user_id}'
                temp["key"] = key
                temp["youtube_link"] =  youtube_link    
                await bot.send(ev, msg)
                
    except Exception as e:
        error_msg = f'发生错误：{str(e)}'
        print(error_msg)
        # 发送不支持的链接
        unsupported_msg = '抱歉，暂时不支持该链接。'
        await bot.send(ev, unsupported_msg)

@sv.on_prefix(('QQ下载'))
async def qq_download(bot, ev):
    global temp
    key = f'{ev.group_id}-{ev.user_id}'
    if "key" not in temp:
        await bot.send(ev, '请先发送"下视频"搜索需要下载的视频哦！')
    else:
        await bot.send(ev, '请稍等片刻~,视频正在下载中')
        url = temp['youtube_link']
        print(url)
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': f'{opt_path}%(id)s.%(ext)s',
            'external_downloader': aria2c,
            'external-downloader-args': '-j 16 -x 16 -s 16 -k 1M',
            'proxy': 'http://127.0.0.1:20172' # 你的代理地址
        }

        video = await download_video(url, ydl_opts, retry_count=3)

        if video is None:
            await bot.send(ev, '视频下载失败，请稍后再试。')
            return

        id = video['id']
        file_ext = video['ext'] 
        file = f'{opt_path}{id}.{file_ext}'
        print(file)
        mv = '[CQ:video,file=file:' + str(file) + ']'
        del temp["key"]
        del temp["youtube_link"]
        await bot.send(ev, mv)

@sv.on_prefix(('音乐下载'))
async def qq_download_music(bot, ev):
    global temp
    key = f'{ev.group_id}-{ev.user_id}'
    if "key" not in temp:
        await bot.send(ev, '请先发送"下视频"搜索需要下载的视频哦！')
    else:
        await bot.send(ev, '请稍等片刻，视频正在下载中')
        url = temp['youtube_link']
        print(url)
        ydl_opts = {
            'format': 'best[ext=mp4]',
            'outtmpl': f'{opt_path}%(id)s.%(ext)s',
            'external_downloader': aria2c,
            'external-downloader-args': '-j 16 -x 16 -s 16 -k 1M',
            'proxy': 'http://127.0.0.1:20172' # 你的代理地址
        }

        video = await download_video(url, ydl_opts, retry_count=3)

        if video is None:
            await bot.send(ev, '视频下载失败，请稍后再试。')
            return

        id = video['id']
        file_ext = video['ext'] 
        file = f'{opt_path}{id}.{file_ext}'
        print(file)

        # 转码
        mp3_file = f'{opt_path}{id}.mp3'
        video_clip = VideoFileClip(file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_file)

        mv = '[CQ:record,file=file:' + mp3_file + ']'
        del temp["key"]
        del temp["youtube_link"]
        msg = '视频已下载并转换为MP3格式，即将发送'
        await bot.send(ev, msg)
        await bot.send(ev, mv)