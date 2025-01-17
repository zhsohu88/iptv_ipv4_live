import re  # 导入正则表达式模块，用于字符串匹配和搜索。
import requests  # 导入 requests 模块，用于发送 HTTP 请求。
import logging  # 导入 logging 模块，用于记录日志。
from collections import OrderedDict  # 从 collections 模块中导入 OrderedDict，用于创建有序字典。
from datetime import datetime  # 从 datetime 模块中导入 datetime 类，用于处理日期和时间。
import config  # 导入 config 模块，用于加载配置数据。

# 配置日志记录
logging.basicConfig(
    level=logging.INFO,  # 设置日志记录级别为 INFO。
    format='%(asctime)s - %(levelname)s - %(message)s',  # 设置日志记录格式。
    handlers=[
        logging.FileHandler("function.log", "w", encoding="utf-8"),  # 将日志记录到文件中。
        logging.StreamHandler()  # 将日志输出到控制台。
    ]
)

# 解析模板文件
def parse_template(template_file):
    template_channels = OrderedDict()  # 创建一个有序字典，用于存储解析后的频道信息。
    current_category = None  # 初始化当前分类变量。

    # 打开并读取模板文件
    with open(template_file, "r", encoding="utf-8") as f:
        for line in f:  # 遍历文件中的每一行
            line = line.strip()  # 去除行首和行尾的空白字符
            if line and not line.startswith("#"):  # 如果行不为空且不以 # 开头
                if "#genre#" in line:  # 如果行中包含 #genre#
                    current_category = line.split(",")[0].strip()  # 获取当前分类
                    template_channels[current_category] = []  # 初始化当前分类的频道列表
                elif current_category:
                    channel_name = line.split(",")[0].strip()  # 获取频道名称
                    template_channels[current_category].append(channel_name)  # 将频道名称添加到当前分类的频道列表中

    return template_channels  # 返回解析后的频道信息

# 获取频道信息
def fetch_channels(url):
    channels = OrderedDict()  # 创建一个有序字典，用于存储频道信息。

    try:
        response = requests.get(url)  # 发送 HTTP GET 请求
        response.raise_for_status()  # 如果响应状态码不是 200 则抛出异常
        response.encoding = 'utf-8'  # 设置响应编码为 UTF-8
        lines = response.text.split("\n")  # 将响应内容按行分割
        current_category = None  # 初始化当前分类变量
        is_m3u = any("#EXTINF" in line for line in lines[:15])  # 判断是否为 m3u 格式
        source_type = "m3u" if is_m3u else "txt"  # 根据格式类型设置 source_type
        logging.info(f"url: {url} 获取成功，判断为 {source_type} 格式")  # 记录获取成功日志

        if is_m3u:
            for line in lines:  # 遍历每一行
                line = line.strip()  # 去除行首和行尾的空白字符
                if line.startswith("#EXTINF"):  # 如果行以 #EXTINF 开头
                    match = re.search(r'group-title="(.*?)",(.*)', line)  # 使用正则表达式匹配分类和频道名称
                    if match:
                        current_category = match.group(1).strip()  # 获取当前分类
                        channel_name = match.group(2).strip()  # 获取频道名称
                        if current_category not in channels:
                            channels[current_category] = []  # 初始化当前分类的频道列表
                elif line and not line.startswith("#"):  # 如果行不为空且不以 # 开头
                    channel_url = line.strip()  # 获取频道 URL
                    if current_category and channel_name:
                        channels[current_category].append((channel_name, channel_url))  # 将频道名称和 URL 添加到当前分类的频道列表中
        else:
            for line in lines:  # 遍历每一行
                line = line.strip()  # 去除行首和行尾的空白字符
                if "#genre#" in line:  # 如果行中包含 #genre#
                    current_category = line.split(",")[0].strip()  # 获取当前分类
                    channels[current_category] = []  # 初始化当前分类的频道列表
                elif current_category:
                    match = re.match(r"^(.*?),(.*?)$", line)  # 使用正则表达式匹配频道名称和 URL
                    if match:
                        channel_name = match.group(1).strip()  # 获取频道名称
                        channel_url = match.group(2).strip()  # 获取频道 URL
                        channels[current_category].append((channel_name, channel_url))  # 将频道名称和 URL 添加到当前分类的频道列表中
                    elif line:
                        channels[current_category].append((line, ''))  # 如果行中只有频道名称无 URL，则只添加频道名称
        if channels:
            categories = ", ".join(channels.keys())  # 获取所有分类名称
            logging.info(f"url: {url} 爬取成功✅，包含频道分类: {categories}")  # 记录爬取成功日志
    except requests.RequestException as e:
        logging.error(f"url: {url} 爬取失败❌, Error: {e}")  # 记录爬取失败日志

    return channels  # 返回获取的频道信息

# 匹配频道信息
def match_channels(template_channels, all_channels):
    matched_channels = OrderedDict()  # 创建一个有序字典，用于存储匹配的频道信息。

    for category, channel_list in template_channels.items():  # 遍历模板中的每个分类和频道列表
        matched_channels[category] = OrderedDict()  # 初始化当前分类的匹配频道列表
        for channel_name in channel_list:  # 遍历模板中的每个频道名称
            for online_category, online_channel_list in all_channels.items():  # 遍历所有获取的分类和频道列表
                for online_channel_name, online_channel_url in online_channel_list:  # 遍历获取的每个频道名称和 URL
                    if channel_name == online_channel_name:  # 如果频道名称匹配
                        matched_channels[category].setdefault(channel_name, []).append(online_channel_url)  # 将匹配的频道 URL 添加到匹配频道列表中

    return matched_channels  # 返回匹配的频道信息

