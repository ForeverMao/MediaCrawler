# -*- coding: utf-8 -*-
# Copyright (c) 2025 relakkes@gmail.com
#
# This file is part of MediaCrawler project.
# Repository: https://github.com/NanmiCoder/MediaCrawler/blob/main/config/base_config.py
# GitHub: https://github.com/NanmiCoder
# Licensed under NON-COMMERCIAL LEARNING LICENSE 1.1
#

# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：
# 1. 不得用于任何商业用途。
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。
# 3. 不得进行大规模爬取或对平台造成运营干扰。
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。
# 5. 不得用于任何非法或不当的用途。
#
# 详细许可条款请参阅项目根目录下的LICENSE文件。
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。

# 基础配置
PLATFORM = "xhs"  # 平台，xhs | dy | ks | bili | wb | tieba | zhihu
KEYWORDS = "王城景区,靖江王城,芦笛岩,桂花公社景区,刘三姐大观园,印象·刘三姐,古南门历史文化街区,象鼻山景区,独秀峰景区,南溪山公园,虞山公园,桃花江景区,象山水月洞,叠彩山景区,伏波山,桂林东西巷,桂林逍遥楼,桂林逍遥湖景区,正阳步行街,桂林西山公园,桂林西山石窟,铁封山公园,桂林博物馆旧馆,桂林融创国际旅游度假区,桂林飞虎队遗址公园,桂林千古情,桂林桂海晴岚,桂林大剧院,桂林神龙谷青岚度假区,王城遗址,七星公园,七星岩,花桥景区,骆驼山,尧山景区,尧山索道,穿山公园,红桥景区,桂林东山公园,漓江风景名胜区,阳朔遇龙河景区,阳朔画山云舍,遇龙河竹筏漂流,十里画廊景区,阳朔月亮山景区,阳朔大榕树,阳朔西街景区,阳朔工农桥,阳朔聚龙潭,兴坪古镇,兴坪佳境,兴坪三千漓,九马画山,阳朔世外桃源,阳朔蝴蝶泉景区,阳朔老寨山,阳朔相公山,阳朔如意峰,如意峰索道景区,图腾古道景区,莲花岩景区,金水岩景区,龙颈河漂流,腐竹山景区,旧县村乡村度假区,白沙镇古建筑群,葡萄古寨,银子岩,漓江竹筏旅游码头群,龙州峡谷群景区,两江四湖景区,桂林杉湖景区,桂林榕湖景区,桂林桂湖景区,桂林木龙湖景区,日月双塔,桂海碑林,漓江竹筏,漓江源大峡谷,漓江三星游船,漓江豪华游船桂花号,漓江兴坪游船,桂林市植物园,桂林动物园,桂林园博园,冠岩景区,草坪风景区,龙门瀑布,雁山公园,大埠乡乡村旅游区,临桂会仙湿地公园,红溪景区,罗山湖玛雅水上乐园,四塘镇田园综合体,山水公园,兴安灵渠,灵渠秦堤古运河遗址,猫儿山景区,溶江古镇,兴安乐满地主题乐园,全州天湖生态旅游度假区,全州天湖滑雪场,湘江战役旧址,灵川古东瀑布,古东森林公园,九龙泉景区,青狮潭景区,定江瀑布,大圩古镇,大圩万寿桥,潭下古村,会仙河湿地,龙州峡谷群景区,漓江竹筏,全州湘山景区,湘源历史文化旅游区,大碧头景区,资口古村,绍水古镇,石塘瀑布,灌阳千家洞,新圩阻击战旧址,水车坪景区,灌江风光带,恭城三庙,恭城武庙,红岩景区,栗木古村,莲花岩,嘉会古镇,资源八角寨,资源龙胜界古道,资源天门山,梅溪景区,资源金紫山,龙胜梯田,龙胜七星伴月,龙胜九龙五虎,龙胜南山牧场,布尼梯田加乌瀑布景区,平安寨梯田,大寨梯田,龙脊古壮寨,龙脊梯田,黄洛瑶寨,龙胜温泉,龙脊云海观景带,荔浦银子岩景区,荔浦丰鱼岩景区,天河瀑布,青山瀑布群,十里画廊漂流,龙怀瀑布,荔江湾景区,平乐二塘天湖景区,平乐榕津古镇,三江口景区,沙子古镇,平顺瀑布群,20元背景,黄布倒影,红军长征湘江战役纪念园,野享大岭山营地"  # 关键词搜索配置，以英文逗号分隔  # 关键词搜索配置，以英文逗号分隔
LOGIN_TYPE = "qrcode"  # qrcode or phone or cookie
COOKIES = ""
CRAWLER_TYPE = (
    "search"  # 爬取类型，search(关键词搜索) | detail(帖子详情)| creator(创作者主页数据)
)
# 是否开启 IP 代理
ENABLE_IP_PROXY = False

