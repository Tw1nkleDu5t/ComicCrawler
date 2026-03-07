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

### 一分钟安装

```bash
# 1. 克隆仓库
git clone https://github.com/Tw1nkleDu5t/ComicCrawler.git
cd ComicCrawler

# 2. 安装依赖
pip install requests

# 3. 准备章节文件（见下文）
# 4. 运行程序
python comic_downloader.py