# 过滤来源 URL
def filter_source_urls(template_file):
    template_channels = parse_template(template_file)  # 解析模板文件获取模板频道信息
    source_urls = config.source_urls  # 从配置文件中获取来源 URL 列表

    all_channels = OrderedDict()  # 创建一个有序字典，用于存储所有获取的频道信息。
    for url in source_urls:  # 遍历每个来源 URL
        fetched_channels = fetch_channels(url)  # 获取频道信息
        for category, channel_list in fetched_channels.items():  # 遍历获取的每个分类和频道列表
            if category in all_channels:
                all_channels[category].extend(channel_list)  # 如果分类已存在，扩展频道列表
            else:
                all_channels[category] = channel_list  # 否则，初始化分类的频道列表

    matched_channels = match_channels(template_channels, all_channels)  # 匹配频道信息

    return matched_channels, template_channels  # 返回匹配的频道信息和模板频道信息

# 判断是否为 IPv6
def is_ipv6(url):
    return re.match(r'^http:\/\/\[[0-9a-fA-F:]+\]', url) is not None  # 使用正则表达式判断 URL 是否为 IPv6 格式

# 更新频道 URL 到 M3U 文件
def updateChannelUrlsM3U(channels, template_channels):
    written_urls = set()  # 创建一个集合来存储已写入的 URL，以避免重复

    # 注释掉这一段代码
    # current_date = datetime.now().strftime("%Y-%m-%d")
    # for group in config.announcements:
    #     for announcement in group['entries']:
    #         if announcement['name'] is None:
    #             announcement['name'] = current_date

    with open("live.m3u", "w", encoding="utf-8") as f_m3u:
        # 写入 M3U 文件头部信息，包括 EPG URL 列表
        f_m3u.write(f"""#EXTM3U x-tvg-url={",".join(f'"{epg_url}"' for epg_url in config.epg_urls)}\n""")

        with open("live.txt", "w", encoding="utf-8") as f_txt:
            # 注释掉这一段代码
            # for group in config.announcements:
            #     f_txt.write(f"{group['channel']},#genre#\n")
            #     for announcement in group['entries']:
            #         f_m3u.write(f"""#EXTINF:-1 tvg-id="1" tvg-name="{announcement['name']}" tvg-logo="{announcement['logo']}" group-title="{group['channel']}",{announcement['name']}\n""")
            #         f_m3u.write(f"{announcement['url']}\n")
            #         f_txt.write(f"{announcement['name']},{announcement['url']}\n")

            for category, channel_list in template_channels.items():  # 遍历模板中的频道分类
                f_txt.write(f"{category},#genre#\n")  # 写入每个频道分类
                if category in channels:  # 如果频道分类存在于获取的频道列表中
                    for channel_name in channel_list:  # 遍历每个频道名称
                        if channel_name in channels[category]:  # 如果频道名称存在于获取的频道分类中
                            # 根据 IP 版本优先级排序 URL 列表
                            sorted_urls = sorted(channels[category][channel_name], key=lambda url: not is_ipv6(url) if config.ip_version_priority == "ipv6" else is_ipv6(url))
                            filtered_urls = []  # 创建一个列表来存储过滤后的 URL
                            for url in sorted_urls:  # 遍历排序后的 URL
                                # 使用 is_ipv6 函数过滤掉 IPv6 地址
                                if not is_ipv6(url):
                                    if url and url not in written_urls and not any(blacklist in url for blacklist in config.url_blacklist):
                                        filtered_urls.append(url)
                                        written_urls.add(url)  # 将 URL 添加到已写入的 URL 集合中

                            for index, url in enumerate(filtered_urls, start=1):  # 遍历过滤后的 URL，并从 1 开始计数
                                # 注释掉在链接后面加东西的代码
                                # if is_ipv6(url):
                                #     url_suffix = f"$LR•IPV6" if total_urls == 1 else f"$LR•IPV6『线路{index}』"
                                # else:
                                #     url_suffix = f"$LR•IPV4" if total_urls == 1 else f"$LR•IPV4『线路{index}』"
                                # if '$' in url:
                                #     base_url = url.split('$', 1)[0]
                                # else:
                                #     base_url = url

                                # new_url = f"{base_url}{url_suffix}"
                                new_url = url  # 不对 URL 进行任何修改

                                # 写入 M3U 文件中的频道信息
                                f_m3u.write(f"#EXTINF:-1 tvg-id=\"{index}\" tvg-name=\"{channel_name}\" tvg-logo=\"https://gcore.jsdelivr.net/gh/yuanzl77/TVlogo@master/png/{channel_name}.png\" group-title=\"{category}\",{channel_name}\n")
                                f_m3u.write(new_url + "\n")
                                # 写入 TXT 文件中的频道信息
                                f_txt.write(f"{channel_name},{new_url}\n")

            f_txt.write("\n")  # 添加空行以分隔不同部分

if __name__ == "__main__":
    template_file = "demo.txt"  # 模板文件名
    channels, template_channels = filter_source_urls(template_file)  # 过滤来源 URL 并匹配频道信息
    updateChannelUrlsM3U(channels, template_channels)  # 更新频道 URL 到 M3U 文件
