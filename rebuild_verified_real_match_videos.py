# -*- coding: utf-8 -*-
"""
Download, Trim, Mute, and Save Verified 100% Real Match Footage for the 8 Attacking Doctrines.
"""

import os
import subprocess
import imageio_ffmpeg

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "assets", "doctrines_video")
TEMP_DIR = os.path.join(OUTPUT_DIR, "_tmp")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

FFMPEG_EXE = imageio_ffmpeg.get_ffmpeg_exe()
YT_DLP_EXE = os.path.join(BASE_DIR, ".venv", "Scripts", "yt-dlp.exe")

VERIFIED_MATCHES = [
    {
        "id": "doctrine_01_third_man",
        "name": "流派① 第三人跑位渗透 (阿森纳威尔希尔经典配合)",
        "url": "https://www.youtube.com/watch?v=Zj8Q-MaGM5g",
        "start": "00:02",
        "end": "00:08"
    },
    {
        "id": "doctrine_02_switch_play",
        "name": "流派② 强侧弱侧转移 (克罗斯大范围对角斜长传)",
        "url": "https://www.youtube.com/watch?v=EyKXf_1ZA6c",
        "start": "00:03",
        "end": "00:09"
    },
    {
        "id": "doctrine_03_over_the_top",
        "name": "流派③ 纵深越顶反越位 (埃德森70米长传哈兰德反越位)",
        "url": "https://www.youtube.com/watch?v=gfeUYoDXgJI",
        "start": "00:02",
        "end": "00:08"
    },
    {
        "id": "doctrine_04_counter_blitz",
        "name": "流派④ 攻防转换5秒闪击 (皇马对阿贾克斯四脚闪电战)",
        "url": "https://www.youtube.com/watch?v=PN2riyRDuZI",
        "start": "00:00",
        "end": "00:05"
    },
    {
        "id": "doctrine_05_target_layoff",
        "name": "流派⑤ 空战中锋胸部做球 (德罗巴经典胸部卸球转身爆射)",
        "url": "https://www.youtube.com/watch?v=bL03tfv6fCg",
        "start": "00:01",
        "end": "00:07"
    },
    {
        "id": "doctrine_06_cut_back",
        "name": "流派⑥ 禁区底线倒三角 (阿森纳底线倒三角厄德高助攻萨卡)",
        "url": "https://www.youtube.com/watch?v=7v0FLz3eh0c",
        "start": "00:08",
        "end": "00:14"
    },
    {
        "id": "doctrine_07_dummy",
        "name": "流派⑦ 假接真漏特种破局 (赛场无球漏球晃飞后卫)",
        "url": "https://www.youtube.com/watch?v=EczjXCPXmP4",
        "start": "00:06",
        "end": "00:12"
    },
    {
        "id": "doctrine_08_throwin",
        "name": "流派⑧ 战术界外球三角 (斯托克城德拉普界外球重炮)",
        "url": "https://www.youtube.com/watch?v=Mben3yvBstM",
        "start": "00:07",
        "end": "00:13"
    }
]

def process_one(item):
    doc_id = item["id"]
    name = item["name"]
    url = item["url"]
    start = item["start"]
    end = item["end"]
    
    final_mp4 = os.path.join(OUTPUT_DIR, f"{doc_id}.mp4")
    temp_clip = os.path.join(TEMP_DIR, f"temp_{doc_id}.mp4")
    
    print(f"\n▶ 正在生成: {name}")
    print(f"  源: {url} [{start} -> {end}]")
    
    # 1. Download slice
    cmd_dl = [
        YT_DLP_EXE,
        "--ffmpeg-location", FFMPEG_EXE,
        "--extractor-args", "youtube:player_client=android",
        "--download-sections", f"*{start}-{end}",
        "-f", "18/best[height<=480]/best",
        "-o", temp_clip,
        "--force-overwrites",
        url
    ]
    res_dl = subprocess.run(cmd_dl, capture_output=True, text=True)
    if res_dl.returncode != 0:
        print(f"❌ 下载失败: {res_dl.stderr}")
        return False
        
    # Check if downloaded
    real_temp = None
    for cand in [temp_clip, temp_clip + ".mp4", temp_clip + ".part"]:
        if os.path.exists(cand):
            real_temp = cand
            break
    if not real_temp:
        for f in os.listdir(TEMP_DIR):
            if f.startswith(f"temp_{doc_id}"):
                real_temp = os.path.join(TEMP_DIR, f)
                break
                
    if not real_temp or not os.path.exists(real_temp):
        print(f"❌ 找不到下载切片文件: {temp_clip}")
        return False
        
    # 2. Mute and transcode to final web mp4
    cmd_trans = [
        FFMPEG_EXE,
        "-y",
        "-i", real_temp,
        "-an", # strip audio
        "-c:v", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", "23",
        "-preset", "fast",
        final_mp4
    ]
    res_trans = subprocess.run(cmd_trans, capture_output=True, text=True)
    if res_trans.returncode != 0:
        print(f"❌ 转码失败: {res_trans.stderr}")
        return False
        
    size_kb = os.path.getsize(final_mp4) / 1024
    print(f"✅ 成功输出: {final_mp4} ({size_kb:.1f} KB)")
    return True

def main():
    success = 0
    for item in VERIFIED_MATCHES:
        if process_one(item):
            success += 1
            
    print(f"\n==========================================")
    print(f"🎉 全部处理完毕: {success}/{len(VERIFIED_MATCHES)} 成功！")
    print(f"==========================================")

if __name__ == "__main__":
    main()