# 代理IP池数量
IP_PROXY_POOL_COUNT = 2

# 代理IP提供商名称
IP_PROXY_PROVIDER_NAME = "kuaidaili"  # kuaidaili | wandouhttp

# 设置为True不会打开浏览器（无头浏览器）
# 设置False会打开一个浏览器
# 小红书如果一直扫码登录不通过，打开浏览器手动过一下滑动验证码
# 抖音如果一直提示失败，打开浏览器看下是否扫码登录之后出现了手机号验证，如果出现了手动过一下再试。
HEADLESS = False

# 是否保存登录状态
SAVE_LOGIN_STATE = True

# ==================== CDP (Chrome DevTools Protocol) 配置 ====================
# 是否启用CDP模式 - 使用用户现有的Chrome/Edge浏览器进行爬取，提供更好的反检测能力
# 启用后将自动检测并启动用户的Chrome/Edge浏览器，通过CDP协议进行控制
# 这种方式使用真实的浏览器环境，包括用户的扩展、Cookie和设置，大大降低被检测的风险
ENABLE_CDP_MODE = True

# CDP调试端口，用于与浏览器通信
# 如果端口被占用，系统会自动尝试下一个可用端口
CDP_DEBUG_PORT = 9222

# 自定义浏览器路径（可选）
# 如果为空，系统会自动检测Chrome/Edge的安装路径
# Windows示例: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
# macOS示例: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CUSTOM_BROWSER_PATH = ""

# CDP模式下是否启用无头模式
# 注意：即使设置为True，某些反检测功能在无头模式下可能效果不佳
CDP_HEADLESS = False

# 浏览器启动超时时间（秒）
BROWSER_LAUNCH_TIMEOUT = 60

# 是否在程序结束时自动关闭浏览器
# 设置为False可以保持浏览器运行，便于调试
AUTO_CLOSE_BROWSER = True

# 数据保存类型选项配置,支持五种类型：csv、db、json、sqlite、excel, 最好保存到DB，有排重的功能。
SAVE_DATA_OPTION = "json"  # csv or db or json or sqlite or excel

# 用户浏览器缓存的浏览器文件配置
USER_DATA_DIR = "%s_user_data_dir"  # %s will be replaced by platform name

# 爬取开始页数 默认从第一页开始
START_PAGE = 1

# 爬取视频/帖子的数量控制
CRAWLER_MAX_NOTES_COUNT = 100

# 并发爬虫数量控制
MAX_CONCURRENCY_NUM = 1

# 是否开启爬媒体模式（包含图片或视频资源），默认不开启爬媒体
ENABLE_GET_MEIDAS = False

# 是否开启爬评论模式, 默认开启爬评论
ENABLE_GET_COMMENTS = True

# 爬取一级评论的数量控制(单视频/帖子)
CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES = 1000

# 是否开启爬二级评论模式, 默认不开启爬二级评论
# 老版本项目使用了 db, 则需参考 schema/tables.sql line 287 增加表字段
ENABLE_GET_SUB_COMMENTS = False

# 词云相关
# 是否开启生成评论词云图
ENABLE_GET_WORDCLOUD = False
# 自定义词语及其分组
# 添加规则：xx:yy 其中xx为自定义添加的词组，yy为将xx该词组分到的组名。
CUSTOM_WORDS = {
    "零几": "年份",  # 将“零几”识别为一个整体
    "高频词": "专业术语",  # 示例自定义词
}

# 停用(禁用)词文件路径
STOP_WORDS_FILE = "./docs/hit_stopwords.txt"

# 中文字体文件路径
FONT_PATH = "./docs/STZHONGS.TTF"

# 爬取间隔时间
CRAWLER_MAX_SLEEP_SEC = 2

from .bilibili_config import *
from .xhs_config import *
from .dy_config import *
from .ks_config import *
from .weibo_config import *
from .tieba_config import *
from .zhihu_config import *
