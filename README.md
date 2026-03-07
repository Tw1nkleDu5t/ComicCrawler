# 🦸 ComicCrawler - 通用漫画下载工具

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/Tw1nkleDu5t/ComicCrawler?style=for-the-badge&logo=github" alt="Stars">
  <img src="https://img.shields.io/github/issues/Tw1nkleDu5t/ComicCrawler?style=for-the-badge" alt="Issues">
  <img src="https://img.shields.io/github/forks/Tw1nkleDu5t/ComicCrawler?style=for-the-badge" alt="Forks">
</p>

<p align="center">
  <b>✨ 一个强大、灵活、易用的漫画章节下载工具 ✨</b><br>
  <i>支持自动重试 · 断点续传 · 批量管理 · 代理配置</i>
</p>

<p align="center">
  <a href="#-项目简介">📖 项目简介</a> •
  <a href="#-快速开始">🚀 快速开始</a> •
  <a href="#-使用教程">📚 使用教程</a> •
  <a href="#-常见问题">❓ 常见问题</a> •
  <a href="#-高级配置">⚙️ 高级配置</a>
</p>

<p align="center">
  <a href="https://github.com/Tw1nkleDu5t" target="_blank">👤 作者主页</a> •
  <a href="https://github.com/Tw1nkleDu5t/ComicCrawler/issues" target="_blank">🐛 提交Issue</a>
</p>

---

## 📖 项目简介

ComicCrawler 是一款专为漫画爱好者设计的通用下载工具。只需提供章节页面链接，它就能自动解析图片地址、批量抓取并整理成本地归档文件。无论是追更热门连载，还是收藏经典老漫画，ComicCrawler 都能助你轻松搞定。

### ✨ 核心功能

| 功能 | 说明 |
|:----:|:------|
| 🔄 智能重试 | 网络波动时自动重试（最多可设 8 次），确保完整下载 |
| 📝 精确失败记录 | 单独记录失败的图片和章节，支持一键重试 |
| ⏸️ 断点续传 | 已下载图片自动跳过，随时中断也不用担心重复下载 |
| 🚀 批量下载 | 支持全部下载、指定范围下载（如 1-50 话）或测试下载前 5 话 |
| 🔧 高度可配置 | 延迟时间、超时设置、代理服务器、请求头均可自定义 |
| 🌐 代理支持 | 内置代理开关，轻松绕过访问限制 |
| 📊 实时进度 | 清晰的进度显示，实时查看下载状态和剩余时间 |
| 📂 智能命名 | 自动创建规范的文件夹和文件命名，便于管理 |

---

## 🚀 快速开始

### 📋 环境要求

- Python 3.6 或更高版本
- pip 包管理工具

### ⏱️ 一分钟安装指南

**步骤1：克隆仓库**

在终端中执行以下命令：
```
git clone https://github.com/Tw1nkleDu5t/ComicCrawler.git

cd ComicCrawler
```
**步骤2：安装依赖**

执行命令：
```
pip install requests
```
**步骤3：准备章节文件**

在脚本同目录下创建 chapters.json 文件，内容格式如下：
```
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
    },
    {
        "order": 3,
        "title": "第三章 重逢",
        "url": "https://www.example.com/comic/3"
    }
]
```
| 字段 | 说明 |
|:----:|:------|
| order | 章节序号（用于排序和文件夹命名） |
| title | 章节标题 |
| url | 章节页面的完整网址 |

**步骤4：运行程序**

执行命令：
```
python comic_downloader.py
```
---

## 📚 使用教程

### 一、首次运行配置

第一次运行程序时，会进入配置向导。**新手推荐全部使用默认值**，直接回车即可。

ComicCrawler v1.0.0 - 通用漫画下载工具

欢迎使用 ComicCrawler！

初始配置 (可直接回车使用默认值)

