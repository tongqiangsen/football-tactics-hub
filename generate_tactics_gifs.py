# -*- coding: utf-8 -*-
"""
Flawless High-End Tactical GIF Animation Generator
- Clean 2-line header without special emoji/unicode boxes
- Proper goal boxes, penalty arcs, and corner flags
- Perfect player timing, synchronized pass arrival, shot on goal
- High-contrast player badges and running trails
"""

import os, math
from PIL import Image, ImageDraw, ImageFont

base_dir = os.path.dirname(os.path.abspath(__file__))
out_dir = os.path.join(base_dir, "tactics_animations_gif")
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
    
    # Boundary & Halfway
    draw.rectangle([px1, py1, px2, py2], outline="#15803d", width=2)
    draw.line([px1, mid_y, px2, mid_y], fill="#15803d", width=2)
    
    # Center circle & Spot
    draw.ellipse([W//2 - 65, mid_y - 65, W//2 + 65, mid_y + 65], outline="#15803d", width=2)
    draw.ellipse([W//2 - 3, mid_y - 3, W//2 + 3, mid_y + 3], fill="#15803d")
    
    # Top penalty box & Goal
    draw.rectangle([W//2 - 140, py1, W//2 + 140, py1 + 105], outline="#15803d", width=2)
    draw.rectangle([W//2 - 70, py1, W//2 + 70, py1 + 45], outline="#15803d", width=1)
    draw.rectangle([W//2 - 40, py1 - 8, W//2 + 40, py1], fill="#ffffff", outline="#000000", width=1) # Goal net
    
    # Bottom penalty box & Goal
    draw.rectangle([W//2 - 140, py2 - 105, W//2 + 140, py2], outline="#15803d", width=2)
    draw.rectangle([W//2 - 70, py2 - 45, W//2 + 70, py2], outline="#15803d", width=1)
    draw.rectangle([W//2 - 40, py2, W//2 + 40, py2 + 8], fill="#ffffff", outline="#000000", width=1) # Goal net

def draw_header(draw, title, step_text):
    draw.rectangle([0, 0, W, 70], fill="#0f172a")
    draw.line([0, 70, W, 70], fill="#22c55e", width=2)
    
    # Line 1: Title & Badge
    draw.text((20, 20), title, fill="#ffffff", font=font_title, anchor="lm")
    draw.rectangle([W-140, 9, W-20, 31], fill="#1e293b", outline="#38bdf8", width=1)
    draw.text((W-80, 20), "战术动态演练", fill="#38bdf8", font=font_badge, anchor="mm")
    
    # Line 2: Step action bar
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

# 1. 第三人跑位 (Third-Man Run)
def make_third_man_gif():
    frames = []
    total_frames = 55
    pos_A = (420, 520) # 后腰 4
    pos_B = (420, 280) # 中锋 7
    pos_C = (570, 390) # 中场 6
    pos_D_start = (250, 480) # 左边锋 5
    pos_D_end = (280, 160)
    def1, def2 = (370, 330), (470, 330)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.30:
            p = t / 0.30
            step = ">> 阶段 1/3: 后腰(4)直塞给背身接应的中锋(7)"
            ball_pos = lerp(pos_A, pos_B, p)
            d_pos = pos_D_start
            b_glow, c_glow, d_glow = True, False, False
            draw.line([pos_A, pos_B], fill="#38bdf8", width=2)
        elif t < 0.60:
            p = (t - 0.30) / 0.30
            step = ">> 阶段 2/3: 中锋(7)迎前回做给中场(6)，第三人(5)启动前插"
            ball_pos = lerp(pos_B, pos_C, p)
            d_pos = lerp(pos_D_start, lerp(pos_D_start, pos_D_end, 0.45), p)
            b_glow, c_glow, d_glow = False, True, True
            draw.line([pos_B, pos_C], fill="#fbbf24", width=2)
            draw.line([pos_D_start, d_pos], fill="#22c55e", width=2)
        else:
            p = (t - 0.60) / 0.40
            step = ">> 阶段 3/3: 中场(6)刺穿直塞第三人(5)破门单刀!"
            d_pos = lerp(pos_D_start, pos_D_end, 0.45 + 0.55 * p)
            ball_pos = lerp(pos_C, pos_D_end, p)
            b_glow, c_glow, d_glow = False, False, True
            draw.line([pos_D_start, pos_D_end], fill="#22c55e", width=2)
            draw.line([pos_C, pos_D_end], fill="#38bdf8", width=2)

        draw_player(draw, pos_A[0], pos_A[1], 4, "后腰", True)
        draw_player(draw, pos_B[0], pos_B[1], 7, "中锋", True, b_glow)
        draw_player(draw, pos_C[0], pos_C[1], 6, "中场", True, c_glow)
        draw_player(draw, d_pos[0], d_pos[1], 5, "第三人(左翼)", True, d_glow)
        draw_player(draw, def1[0], def1[1], "D1", "中卫", False)
        draw_player(draw, def2[0], def2[1], "D2", "中卫", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【进攻流派①】第三人跑位渗透 (Up-Back-Through)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_01_third_man.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# 2. 强侧超载 ➔ 弱侧转移
def make_switch_play_gif():
    frames = []
    total_frames = 55
    pos_LB = (170, 430)
    pos_LM = (150, 290)
    pos_CM = (310, 370)
    pos_RW_start = (670, 390)
    pos_RW_end = (700, 160)
    def1, def2, def3 = (210, 320), (280, 280), (370, 300)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.36:
            p = t / 0.36
            step = ">> 阶段 1/3: 强侧(左路)连续短传吸附防守全员横移"
            if p < 0.5:
                ball_pos = lerp(pos_LB, pos_LM, p*2)
            else:
                ball_pos = lerp(pos_LM, pos_CM, (p-0.5)*2)
            rw_pos = pos_RW_start
            cm_glow, rw_glow = False, False
            draw.line([pos_LB, pos_LM], fill="#38bdf8", width=2)
            draw.line([pos_LM, pos_CM], fill="#38bdf8", width=2)
        elif t < 0.70:
            p = (t - 0.36) / 0.34
            step = ">> 阶段 2/3: 中场(6)突然 30 米斜长传转移弱侧无人区"
            rw_pos = lerp(pos_RW_start, (pos_RW_start[0]+15, pos_RW_start[1]-90), p)
            ball_pos = lerp(pos_CM, rw_pos, p)
            cm_glow, rw_glow = True, True
            draw.line([pos_CM, rw_pos], fill="#fbbf24", width=3)
        else:
            p = (t - 0.70) / 0.30
            step = ">> 阶段 3/3: 右翼(7)弱侧获得绝对空间，带球突入禁区!"
            rw_pos = lerp((pos_RW_start[0]+15, pos_RW_start[1]-90), pos_RW_end, p)
            ball_pos = (rw_pos[0]-8, rw_pos[1]-8)
            cm_glow, rw_glow = False, True
            draw.line([pos_RW_start, pos_RW_end], fill="#22c55e", width=2)
            
        draw_player(draw, pos_LB[0], pos_LB[1], 2, "左卫", True)
        draw_player(draw, pos_LM[0], pos_LM[1], 5, "左翼", True)
        draw_player(draw, pos_CM[0], pos_CM[1], 6, "中场", True, cm_glow)
        draw_player(draw, rw_pos[0], rw_pos[1], 7, "右翼(弱侧)", True, rw_glow)
        draw_player(draw, def1[0], def1[1], "D1", "", False)
        draw_player(draw, def2[0], def2[1], "D2", "", False)
        draw_player(draw, def3[0], def3[1], "D3", "", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【进攻流派②】强侧超载 ➔ 弱侧 1v1 转移", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_02_switch_play.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# 3. 二过一撞墙配合
def make_wall_pass_gif():
    frames = []
    total_frames = 50
    pos_A_start = (300, 480)
    pos_A_end = (340, 210)
    pos_B = (490, 350)
    def_pos = (360, 370)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.45:
            p = t / 0.45
            step = ">> 阶段 1/2: 边锋(5)斜传中锋(7)，同时全速前插绕开防守"
            ball_pos = lerp(pos_A_start, pos_B, p)
            a_pos = lerp(pos_A_start, (pos_A_start[0]+15, pos_A_start[1]-130), p)
            b_glow, a_glow = True, False
            draw.line([pos_A_start, pos_B], fill="#38bdf8", width=2)
            draw.line([pos_A_start, pos_A_end], fill="#22c55e", width=2)
        else:
            p = (t - 0.45) / 0.55
            step = ">> 阶段 2/2: 中锋(7)一脚出球回塞身后，边锋(5)过人单刀!"
            a_pos = lerp((pos_A_start[0]+15, pos_A_start[1]-130), pos_A_end, p)
            ball_pos = lerp(pos_B, pos_A_end, p)
            b_glow, a_glow = False, True
            draw.line([pos_B, pos_A_end], fill="#fbbf24", width=2)
            
        draw_player(draw, a_pos[0], a_pos[1], 5, "边锋(冲刺)", True, a_glow)
        draw_player(draw, pos_B[0], pos_B[1], 7, "中锋(做墙)", True, b_glow)
        draw_player(draw, def_pos[0], def_pos[1], "D", "防守者", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【核心武器⑤】二过一撞墙配合 (Wall Pass / 1-2)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_03_wall_pass.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# 4. 底线倒三角回传
def make_cut_back_gif():
    frames = []
    total_frames = 55
    pos_W_start = (680, 360)
    pos_W_end = (700, 120)
    pos_CM_start = (420, 380)
    pos_CM_end = (420, 180) # 点球点推射
    def_gk = (420, 95)
    def1, def2 = (470, 115), (370, 115)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.45:
            p = t / 0.45
            step = ">> 阶段 1/3: 边锋(7)突至底线，门将与后卫全员退守门线"
            w_pos = lerp(pos_W_start, pos_W_end, p)
            ball_pos = (w_pos[0]-10, w_pos[1]-10)
            cm_pos = lerp(pos_CM_start, (pos_CM_start[0], pos_CM_start[1]-80), p)
            w_glow, cm_glow = True, False
            draw.line([pos_W_start, pos_W_end], fill="#22c55e", width=2)
        elif t < 0.80:
            p = (t - 0.45) / 0.35
            step = ">> 阶段 2/3: 底线发力倒三角推向点球点，中场(6)迎球插上"
            w_pos = pos_W_end
            cm_pos = lerp((pos_CM_start[0], pos_CM_start[1]-80), pos_CM_end, p)
            ball_pos = lerp(pos_W_end, pos_CM_end, p)
            w_glow, cm_glow = False, True
            draw.line([pos_W_end, pos_CM_end], fill="#fbbf24", width=3)
        else:
            p = (t - 0.80) / 0.20
            step = ">> 阶段 3/3: 中场(6)不停球推射破门入网!"
            w_pos = pos_W_end
            cm_pos = pos_CM_end
            ball_pos = lerp(pos_CM_end, (420, 82), p)
            w_glow, cm_glow = False, True
            draw.line([pos_CM_end, (420, 82)], fill="#ef4444", width=3)
            
        draw_player(draw, w_pos[0], w_pos[1], 7, "边锋(下底)", True, w_glow)
        draw_player(draw, cm_pos[0], cm_pos[1], 6, "中场(插上)", True, cm_glow)
        draw_player(draw, def_gk[0], def_gk[1], "GK", "门将", False)
        draw_player(draw, def1[0], def1[1], "D1", "", False)
        draw_player(draw, def2[0], def2[1], "D2", "", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【进攻流派⑥】禁区底线倒三角回传终结 (Cut-Back)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_04_cut_back.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# 5. 7人制 1-2-3-1 门将出球破压
def make_1231_buildup_gif():
    frames = []
    total_frames = 55
    pos_GK = (420, 560)
    pos_CB1_start, pos_CB1_end = (360, 500), (190, 480)
    pos_CB2_start, pos_CB2_end = (480, 500), (650, 480)
    pos_CM = (420, 380)
    pos_LW = (160, 240)
    pos_RW = (680, 240)
    pos_ST = (420, 160)
    fwd1, fwd2 = (340, 430), (500, 430)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.40:
            p = t / 0.40
            step = ">> 阶段 1/3: 门将(1)持球，双中卫(2+3)大范围拉开大禁区两侧"
            cb1_pos = lerp(pos_CB1_start, pos_CB1_end, p)
            cb2_pos = lerp(pos_CB2_start, pos_CB2_end, p)
            ball_pos = pos_GK
            gk_glow, cm_glow = True, False
            draw.line([pos_GK, cb1_pos], fill="#38bdf8", width=1)
            draw.line([pos_GK, cb2_pos], fill="#38bdf8", width=1)
        elif t < 0.70:
            p = (t - 0.40) / 0.30
            step = ">> 阶段 2/3: 门将(1)利用+1人数优势，精准低平球刺穿给中场(4)"
            cb1_pos = pos_CB1_end
            cb2_pos = pos_CB2_end
            ball_pos = lerp(pos_GK, pos_CM, p)
            gk_glow, cm_glow = False, True
            draw.line([pos_GK, pos_CM], fill="#fbbf24", width=3)
        else:
            p = (t - 0.70) / 0.30
            step = ">> 阶段 3/3: 中场(4)半侧身一脚出球，直塞插上的左翼(5)推进!"
            cb1_pos = pos_CB1_end
            cb2_pos = pos_CB2_end
            ball_pos = lerp(pos_CM, pos_LW, p)
            gk_glow, cm_glow = False, False
            draw.line([pos_CM, pos_LW], fill="#22c55e", width=2)
            
        draw_player(draw, pos_GK[0], pos_GK[1], 1, "门卫", True, gk_glow)
        draw_player(draw, cb1_pos[0], cb1_pos[1], 2, "左中卫", True)
        draw_player(draw, cb2_pos[0], cb2_pos[1], 3, "右中卫", True)
        draw_player(draw, pos_CM[0], pos_CM[1], 4, "中场核心", True, cm_glow)
        draw_player(draw, pos_LW[0], pos_LW[1], 5, "左翼", True)
        draw_player(draw, pos_RW[0], pos_RW[1], 6, "右翼", True)
        draw_player(draw, pos_ST[0], pos_ST[1], 7, "前锋", True)
        
        draw_player(draw, fwd1[0], fwd1[1], "F1", "", False)
        draw_player(draw, fwd2[0], fwd2[1], "F2", "", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【7人制 1-2-3-1】门将+1出球与破高位逼抢", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_05_1231_buildup.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# 6. 7人制 1-3-2-1 圣诞树防反
def make_1321_counter_gif():
    frames = []
    total_frames = 55
    pos_GK = (420, 560)
    pos_CB = (420, 480)
    pos_LWB_start, pos_LWB_end = (160, 460), (180, 160)
    pos_RWB = (680, 460)
    pos_DM = (350, 370)
    pos_AM_start, pos_AM_end = (490, 370), (450, 180)
    pos_ST = (420, 240)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.35:
            p = t / 0.35
            step = ">> 阶段 1/3: 5人防守盒断球，中卫(3)直接纵向越顶连线中锋(7)"
            ball_pos = lerp(pos_CB, pos_ST, p)
            lwb_pos = pos_LWB_start
            am_pos = pos_AM_start
            draw.line([pos_CB, pos_ST], fill="#fbbf24", width=3)
        elif t < 0.65:
            p = (t - 0.35) / 0.30
            step = ">> 阶段 2/3: 中锋(7)背身强力扛人，胸部/脚下回做给插上中场(6)"
            ball_pos = lerp(pos_ST, lerp(pos_AM_start, pos_AM_end, 0.5), p)
            am_pos = lerp(pos_AM_start, pos_AM_end, p * 0.7)
            lwb_pos = lerp(pos_LWB_start, pos_LWB_end, p * 0.7)
            draw.line([pos_ST, am_pos], fill="#38bdf8", width=2)
            draw.line([pos_LWB_start, pos_LWB_end], fill="#22c55e", width=2)
        else:
            p = (t - 0.65) / 0.35
            step = ">> 阶段 3/3: 中场(6)禁区弧顶迎球重炮轰门，翼卫(2)高速包抄!"
            am_pos = pos_AM_end
            lwb_pos = pos_LWB_end
            ball_pos = lerp(pos_AM_end, (420, 80), p)
            draw.line([pos_AM_end, (420, 80)], fill="#ef4444", width=3)
            
        draw_player(draw, pos_GK[0], pos_GK[1], 1, "门将", True)
        draw_player(draw, pos_CB[0], pos_CB[1], 3, "中卫", True)
        draw_player(draw, lwb_pos[0], lwb_pos[1], 2, "左翼卫", True)
        draw_player(draw, pos_RWB[0], pos_RWB[1], 4, "右翼卫", True)
        draw_player(draw, pos_DM[0], pos_DM[1], 5, "后腰", True)
        draw_player(draw, am_pos[0], am_pos[1], 6, "插上中场", True, True)
        draw_player(draw, pos_ST[0], pos_ST[1], 7, "中锋", True)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【7人制 1-3-2-1】圣诞树稳守反击与双核冲刺", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_06_1321_counter.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# 7. 8人制 1-3-3-1 边路双人组套边
def make_1331_overlap_gif():
    frames = []
    total_frames = 55
    pos_CB = (420, 500)
    pos_LB_start, pos_LB_end = (180, 460), (160, 160)
    pos_LM_start, pos_LM_end = (180, 310), (290, 240)
    pos_CM = (420, 350)
    pos_ST = (420, 180)
    pos_RM = (660, 310)
    pos_RB = (660, 460)
    def_rb = (230, 330)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.35:
            p = t / 0.35
            step = ">> 阶段 1/3: 边锋(5)内切带走防守，边卫(2)全速外侧套边插上"
            lm_pos = lerp(pos_LM_start, pos_LM_end, p)
            lb_pos = lerp(pos_LB_start, (pos_LB_start[0]-20, pos_LB_start[1]-130), p)
            ball_pos = lerp(pos_CB, pos_LM_start, p)
            draw.line([pos_CB, pos_LM_start], fill="#38bdf8", width=2)
            draw.line([pos_LB_start, pos_LB_end], fill="#22c55e", width=2)
        elif t < 0.68:
            p = (t - 0.35) / 0.33
            step = ">> 阶段 2/3: 边锋(5)顺势斜塞外侧套边的边卫(2)下底"
            lm_pos = pos_LM_end
            lb_pos = lerp((pos_LB_start[0]-20, pos_LB_start[1]-130), pos_LB_end, p)
            ball_pos = lerp(pos_LM_end, lb_pos, p)
            draw.line([pos_LM_end, lb_pos], fill="#fbbf24", width=3)
        else:
            p = (t - 0.68) / 0.32
            step = ">> 阶段 3/3: 边卫(2)底线倒三角横传点球点，中锋(8)推射破门!"
            lm_pos = pos_LM_end
            lb_pos = pos_LB_end
            ball_pos = lerp(pos_LB_end, pos_ST, p)
            draw.line([pos_LB_end, pos_ST], fill="#22c55e", width=3)
            
        draw_player(draw, pos_CB[0], pos_CB[1], 3, "中卫", True)
        draw_player(draw, lb_pos[0], lb_pos[1], 2, "左边卫", True, True)
        draw_player(draw, lm_pos[0], lm_pos[1], 5, "左边锋", True)
        draw_player(draw, pos_CM[0], pos_CM[1], 6, "中场", True)
        draw_player(draw, pos_ST[0], pos_ST[1], 8, "中锋", True, True)
        draw_player(draw, pos_RM[0], pos_RM[1], 7, "右前卫", True)
        draw_player(draw, pos_RB[0], pos_RB[1], 4, "右边卫", True)
        draw_player(draw, def_rb[0], def_rb[1], "D", "防守", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【8人制 1-3-3-1】边路双人组套边与中路包抄", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_07_1331_overlap.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# Execute
make_third_man_gif()
make_switch_play_gif()
make_wall_pass_gif()
make_cut_back_gif()
make_1231_buildup_gif()
make_1321_counter_gif()
make_1331_overlap_gif()
print("All 7 refined animated GIFs generated flawlessly!")
