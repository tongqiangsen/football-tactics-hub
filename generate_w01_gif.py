# -*- coding: utf-8 -*-
"""
Generate dedicated isolated animation for Weapon 01: 直塞穿透球 (Through Ball)
Demonstrates: CM delivering driven ground ball slicing through two center-backs, ST running onto it to score.
"""

import os, math
from PIL import Image, ImageDraw, ImageFont

out_dir = r"e:\06_Study\书籍\足球\tactics_animations_gif"
os.makedirs(out_dir, exist_ok=True)

W, H = 840, 640

def get_font(size, bold=False):
    font_file = "msyhbd.ttc" if bold else "msyh.ttc"
    try:
        return ImageFont.truetype(f"C:\\Windows\\Fonts\\{font_file}", size)
    except Exception:
        try:
            return ImageFont.truetype("C:\\Windows\\Fonts\\msyh.ttc", size)
        except Exception:
            return ImageFont.load_default()

font_title = get_font(17, bold=True)
font_badge = get_font(12, bold=True)
font_step = get_font(14, bold=True)
font_lbl = get_font(13, bold=True)
font_small = get_font(11, bold=True)

def draw_pitch(draw):
    draw.rectangle([0, 0, W, H], fill="#081810")
    px1, py1, px2, py2 = 40, 80, W-40, H-25
    mid_y = (py1 + py2) // 2
    
    draw.rectangle([px1, py1, px2, py2], outline="#15803d", width=2)
    draw.line([px1, mid_y, px2, mid_y], fill="#15803d", width=2)
    
    draw.ellipse([W//2 - 65, mid_y - 65, W//2 + 65, mid_y + 65], outline="#15803d", width=2)
    draw.ellipse([W//2 - 3, mid_y - 3, W//2 + 3, mid_y + 3], fill="#15803d")
    
    # Top box & goal
    draw.rectangle([W//2 - 140, py1, W//2 + 140, py1 + 105], outline="#15803d", width=2)
    draw.rectangle([W//2 - 70, py1, W//2 + 70, py1 + 45], outline="#15803d", width=1)
    draw.rectangle([W//2 - 40, py1 - 8, W//2 + 40, py1], fill="#ffffff", outline="#000000", width=1)
    
    # Bottom box & goal
    draw.rectangle([W//2 - 140, py2 - 105, W//2 + 140, py2], outline="#15803d", width=2)
    draw.rectangle([W//2 - 70, py2 - 45, W//2 + 70, py2], outline="#15803d", width=1)
    draw.rectangle([W//2 - 40, py2, W//2 + 40, py2 + 8], fill="#ffffff", outline="#000000", width=1)

def draw_header(draw, title, step_text):
    draw.rectangle([0, 0, W, 70], fill="#0f172a")
    draw.line([0, 70, W, 70], fill="#22c55e", width=2)
    
    draw.text((20, 20), title, fill="#ffffff", font=font_title, anchor="lm")
    draw.rectangle([W-140, 9, W-20, 31], fill="#1e293b", outline="#38bdf8", width=1)
    draw.text((W-80, 20), "武器专属演练", fill="#38bdf8", font=font_badge, anchor="mm")
    
    draw.rectangle([20, 38, W-20, 62], fill="#14281f", outline="#10b981", width=1)
    draw.text((32, 50), step_text, fill="#fbbf24", font=font_step, anchor="lm")

def draw_player(draw, x, y, num, name, is_white=True, glow=False):
    x, y = int(x), int(y)
    r = 15
    if glow:
        draw.ellipse([x-r-5, y-r-5, x+r+5, y+r+5], fill="#fbbf24")
    
    if is_white:
        draw.ellipse([x-r, y-r, x+r, y+r], fill="#ffffff", outline="#0284c7", width=2)
        draw.text((x, y-1), str(num), fill="#0f172a", font=font_lbl, anchor="mm")
        if name:
            tw = len(name) * 12
            draw.rectangle([x-tw//2-4, y+16, x+tw//2+4, y+30], fill="#071710", outline="#0284c7", width=1)
            draw.text((x, y+23), name, fill="#38bdf8", font=font_small, anchor="mm")
    else:
        draw.ellipse([x-r, y-r, x+r, y+r], fill="#ef4444", outline="#7f1d1d", width=2)
        draw.text((x, y-1), str(num), fill="#ffffff", font=font_lbl, anchor="mm")
        if name:
            tw = len(name) * 12
            draw.rectangle([x-tw//2-4, y+16, x+tw//2+4, y+30], fill="#1a0808", outline="#ef4444", width=1)
            draw.text((x, y+23), name, fill="#fca5a5", font=font_small, anchor="mm")

def draw_ball(draw, x, y):
    x, y = int(x), int(y)
    r = 6
    draw.ellipse([x-r-3, y-r-3, x+r+3, y+r+3], fill="#fbbf24")
    draw.ellipse([x-r, y-r, x+r, y+r], fill="#ffffff", outline="#000000", width=1)

def lerp(p1, p2, t):
    t = max(0.0, min(1.0, t))
    return p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t

def make_w01_through_ball_gif():
    frames = []
    total_frames = 55
    pos_CM = (420, 480) # 中场持球
    pos_ST_start, pos_ST_end = (420, 340), (420, 150) # 中锋前插
    def1_start, def1_end = (365, 320), (380, 260) # 双中卫夹击
    def2_start, def2_end = (475, 320), (460, 260)
    def_gk = (420, 95)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.35:
            p = t / 0.35
            step = ">> 阶段 1/3: 中场(4)抬头观察两名中卫结合部空隙，中锋(7)反向摆脱准备前插"
            cm_pos = pos_CM
            st_pos = pos_ST_start
            ball_pos = pos_CM
            def1 = def1_start
            def2 = def2_start
            draw.line([pos_CM, (pos_CM[0], pos_CM[1]-40)], fill="#38bdf8", width=2)
        elif t < 0.70:
            p = (t - 0.35) / 0.35
            step = ">> 阶段 2/3: [W01 直塞穿透] 脚内侧发力平推刺穿双人结合部！给足前插提前量"
            cm_pos = pos_CM
            st_pos = lerp(pos_ST_start, pos_ST_end, p)
            ball_pos = lerp(pos_CM, pos_ST_end, p)
            def1 = lerp(def1_start, def1_end, p*0.4)
            def2 = lerp(def2_start, def2_end, p*0.4)
            draw.line([pos_CM, pos_ST_end], fill="#fbbf24", width=3)
            draw.line([pos_ST_start, pos_ST_end], fill="#22c55e", width=2)
        else:
            p = (t - 0.70) / 0.30
            step = ">> 阶段 3/3: 中锋(7)高速超车形成单刀，面对出击门将轻推远角死角破门!"
            cm_pos = pos_CM
            st_pos = pos_ST_end
            ball_pos = lerp(pos_ST_end, (400, 82), p)
            def1 = def1_end
            def2 = def2_end
            draw.line([pos_ST_end, (400, 82)], fill="#ef4444", width=3)
            
        draw_player(draw, cm_pos[0], cm_pos[1], 4, "中场/直塞", True, t<0.7)
        draw_player(draw, st_pos[0], st_pos[1], 7, "中锋(单刀)", True, t>=0.35)
        draw_player(draw, def1[0], def1[1], "D1", "中卫", False)
        draw_player(draw, def2[0], def2[1], "D2", "中卫", False)
        draw_player(draw, def_gk[0], def_gk[1], "GK", "门将", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【Weapon 01】直塞穿透球 (Through Ball · 贴地刺穿防线)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_w01_through_ball.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

make_w01_through_ball_gif()
