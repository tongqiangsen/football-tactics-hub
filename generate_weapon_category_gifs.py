# -*- coding: utf-8 -*-
"""
Generate representative animated GIFs for Weapon Categories 1, 3, 4, 5:
- anim_w_cat1_chipped.gif (分类一：肋部挑传空当与贴地横扫 Weapons 02 & 04)
- anim_w_cat3_curled.gif (分类三：弧线绕顶调度与边线推进 Weapons 11 & 09)
- anim_w_cat4_fake_shot.gif (分类四：假射真传与节奏差特种破局 Weapons 14 & 13)
- anim_w_cat5_gk_laser.gif (分类五：门将低平快激光直塞与死球配合 Weapons 17 & 19)
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
    draw.text((W-80, 20), "武器库实战演练", fill="#38bdf8", font=font_badge, anchor="mm")
    
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

def draw_ball(draw, x, y, size_offset=0):
    x, y = int(x), int(y)
    r = 6 + size_offset
    draw.ellipse([x-r-3, y-r-3, x+r+3, y+r+3], fill="#fbbf24")
    draw.ellipse([x-r, y-r, x+r, y+r], fill="#ffffff", outline="#000000", width=1)

def lerp(p1, p2, t):
    t = max(0.0, min(1.0, t))
    return p1[0] + (p2[0] - p1[0]) * t, p1[1] + (p2[1] - p1[1]) * t

# ============================================================
# 1. 分类一：肋部挑传空当与贴地横扫 (Weapons 02 & 04)
# ============================================================
def make_cat1_chipped_gif():
    frames = []
    total_frames = 55
    pos_CM = (280, 420) # 中场持球
    pos_W_start, pos_W_end = (140, 320), (160, 160) # 边锋肋部插上接挑传
    pos_ST_start, pos_ST_end = (420, 240), (400, 110) # 中锋抢前点
    def_mid = (260, 310)
    def_cb = (360, 200)
    def_gk = (420, 95)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.40:
            p = t / 0.40
            step = ">> 阶段 1/3: [Weapon 02 肋部挑传] 中场(4)脚尖搓起挑传，越过防线打入左肋空当"
            w_pos = lerp(pos_W_start, pos_W_end, p)
            st_pos = pos_ST_start
            ball_pos = lerp(pos_CM, pos_W_end, p)
            ball_size = int(math.sin(p * math.pi) * 4)
            draw.line([pos_CM, pos_W_end], fill="#fbbf24", width=3)
            draw.line([pos_W_start, pos_W_end], fill="#22c55e", width=2)
        elif t < 0.70:
            p = (t - 0.40) / 0.30
            step = ">> 阶段 2/3: [Weapon 04 贴地横扫] 边锋(5)不停球脚内侧发力平抽门前走廊!"
            w_pos = pos_W_end
            st_pos = lerp(pos_ST_start, pos_ST_end, p)
            ball_pos = lerp(pos_W_end, pos_ST_end, p)
            ball_size = 0
            draw.line([pos_W_end, pos_ST_end], fill="#38bdf8", width=3)
            draw.line([pos_ST_start, pos_ST_end], fill="#22c55e", width=2)
        else:
            p = (t - 0.70) / 0.30
            step = ">> 阶段 3/3: 中锋(7)高速抢前点迎球垫射折射破门入网!"
            w_pos = pos_W_end
            st_pos = pos_ST_end
            ball_pos = lerp(pos_ST_end, (420, 82), p)
            ball_size = 0
            draw.line([pos_ST_end, (420, 82)], fill="#ef4444", width=3)
            
        draw_player(draw, pos_CM[0], pos_CM[1], 4, "中场/挑传", True, t<0.4)
        draw_player(draw, w_pos[0], w_pos[1], 5, "左翼(插上)", True, 0.4<=t<0.7)
        draw_player(draw, st_pos[0], st_pos[1], 7, "中锋(抢点)", True, t>=0.7)
        draw_player(draw, def_mid[0], def_mid[1], "D1", "防守后腰", False)
        draw_player(draw, def_cb[0], def_cb[1], "D2", "防守中卫", False)
        draw_player(draw, def_gk[0], def_gk[1], "GK", "门将", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1], ball_size)
        draw_header(draw, "【武器分类一】肋部挑传空当 + 贴地横扫传中 (Weapons 02 & 04)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_w_cat1_chipped.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# ============================================================
# 2. 分类三：弧线绕顶与宽度调度 (Weapons 11 & 09)
# ============================================================
def make_cat3_curled_gif():
    frames = []
    total_frames = 55
    pos_CB = (340, 520) # 中卫持球
    pos_RW_start, pos_RW_end = (680, 420), (680, 220) # 右翼前插
    pos_Block = (420, 380) # 中路密集防守堵塞区
    pos_Curve_mid = (540, 410) # 弧线球弯曲点
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.45:
            p = t / 0.45
            step = ">> 阶段 1/2: [Weapon 11 弧线绕顶] 中路防守密集封堵，中卫(3)拉出外侧强侧旋弧线球"
            rw_pos = lerp(pos_RW_start, pos_RW_end, p*0.6)
            # Quadratic Bezier Curve for curled trajectory
            p0, p1, p2 = pos_CB, pos_Curve_mid, pos_RW_end
            bx = (1-p)**2 * p0[0] + 2*(1-p)*p * p1[0] + p**2 * p2[0]
            by = (1-p)**2 * p0[1] + 2*(1-p)*p * p1[1] + p**2 * p2[1]
            ball_pos = (bx, by)
            # Draw curled path
            for step_idx in range(15):
                s1 = step_idx / 15.0
                s2 = (step_idx+1) / 15.0
                b1x = (1-s1)**2 * p0[0] + 2*(1-s1)*s1 * p1[0] + s1**2 * p2[0]
                b1y = (1-s1)**2 * p0[1] + 2*(1-s1)*s1 * p1[1] + s1**2 * p2[1]
                b2x = (1-s2)**2 * p0[0] + 2*(1-s2)*s2 * p1[0] + s2**2 * p2[0]
                b2y = (1-s2)**2 * p0[1] + 2*(1-s2)*s2 * p1[1] + s2**2 * p2[1]
                draw.line([(b1x, b1y), (b2x, b2y)], fill="#fbbf24", width=2)
        else:
            p = (t - 0.45) / 0.55
            step = ">> 阶段 2/2: [Weapon 10 边线推进] 避开中路封锁直接连线右翼(6)，右翼高速长驱直入!"
            rw_pos = lerp(lerp(pos_RW_start, pos_RW_end, 0.6), pos_RW_end, p)
            ball_pos = rw_pos
            draw.line([pos_RW_start, pos_RW_end], fill="#22c55e", width=2)
            
        draw_player(draw, pos_CB[0], pos_CB[1], 3, "出球中卫", True, t<0.45)
        draw_player(draw, rw_pos[0], rw_pos[1], 6, "右翼(空当)", True, t>=0.45)
        draw_player(draw, pos_Block[0]-40, pos_Block[1], "D1", "中路封堵", False)
        draw_player(draw, pos_Block[0]+40, pos_Block[1], "D2", "中路封堵", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【武器分类三】弧线绕顶传球 + 边线弱侧推进 (Weapons 11 & 10)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_w_cat3_curled.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# ============================================================
# 3. 分类四：假射真传与节奏差特种破局 (Weapons 14 & 13)
# ============================================================
def make_cat4_fake_shot_gif():
    frames = []
    total_frames = 55
    pos_CM = (420, 290) # 前腰持球
    pos_ST_start, pos_ST_end = (520, 240), (520, 130) # 锋线斜插
    def1_start, def1_slide = (420, 220), (360, 210) # 后卫被假射滑铲引开
    def_gk = (420, 95)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.40:
            p = t / 0.40
            step = ">> 阶段 1/3: [Weapon 14 假射真传] 前腰(6)禁区弧顶大动作扬腿假射，诱使后卫滑铲封堵"
            cm_pos = pos_CM
            st_pos = pos_ST_start
            def1_pos = lerp(def1_start, def1_slide, p)
            ball_pos = pos_CM
            draw.line([pos_CM, (pos_CM[0]-30, pos_CM[1]-40)], fill="#ef4444", width=2) # Fake shot line
        elif t < 0.70:
            p = (t - 0.40) / 0.30
            step = ">> 阶段 2/3: 后卫重心倒地！前腰(6)瞬间脚腕一扣，节奏差隐蔽直塞右肋空当"
            cm_pos = pos_CM
            def1_pos = def1_slide
            st_pos = lerp(pos_ST_start, pos_ST_end, p)
            ball_pos = lerp(pos_CM, pos_ST_end, p)
            draw.line([pos_CM, pos_ST_end], fill="#fbbf24", width=3)
            draw.line([pos_ST_start, pos_ST_end], fill="#22c55e", width=2)
        else:
            p = (t - 0.70) / 0.30
            step = ">> 阶段 3/3: 锋线(7)斜插接球面对出击门将，轻巧推射远角得手!"
            cm_pos = pos_CM
            def1_pos = def1_slide
            st_pos = pos_ST_end
            ball_pos = lerp(pos_ST_end, (400, 82), p)
            draw.line([pos_ST_end, (400, 82)], fill="#ef4444", width=3)
            
        draw_player(draw, cm_pos[0], cm_pos[1], 6, "前腰(假射扣传)", True, t<0.7)
        draw_player(draw, st_pos[0], st_pos[1], 7, "中锋(斜插)", True, t>=0.7)
        draw_player(draw, def1_pos[0], def1_pos[1], "D", "滑铲失位", False)
        draw_player(draw, def_gk[0], def_gk[1], "GK", "门将", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【武器分类四】假射真传/节奏差 + 隐蔽塞球 (Weapons 14 & 13)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_w_cat4_fake_shot.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# ============================================================
# 4. 分类五：门将低平快激光球与死球破压 (Weapons 17 & 19)
# ============================================================
def make_cat5_gk_laser_gif():
    frames = []
    total_frames = 55
    pos_GK = (420, 560) # 门将推至弧顶
    pos_CM_start, pos_CM_end = (420, 420), (420, 270) # 中场后腰接球并转身
    pos_W_start, pos_W_end = (640, 360), (640, 180) # 边锋插上
    opp_press1, opp_press2 = (340, 470), (500, 470) # 对方双前锋前压逼抢
    def_gk = (420, 95)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.38:
            p = t / 0.38
            step = ">> 阶段 1/3: [Weapon 17 门将穿透球] 门将(1)弧顶持球，脚内侧大力贴地穿透双人逼抢线!"
            cm_pos = pos_CM_start
            w_pos = pos_W_start
            ball_pos = lerp(pos_GK, pos_CM_start, p)
            draw.line([pos_GK, pos_CM_start], fill="#38bdf8", width=3)
        elif t < 0.70:
            p = (t - 0.38) / 0.32
            step = ">> 阶段 2/3: 中场(4)半侧身顺势领球转身，立即送出斜长传分边"
            cm_pos = lerp(pos_CM_start, pos_CM_end, p*0.5)
            w_pos = lerp(pos_W_start, pos_W_end, p)
            ball_pos = lerp(pos_CM_start, pos_W_end, p)
            draw.line([pos_CM_start, pos_W_end], fill="#fbbf24", width=3)
            draw.line([pos_W_start, pos_W_end], fill="#22c55e", width=2)
        else:
            p = (t - 0.70) / 0.30
            step = ">> 阶段 3/3: 右翼(6)高速套边突入禁区完成威胁射门，瞬间瓦解高位逼抢!"
            cm_pos = pos_CM_end
            w_pos = pos_W_end
            ball_pos = lerp(pos_W_end, (420, 82), p)
            draw.line([pos_W_end, (420, 82)], fill="#ef4444", width=3)
            
        draw_player(draw, pos_GK[0], pos_GK[1], 1, "门将(出球核心)", True, t<0.38)
        draw_player(draw, cm_pos[0], cm_pos[1], 4, "中场(接应)", True, 0.38<=t<0.7)
        draw_player(draw, w_pos[0], w_pos[1], 6, "右翼(反击)", True, t>=0.7)
        draw_player(draw, opp_press1[0], opp_press1[1], "F1", "逼抢前锋", False)
        draw_player(draw, opp_press2[0], opp_press2[1], "F2", "逼抢前锋", False)
        draw_player(draw, def_gk[0], def_gk[1], "GK", "对方门将", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【武器分类五】门将穿透性低平球破压 (Weapons 17 & 18)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_w_cat5_gk_laser.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# Execute all
make_cat1_chipped_gif()
make_cat3_curled_gif()
make_cat4_fake_shot_gif()
make_cat5_gk_laser_gif()
print("All weapon category GIFs generated successfully!")
