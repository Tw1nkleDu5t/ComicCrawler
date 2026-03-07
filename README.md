# 通用漫画下载工具

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

一个通用的漫画章节下载工具，支持从漫画网站批量下载图片，自动重试失败任务，断点续传。

## 📖 简介

本项目是一个通用的漫画下载脚本，可以从支持网页浏览的漫画网站下载章节图片。它通过解析章节页面的HTML，提取图片URL并进行下载。支持自动重试、失败记录、断点续传等功能。

## ✨ 特性

- 🔄 **自动重试**：网络不稳定时自动重试下载
- 📝 **失败记录**：记录下载失败的图片和章节，支持单独重试
- ⏸️ **断点续传**：已下载的图片自动跳过
- 🚀 **批量下载**：支持指定范围下载
- 🔧 **高度可配置**：延迟时间、重试次数、代理等均可自定义
- 📊 **进度显示**：显示下载进度和预计剩余时间

## 📋 安装

1. 克隆仓库：
```bash
git clone https://github.com/Tw1nkleDu5t/ComicCrawler
cd comic-downloader