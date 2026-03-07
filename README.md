# ComicCrawler - 通用漫画下载工具

<p align="center">
  <img src="https://img.shields.io/badge/python-3.6%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/github/license/Tw1nkleDu5t/ComicCrawler" alt="License">
  <img src="https://img.shields.io/github/stars/Tw1nkleDu5t/ComicCrawler" alt="Stars">
  <img src="https://img.shields.io/github/issues/Tw1nkleDu5t/ComicCrawler" alt="Issues">
  <img src="https://img.shields.io/github/forks/Tw1nkleDu5t/ComicCrawler" alt="Forks">
</p>

<p align="center">
  一个通用的漫画章节下载工具 | A universal comic chapter downloader
</p>

<p align="center">
  <a href="#-项目简介">项目简介</a> •
  <a href="#-快速开始">快速开始</a> •
  <a href="#-使用教程">使用教程</a> •
  <a href="#-常见问题">常见问题</a> •
  <a href="#-高级配置">高级配置</a>
</p>

<p align="center">
  <a href="https://github.com/Tw1nkleDu5t" target="_blank">作者主页</a> •
  <a href="https://github.com/Tw1nkleDu5t/ComicCrawler/issues" target="_blank">提交Issue</a>
</p>

---

## 📖 项目简介

ComicCrawler 是一个灵活强大的漫画下载工具，能够从支持网页浏览的漫画网站自动抓取章节图片。它通过解析章节页面HTML提取图片URL，支持批量下载、自动重试失败任务、断点续传等功能，让您轻松离线阅读喜欢的漫画。

### ✨ 核心功能

| 功能 | 说明 |
|------|------|
| 🔄 **自动重试** | 网络不稳定时自动重试，最多可配置8次 |
| 📝 **失败记录** | 精确记录失败的图片和章节，支持单独重试 |
| ⏸️ **断点续传** | 已下载图片自动跳过，避免重复下载 |
| 🚀 **批量下载** | 支持指定范围下载（如1-50话） |
| 🔧 **高度可配置** | 延迟、重试次数、代理等均可自定义 |
| 📊 **进度显示** | 实时显示进度和预计剩余时间 |
| 🌐 **代理支持** | 内置代理配置，方便绕过访问限制 |

---

## 🚀 快速开始

### 环境要求
- Python 3.6 或更高版本
- pip 包管理工具

### ⏱️ 一分钟安装

**步骤1：克隆仓库**

git clone https://github.com/Tw1nkleDu5t/ComicCrawler.git

cd ComicCrawler

步骤2：安装依赖
bath

[

pip install requests

]
步骤3：准备章节文件
在脚本同目录下创建 chapters.json，格式如下：

json
[

    {
        "order": 1,
        "title": "第一章 相遇",
        "url": "https://www.example.com/comic/1"
    },
    {
        "order": 2,
        "title": "第二章 离别",
        "url": "https://www.example.com/comic/2"
    }
    
]

步骤4：运行程序
python
[

python comic_downloader.py

]


##📖 使用教程
一、首次运行配置
运行程序后，首先进入配置向导：

ComicCrawler v1.0.0 - 通用漫画下载工具

欢迎使用 ComicCrawler！

初始配置 (可直接回车使用默认值)

配置项详解

配置项	说明	默认值	示例输入

保存目录	下载文件的保存位置	桌面/ComicDownload	D:\comic 或直接回车

章节文件路径	chapters.json的位置	脚本目录/chapters.json	E:\manga\list.json

Referer	⚠️ 重要！需设为漫画网站域名	https://www.example.com/	https://www.manhua.com

最大重试次数	图片下载失败后的重试次数	8	5

超时秒数	请求超时时间	45	30

图片间延迟	每张图片后的等待时间(秒)	2	1

章节间延迟	每章后的等待时间(秒)	8	5

重试延迟	失败后重试的等待时间(秒)	5	3

💡 提示： 所有配置项都可以直接回车使用默认值，新手推荐全部默认！

二、主菜单功能
配置完成后，进入主菜单：

请选择：
1. 下载全部
2. 指定范围
3. 重试失败
4. 测试下载 (前5章)
0. 退出
请输入选项: 
功能详解
选项	用途	操作步骤
1. 下载全部	下载所有章节	输入 1 → 回车确认
2. 指定范围	下载特定章节范围	输入 2 → 输入开始章节（如 1）→ 输入结束章节（如 50）
3. 重试失败	重新下载失败的图片/章节	输入 3 → 自动重试
4. 测试下载	快速测试配置是否正确	输入 4 → 下载前5章验证
0. 退出	退出程序	输入 0
三、下载过程演示
示例：下载全部章节

请输入选项: 1
准备下载 100 章 (第1话-第100话)

按回车键开始下载，或输入n取消: 

进度: [1/100]

[1] 第一章 相遇
  获取图片列表 (尝试 1/8)...
  找到 25 张图片
  
  第1页: 尝试 1/8... ✓ 成功 (245.6KB)
  
  第2页: 尝试 1/8... ✓ 成功 (189.3KB)
  
  第3页: 已存在  ✓ 跳过
  ...
  ✓ 完成: 25/25

已用: 2.5分钟, 剩余: 247.5分钟  # 每5章显示一次进度估算

进度: [2/100]
[2] 第二章 离别

下载状态说明
状态	含义

✓ 成功	图片下载成功

已存在	图片已存在，自动跳过

尝试 x/8	第x次尝试下载

