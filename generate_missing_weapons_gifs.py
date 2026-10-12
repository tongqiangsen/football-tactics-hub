# -*- coding: utf-8 -*-
"""
Generate dedicated isolated animations for missing weapons:
W02 Chipped Through Ball
W04 Driven Low Cross
W06 Lay-off Pass
W07 Line-Breaking Laser Pass
W10 Touchline Channel Pass
W12 Recycling / Reset Pass
W13 No-Look Disguised Pass
W15 Reverse Diagonal Pass
W19 Set-piece Short Corner Cut-Back
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

def draw_ball(draw, x, y, scale=1.0):
    x, y = int(x), int(y)
    r = int(6 * scale)
    draw.ellipse([x-r-3, y-r-3, x+r+3, y+r+3], fill="#fbbf24")
    draw.ellipse([x-r, y-r, x+r, y+r], fill="#ffffff", outline="#000000", width=1)

def lerp(p1, p2, t):
    t = max(0.0, min(1.0, t))
    return p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t

def save_gif(frames, filename, duration=80):
    filepath = os.path.join(out_dir, filename)
    frames[0].save(filepath, save_all=True, append_images=frames[1:], duration=duration, loop=0, optimize=True)
    print(f"Saved: {filepath} ({len(frames)} frames)")

# ==============================================================================
# 1. W02: 肋部挑传空当 (Chipped Through Ball)
# ==============================================================================
def make_w02_gif():
    frames = []
    total_frames = 55
    cm_pos = (360, 470)
    winger_start, winger_end = (180, 360), (300, 220) # 左肋插上
    st_pos = (500, 260) # 中锋牵制右中卫
    def1 = (350, 310) # 密集防守中卫
    def2 = (440, 280)
    target_spot = (300, 220)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H), "#081810")
        d = ImageDraw.Draw(img)
        draw_pitch(d)
        
        if i < 18:
            step = "① 中场(4)持球观察，左边锋(5)从外侧突然折向内插左肋盲区"
            t = i / 18.0
            w_cur = lerp(winger_start, (230, 300), t)
            b_cur = cm_pos
            ball_scale = 1.0
        elif i < 36:
            step = "② 脚尖搓球底部制造回旋，皮球越过防守头顶落入肋部无人区"
            t = (i - 18) / 18.0
            w_cur = lerp((230, 300), winger_end, t)
            b_cur = lerp(cm_pos, target_spot, t)
            # Arc effect (scale up then down)
            arc_height = math.sin(t * math.pi)
            ball_scale = 1.0 + arc_height * 0.7
            # Trajectory
            d.line([cm_pos, b_cur], fill="#38bdf8", width=2)
        else:
            step = "③ 边锋(5)在肋部无人区顺势领球单刀破门！"
            t = (i - 36) / 18.0
            w_cur = lerp(winger_end, (340, 150), t)
            b_cur = lerp(target_spot, (340, 150), t)
            ball_scale = 1.0
            d.text((420, 120), "GOAL! 垫射球门近角！", fill="#fbbf24", font=font_title, anchor="mm")
            
        draw_header(d, "W 02 · 肋部挑传空当 (Chipped Through Ball)", step)
        draw_player(d, cm_pos[0], cm_pos[1], 4, "中场", True, glow=(i >= 16 and i <= 22))
        draw_player(d, w_cur[0], w_cur[1], 5, "边锋", True)
        draw_player(d, st_pos[0], st_pos[1], 7, "中锋", True)
        draw_player(d, def1[0], def1[1], 3, "后卫", False)
        draw_player(d, def2[0], def2[1], 4, "后卫", False)
        draw_player(d, 420, 95, 1, "门将", False)
        draw_ball(d, b_cur[0], b_cur[1], scale=ball_scale)
        
        frames.append(img)
    save_gif(frames, "anim_w02_chipped_through.gif")

# ==============================================================================
# 2. W04: 贴地横扫传中 (Driven Low Cross)
# ==============================================================================
def make_w04_gif():
    frames = []
    total_frames = 55
    winger_start, winger_end = (700, 380), (690, 190) # 右翼高速突底
    st_start, st_end = (460, 280), (450, 130) # 中锋抢前点
    gk_pos = (420, 95)
    def_pos = (510, 200) # 后卫被动退防转身困难
    
    cross_start = (690, 190)
    cross_end = (450, 130)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H), "#081810")
        d = ImageDraw.Draw(img)
        draw_pitch(d)
        
        if i < 20:
            step = "① 右边锋(7)高速下底突入禁区边缘，防线整体被迫退防门线"
            t = i / 20.0
            w_cur = lerp(winger_start, winger_end, t)
            b_cur = (w_cur[0] - 12, w_cur[1] - 8)
            st_cur = lerp(st_start, (460, 220), t)
        elif i < 35:
            step = "② 脚内侧大力贴地平抽门前走廊，球速极快专打后卫转身困难"
            t = (i - 20) / 15.0
            w_cur = winger_end
            st_cur = lerp((460, 220), st_end, t)
            b_cur = lerp(cross_start, cross_end, t)
            d.line([cross_start, b_cur], fill="#fbbf24", width=3)
        else:
            step = "③ 中锋(8)高速抢前点闪电垫射，防守与门将来不及反应破门！"
            w_cur = winger_end
            st_cur = st_end
            t = (i - 35) / 20.0
            b_cur = lerp(st_end, (420, 80), t)
            d.text((420, 150), "GOAL! 抢前点贴地折射入网！", fill="#fbbf24", font=font_title, anchor="mm")
            
        draw_header(d, "W 04 · 贴地横扫传中 (Driven Low Cross)", step)
        draw_player(d, w_cur[0], w_cur[1], 7, "边锋", True)
        draw_player(d, st_cur[0], st_cur[1], 8, "中锋", True, glow=(i >= 33))
        draw_player(d, def_pos[0], def_pos[1], 4, "中卫", False)
        draw_player(d, gk_pos[0], gk_pos[1], 1, "门将", False)
        draw_ball(d, b_cur[0], b_cur[1])
        
        frames.append(img)
    save_gif(frames, "anim_w04_driven_cross.gif")

# ==============================================================================
# 3. W06: 迎前回敲做球 (Lay-off Pass)
# ==============================================================================
def make_w06_gif():
    frames = []
    total_frames = 55
    cm4_pos = (360, 520) # 后腰发起
    st_start, st_receive = (420, 250), (420, 310) # 中锋迎前背身
    cm6_start, cm6_shoot = (320, 440), (390, 330) # 插上中场迎球射门
    def_pos = (420, 230) # 贴身中卫
    
    layoff_target = (390, 330)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H), "#081810")
        d = ImageDraw.Draw(img)
        draw_pitch(d)
        
        if i < 16:
            step = "① 中锋(7)突然迎前撤出禁区背身接应，吸引后卫紧逼上抢"
            t = i / 16.0
            st_cur = lerp(st_start, st_receive, t)
            cm6_cur = lerp(cm6_start, (340, 400), t)
            b_cur = lerp(cm4_pos, st_receive, t)
            d.line([cm4_pos, b_cur], fill="#38bdf8", width=2)
        elif i < 30:
            step = "② 中锋一脚软推回敲空当，出球温和不减速供二梯队迎球"
            t = (i - 16) / 14.0
            st_cur = st_receive
            cm6_cur = lerp((340, 400), cm6_shoot, t)
            b_cur = lerp(st_receive, layoff_target, t)
            d.line([st_receive, b_cur], fill="#fbbf24", width=3)
        else:
            step = "③ 插上中场(6)不停球迎球正脚背重炮轰门破网！"
            st_cur = st_receive
            cm6_cur = cm6_shoot
            t = (i - 30) / 25.0
            b_cur = lerp(layoff_target, (415, 80), t)
            d.line([layoff_target, b_cur], fill="#22c55e", width=3)
            d.text((420, 140), "GOAL! 迎球不停球直接重炮轰门！", fill="#fbbf24", font=font_title, anchor="mm")
            
        draw_header(d, "W 06 · 迎前回敲做球 (Lay-off Pass)", step)
        draw_player(d, cm4_pos[0], cm4_pos[1], 4, "后腰", True)
        draw_player(d, st_cur[0], st_cur[1], 7, "中锋", True, glow=(15 <= i <= 22))
        draw_player(d, cm6_cur[0], cm6_cur[1], 6, "插上中场", True, glow=(i >= 28))
        draw_player(d, def_pos[0], def_pos[1], 3, "中卫", False)
        draw_player(d, 420, 95, 1, "门将", False)
        draw_ball(d, b_cur[0], b_cur[1])
        
        frames.append(img)
    save_gif(frames, "anim_w06_layoff_pass.gif")

# ==============================================================================
# 4. W07: 刺穿线形传球 (Line-Breaking Laser Pass)
# ==============================================================================
def make_w07_gif():
    frames = []
    total_frames = 55
    cb_pos = (420, 560) # 中卫持球
    am_target = (420, 310) # 前腰在两线之间空当接应
    
    # Opponent lines
    fw1, fw2 = (380, 480), (460, 480) # 逼抢锋线
    mf1, mf2 = (360, 390), (480, 390) # 中场线
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H), "#081810")
        d = ImageDraw.Draw(img)
        draw_pitch(d)
        
        # Draw opposing defensive horizontal lines
        d.line([(320, 480), (520, 480)], fill="#ef4444", width=1)
        d.text((540, 480), "第一道锋线", fill="#f87171", font=font_small, anchor="lm")
        d.line([(300, 390), (540, 390)], fill="#ef4444", width=1)
        d.text((560, 390), "第二道中场线", fill="#f87171", font=font_small, anchor="lm")
        
        if i < 15:
            step = "① 前腰(6)悄然游弋至对方中卫与中场之间的巨大真空口袋区"
            b_cur = cb_pos
            am_cur = lerp((420, 360), am_target, i/15.0)
        elif i < 35:
            step = "② 中卫(3)正脚背贴地重炮激光直塞，0.3秒连续穿透双层防线！"
            t = (i - 15) / 20.0
            am_cur = am_target
            b_cur = lerp(cb_pos, am_target, t)
            d.line([cb_pos, b_cur], fill="#38bdf8", width=4)
        else:
            step = "③ 前腰在防线结合部半转身拿球，正面冲击对手最后一条后卫线！"
            am_cur = am_target
            t = (i - 35) / 20.0
            b_cur = lerp(am_target, (420, 240), t)
            d.text((420, 210), "破线成功！正面对决后卫线！", fill="#22c55e", font=font_title, anchor="mm")
            
        draw_header(d, "W 07 · 刺穿线形传球 (Line-Breaking Laser Pass)", step)
        draw_player(d, cb_pos[0], cb_pos[1], 3, "中卫", True, glow=(13 <= i <= 18))
        draw_player(d, am_cur[0], am_cur[1], 6, "前腰", True, glow=(i >= 33))
        draw_player(d, fw1[0], fw1[1], 9, "前锋", False)
        draw_player(d, fw2[0], fw2[1], 10, "前锋", False)
        draw_player(d, mf1[0], mf1[1], 6, "中场", False)
        draw_player(d, mf2[0], mf2[1], 8, "中场", False)
        draw_ball(d, b_cur[0], b_cur[1])
        
        frames.append(img)
    save_gif(frames, "anim_w07_line_breaking.gif")

# ==============================================================================
# 5. W10: 边线贴地推进球 (Touchline Channel Pass)
# ==============================================================================
def make_w10_gif():
    frames = []
    total_frames = 55
    lb_pos = (75, 480) # 紧贴左边线
    winger_start, winger_end = (75, 340), (75, 170)
    def_winger = (130, 440) # 封堵内线的边锋
    def_back = (120, 220)
    
    target_pos = (75, 170)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H), "#081810")
        d = ImageDraw.Draw(img)
        draw_pitch(d)
        
        # Highlight touchline
        d.line([(40, 80), (40, H-25)], fill="#38bdf8", width=3)
        
        if i < 16:
            step = "① 边路内线传球角度被完全封堵，边后卫(2)沿边线向前观察"
            b_cur = lb_pos
            w_cur = winger_start
        elif i < 34:
            step = "② 贴边线外侧大力推地平直塞，边锋(5)从外侧启动超车"
            t = (i - 16) / 18.0
            w_cur = lerp(winger_start, winger_end, t)
            b_cur = lerp(lb_pos, target_pos, t)
            d.line([lb_pos, b_cur], fill="#fbbf24", width=3)
        else:
            step = "③ 边锋顺边线全速趟球杀入前场进攻三区！"
            t = (i - 34) / 21.0
            w_cur = lerp(winger_end, (110, 110), t)
            b_cur = (w_cur[0] + 10, w_cur[1] - 8)
            d.text((420, 150), "破逼抢！边路通道高速打通！", fill="#22c55e", font=font_title, anchor="mm")
            
        draw_header(d, "W 10 · 边线贴地推进球 (Channel Pass)", step)
        draw_player(d, lb_pos[0], lb_pos[1], 2, "边卫", True, glow=(14 <= i <= 20))
        draw_player(d, w_cur[0], w_cur[1], 5, "边锋", True)
        draw_player(d, def_winger[0], def_winger[1], 7, "逼抢", False)
        draw_player(d, def_back[0], def_back[1], 2, "边卫", False)
        draw_ball(d, b_cur[0], b_cur[1])
        
        frames.append(img)
    save_gif(frames, "anim_w10_channel_pass.gif")

# ==============================================================================
# 6. W12: 回传重新组织球 (Recycling / Reset Pass)
# ==============================================================================
def make_w12_gif():
    frames = []
    total_frames = 55
    winger_trap = (120, 240)
    def1, def2 = (150, 210), (120, 200) # 包夹逼入死胡同
    cb_pos = (420, 520) # 拖后中卫
    rb_pos = (720, 320) # 弱侧右边后卫大空当
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H), "#081810")
        d = ImageDraw.Draw(img)
        draw_pitch(d)
        
        if i < 18:
            step = "① 强侧左路陷入双人包夹死胡同，强行突破极易丢球"
            b_cur = winger_trap
            d.ellipse([winger_trap[0]-45, winger_trap[1]-45, winger_trap[0]+45, winger_trap[1]+45], outline="#ef4444", width=2)
            d.text((winger_trap[0]+60, winger_trap[1]), "死胡同包夹", fill="#f87171", font=font_small, anchor="lm")
        elif i < 34:
            step = "② 拒绝盲目下底！果断倒脚回传拖后中卫(3)，全队阵型横向展开"
            t = (i - 18) / 16.0
            b_cur = lerp(winger_trap, cb_pos, t)
            d.line([winger_trap, b_cur], fill="#38bdf8", width=3)
        else:
            step = "③ 中卫不停球顺势大范围横敲弱侧右边卫(4)，重获开阔进攻面！"
            t = (i - 34) / 21.0
            b_cur = lerp(cb_pos, rb_pos, t)
            d.line([cb_pos, b_cur], fill="#fbbf24", width=3)
            d.text((rb_pos[0]-80, rb_pos[1]-30), "弱侧大空当！", fill="#22c55e", font=font_step, anchor="mm")
            
        draw_header(d, "W 12 · 回传重新组织球 (Recycling / Reset Pass)", step)
        draw_player(d, winger_trap[0], winger_trap[1], 5, "边锋", True)
        draw_player(d, cb_pos[0], cb_pos[1], 3, "中卫", True, glow=(32 <= i <= 38))
        draw_player(d, rb_pos[0], rb_pos[1], 4, "右卫", True)
        draw_player(d, def1[0], def1[1], 7, "夹击", False)
        draw_player(d, def2[0], def2[1], 2, "夹击", False)
        draw_ball(d, b_cur[0], b_cur[1])
        
        frames.append(img)
    save_gif(frames, "anim_w12_recycling.gif")

# ==============================================================================
# 7. W13: 不看人隐蔽传球 (No-Look Disguised Pass)
# ==============================================================================
def make_w13_gif():
    frames = []
    total_frames = 55
    am_pos = (420, 360) # 前腰持球
    left_runner = (240, 240) # 左侧假跑位吸引防守
    right_winger = (620, 220) # 右侧真实空当接应
    def_center = (420, 290) # 防守球员被眼神完全欺骗
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H), "#081810")
        d = ImageDraw.Draw(img)
        draw_pitch(d)
        
        if i < 20:
            step = "① 前腰(6)身体朝向与视线坚决盯向左路，诱使后卫重心向左偏移"
            b_cur = am_pos
            # Gaze cone to left
            d.line([am_pos, left_runner], fill="#f87171", width=2)
            d.text((310, 290), "虚假视线欺骗", fill="#f87171", font=font_small, anchor="mm")
            def_pos = lerp((420, 290), (370, 290), i/20.0)
        elif i < 36:
            step = "② 眼神不转！出球瞬间脚腕突然外拨，反向送右侧大空当！"
            t = (i - 20) / 16.0
            def_pos = (370, 290)
            b_cur = lerp(am_pos, right_winger, t)
            d.line([am_pos, b_cur], fill="#fbbf24", width=3)
        else:
            step = "③ 防守被完全晃开扑向虚无，右翼(7)无人盯防插上单刀！"
            def_pos = (370, 290)
            t = (i - 36) / 19.0
            b_cur = lerp(right_winger, (560, 130), t)
            draw_player(d, b_cur[0], b_cur[1], 7, "右翼", True)
            d.text((420, 150), "声东击西！防线重心被彻底撕裂！", fill="#22c55e", font=font_title, anchor="mm")
            
        draw_header(d, "W 13 · 不看人隐蔽传球 (No-Look Disguised Pass)", step)
        draw_player(d, am_pos[0], am_pos[1], 6, "前腰", True, glow=(18 <= i <= 24))
        draw_player(d, left_runner[0], left_runner[1], 5, "左翼", True)
        if i < 36:
            draw_player(d, right_winger[0], right_winger[1], 7, "右翼", True)
        draw_player(d, def_pos[0], def_pos[1], 4, "中卫", False)
        draw_ball(d, b_cur[0], b_cur[1])
        
        frames.append(img)
    save_gif(frames, "anim_w13_no_look.gif")

# ==============================================================================
# 8. W15: 反向对角塞球 (Reverse Diagonal Pass)
# ==============================================================================
def make_w15_gif():
    frames = []
    total_frames = 55
    start_dribble = (540, 380)
    end_dribble = (360, 380) # 横向盘带吸引防线向左移动
    st_run_start, st_run_end = (460, 260), (520, 180) # 前锋反向切身后
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H), "#081810")
        d = ImageDraw.Draw(img)
        draw_pitch(d)
        
        if i < 20:
            step = "① 持球人(6)大步横向盘带，牵引整条后卫线集体同向横移"
            t = i / 20.0
            p_cur = lerp(start_dribble, end_dribble, t)
            b_cur = (p_cur[0] - 12, p_cur[1] + 6)
            def1 = lerp((500, 300), (430, 300), t)
            def2 = lerp((420, 300), (350, 300), t)
            d.line([start_dribble, p_cur], fill="#38bdf8", width=2)
        elif i < 36:
            step = "② 突然逆着后卫横移惯性，脚腕切出反向右对角贴地直塞！"
            t = (i - 20) / 16.0
            p_cur = end_dribble
            def1, def2 = (430, 300), (350, 300)
            b_cur = lerp(end_dribble, st_run_end, t)
            st_cur = lerp(st_run_start, st_run_end, t)
            d.line([end_dribble, b_cur], fill="#fbbf24", width=3)
        else:
            step = "③ 后卫重心逆向难以及时回追，前锋(8)反跑切入单刀破门！"
            p_cur = end_dribble
            def1, def2 = (430, 300), (350, 300)
            t = (i - 36) / 19.0
            b_cur = lerp(st_run_end, (470, 90), t)
            st_cur = (b_cur[0] - 8, b_cur[1] + 12)
            d.text((420, 140), "GOAL! 打破防守横向惯性！", fill="#fbbf24", font=font_title, anchor="mm")
            
        draw_header(d, "W 15 · 反向对角塞球 (Reverse Diagonal Pass)", step)
        draw_player(d, p_cur[0], p_cur[1], 6, "前腰", True, glow=(18 <= i <= 24))
        draw_player(d, (st_cur[0] if i>=20 else st_run_start[0]), (st_cur[1] if i>=20 else st_run_start[1]), 8, "中锋", True)
        draw_player(d, def1[0], def1[1], 3, "中卫", False)
        draw_player(d, def2[0], def2[1], 4, "中卫", False)
        draw_player(d, 420, 95, 1, "门将", False)
        draw_ball(d, b_cur[0], b_cur[1])
        
        frames.append(img)
    save_gif(frames, "anim_w15_reverse_diagonal.gif")

# ==============================================================================
# 9. W19: 定位球低平倒三角 (Set-piece Short Cross / Cut-Back)
# ==============================================================================
def make_w19_gif():
    frames = []
    total_frames = 55
    corner_flag = (790, 90) # 角球区
    short_receiver = (730, 180) # 战术角球接应人
    box_runner = (420, 240) # 点球点包抄推射队员
    
    byline_in = (690, 110)
    cutback_target = (460, 210)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H), "#081810")
        d = ImageDraw.Draw(img)
        draw_pitch(d)
        
        if i < 16:
            step = "① 角球发2人战术短传给接应队友(5)，主罚队员(7)迅速沿底线内插"
            t = i / 16.0
            b_cur = lerp(corner_flag, short_receiver, t)
            p7_cur = lerp(corner_flag, byline_in, t)
            d.line([corner_flag, b_cur], fill="#38bdf8", width=2)
        elif i < 28:
            step = "② 接应队友顺势回推底线二过一，主罚队员突入禁区形成倒三角角度"
            t = (i - 16) / 12.0
            p7_cur = byline_in
            b_cur = lerp(short_receiver, byline_in, t)
            d.line([short_receiver, byline_in], fill="#38bdf8", width=2)
        elif i < 40:
            step = "③ 底线大力平抽倒三角推向点球点，后插上中场(6)拍马赶到！"
            t = (i - 28) / 12.0
            p7_cur = byline_in
            b_cur = lerp(byline_in, cutback_target, t)
            d.line([byline_in, cutback_target], fill="#fbbf24", width=3)
        else:
            step = "④ 点球点不停球推射球门反角！战术角球轻松打穿死防守！"
            p7_cur = byline_in
            t = (i - 40) / 15.0
            b_cur = lerp(cutback_target, (410, 80), t)
            d.text((420, 150), "GOAL! 战术角球倒三角破门！", fill="#fbbf24", font=font_title, anchor="mm")
            
        draw_header(d, "W 19 · 定位球低平倒三角 (Set-piece Short Cross)", step)
        draw_player(d, p7_cur[0], p7_cur[1], 7, "边锋", True)
        draw_player(d, short_receiver[0], short_receiver[1], 5, "边前", True)
        draw_player(d, box_runner[0], box_runner[1], 6, "插上中场", True, glow=(i >= 38))
        draw_player(d, 520, 130, 4, "后卫", False)
        draw_player(d, 420, 95, 1, "门将", False)
        draw_ball(d, b_cur[0], b_cur[1])
        
        frames.append(img)
    save_gif(frames, "anim_w19_setpiece_cutback.gif")

if __name__ == "__main__":
    print("Generating dedicated GIFs for missing weapons...")
    make_w02_gif()
    make_w04_gif()
    make_w06_gif()
    make_w07_gif()
    make_w10_gif()
    make_w12_gif()
    make_w13_gif()
    make_w15_gif()
    make_w19_gif()
    print("All 9 dedicated GIFs generated successfully!")
