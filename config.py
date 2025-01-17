ip_version_priority = "ipv6"

source_urls = [
    # "http://175.178.251.183:6689/aktvlive.txt",
    # "https://live.fanmingming.com/tv/m3u/ipv6.m3u",
    # "https://raw.githubusercontent.com/yuanzl77/IPTV/main/直播/央视频道.txt",
    # "https://live.zhoujie218.top/tv/iptv6.txt",
    # "https://live.zhoujie218.top/tv/iptv4.txt",
    # "https://tv.youdu.fan:666/live/",
    # "http://ww.weidonglong.com/dsj.txt",
    # "http://xhztv.top/zbc.txt",
    # "https://raw.githubusercontent.com/qingwen07/awesome-iptv/main/tvbox_live_all.txt",
    # "https://raw.githubusercontent.com/Guovin/TV/gd/output/result.txt",
    # "https://raw.githubusercontent.com/vbskycn/iptv/master/tv/hd.txt",
    # "https://cdn.jsdelivr.net/gh/YueChan/live@main/IPTV.m3u",
    # "https://raw.githubusercontent.com/PizazzGY/TVBox_warehouse/main/live.txt",
    # "https://fm1077.serv00.net/SmartTV.m3u",
    # "https://raw.githubusercontent.com/ssili126/tv/main/itvlist.txt",
    # "https://raw.githubusercontent.com/kimwang1978/collect-tv-txt/main/merged_output.txt"
    
    # "https://raw.githubusercontent.com/zhsohu88/iptv_ipv4_live/main/live_ipv4.txt",
    # "https://raw.githubusercontent.com/zhsohu88/iptv_ipv4_live/main/ygbh.txt",
    # "http://wp.wadg.pro/down.php/d7b52d125998d00e2d2339bac6abd2b5.txt",            # 小苹果，蜗牛线路[测试2]
    "https://raw.githubusercontent.com/zhsohu88/iptv_ipv4_live/main/JJdoudizhu.txt",    # 自己的JJ斗地主
    "https://raw.githubusercontent.com/zhsohu88/iptv_ipv4_live/main/chs.txt",           # 成人
    "https://raw.githubusercontent.com/zhsohu88/iptv_ipv4_live/main/dalian.txt",       # 大连
    "http://106.53.99.30/8.txt",     # 电视家9
    # "https://ygbh.site/bh.txt",      # 月光宝盒
    "https://raw.githubusercontent.com/chuzjie/wuihui/main/小米/DSJ240101.txt",     # NEW直播
    "https://4708.kstore.space/omg/tv.txt",     # 拾光电视
    "https://gitlab.com/tvkj/loong/-/raw/main/loog.txt"    # 七星itv
]

url_blacklist = [
    "epg.pw/stream/",
    "103.40.13.71:12390",
    "[2409:8087:1a01:df::4077]/PLTV/",
    "8.210.140.75:68",
    "154.12.50.54",
    "yinhe.live_hls.zte.com",
    "8.137.59.151",
    "[2409:8087:7000:20:1000::22]:6060",
    "histar.zapi.us.kg",
    "www.tfiplaytv.vip",
    "dp.sxtv.top",
    "111.230.30.193",
    "148.135.93.213:81",
    "live.goodiptv.club",
    "iptv.luas.edu.cn",
    "[2409:8087:2001:20:2800:0:df6e:eb22]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb23]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]/ott.mobaibox.com/",
    "[2409:8087:2001:20:2800:0:df6e:eb1d]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb24]",
    "[2409:8087:2001:20:2800:0:df6e:eb25]:80",
    "[2409:8087:2001:20:2800:0:df6e:eb27]",
    
    "generationnexxxt.com:19806",
    "110.53.218.182:9902",
    "111.14.181.15:9901",
    "112.84.131.28:80",
    "116.128.242.83:9901",
    "116.148.164.119",
    "120.197.112.28:9901",
    "120.234.5.29:6000",
    "122.233.199.46:8888",
    "122.234.14.200:8888",
    "123.182.60.29:9002",
    "123.184.28.3",
    "123.184.28.50",
    "123.6.102.32:11789",
    "124.115.205.101:8888",
    "182.122.73.43:10086",
    "183.133.104.144:8899",
    "183.92.4.163:4000",
    "1b6467f415.iok.la:9931",
    "nb.thkss.com:9981",
    "jrys.haycker.eu.org:4443",
    "cdn.jdshipin.com:8880",
    "ygbh.live",
    "39.134.66.66",
    "mail.petzhu.top:7000",
    "alvin.ergotron.net:8000",
    "home.huaz.site:4000",
    "dms.yryyj.site:8188",
    "218.241.192.50:8808",
    "39.77.3.5:8989",
    "webmail.axxe.top:4022",
    "hlsbkmgsplive.miguvideo.com",
    "22725y284r.yicp.fun:9902",
    "60.10.139.10:8801",
    "http://159.75.85.63:35455",
    "openhls-tct.douyucdn2.cn"
]

announcements = [
    {
        "channel": "公告",
        "entries": [
            {"name": "请阅读", "url": "https://liuliuliu.tv/api/channels/1997/stream", "logo": "http://175.178.251.183:6689/LR.jpg"},
            {"name": "yuanzl77.github.io", "url": "https://liuliuliu.tv/api/channels/233/stream", "logo": "http://175.178.251.183:6689/LR.jpg"},
            {"name": "更新日期", "url": "https://gitlab.com/lr77/IPTV/-/raw/main/%E4%B8%BB%E8%A7%92.mp4", "logo": "http://175.178.251.183:6689/LR.jpg"},
            {"name": None, "url": "https://gitlab.com/lr77/IPTV/-/raw/main/%E8%B5%B7%E9%A3%8E%E4%BA%86.mp4", "logo": "http://175.178.251.183:6689/LR.jpg"}
        ]
    }
]

epg_urls = [
    "https://live.fanmingming.com/e.xml",
    "http://epg.51zmt.top:8000/e.xml",
    "http://epg.aptvapp.com/xml",
    "https://epg.pw/xmltv/epg_CN.xml",
    "https://epg.pw/xmltv/epg_HK.xml",
    "https://epg.pw/xmltv/epg_TW.xml"
]
