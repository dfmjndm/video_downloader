# video_downloader
适用于Hoshino的视频下载器插件，自动下载视频发送到群

# 安装方法
查找搜索引擎，安装aria2c和ffmpeg

安装yt_dlp以及其他必要依赖(缺什么装什么)

```
pip/pip3 install yt_dlp
```

在 HoshinoBot\hoshino\modules 目录下使用以下命令拉取本项目
```
git clone https://github.com/dfmjndm/video_downloader.git
```

然后在 HoshinoBot\\hoshino\\config\\\__bot__.py 文件的 MODULES_ON 加入 video_downloader

修改video_downloader.py里面的'opt_path'为你的视频下载目录(需要预先新建)，修改'proxy'为你打算使用的http代理.

重启 HoshinoBot

# 使用方法

群内发送 下视频 视频链接

等待bot返回视频信息之后，发送 QQ下载 音乐下载

QQ下载即通过QQ文件发送视频

音乐下载即将视频的音频部分单独发送   注：视频长度过长时你可能需要开个svip才能发送声音

# 支持媒体平台

0000studio:archive
0000studio:clip
17live
17live:clip
1tv: Первый канал
20.detik.com
20min
23video
247sports
24video
3qsdn: 3Q SDN
3sat
4tube
56.com
6play
7plus
8tracks
91porn
9c9media
9gag
9now.com.au
abc.net.au
abc.net.au:iview
abc.net.au:iview:showseries
abcnews
abcnews:video
abcotvs: ABC Owned Television Stations
abcotvs:clips
AbemaTV: [abematv]
AbemaTVTitle
AcademicEarth:Course
acast
acast:channel
AcFunBangumi
AcFunVideo
ADN: [animedigitalnetwork] Anime Digital Network
AdobeConnect
adobetv
adobetv:channel
adobetv:embed
adobetv:show
adobetv:video
AdultSwim
aenetworks: A+E Networks: A&E, Lifetime, History.com, FYI Network and History Vault
aenetworks:collection
aenetworks:show
afreecatv: [afreecatv] afreecatv.com
afreecatv:live: [afreecatv] afreecatv.com
afreecatv:user
AirMozilla
AliExpressLive
AlJazeera
Allocine
AlphaPorno
Alsace20TV
Alsace20TVEmbed
Alura: [alura]
AluraCourse: [aluracourse]
Amara
AmazonStore
AMCNetworks
AmericasTestKitchen
AmericasTestKitchenSeason
AmHistoryChannel
anderetijden: npo.nl, ntr.nl, omroepwnl.nl, zapp.nl and npo3.nl
AnimalPlanet
AnimeOnDemand: [animeondemand]
ant1newsgr:article: ant1news.gr articles
ant1newsgr:embed: ant1news.gr embedded videos
ant1newsgr:watch: ant1news.gr videos
Anvato
aol.com: Yahoo screen and movies
APA
Aparat
AppleConnect
AppleDaily: 臺灣蘋果日報
ApplePodcasts
appletrailers
appletrailers:section
archive.org: archive.org video and audio
ArcPublishing
ARD
ARD:mediathek
ARDBetaMediathek
Arkena
arte.sky.it
ArteTV
ArteTVCategory
ArteTVEmbed
ArteTVPlaylist
AsianCrush
AsianCrushPlaylist
AtresPlayer: [atresplayer]
AtScaleConfEvent
ATTTechChannel
ATVAt
AudiMedia
AudioBoom
Audiodraft:custom
Audiodraft:generic
audiomack
audiomack:album
Audius: Audius.co
audius:artist: Audius.co profile/artist pages
audius:playlist: Audius.co playlists
audius:track: Audius track ID or API link. Prepend with "audius:"
AWAAN
awaan:live
awaan:season
awaan:video
AZMedien: AZ Medien videos
BaiduVideo: 百度视频
BanBye
BanByeChannel
bandaichannel
Bandcamp
Bandcamp:album
Bandcamp:user
Bandcamp:weekly
bangumi.bilibili.com: BiliBili番剧
BannedVideo
bbc: [bbc] BBC
bbc.co.uk: [bbc] BBC iPlayer
bbc.co.uk:article: BBC articles
bbc.co.uk:iplayer:episodes
bbc.co.uk:iplayer:group
bbc.co.uk:playlist
BBVTV: [bbvtv]
Beatport
Beeg
BehindKink
Bellator
BellMedia
Bet
bfi:player
bfmtv
bfmtv:article
bfmtv:live
BibelTV
Bigflix
Bigo
Bild: Bild.de
BiliBili
Bilibili category extractor
BilibiliAudio
BilibiliAudioAlbum
BilibiliChannel
BiliBiliPlayer
BiliBiliSearch: Bilibili video search; "bilisearch:" prefix (Example: "bilisearch10:running tortoise")
BiliIntl: [biliintl]
BiliIntlSeries: [biliintl]
BiliLive
BioBioChileTV
Biography
BIQLE
BitChute
BitChuteChannel
bitwave:replay
bitwave:stream
BlackboardCollaborate
BleacherReport
BleacherReportCMS
blogger.com
Bloomberg
BokeCC
BongaCams
BostonGlobe
Box
Bpb: Bundeszentrale für politische Bildung
BR: Bayerischer Rundfunk
BravoTV
Break
BreitBart
brightcove:legacy
brightcove:new
BRMediathek: Bayerischer Rundfunk Mediathek
bt:article: Bergens Tidende Articles
bt:vestlendingen: Bergens Tidende - Vestlendingen
BusinessInsider
BuzzFeed
BYUtv
CableAV
Callin
Caltrans
CAM4
Camdemy
CamdemyFolder
CamModels
CamWithHer
CanalAlpha
canalc2.tv
Canalplus: mycanal.fr and piwiplus.fr
Canvas
CanvasEen: canvas.be and een.be
CarambaTV
CarambaTVPage
CartoonNetwork
cbc.ca
cbc.ca:player
CBS
CBSInteractive
CBSLocal
CBSLocalArticle
cbsnews: CBS News
cbsnews:embed
cbsnews:livevideo: CBS News Live Videos
cbssports
cbssports:embed
CCMA
CCTV: 央视网
CDA
Cellebrite
CeskaTelevize
CGTN
channel9: Channel 9
CharlieRose
Chaturbate
Chilloutzone
Chingari
ChingariUser
chirbit
chirbit:profile
cielotv.it
Cinchcast
Cinemax
CiscoLiveSearch
CiscoLiveSession
ciscowebex: Cisco Webex
CJSW
cliphunter
Clippit
ClipRs
Clipsyndicate
CloserToTruth
CloudflareStream
Cloudy
Clubic
Clyp
cmt.com
CNBC
CNBCVideo
CNN
CNNArticle
CNNBlogs
ComedyCentral
ComedyCentralTV
CondeNast: Condé Nast media group: Allure, Architectural Digest, Ars Technica, Bon Appétit, Brides, Condé Nast, Condé Nast Traveler, Details, Epicurious, GQ, Glamour, Golf Digest, SELF, Teen Vogue, The New Yorker, Vanity Fair, Vogue, W Magazine, WIRED
CONtv
CookingChannel
Corus
Coub
CozyTV
cp24
cpac
cpac:playlist
Cracked
Crackle
Craftsy
CrooksAndLiars
CrowdBunker
CrowdBunkerChannel
crunchyroll: [crunchyroll]
crunchyroll:beta: [crunchyroll]
crunchyroll:playlist: [crunchyroll]
crunchyroll:playlist:beta: [crunchyroll]
CSpan: C-SPAN
CSpanCongress
CtsNews: 華視新聞
CTV
CTVNews
cu.ntv.co.jp: Nippon Television Network
CultureUnplugged
curiositystream: [curiositystream]
curiositystream:collections: [curiositystream]
curiositystream:series: [curiositystream]
CWTV
Cybrary: [cybrary]
CybraryCourse: [cybrary]
Daftsex
DagelijkseKost: dagelijksekost.een.be
DailyMail
dailymotion: [dailymotion]
dailymotion:playlist: [dailymotion]
dailymotion:user: [dailymotion]
DailyWire
DailyWirePodcast
damtomo:record
damtomo:video
daum.net
daum.net:clip
daum.net:playlist
daum.net:user
daystar:clip
DBTV
DctpTv
DeezerAlbum
DeezerPlaylist
defense.gouv.fr
democracynow
DestinationAmerica
DHM: Filmarchiv - Deutsches Historisches Museum
Digg
DigitalConcertHall: [digitalconcerthall] DigitalConcertHall extractor
DigitallySpeaking
Digiteka
Discovery
DiscoveryLife
DiscoveryNetworksDe
DiscoveryPlus
DiscoveryPlusIndia
DiscoveryPlusIndiaShow
DiscoveryPlusItaly
DiscoveryPlusItalyShow
Disney
DIYNetwork
dlive:stream
dlive:vod
DoodStream
Dotsub
Douyin
DouyuShow
DouyuTV: 斗鱼
DPlay
DRBonanza
Drooble
Dropbox
Dropout: [dropout]
DropoutSeason
DrTuber
drtv
drtv:live
DTube
duboku: www.duboku.io
duboku:list: www.duboku.io entire series
Dumpert
dvtv: http://video.aktualne.cz/
dw
dw:article
EaglePlatform
EbaumsWorld
EchoMsk
egghead:course: egghead.io course
egghead:lesson: egghead.io lesson
ehftv
eHow
EinsUndEinsTV: [1und1tv]
Einthusan
eitb.tv
EllenTube
EllenTubePlaylist
EllenTubeVideo
Elonet
ElPais: El País
Embedly
EMPFlix
Engadget
Epicon
EpiconSeries
Eporner
EroProfile: [eroprofile]
EroProfile:album
ertflix: ERTFLIX videos
ertflix:codename: ERTFLIX videos by codename
ertwebtv:embed: ert.gr webtv embedded videos
Escapist
ESPN
ESPNArticle
ESPNCricInfo
EsriVideo
Europa
EuropeanTour
EUScreen
EWETV: [ewetv]
ExpoTV
Expressen
ExtremeTube
EyedoTV
facebook: [facebook]
FacebookPluginsVideo
fancode:live: [fancode]
fancode:vod: [fancode]
faz.net
fc2: [fc2]
fc2:embed
fc2:live
Fczenit
Fifa
Filmmodu
filmon
filmon:channel
Filmweb
FiveThirtyEight
FiveTV
Flickr
Folketinget: Folketinget (ft.dk; Danish parliament)
FoodNetwork
FootyRoom
Formula1
FOX
FOX9
FOX9News
Foxgay
foxnews: Fox News and Fox Business Video
foxnews:article
FoxSports
fptplay: fptplay.vn
FranceCulture
FranceInter
FranceTV
francetvinfo.fr
FranceTVSite
Freesound
freespeech.org
freetv:series
FreeTvMovies
FrontendMasters: [frontendmasters]
FrontendMastersCourse: [frontendmasters]
FrontendMastersLesson: [frontendmasters]
FujiTVFODPlus7
Funimation: [funimation]
funimation:page: [funimation]
funimation:show: [funimation]
Funk
Fusion
Fux
FuyinTV
Gab
GabTV
Gaia: [gaia]
GameInformer
GameJolt
GameJoltCommunity
GameJoltGame
GameJoltGameSoundtrack
GameJoltSearch
GameJoltUser
GameSpot
GameStar
Gaskrank
Gazeta
GDCVault: [gdcvault]
GediDigital
gem.cbc.ca: [cbcgem]
gem.cbc.ca:live
gem.cbc.ca:playlist
generic: Generic downloader that works on some sites
Gettr
GettrStreaming
Gfycat
GiantBomb
Giga
GlattvisionTV: [glattvisiontv]
Glide: Glide mobile video messages (glide.me)
Globo: [globo]
GloboArticle
glomex: Glomex videos
glomex:embed: Glomex embedded videos
Go
GoDiscovery
GodTube
Gofile
Golem
goodgame:stream
google:podcasts
google:podcasts:feed
GoogleDrive
GoogleDrive:Folder
GoPro
Goshgay
GoToStage
GPUTechConf
Gronkh
gronkh:feed
gronkh:vods
Groupon
hbo
HearThisAt
Heise
HellPorno
Helsinki: helsinki.fi
HentaiStigma
hetklokhuis
hgtv.com:show
HGTVDe
HGTVUsa
HiDive: [hidive]
HistoricFilms
history:player
history:topic: History.com Topic
hitbox
hitbox:live
HitRecord
hketv: 香港教育局教育電視 (HKETV) Educational Television, Hong Kong Educational Bureau
HotNewHipHop
hotstar
hotstar:playlist
hotstar:series
Howcast
HowStuffWorks
hrfernsehen
HRTi: [hrti]
HRTiPlaylist: [hrti]
HSEProduct
HSEShow
Huajiao: 花椒直播
HuffPost: Huffington Post
Hungama
HungamaAlbumPlaylist
HungamaSong
huya:live: huya.com
Hypem
Hytale
Icareus
ign.com
IGNArticle
IGNVideo
IHeartRadio
iheartradio:podcast
imdb: Internet Movie Database trailers
imdb:list: Internet Movie Database lists
Imgur
imgur:album
imgur:gallery
Ina
Inc
IndavideoEmbed
InfoQ
Instagram: [instagram]
instagram:story: [instagram]
instagram:tag: [instagram] Instagram hashtag search URLs
instagram:user: [instagram] Instagram user profile
InstagramIOS: IOS instagram:// URL
Internazionale
InternetVideoArchive
InvestigationDiscovery
IPrima: [iprima]
IPrimaCNN
iq.com: International version of iQiyi
iq.com:album
iqiyi: [iqiyi] 爱奇艺
ITProTV
ITProTVCourse
ITTF
ITV
ITVBTCC
ivi: ivi.ru
ivi:compilation: ivi.ru compilations
ivideon: Ivideon TV
Iwara
iwara:playlist
iwara:user
Ixigua
Izlesene
Jable
JablePlaylist
Jamendo
JamendoAlbum
JeuxVideo
Joj
Jove
JWPlatform
Kakao
Kaltura
Karaoketv
KarriereVideos
Katsomo
KeezMovies
KelbyOne
Ketnet
khanacademy
khanacademy:unit
Kicker
KickStarter
KinjaEmbed
KinoPoisk
KonserthusetPlay
Koo
KrasView: Красвью
KTH
Ku6
KUSI
kuwo:album: 酷我音乐 - 专辑
kuwo:category: 酷我音乐 - 分类
kuwo:chart: 酷我音乐 - 排行榜
kuwo:mv: 酷我音乐 - MV
kuwo:singer: 酷我音乐 - 歌手
kuwo:song: 酷我音乐
la7.it
la7.it:pod:episode
la7.it:podcast
laola1tv
laola1tv:embed
LastFM
LastFMPlaylist
LastFMUser
lbry
lbry:channel
LCI
Lcp
LcpPlay
Le: 乐视网
Lecture2Go
Lecturio: [lecturio]
LecturioCourse: [lecturio]
LecturioDeCourse: [lecturio]
LEGO
Lemonde
Lenta
LePlaylist
LetvCloud: 乐视云
Libsyn
life: Life.ru
life:embed
likee
likee:user
limelight
limelight:channel
limelight:channel_list
LineLive
LineLiveChannel
LinkedIn: [linkedin]
linkedin:learning: [linkedin]
linkedin:learning:course: [linkedin]
LinuxAcademy: [linuxacademy]
Liputan6
LiTV
LiveJournal
livestream
livestream:original
Livestreamfails
Lnk
LnkGo
loc: Library of Congress
LocalNews8
LoveHomePorn
LRTStream
LRTVOD
lynda: [lynda] lynda.com videos
lynda:course: [lynda] lynda.com online courses
m6
MagentaMusik360
mailru: Видео@Mail.Ru
mailru:music: Музыка@Mail.Ru
mailru:music:search: Музыка@Mail.Ru
MainStreaming: MainStreaming Player
MallTV
mangomolo:live
mangomolo:video
MangoTV: 芒果TV
ManotoTV: Manoto TV (Episode)
ManotoTVLive: Manoto TV (Live)
ManotoTVShow: Manoto TV (Show)
ManyVids
MaoriTV
Markiza
MarkizaPage
massengeschmack.tv
Masters
MatchTV
MDR: MDR.DE and KiKA
MedalTV
media.ccc.de
media.ccc.de:lists
Mediaite
MediaKlikk
Medialaan
Mediaset
MediasetShow
Mediasite
MediasiteCatalog
MediasiteNamedCatalog
Medici
megaphone.fm: megaphone.fm embedded players
megatvcom: megatv.com videos
megatvcom:embed: megatv.com embedded videos
Meipai: 美拍
MelonVOD
META
metacafe
Metacritic
mewatch
Mgoon
MiaoPai
microsoftstream: Microsoft Stream
mildom: Record ongoing live by specific user in Mildom
mildom:clip: Clip in Mildom
mildom:user:vod: Download all VODs from specific user in Mildom
mildom:vod: VOD in Mildom
minds
minds:channel
minds:group
MinistryGrid
Minoto
miomio.tv
mirrativ
mirrativ:user
MirrorCoUK
MiTele: mitele.es
mixch
mixch:archive
mixcloud
mixcloud:playlist
mixcloud:user
MLB
MLBVideo
MLSSoccer
Mnet
MNetTV: [mnettv]
MochaVideo
MoeVideo: LetitBit video services: moevideo.net, playreplay.net and videochart.net
Mofosex
MofosexEmbed
Mojvideo
Morningstar: morningstar.com
Motherless
MotherlessGroup
Motorsport: motorsport.com
MovieClips
MovieFap
Moviepilot
Moviezine
MovingImage
MSN
mtg: MTG services
mtv
mtv.de
mtv.it
mtv.it:programma
mtv:video
mtvjapan
mtvservices:embedded
MTVUutisetArticle
MuenchenTV: münchen.tv
Murrtube
MurrtubeUser: Murrtube user profile
MuseScore
MusicdexAlbum
MusicdexArtist
MusicdexPlaylist
MusicdexSong
mva: Microsoft Virtual Academy videos
mva:course: Microsoft Virtual Academy courses
Mwave
MwaveMeetGreet
Mxplayer
MxplayerShow
MyChannels
MySpace
MySpace:album
MySpass
Myvi
MyVideoGe
MyVidster
MyviEmbed
n-tv.de
N1Info:article
N1InfoAsset
Nate
NateProgram
natgeo:video
NationalGeographicTV
Naver
Naver:live
navernow
NBA
nba:watch
nba:watch:collection
NBAChannel
NBAEmbed
NBAWatchEmbed
NBC
NBCNews
nbcolympics
nbcolympics:stream
NBCSports
NBCSportsStream
NBCSportsVPlayer
ndr: NDR.de - Norddeutscher Rundfunk
ndr:embed
ndr:embed:base
NDTV
Nebula: [watchnebula]
nebula:channel: [watchnebula]
nebula:subscriptions: [watchnebula]
NerdCubedFeed
netease:album: 网易云音乐 - 专辑
netease:djradio: 网易云音乐 - 电台
netease:mv: 网易云音乐 - MV
netease:playlist: 网易云音乐 - 歌单
netease:program: 网易云音乐 - 电台节目
netease:singer: 网易云音乐 - 歌手
netease:song: 网易云音乐
NetPlus: [netplus]
Netverse
NetversePlaylist
Netzkino
Newgrounds
Newgrounds:playlist
Newgrounds:user
Newstube
Newsy
NextMedia: 蘋果日報
NextMediaActionNews: 蘋果日報 - 動新聞
NextTV: 壹電視
Nexx
NexxEmbed
NFB
NFHSNetwork
NhkForSchoolBangumi
NhkForSchoolProgramList
NhkForSchoolSubject: Portal page for each school subjects, like Japanese (kokugo, 国語) or math (sansuu/suugaku or 算数・数学)
NhkVod
NhkVodProgram
nhl.com
nick.com
nick.de
nickelodeon:br
nickelodeonru
nicknight
niconico: [niconico] ニコニコ動画
niconico:history: NicoNico user history. Requires cookies.
niconico:playlist
niconico:series
niconico:tag: NicoNico video tag URLs
NiconicoUser
nicovideo:search: Nico video search; "nicosearch:" prefix (Example: "nicosearch:running tortoise")
nicovideo:search:date: Nico video search, newest first; "nicosearchdate:" prefix (Example: "nicosearchdate:falling cat")
nicovideo:search_url: Nico video search URLs
Nintendo
Nitter
njoy: N-JOY
njoy:embed
NJPWWorld: [njpwworld] 新日本プロレスワールド
NobelPrize
NonkTube
NoodleMagazine
Noovo
Normalboots
NosVideo
Nova: TN.cz, Prásk.tv, Nova.cz, Novaplus.cz, FANDA.tv, Krásná.cz and Doma.cz
NovaEmbed
NovaPlay
nowness
nowness:playlist
nowness:series
Noz
npo: npo.nl, ntr.nl, omroepwnl.nl, zapp.nl and npo3.nl
npo.nl:live
npo.nl:radio
npo.nl:radio:fragment
Npr
NRK
NRKPlaylist
NRKRadioPodkast
NRKSkole: NRK Skole
NRKTV: NRK TV and NRK Radio
NRKTVDirekte: NRK TV Direkte and NRK Radio Direkte
NRKTVEpisode
NRKTVEpisodes
NRKTVSeason
NRKTVSeries
NRLTV
ntv.ru
Nuvid
NYTimes
NYTimesArticle
NYTimesCooking
nzherald
NZZ
ocw.mit.edu
OdaTV
Odnoklassniki
OktoberfestTV
OlympicsReplay
on24: ON24
OnDemandKorea
OneFootball
onet.pl
onet.tv
onet.tv:channel
OnetMVP
OnionStudios
Ooyala
OoyalaExternal
Opencast
OpencastPlaylist
openrec
openrec:capture
openrec:movie
OraTV
orf:burgenland: Radio Burgenland
orf:fm4: radio FM4
orf:fm4:story: fm4.orf.at stories
orf:iptv: iptv.ORF.at
orf:kaernten: Radio Kärnten
orf:noe: Radio Niederösterreich
orf:oberoesterreich: Radio Oberösterreich
orf:oe1: Radio Österreich 1
orf:oe3: Radio Österreich 3
orf:salzburg: Radio Salzburg
orf:steiermark: Radio Steiermark
orf:tirol: Radio Tirol
orf:tvthek: ORF TVthek
orf:vorarlberg: Radio Vorarlberg
orf:wien: Radio Wien
OsnatelTV: [osnateltv]
OutsideTV
PacktPub: [packtpub]
PacktPubCourse
PalcoMP3:artist
PalcoMP3:song
PalcoMP3:video
pandora.tv: 판도라TV
Panopto
PanoptoList
PanoptoPlaylist
ParamountNetwork
ParamountPlus
ParamountPlusSeries
parliamentlive.tv: UK parliament videos
Parlview
Patreon
PatreonUser
pbs: Public Broadcasting Service (PBS) and member stations: PBS: Public Broadcasting Service, APT - Alabama Public Television (WBIQ), GPB/Georgia Public Broadcasting (WGTV), Mississippi Public Broadcasting (WMPN), Nashville Public Television (WNPT), WFSU-TV (WFSU), WSRE (WSRE), WTCI (WTCI), WPBA/Channel 30 (WPBA), Alaska Public Media (KAKM), Arizona PBS (KAET), KNME-TV/Channel 5 (KNME), Vegas PBS (KLVX), AETN/ARKANSAS ETV NETWORK (KETS), KET (WKLE), WKNO/Channel 10 (WKNO), LPB/LOUISIANA PUBLIC BROADCASTING (WLPB), OETA (KETA), Ozarks Public Television (KOZK), WSIU Public Broadcasting (WSIU), KEET TV (KEET), KIXE/Channel 9 (KIXE), KPBS San Diego (KPBS), KQED (KQED), KVIE Public Television (KVIE), PBS SoCal/KOCE (KOCE), ValleyPBS (KVPT), CONNECTICUT PUBLIC TELEVISION (WEDH), KNPB Channel 5 (KNPB), SOPTV (KSYS), Rocky Mountain PBS (KRMA), KENW-TV3 (KENW), KUED Channel 7 (KUED), Wyoming PBS (KCWC), Colorado Public Television / KBDI 12 (KBDI), KBYU-TV (KBYU), Thirteen/WNET New York (WNET), WGBH/Channel 2 (WGBH), WGBY (WGBY), NJTV Public Media NJ (WNJT), WLIW21 (WLIW), mpt/Maryland Public Television (WMPB), WETA Television and Radio (WETA), WHYY (WHYY), PBS 39 (WLVT), WVPT - Your Source for PBS and More! (WVPT), Howard University Television (WHUT), WEDU PBS (WEDU), WGCU Public Media (WGCU), WPBT2 (WPBT), WUCF TV (WUCF), WUFT/Channel 5 (WUFT), WXEL/Channel 42 (WXEL), WLRN/Channel 17 (WLRN), WUSF Public Broadcasting (WUSF), ETV (WRLK), UNC-TV (WUNC), PBS Hawaii - Oceanic Cable Channel 10 (KHET), Idaho Public Television (KAID), KSPS (KSPS), OPB (KOPB), KWSU/Channel 10 & KTNW/Channel 31 (KWSU), WILL-TV (WILL), Network Knowledge - WSEC/Springfield (WSEC), WTTW11 (WTTW), Iowa Public Television/IPTV (KDIN), Nine Network (KETC), PBS39 Fort Wayne (WFWA), WFYI Indianapolis (WFYI), Milwaukee Public Television (WMVS), WNIN (WNIN), WNIT Public Television (WNIT), WPT (WPNE), WVUT/Channel 22 (WVUT), WEIU/Channel 51 (WEIU), WQPT-TV (WQPT), WYCC PBS Chicago (WYCC), WIPB-TV (WIPB), WTIU (WTIU), CET  (WCET), ThinkTVNetwork (WPTD), WBGU-TV (WBGU), WGVU TV (WGVU), NET1 (KUON), Pioneer Public Television (KWCM), SDPB Television (KUSD), TPT (KTCA), KSMQ (KSMQ), KPTS/Channel 8 (KPTS), KTWU/Channel 11 (KTWU), East Tennessee PBS (WSJK), WCTE-TV (WCTE), WLJT, Channel 11 (WLJT), WOSU TV (WOSU), WOUB/WOUC (WOUB), WVPB (WVPB), WKYU-PBS (WKYU), KERA 13 (KERA), MPBN (WCBB), Mountain Lake PBS (WCFE), NHPTV (WENH), Vermont PBS (WETK), witf (WITF), WQED Multimedia (WQED), WMHT Educational Telecommunications (WMHT), Q-TV (WDCQ), WTVS Detroit Public TV (WTVS), CMU Public Television (WCMU), WKAR-TV (WKAR), WNMU-TV Public TV 13 (WNMU), WDSE - WRPT (WDSE), WGTE TV (WGTE), Lakeland Public Television (KAWE), KMOS-TV - Channels 6.1, 6.2 and 6.3 (KMOS), MontanaPBS (KUSM), KRWG/Channel 22 (KRWG), KACV (KACV), KCOS/Channel 13 (KCOS), WCNY/Channel 24 (WCNY), WNED (WNED), WPBS (WPBS), WSKG Public TV (WSKG), WXXI (WXXI), WPSU (WPSU), WVIA Public Media Studios (WVIA), WTVI (WTVI), Western Reserve PBS (WNEO), WVIZ/PBS ideastream (WVIZ), KCTS 9 (KCTS), Basin PBS (KPBT), KUHT / Channel 8 (KUHT), KLRN (KLRN), KLRU (KLRU), WTJX Channel 12 (WTJX), WCVE PBS (WCVE), KBTC Public Television (KBTC)
PearVideo
PeekVids
peer.tv
PeerTube
PeerTube:Playlist
peloton: [peloton]
peloton:live: Peloton Live
People
PerformGroup
periscope: Periscope
periscope:user: Periscope user videos
PhilharmonieDeParis: Philharmonie de Paris
phoenix.de
Photobucket
Piapro: [piapro]
Picarto
PicartoVod
Piksel
Pinkbike
Pinterest
PinterestCollection
pixiv:sketch
pixiv:sketch:user
Pladform
PlanetMarathi
Platzi: [platzi]
PlatziCourse: [platzi]
play.fm
player.sky.it
PlayPlusTV: [playplustv]
PlayStuff
PlaysTV
PlaySuisse
Playtvak: Playtvak.cz, iDNES.cz and Lidovky.cz
Playvid
PlayVids
Playwire
pluralsight: [pluralsight]
pluralsight:course
PlutoTV
Podchaser
podomatic
Pokemon
PokemonWatch
PokerGo: [pokergo]
PokerGoCollection: [pokergo]
PolsatGo
PolskieRadio
polskieradio:kierowcow
polskieradio:player
polskieradio:podcast
polskieradio:podcast:list
PolskieRadioCategory
Popcorntimes
PopcornTV
PornCom
PornerBros
Pornez
PornFlip
PornHd
PornHub: [pornhub] PornHub and Thumbzilla
PornHubPagedVideoList: [pornhub]
PornHubPlaylist: [pornhub]
PornHubUser: [pornhub]
PornHubUserVideosUpload: [pornhub]
Pornotube
PornoVoisines
PornoXO
PornTube
PremiershipRugby
PressTV
ProjectVeritas
prosiebensat1: ProSiebenSat.1 Digital
PRXAccount
PRXSeries
prxseries:search: PRX Series Search; "prxseries:" prefix (Example: "prxseriesall:running tortoise")
prxstories:search: PRX Stories Search; "prxstories:" prefix (Example: "prxstories10:falling cat")
PRXStory
puhutv
puhutv:serie
Puls4
Pyvideo
qqmusic: QQ音乐
qqmusic:album: QQ音乐 - 专辑
qqmusic:playlist: QQ音乐 - 歌单
qqmusic:singer: QQ音乐 - 歌手
qqmusic:toplist: QQ音乐 - 排行榜
QuantumTV: [quantumtv]
Qub
R7
R7Article
Radiko
RadikoRadio
radio.de
radiobremen
radiocanada
radiocanada:audiovideo
radiofrance
RadioJavan
radiokapital
radiokapital:show
RadioZetPodcast
radlive
radlive:channel
radlive:season
Rai
RaiPlay
RaiPlayLive
RaiPlayPlaylist
RaiPlaySound
RaiPlaySoundLive
RaiPlaySoundPlaylist
RayWenderlich
RayWenderlichCourse
RBMARadio
RCS
RCSEmbeds
RCSVarious
RCTIPlus
RCTIPlusSeries
RCTIPlusTV
RDS: RDS.ca
RedBull
RedBullEmbed
RedBullTV
RedBullTVRrnContent
Reddit
RedGifs
RedGifsSearch: Redgifs search
RedGifsUser: Redgifs user
RedTube
RegioTV
RENTV
RENTVArticle
Restudy
Reuters
ReverbNation
RICE
RMCDecouverte
RockstarGames
Rokfin: [rokfin]
rokfin:channel: Rokfin Channels
rokfin:search: Rokfin Search; "rkfnsearch:" prefix (Example: "rkfnsearch10:sleeping bunny")
rokfin:stack: Rokfin Stacks
RoosterTeeth: [roosterteeth]
RoosterTeethSeries: [roosterteeth]
RottenTomatoes
Rozhlas
RTBF
RTDocumentry
RTDocumentryPlaylist
rte: Raidió Teilifís Éireann TV
rte:radio: Raidió Teilifís Éireann radio
rtl.lu:article
rtl.lu:tele-vod
rtl.nl: rtl.nl and rtlxl.nl
rtl2
rtl2:you
rtl2:you:series
RTLLuLive
RTLLuRadio
RTNews
RTP
RTRFM
RTS: RTS.ch
rtve.es:alacarta: RTVE a la carta
rtve.es:audio: RTVE audio
rtve.es:infantil: RTVE infantil
rtve.es:live: RTVE.es live streams
rtve.es:television
RTVNH
RTVS
rtvslo.si
RUHD
Rule34Video
RumbleChannel
RumbleEmbed
Ruptly
rutube: Rutube videos
rutube:channel: Rutube channel
rutube:embed: Rutube embedded videos
rutube:movie: Rutube movies
rutube:person: Rutube person videos
rutube:playlist: Rutube playlists
rutube:tags: Rutube tags
RUTV: RUTV.RU
Ruutu
Ruv
ruv.is:spila
safari: [safari] safaribooksonline.com online video
safari:api: [safari]
safari:course: [safari] safaribooksonline.com online courses
Saitosan
SAKTV: [saktv]
SaltTV: [salttv]
SampleFocus
Sapo: SAPO Vídeos
savefrom.net
SBS: sbs.com.au
schooltv
ScienceChannel
screen.yahoo:search: Yahoo screen search; "yvsearch:" prefix (Example: "yvsearch:burping cow")
Screencast
ScreencastOMatic
ScrippsNetworks
scrippsnetworks:watch
Scrolller
SCTE: [scte]
SCTECourse: [scte]
Seeker
SenateGov
SenateISVP
SendtoNews
Servus
Sexu
SeznamZpravy
SeznamZpravyArticle
Shahid: [shahid]
ShahidShow
Shared: shared.sx
ShemarooMe
ShowRoomLive
simplecast
simplecast:episode
simplecast:podcast
Sina
Skeb
sky.it
sky:news
sky:news:story
sky:sports
sky:sports:news
skyacademy.it
SkylineWebcams
skynewsarabia:article
skynewsarabia:video
SkyNewsAU
Slideshare
SlidesLive
Slutload
Snotr
Sohu
SonyLIV: [sonyliv]
SonyLIVSeries
soundcloud: [soundcloud]
soundcloud:playlist: [soundcloud]
soundcloud:related: [soundcloud]
soundcloud:search: [soundcloud] Soundcloud search; "scsearch:" prefix (Example: "scsearch5:sleeping bunny")
soundcloud:set: [soundcloud]
soundcloud:trackstation: [soundcloud]
soundcloud:user: [soundcloud]
SoundcloudEmbed
soundgasm
soundgasm:profile
southpark.cc.com
southpark.cc.com:español
southpark.de
southpark.lat
southpark.nl
southparkstudios.dk
SovietsCloset
SovietsClosetPlaylist
SpankBang
SpankBangPlaylist
Spankwire
Spiegel
Sport5
SportBox
SportDeutschland
spotify: Spotify episodes
spotify:show: Spotify shows
Spreaker
SpreakerPage
SpreakerShow
SpreakerShowPage
SpringboardPlatform
Sprout
sr:mediathek: Saarländischer Rundfunk
SRGSSR
SRGSSRPlay: srf.ch, rts.ch, rsi.ch, rtr.ch and swissinfo.ch play sites
stanfordoc: Stanford Open ClassRoom
StarTrek
startv
Steam
SteamCommunityBroadcast
Stitcher
StitcherShow
StoryFire
StoryFireSeries
StoryFireUser
Streamable
Streamanity
streamcloud.eu
StreamCZ
StreamFF
StreetVoice
StretchInternet
Stripchat
stv:player
Substack
SunPorno
sverigesradio:episode
sverigesradio:publication
SVT
SVTPage
SVTPlay: SVT Play and Öppet arkiv
SVTSeries
SWRMediathek
Syfy
SYVDK
SztvHu
t-online.de
Tagesschau
Tass
TBS
TDSLifeway
Teachable: [teachable]
TeachableCourse: [teachable]
teachertube: teachertube.com videos
teachertube:user:collection: teachertube.com user and collection videos
TeachingChannel
Teamcoco
TeamTreeHouse: [teamtreehouse]
TechTalks
techtv.mit.edu
TedEmbed
TedPlaylist
TedSeries
TedTalk
Tele13
Tele5
TeleBruxelles
Telecinco: telecinco.es, cuatro.com and mediaset.es
Telegraaf
telegram:embed
TeleMB
Telemundo
TeleQuebec
TeleQuebecEmission
TeleQuebecLive
TeleQuebecSquat
TeleQuebecVideo
TeleTask
Telewebion
TennisTV: [tennistv]
TenPlay: [10play]
TF1
TFO
TheHoleTv
TheIntercept
ThePlatform
ThePlatformFeed
TheStar
TheSun
ThetaStream
ThetaVideo
TheWeatherChannel
ThisAmericanLife
ThisAV
ThisOldHouse
ThreeSpeak
ThreeSpeakUser
TikTok
tiktok:effect
tiktok:sound
tiktok:tag
tiktok:user
tinypic: tinypic.com videos
TLC
TMZ
TNAFlix
TNAFlixNetworkEmbed
toggle
toggo
Tokentube
Tokentube:channel
ToonGoggles
tou.tv: [toutv]
Toypics: Toypics video
ToypicsUser: Toypics user profile
TravelChannel
Trilulilu
Trovo
TrovoChannelClip: All Clips of a trovo.live channel; "trovoclip:" prefix
TrovoChannelVod: All VODs of a trovo.live channel; "trovovod:" prefix
TrovoVod
TrueID
TruNews
TruTV
Tube8
TubeTuGraz: [tubetugraz] tube.tugraz.at
TubeTuGrazSeries: [tubetugraz]
TubiTv: [tubitv]
TubiTvShow
Tumblr: [tumblr]
tunein:clip
tunein:program
tunein:station
tunein:topic
TunePk
Turbo
tv.dfb.de
TV2
TV2Article
TV2DK
TV2DKBornholmPlay
tv2play.hu
tv2playseries.hu
TV4: tv4.se and tv4play.se
TV5MondePlus: TV5MONDE+
tv5unis
tv5unis:video
tv8.it
TVA
TVANouvelles
TVANouvellesArticle
TVC
TVCArticle
TVer
tvigle: Интернет-телевидение Tvigle.ru
TVIPlayer
tvland.com
TVN24
TVNet
TVNoe
TVNow
TVNowAnnual
TVNowFilm
TVNowNew
TVNowSeason
TVNowShow
tvopengr:embed: tvopen.gr embedded videos
tvopengr:watch: tvopen.gr (and ethnos.gr) videos
tvp: Telewizja Polska
tvp:embed: Telewizja Polska
tvp:series
tvp:stream
TVPlayer
TVPlayHome
Tweakers
TwitCasting
TwitCastingLive
TwitCastingUser
twitch:clips: [twitch]
twitch:stream: [twitch]
twitch:vod: [twitch]
TwitchCollection: [twitch]
TwitchVideos: [twitch]
TwitchVideosClips: [twitch]
TwitchVideosCollections: [twitch]
twitter
twitter:amplify
twitter:broadcast
twitter:card
twitter:shortener
udemy: [udemy]
udemy:course: [udemy]
UDNEmbed: 聯合影音
UFCArabia: [ufcarabia]
UFCTV: [ufctv]
ukcolumn
UKTVPlay
umg:de: Universal Music Deutschland
Unistra
Unity
uol.com.br
uplynk
uplynk:preplay
Urort: NRK P3 Urørt
URPlay
USANetwork
USAToday
ustream
ustream:channel
ustudio
ustudio:embed
Utreon
Varzesh3
Vbox7
VeeHD
Veo
Veoh
Vesti: Вести.Ru
Vevo
VevoPlaylist
VGTV: VGTV, BTTV, FTV, Aftenposten and Aftonbladet
vh1.com
vhx:embed: [vimeo]
Viafree
vice
vice:article
vice:show
Vidbit
Viddler
Videa
video.arnes.si: Arnes Video
video.google:search: Google Video search; "gvsearch:" prefix (Example: "gvsearch5:sleeping bunny")
video.sky.it
video.sky.it:live
VideoDetective
videofy.me
videomore
videomore:season
videomore:video
VideoPress
Vidio: [vidio]
VidioLive: [vidio]
VidioPremier: [vidio]
VidLii
vier: [vier] vier.be and vijf.be
vier:videos
viewlift
viewlift:embed
Viidea
viki: [viki]
viki:channel: [viki]
vimeo: [vimeo]
vimeo:album: [vimeo]
vimeo:channel: [vimeo]
vimeo:group: [vimeo]
vimeo:likes: [vimeo] Vimeo user likes
vimeo:ondemand: [vimeo]
vimeo:review: [vimeo] Review pages on vimeo
vimeo:user: [vimeo]
vimeo:watchlater: [vimeo] Vimeo watch later list, ":vimeowatchlater" keyword (requires authentication)
Vimm:recording
Vimm:stream
ViMP
ViMP:Playlist
Vimple: Vimple - one-click video hosting
Vine
vine:user
Viqeo
Viu
viu:ott: [viu]
viu:playlist
Vivo: vivo.sx
vk: [vk] VK
vk:uservideos: [vk] VK - User's Videos
vk:wallpost: [vk]
vlive: [vlive]
vlive:channel: [vlive]
vlive:post: [vlive]
vm.tiktok
Vodlocker
VODPl
VODPlatform
VoiceRepublic
voicy
voicy:channel
Voot
VootSeries
VoxMedia
VoxMediaVolume
vpro: npo.nl, ntr.nl, omroepwnl.nl, zapp.nl and npo3.nl
Vrak
VRT: VRT NWS, Flanders News, Flandern Info and Sporza
VrtNU: [vrtnu] VrtNU.be
vrv: [vrv]
vrv:series
VShare
VTM
VTXTV: [vtxtv]
VuClip
Vupload
VVVVID
VVVVIDShow
VyboryMos
Vzaar
Wakanim
Walla
WalyTV: [walytv]
wasdtv:clip
wasdtv:record
wasdtv:stream
washingtonpost
washingtonpost:article
wat.tv
WatchBox
WatchESPN
WatchIndianPorn: Watch Indian Porn
WDR
WDRElefant
WDRPage
web.archive:youtube: web.archive.org saved youtube videos, "ytarchive:" prefix
Webcaster
WebcasterFeed
WebOfStories
WebOfStoriesPlaylist
Weibo
WeiboMobile
WeiqiTV: WQTV
wetv:episode
WeTvSeries
whowatch
wikimedia.org
Willow
WimTV
Wistia
WistiaPlaylist
wnl: npo.nl, ntr.nl, omroepwnl.nl, zapp.nl and npo3.nl
WorldStarHipHop
wppilot
wppilot:channels
WSJ: Wall Street Journal
WSJArticle
WWE
XBef
XboxClips
XFileShare: XFileShare based sites: Aparat, ClipWatching, GoUnlimited, GoVid, HolaVid, Streamty, TheVideoBee, Uqload, VidBom, vidlo, VidLocker, VidShare, VUp, WolfStream, XVideoSharing
XHamster
XHamsterEmbed
XHamsterUser
xiami:album: 虾米音乐 - 专辑
xiami:artist: 虾米音乐 - 歌手
xiami:collection: 虾米音乐 - 精选集
xiami:song: 虾米音乐
ximalaya: 喜马拉雅FM
ximalaya:album: 喜马拉雅FM 专辑
xinpianchang: xinpianchang.com
XMinus
XNXX
Xstream
XTube
XTubeUser: XTube user profile
Xuite: 隨意窩Xuite影音
XVideos
XXXYMovies
Yahoo: Yahoo screen and movies
yahoo:gyao
yahoo:gyao:player
yahoo:japannews: Yahoo! Japan News
YandexDisk
yandexmusic:album: Яндекс.Музыка - Альбом
yandexmusic:artist:albums: Яндекс.Музыка - Артист - Альбомы
yandexmusic:artist:tracks: Яндекс.Музыка - Артист - Треки
yandexmusic:playlist: Яндекс.Музыка - Плейлист
yandexmusic:track: Яндекс.Музыка - Трек
YandexVideo
YandexVideoPreview
YapFiles
YesJapan
yinyuetai:video: 音悦Tai
Ynet
YouJizz
youku: 优酷
youku:show
YouNowChannel
YouNowLive
YouNowMoment
YouPorn
YourPorn
YourUpload
youtube: YouTube
youtube:clip
youtube:favorites: YouTube liked videos; ":ytfav" keyword (requires cookies)
youtube:history: Youtube watch history; ":ythis" keyword (requires cookies)
youtube:music:search_url: YouTube music search URLs with selectable sections (Eg: #songs)
youtube:notif: YouTube notifications; ":ytnotif" keyword (requires cookies)
youtube:playlist: YouTube playlists
youtube:recommended: YouTube recommended videos; ":ytrec" keyword
youtube:search: YouTube search; "ytsearch:" prefix (Example: "ytsearchall:running tortoise")
youtube:search:date: YouTube search, newest videos first; "ytsearchdate:" prefix (Example: "ytsearchdate5:slithering pythons")
youtube:search_url: YouTube search URLs with sorting and filter support
youtube:stories: YouTube channel stories; "ytstories:" prefix
youtube:subscriptions: YouTube subscriptions feed; ":ytsubs" keyword (requires cookies)
youtube:tab: YouTube Tabs
youtube:user: YouTube user videos; "ytuser:" prefix
youtube:watchlater: Youtube watch later list; ":ytwatchlater" keyword (requires cookies)
YoutubeLivestreamEmbed: YouTube livestream embeds
YoutubeYtBe: youtu.be
Zapiks
Zattoo: [zattoo]
ZattooLive: [zattoo]
ZattooMovies: [zattoo]
ZattooRecordings: [zattoo]
ZDF
ZDFChannel
Zee5: [zee5]
zee5:series
ZenYandex
ZenYandexChannel
Zhihu
zingmp3: zingmp3.vn
zingmp3:album
zingmp3:chart-home
zingmp3:chart-music-video
zingmp3:user
zingmp3:week-chart
zoom
Zype
