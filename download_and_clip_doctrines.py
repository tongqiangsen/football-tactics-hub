# -*- coding: utf-8 -*-
"""
Automated Pipeline for Fetching, Trimming, and Optimizing Real Match Tactical Clips
for the 8 Attacking Doctrines (八大实战进攻流派).
"""

import os
import subprocess
import sys
import imageio_ffmpeg

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "assets", "doctrines_video")
TEMP_DIR = os.path.join(OUTPUT_DIR, "_raw_temp")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
YT_DLP_EXE = os.path.join(BASE_DIR, ".venv", "Scripts", "yt-dlp.exe")

# 8 Tactical Doctrines Manifest
DOCTRINES = [
    {
        "id": "doctrine_01_third_man",
        "name": "流派① 第三人跑位渗透",
        "video_id": "7dc8baocH1E",
        "start": "00:05",
        "end": "00:11"
    },
    {
        "id": "doctrine_02_switch_play",
        "name": "流派② 强侧超载弱侧转移",
        "video_id": "IrpaLtQCIQo",
        "start": "00:15",
        "end": "00:21"
    },
    {
        "id": "doctrine_03_over_the_top",
        "name": "流派③ 纵深越顶反越位",
        "video_id": "HNpj-w_9U60",
        "start": "00:10",
        "end": "00:16"
    },
    {
        "id": "doctrine_04_counter_blitz",
        "name": "流派④ 攻防转换5秒闪击",
        "video_id": "aUWtgwO4HaA",
        "start": "00:20",
        "end": "00:26"
    },
    {
        "id": "doctrine_05_target_layoff",
        "name": "流派⑤ 空战中锋胸部做球",
        "video_id": "4aJWcl3JDzI",
        "start": "00:08",
        "end": "00:14"
    },
    {
        "id": "doctrine_06_cut_back",
        "name": "流派⑥ 禁区底线倒三角",
        "video_id": "6ZMZ9mW17G4",
        "start": "00:45",
        "end": "00:51"
    },
    {
        "id": "doctrine_07_dummy",
        "name": "流派⑦ 假接真漏特种破局",
        "video_id": "EczjXCPXmP4",
        "start": "00:06",
        "end": "00:12"
    },
    {
        "id": "doctrine_08_throwin",
        "name": "流派⑧ 战术界外球三角",
        "video_id": "8G8fBnPeiuI",
        "start": "00:12",
        "end": "00:18"
    }
]

def process_doctrine(item):
    doc_id = item["id"]
    name = item["name"]
    vid = item["video_id"]
    start = item["start"]
    end = item["end"]
    
    final_output = os.path.join(OUTPUT_DIR, f"{doc_id}.mp4")
    raw_output = os.path.join(TEMP_DIR, f"raw_{doc_id}.mp4")
    
    print(f"\n==========================================")
    print(f"▶ 正在处理: {name} ({doc_id})")
    print(f"  源视频: https://www.youtube.com/watch?v={vid} [{start} - {end}]")
    print(f"==========================================")
    
    # Step 1: Download section using yt-dlp with android client
    url = f"https://www.youtube.com/watch?v={vid}"
    ytdlp_cmd = [
        YT_DLP_EXE,
        "--ffmpeg-location", FFMPEG_EXE,
        "--extractor-args", "youtube:player_client=android",
        "--download-sections", f"*{start}-{end}",
        "-f", "18/best[height<=480]/best",
        "-o", raw_output,
        "--force-overwrites",
        url
    ]
    
    try:
        ret = subprocess.run(ytdlp_cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ yt-dlp 下载失败 ({doc_id}): {e}")
        return False
        
    if not os.path.exists(raw_output):
        # yt-dlp might output .mkv or .webm if format differs
        candidates = [os.path.join(TEMP_DIR, f) for f in os.listdir(TEMP_DIR) if f.startswith(f"raw_{doc_id}")]
        if candidates:
            raw_output = candidates[0]
        else:
            print(f"❌ 找不到下载文件 ({doc_id})")
            return False

    # Step 2: Strip audio, standardize MP4 container, ensure web compatibility
    print(f"⚡ 正在优化与静音: {final_output}")
    ffmpeg_cmd = [
        FFMPEG_EXE,
        "-y",
        "-i", raw_output,
        "-an", # No audio
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", "24",
        "-preset", "fast",
        final_output
    ]
    
    try:
        subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        file_size_kb = os.path.getsize(final_output) / 1024
        print(f"✅ 成功产出: {final_output} (大小: {file_size_kb:.1f} KB)")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ ffmpeg 转码失败 ({doc_id}): {e}")
        return False

def main():
    success_count = 0
    for doc in DOCTRINES:
        ok = process_doctrine(doc)
        if ok:
            success_count += 1
            
    print(f"\n==========================================")
    print(f"🎉 处理完成: {success_count}/{len(DOCTRINES)} 个流派实战切片已生成！")
    print(f"📁 资源目录: {OUTPUT_DIR}")
    print(f"==========================================")

if __name__ == "__main__":
    main()
