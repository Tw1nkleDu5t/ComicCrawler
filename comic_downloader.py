#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
通用漫画下载工具
支持从漫画网站下载章节图片，自动重试，断点续传
"""

import sys
import traceback
sys.excepthook = lambda exctype, value, tb: print(''.join(traceback.format_exception(exctype, value, tb))) or input('\n发生错误，按回车键退出...')
import requests
import os
import time
import re
import json
import random

__version__ = '1.0.0'
__author__ = 'Your Name'
__license__ = 'MIT'

print('=' * 50)
print('通用漫画下载工具 v' + __version__)
print('=' * 50)

# ========== 初始配置（可修改或交互输入） ==========
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))                 # 获取脚本所在目录
DEFAULT_SAVE_DIR = os.path.join(SCRIPT_DIR, 'download')                 # 默认保存目录
DEFAULT_CHAPTERS_FILE = 'chapters.json'       # 默认章节文件路径
DEFAULT_REFERER = 'https://www.example.com/'  # 默认Referer，可修改
DEFAULT_MAX_RETRIES = 8
DEFAULT_TIMEOUT = 45
DEFAULT_IMAGE_DELAY = 2
DEFAULT_CHAPTER_DELAY = 8
DEFAULT_RETRY_DELAY = 5

# 代理配置（需要时取消注释并填写）
# PROXIES = {
#     'http': 'http://127.0.0.1:7890',
#     'https': 'http://127.0.0.1:7890'
# }
USE_PROXY = False

# 请求头池
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
]

# ========== 全局变量 ==========
SAVE_DIR = DEFAULT_SAVE_DIR
CHAPTERS_FILE = DEFAULT_CHAPTERS_FILE
MAX_RETRIES = DEFAULT_MAX_RETRIES
TIMEOUT = DEFAULT_TIMEOUT
IMAGE_DELAY = DEFAULT_IMAGE_DELAY
CHAPTER_DELAY = DEFAULT_CHAPTER_DELAY
RETRY_DELAY = DEFAULT_RETRY_DELAY
REFERER = DEFAULT_REFERER
FAILED_FILE = 'failed.json'

failed_images = []
failed_chapters = []
success_count = 0
total_images = 0
downloaded_images = 0
CHAPTERS = []

def get_headers():
    return {
        'User-Agent': random.choice(USER_AGENTS),
        'Referer': REFERER,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
    }

def setup_config():
    """交互式设置基本配置"""
    global SAVE_DIR, CHAPTERS_FILE, REFERER, MAX_RETRIES, TIMEOUT, IMAGE_DELAY, CHAPTER_DELAY, RETRY_DELAY
    
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    print('\n--- 初始配置 (可直接回车使用默认值) ---')
    save_dir = input(f'保存目录 (默认: {DEFAULT_SAVE_DIR}): ').strip()
    if save_dir:
        # 如果输入的是相对路径，转换为绝对路径
        if not os.path.isabs(save_dir):
            SAVE_DIR = os.path.join(script_dir, save_dir)
        else:
            SAVE_DIR = save_dir
    else:
        SAVE_DIR = DEFAULT_SAVE_DIR

    chapters_file = input(f'章节JSON文件路径 (默认: {DEFAULT_CHAPTERS_FILE}): ').strip()
    if chapters_file:
        CHAPTERS_FILE = chapters_file
    else:
        CHAPTERS_FILE = DEFAULT_CHAPTERS_FILE

    referer = input(f'Referer (默认: {DEFAULT_REFERER}): ').strip()
    if referer:
        REFERER = referer
    else:
        REFERER = DEFAULT_REFERER

    try:
        mr = input(f'最大重试次数 (默认: {DEFAULT_MAX_RETRIES}): ').strip()
        if mr:
            MAX_RETRIES = int(mr)
        tm = input(f'超时秒数 (默认: {DEFAULT_TIMEOUT}): ').strip()
        if tm:
            TIMEOUT = int(tm)
        idl = input(f'图片间延迟秒数 (默认: {DEFAULT_IMAGE_DELAY}): ').strip()
        if idl:
            IMAGE_DELAY = float(idl)
        cdl = input(f'章节间延迟秒数 (默认: {DEFAULT_CHAPTER_DELAY}): ').strip()
        if cdl:
            CHAPTER_DELAY = float(cdl)
        rdl = input(f'重试延迟秒数 (默认: {DEFAULT_RETRY_DELAY}): ').strip()
        if rdl:
            RETRY_DELAY = float(rdl)
    except ValueError:
        print('输入无效，将使用默认值')

    os.makedirs(SAVE_DIR, exist_ok=True)
    print('配置完成。\n')

def load_chapters():
    global CHAPTERS
    try:
        if not os.path.exists(CHAPTERS_FILE):
            print(f'错误: 章节文件不存在 - {CHAPTERS_FILE}')
            return False
        with open(CHAPTERS_FILE, 'r', encoding='utf-8') as f:
            CHAPTERS = json.load(f)
        print(f'成功加载 {len(CHAPTERS)} 章数据')
        return True
    except Exception as e:
        print(f'加载章节文件失败: {e}')
        return False

def download_image(img_url, file_path, chapter_order, page_num):
    global downloaded_images
    
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            if os.path.exists(file_path) and os.path.getsize(file_path) > 10240:
                downloaded_images += 1
                return True
            
            print(f'    尝试 {attempt}/{MAX_RETRIES}... ', end='')
            
            # 使用代理
            proxies = PROXIES if USE_PROXY else None
            
            resp = requests.get(img_url, headers=get_headers(), timeout=TIMEOUT, proxies=proxies)
            
            if resp.status_code == 200:
                if len(resp.content) < 1024:
                    print('图片太小')
                    if attempt < MAX_RETRIES:
                        time.sleep(RETRY_DELAY * attempt)
                        continue
                    return False
                
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                
                downloaded_images += 1
                print(f'✓ 成功 ({len(resp.content)/1024:.1f}KB)')
                return True
            elif resp.status_code == 403:
                print('被禁止访问 (403)，可能IP被封')
                if attempt < MAX_RETRIES:
                    time.sleep(30 * attempt)  # 被封后多等一会
                    continue
                return False
            else:
                print(f'HTTP {resp.status_code}')
                
        except Exception as e:
            print(f'错误: {str(e)[:30]}')
        
        if attempt < MAX_RETRIES:
            time.sleep(RETRY_DELAY * attempt)
    
    failed_images.append({'chapter': chapter_order, 'page': page_num, 'url': img_url})
    return False

def fetch_chapter_images(url):
    """获取章节图片列表"""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f'  获取图片列表 (尝试 {attempt}/{MAX_RETRIES})...')
            
            proxies = PROXIES if USE_PROXY else None
            resp = requests.get(url, headers=get_headers(), timeout=TIMEOUT, proxies=proxies)
            
            if resp.status_code == 200:
                html = resp.text
                
                # 多种匹配模式
                img_urls = re.findall(r'https?://[^"\']+?\.(?:webp|jpg|jpeg|png)', html)
                
                if not img_urls:
                    img_urls = re.findall(r'src=["\'](https?://[^"\']+?\.(?:webp|jpg|jpeg|png))["\']', html)
                
                if not img_urls:
                    img_urls = re.findall(r'data-src=["\'](https?://[^"\']+?\.(?:webp|jpg|jpeg|png))["\']', html)
                
                img_urls = list(dict.fromkeys(img_urls))  # 去重
                
                if img_urls:
                    print(f'  找到 {len(img_urls)} 张图片')
                    return img_urls
                else:
                    print('  没有找到图片URL')
                    # 保存HTML用于调试
                    with open(f'debug_{url.split("/")[-1]}.html', 'w', encoding='utf-8') as f:
                        f.write(html)
                    
            elif resp.status_code == 403:
                print('  被禁止访问，等待30秒...')
                time.sleep(30)
                continue
                
        except Exception as e:
            print(f'  错误: {e}')
        
        if attempt < MAX_RETRIES:
            time.sleep(RETRY_DELAY * attempt)
    
    return []

def download_chapter(chapter):
    order = chapter['order']
    title = chapter['title']
    url = chapter['url']
    
    safe_title = re.sub(r'[\\/*?:"<>|]', '', title)
    chapter_dir = os.path.join(SAVE_DIR, f"{order:03d}_{safe_title}")
    os.makedirs(chapter_dir, exist_ok=True)
    
    print(f'\n[{order}] {title}')
    
    img_urls = fetch_chapter_images(url)
    
    if not img_urls:
        print('  获取图片列表失败')
        failed_chapters.append(chapter)
        return False, 0, 0
    
    success = 0
    for i, img_url in enumerate(img_urls, 1):
        page_num = str(i).zfill(3)
        ext = img_url.split('.')[-1].split('?')[0]
        if ext not in ['webp', 'jpg', 'jpeg', 'png']:
            ext = 'webp'
        file_path = os.path.join(chapter_dir, f'{page_num}.{ext}')
        
        if os.path.exists(file_path) and os.path.getsize(file_path) > 10240:
            print(f'  第{i}页: 已存在')
            success += 1
            continue
        
        print(f'  第{i}页: ', end='')
        if download_image(img_url, file_path, order, page_num):
            success += 1
        
        if i < len(img_urls):
            time.sleep(IMAGE_DELAY)
    
    fully = (success == len(img_urls))
    if fully:
        print(f'  ✓ 完成: {success}/{len(img_urls)}')
    else:
        print(f'  ⚠ 部分完成: {success}/{len(img_urls)}')
        failed_chapters.append(chapter)
    
    return fully, success, len(img_urls)

def save_failed():
    try:
        with open(FAILED_FILE, 'w', encoding='utf-8') as f:
            json.dump({
                'failed_chapters': [{'order': c['order'], 'title': c['title'], 'url': c['url']} for c in failed_chapters],
                'failed_images': failed_images
            }, f, ensure_ascii=False, indent=2)
        print(f'\n失败记录已保存到 {FAILED_FILE}')
    except Exception as e:
        print(f'保存失败记录出错: {e}')

def retry_failed():
    global failed_images, failed_chapters
    
    if not os.path.exists(FAILED_FILE):
        print('没有失败记录文件')
        return
    
    try:
        with open(FAILED_FILE, 'r', encoding='utf-8') as f:
            failed = json.load(f)
        
        failed_images = failed.get('failed_images', [])
        failed_chapter_data = failed.get('failed_chapters', [])
        
        failed_chapters = []
        for fc in failed_chapter_data:
            chapter = next((c for c in CHAPTERS if c['order'] == fc['order']), None)
            if chapter:
                failed_chapters.append(chapter)
        
        print(f'\n找到 {len(failed_images)} 张失败图片，{len(failed_chapters)} 个失败章节')
        
        # 重试图片
        if failed_images:
            print('\n重试失败的图片...')
            new_failed = []
            for img in failed_images:
                chapter = next((c for c in CHAPTERS if c['order'] == img['chapter']), None)
                if not chapter:
                    continue
                
                safe_title = re.sub(r'[\\/*?:"<>|]', '', chapter['title'])
                chapter_dir = os.path.join(SAVE_DIR, f"{img['chapter']:03d}_{safe_title}")
                ext = img['url'].split('.')[-1].split('?')[0]
                file_path = os.path.join(chapter_dir, f"{img['page']}.{ext}")
                
                print(f'  章节 {img["chapter"]} 第 {img["page"]} 页')
                if not download_image(img['url'], file_path, img['chapter'], img['page']):
                    new_failed.append(img)
                
                time.sleep(IMAGE_DELAY)
            
            failed_images = new_failed
        
        # 重试章节
        if failed_chapters:
            print('\n重试失败的章节...')
            new_failed = []
            for chapter in failed_chapters:
                fully, _, _ = download_chapter(chapter)
                if not fully:
                    new_failed.append(chapter)
                time.sleep(CHAPTER_DELAY)
            
            failed_chapters = new_failed
        
        save_failed()
        
    except Exception as e:
        print(f'重试失败: {e}')

def download_range(start, end):
    global total_images, downloaded_images, success_count
    
    chapters_to_download = [c for c in CHAPTERS if start <= c['order'] <= end]
    
    if not chapters_to_download:
        print(f'没有找到章节 {start}-{end}')
        return
    
    print(f'准备下载 {len(chapters_to_download)} 章 (第{start}话-第{end}话)')
    confirm = input('按回车键开始下载，或输入n取消: ').strip().lower()
    if confirm == 'n':
        return
    
    start_time = time.time()
    
    for i, chapter in enumerate(chapters_to_download, 1):
        print(f'\n进度: [{i}/{len(chapters_to_download)}]')
        fully, succ, total = download_chapter(chapter)
        
        if fully:
            success_count += 1
        total_images += total
        
        if i % 5 == 0:
            elapsed = time.time() - start_time
            avg = elapsed / i
            remaining = avg * (len(chapters_to_download) - i)
            print(f'\n已用: {elapsed/60:.1f}分钟, 剩余: {remaining/60:.1f}分钟')
        
        if i < len(chapters_to_download):
            time.sleep(CHAPTER_DELAY)
    
    elapsed = time.time() - start_time
    print('\n' + '=' * 50)
    print('下载完成！')
    print(f'总章节: {len(chapters_to_download)}')
    print(f'成功章节: {success_count}')
    print(f'总图片: {total_images}')
    print(f'下载图片: {downloaded_images}')
    print(f'总用时: {elapsed/60:.1f} 分钟')
    print('=' * 50)

def main():
    setup_config()  # 先让用户配置
    
    if not load_chapters():
        input('\n按回车键退出...')
        return
    
    # 从配置中获取最大章节数用于下载全部
    max_order = max((c['order'] for c in CHAPTERS), default=0)
    
    while True:
        print('\n' + '=' * 50)
        print('请选择：')
        print('1. 下载全部')
        print('2. 指定范围')
        print('3. 重试失败')
        print('4. 测试下载 (前5章)')
        print('0. 退出')
        print('=' * 50)
        
        choice = input('请输入选项: ').strip()
        
        if choice == '0':
            break
        elif choice == '1':
            if max_order > 0:
                download_range(1, max_order)
            else:
                print('没有可用的章节')
        elif choice == '2':
            try:
                start = int(input('开始章节: '))
                end = int(input('结束章节: '))
                download_range(start, end)
            except:
                print('输入错误')
        elif choice == '3':
            retry_failed()
        elif choice == '4':
            download_range(1, min(5, max_order))
        else:
            print('无效选项')
        
        if choice in ['1', '2', '4'] and (failed_images or failed_chapters):
            save_failed()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n用户中断')
        if failed_images or failed_chapters:
            save_failed()
    except Exception as e:
        print(f'\n程序出错: {e}')
        traceback.print_exc()
    finally:
        input('\n按回车键退出...')