⚠ 部分完成	章节部分图片下载失败

被禁止访问 (403)	IP可能被封，等待30秒后重试

四、失败重试机制

当下载失败时

如果某些图片下载失败，会显示：

⚠ 部分完成: 23/25
程序会自动记录失败的图片到 failed.json：


json
{
  "failed_chapters": [],
  "failed_images": [
    {
      "chapter": 1,
      "page": "024",
      "url": "https://example.com/image/24.jpg"
    }
  ]
}
如何重试失败任务

请输入选项: 3

找到 2 张失败图片，1 个失败章节

重试失败的图片...
  章节 1 第 024 页: 尝试 1/8... ✓ 成功
  章节 1 第 025 页: 尝试 1/8... ✓ 成功

重试失败的章节...
  [3] 第三章 重逢
  ...
五、下载文件结构
下载完成后，文件会按以下结构保存：

桌面/ComicDownload/          # 您设置的保存目录

├── 001_第一章 相遇/         # 第1章（自动创建）

│   ├── 001.webp            # 第1页（自动编号）

│   ├── 002.webp            # 第2页

│   ├── 003.webp

│   └── ... (最多999页)

├── 002_第二章 离别/         # 第2章

│   ├── 001.webp

│   └── ...

├── 003_第三章 重逢/

│   └── ...

└── ...

文件命名规则：

章节文件夹：{三位数编号}_{章节标题}（如 001_第一章 相遇）

图片文件：{三位数页码}.{扩展名}（如 001.webp）

六、实用操作技巧

1. 安全中断下载

按 Ctrl + C 可以随时安全中断

程序会自动保存失败记录

下次运行选择"重试失败"即可继续

2. 断点续传
已下载的图片会自动跳过

即使中断后重新运行，也不会重复下载

程序会检查文件大小（>10KB才算有效）

3. 快速启动脚本
创建 run.bat 文件（Windows）：

batch
@echo off
cd /d %~dp0
python comic_downloader.py
pause
双击即可运行，无需每次都打开命令行。

❓ 常见问题
Q1: 下载时提示"找不到图片"
可能原因：

❌ Referer 设置不正确（需设置为漫画网站域名）

❌ 网站有反爬虫机制

❌ 图片URL格式特殊

解决方法：

检查 Referer 是否正确（必须与漫画网站域名一致）

查看生成的 debug_*.html 文件分析页面结构

可能需要修改正则表达式匹配规则（代码第200行附近）

Q2: 下载速度太慢怎么办？
解决方案：

方法	说明	风险
降低图片延迟	将 IMAGE_DELAY 改为 1秒	⚠️ 易被封IP

使用代理	开启代理配置	✅ 推荐

夜间下载	选择网络空闲时段	✅ 安全

分批次下载	每次下载30-50章	✅ 推荐

Q3: 出现403错误（被禁止访问）

原因： IP可能被网站封禁

解决步骤：

程序会自动等待30秒后重试

建议开启代理（见高级配置）

增加章节间延迟（改为15秒）

分批次下载，避免一次性太多请求

Q4: 如何批量下载大量章节？
最佳实践：

每次下载不超过50章

设置章节间延迟为10-15秒

开启代理分散请求IP

可以夜间挂机下载（设置大延迟）

Q5: 支持哪些图片格式？
✅ 支持的格式：

webp（默认）

jpg / jpeg

png

程序会自动识别图片扩展名，如果无法识别默认保存为 webp。

🔧 高级配置
1. 使用代理
找到代码中的代理配置部分（约30-35行），修改为：

python
# 代理配置
PROXIES = {

    'http': 'http://127.0.0.1:7890',   # 替换为您的代理地址
    'https': 'http://127.0.0.1:7890'
}

USE_PROXY = True  # 改为True启用代理

2. 自定义请求头
3. 
可以修改 USER_AGENTS 列表，添加更多浏览器标识：

python
USER_AGENTS = [

    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15',
    
    # 可以继续添加...
]
3. 调整下载参数
根据您的网络情况调整：

python
# 保守配置（不易被封，速度较慢）
IMAGE_DELAY = 5      # 图片间延迟5秒

CHAPTER_DELAY = 15   # 章节间延迟15秒

MAX_RETRIES = 10     # 最大重试10次

# 激进配置（速度快，易被封）
IMAGE_DELAY = 1      # 图片间延迟1秒

CHAPTER_DELAY = 3    # 章节间延迟3秒

MAX_RETRIES = 5      # 最大重试5次

4. 修改默认保存位置
找到约20行附近的代码：

python
# 修改默认保存目录
DESKTOP_PATH = os.path.join(os.path.expanduser('~'), 'Desktop')

DEFAULT_SAVE_DIR = os.path.join(DESKTOP_PATH, '我的漫画')  # 改为您想要的名称


📄 许可证
本项目采用 MIT 许可证 - 详见 LICENSE 文件

⚠️ 免责声明
本工具仅供学习交流使用，请勿用于商业用途。下载的漫画请于24小时内删除，支持正版漫画创作。

📞 联系方式
作者主页: https://github.com/Tw1nkleDu5t

项目地址: https://github.com/Tw1nkleDu5t/ComicCrawler

提交Issue: https://github.com/Tw1nkleDu5t/ComicCrawler/issues

<p align="center"> <b>如果这个项目对您有帮助，请给一个 ⭐️ 吧！</b> </p><p align="center"> <a href="#">返回顶部 ↑</a> </p> ```