📁 保存目录 [桌面/ComicDownload]: 
📄 章节文件路径 [./chapters.json]: 
🌐 Referer (必填) [https://www.example.com/]: 
🔄 最大重试次数 [8]: 
⏱️ 超时秒数 [45]: 
⏸️ 图片间延迟(秒) [2]: 
⏸️ 章节间延迟(秒) [8]: 
🔄 重试延迟(秒) [5]:

#### 配置项详解

| 配置项 | 说明 | 默认值 | 建议 |
|:------:|:------:|:------:|:----:|
| 保存目录 | 下载文件的存放位置 | 桌面/ComicDownload | 可自定义路径 |
| 章节文件路径 | chapters.json的位置 | ./chapters.json | 保持默认 |
| Referer | 必须设置为漫画网站域名 | https://www.example.com/ | 防反爬关键 |
| 最大重试次数 | 图片下载失败后的重试次数 | 8 | 网络差可调高 |
| 超时秒数 | 请求超时时间 | 45 | 网络慢可调高 |
| 图片间延迟 | 每张图片后的等待时间 | 2秒 | 防封禁 |
| 章节间延迟 | 每章完成后的等待时间 | 8秒 | 防封禁 |
| 重试延迟 | 失败后重试的等待时间 | 5秒 | 保持默认 |

### 二、主菜单功能

配置完成后，进入主菜单：

请选择：
1. 📥 下载全部
2. 🔢 指定范围
3. 🔄 重试失败
4. 🧪 测试下载 (前5章)
0. 🚪 退出

请输入选项:

#### 功能详解

| 选项 | 功能 | 操作说明 |
|:----:|:----:|:--------:|
| 1 | 下载全部 | 下载 chapters.json 中的所有章节 |
| 2 | 指定范围 | 输入起始和结束章节号，例如 1 50 |
| 3 | 重试失败 | 自动重试之前失败的图片或章节 |
| 4 | 测试下载 | 快速测试配置是否正确（仅下载前5章） |
| 0 | 退出程序 | 安全退出 |

### 三、下载过程演示

以选择 **1. 下载全部** 为例：

请输入选项: 1

准备下载 100 章 (第1话-第100话)

按回车键开始下载，或输入n取消: 

进度: [1/100]

[1] 第一章 相遇
  获取图片列表 (尝试 1/8)...
  找到 25 张图片
  
  第1页: 尝试 1/8... ✓ 成功 (245.6KB)
  第2页: 尝试 1/8... ✓ 成功 (189.3KB)
  第3页: 已存在 ✓ 跳过
  ...
  ✓ 完成: 25/25

已用: 2.5分钟, 剩余: 247.5分钟

进度: [2/100]
[2] 第二章 离别

#### 状态图标说明

| 图标 | 含义 |
|:----:|:----:|
| ✓ 成功 | 图片下载成功 |
| 已存在 | 图片已存在，自动跳过 |
| 尝试 x/8 | 第 x 次尝试下载 |
| ⚠ 部分完成 | 该章节有图片未下载成功 |
| 被禁止访问 (403) | IP可能被封，等待30秒后重试 |

### 四、失败重试机制

#### 当下载失败时

如果某些图片下载失败，程序会显示：

⚠ 部分完成: 23/25

失败信息会自动记录到 failed.json 文件中：
```
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
```
#### 如何重试失败任务

在主菜单选择 **3. 重试失败**：

请输入选项: 3

找到 2 张失败图片，1 个失败章节

重试失败的图片...
  章节 1 第 024 页: 尝试 1/8... ✓ 成功
  章节 1 第 025 页: 尝试 1/8... ✓ 成功

重试失败的章节...
  [3] 第三章 重逢
  ...

### 五、下载文件结构

下载完成后，文件按以下结构组织：
```
📁 桌面/ComicDownload/
├── 📁 001_第一章 相遇/
│   ├── 🖼️ 001.webp
│   ├── 🖼️ 002.webp
│   ├── 🖼️ 003.webp
│   └── ...
├── 📁 002_第二章 离别/
│   ├── 🖼️ 001.webp
│   └── ...
├── 📁 003_第三章 重逢/
│   └── ...
└── ...
```
#### 命名规则

| 类型 | 格式 | 示例 |
|:----:|:----:|:----:|
| 章节文件夹 | {三位数编号}_{章节标题} | 001_第一章 相遇 |
| 图片文件 | {三位数页码}.{扩展名} | 001.webp |

💡 支持自动识别的图片格式：webp、jpg、jpeg、png

### 六、实用操作技巧

#### 1. 安全中断下载

- 按 Ctrl + C 可以随时安全中断程序
- 程序会自动保存失败记录到 failed.json
- 下次运行选择 **3. 重试失败** 即可继续下载

#### 2. 断点续传

- 已下载的图片会自动跳过（文件大小 >10KB 才视为有效）
- 即使中断后重新运行，也不会重复下载

#### 3. 快速启动脚本（Windows）

创建 run.bat 文件，内容如下：
```
@echo off
cd /d %~dp0
python comic_downloader.py
pause
```
双击即可运行，无需每次都打开命令行。

---

## ❓ 常见问题

### Q1: 下载时提示"找不到图片"，怎么办？

可能原因：
- ❌ Referer 设置不正确（必须设置为漫画网站域名）
- ❌ 网站有反爬虫机制
- ❌ 图片URL格式特殊

解决方法：
1. 检查 Referer 是否与漫画网站域名一致
2. 查看生成的 debug_*.html 文件分析页面结构
3. 可能需要修改正则表达式匹配规则（代码第200行附近）

### Q2: 下载速度太慢怎么办？

| 方法 | 说明 | 风险 |
|:----:|:----:|:----:|
| 降低图片延迟 | 将 IMAGE_DELAY 改为 1秒 | ⚠️ 易被封IP |
| 使用代理 | 开启代理分散请求 | ✅ 推荐 |
| 分批次下载 | 每次只下载30-50章 | ✅ 推荐 |
| 夜间下载 | 选择网络空闲时段 | ✅ 安全 |

### Q3: 出现403错误（被禁止访问）怎么办？

原因：IP可能被网站暂时封禁

解决步骤：
1. 程序会自动等待30秒后重试
2. 建议开启代理（见高级配置）
3. 增加章节间延迟（改为15-20秒）
4. 分批次下载，避免一次性请求太多

### Q4: 如何批量下载大量章节？

最佳实践：
- 每次下载不超过50章
- 设置章节间延迟为10-15秒
- 开启代理分散请求IP
- 可以夜间挂机下载（设置较大延迟）

### Q5: 支持哪些图片格式？

✅ 自动支持的格式：
- webp（默认格式）
- jpg / jpeg
- png
- gif（静态）
- bmp

程序会自动识别图片扩展名，如果无法识别，默认保存为 .webp 格式。

---

## ⚙️ 高级配置

### 1. 使用代理服务器

找到代码中的代理配置部分（约30-35行），修改为：

# 代理配置
```
PROXIES = {
    'http': 'http://127.0.0.1:7890',   # 替换为您的代理地址
    'https': 'http://127.0.0.1:7890'
}
```
# 是否启用代理
```
USE_PROXY = True  # False为禁用，True为启用
```
常见代理工具端口：

| 工具 | 默认端口 |
|:----:|:--------:|
| Clash | 7890 |
| V2Ray | 10809 |
| SS/SSR | 1080 |

### 2. 自定义请求头

修改 USER_AGENTS 列表，添加更多浏览器标识：
```
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15',
    'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36',
]
```
### 3. 调整下载参数

根据您的网络情况调整参数：
```
# 保守配置（不易被封，速度较慢）
IMAGE_DELAY = 5      # 图片间延迟5秒
CHAPTER_DELAY = 15   # 章节间延迟15秒
MAX_RETRIES = 10     # 最大重试10次

# 激进配置（速度快，易被封）
IMAGE_DELAY = 1      # 图片间延迟1秒
CHAPTER_DELAY = 3    # 章节间延迟3秒
MAX_RETRIES = 5      # 最大重试5次

# 平衡配置（推荐）
IMAGE_DELAY = 2      # 图片间延迟2秒
CHAPTER_DELAY = 8    # 章节间延迟8秒
MAX_RETRIES = 8      # 最大重试8次
```
### 4. 修改默认保存位置

找到代码：
```
import os

# 获取桌面路径
DESKTOP_PATH = os.path.join(os.path.expanduser('~'), 'Desktop')

# 修改默认保存目录
DEFAULT_SAVE_DIR = os.path.join(DESKTOP_PATH, '我的漫画')

# 或者自定义绝对路径
# DEFAULT_SAVE_DIR = r'D:\ComicDownload'
```
---

## 📄 许可证

本项目采用 **MIT 许可证** - 详见 LICENSE 文件

---

## ⚠️ 免责声明

本工具仅供学习交流使用，**请勿用于商业用途**。

- 下载的漫画请于 **24小时内删除**
- 请支持正版漫画创作
- 仅用于个人离线阅读
- 禁止用于任何商业目的
- 请遵守相关网站的服务条款

---

## 📞 联系方式

| 平台 | 链接 |
|:----:|:----:|
| 作者主页 | [@Tw1nkleDu5t](https://github.com/Tw1nkleDu5t) |
| 项目地址 | [ComicCrawler](https://github.com/Tw1nkleDu5t/ComicCrawler) |
| 提交Issue | [GitHub Issues](https://github.com/Tw1nkleDu5t/ComicCrawler/issues) |

---

<div align="center">
  
### ⭐ 如果这个项目对您有帮助，请给一个 Star 吧！ ⭐

**[⬆ 返回顶部](#-comiccrawler---通用漫画下载工具)**

</div>
