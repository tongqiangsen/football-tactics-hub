# -*- coding: utf-8 -*-
"""
Generate complete animated GIFs for ALL 8 football attacking doctrines:
- anim_01_third_man.gif (流派① 第三人跑位渗透)
- anim_02_switch_play.gif (流派② 强侧超载弱侧转移)
- anim_08_over_the_top.gif (流派③ 纵深越顶反越位突袭)
- anim_09_5s_counter_blitz.gif (流派④ 攻防转换5秒快攻闪击)
- anim_10_target_man_aerial.gif (流派⑤ 立体空战中锋胸部做球远射)
- anim_04_cut_back.gif (流派⑥ 禁区底线倒三角回传终结)
- anim_11_dummy_let_through.gif (流派⑦ 迎球假接真漏特种破局)
- anim_12_tactical_throwin.gif (流派⑧ 战术手抛界外球三角配合)
Plus formation GIFs:
- anim_05_1231_buildup.gif (7人制 1-2-3-1)
- anim_06_1321_counter.gif (7人制 1-3-2-1)
- anim_07_1331_overlap.gif (8人制 1-3-3-1)
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
    draw.text((W-80, 20), "战术动态演练", fill="#38bdf8", font=font_badge, anchor="mm")
    
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
# 8. 流派③ 纵深越顶身后流 (Over-the-Top Chip into Space)
# ============================================================
def make_over_the_top_gif():
    frames = []
    total_frames = 55
    pos_CB = (420, 520) # 中卫/后腰
    pos_ST_start = (420, 330) # 前锋起始站位（压在越位线）
    pos_ST_end = (420, 150) # 冲刺到身后单刀点
    
    # Opponents high defense line
    def1_start, def1_end = (360, 320), (360, 240)
    def2_start, def2_end = (480, 320), (480, 240)
    def_gk = (420, 95)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.35:
            p = t / 0.35
            step = ">> 阶段 1/3: 对方防线整体压上逼抢，中卫(3)观察到身后 25 米巨大空当"
            ball_pos = pos_CB
            st_pos = pos_ST_start
            def1 = def1_start
            def2 = def2_start
            cb_glow, st_glow = True, False
            ball_size = 0
            draw.line([pos_CB, (pos_CB[0], pos_CB[1]-40)], fill="#38bdf8", width=2)
        elif t < 0.70:
            p = (t - 0.35) / 0.35
            step = ">> 阶段 2/3: 中卫(3)送出精准过顶挑传，中锋(7)盲区反越位高速冲刺!"
            ball_pos = lerp(pos_CB, pos_ST_end, p)
            st_pos = lerp(pos_ST_start, pos_ST_end, p)
            # Defenders turn and chase slowly
            def1 = lerp(def1_start, def1_end, p*0.6)
            def2 = lerp(def2_start, def2_end, p*0.6)
            cb_glow, st_glow = False, True
            # Simulate height arc in ball size
            ball_size = int(math.sin(p * math.pi) * 4)
            draw.line([pos_ST_start, pos_ST_end], fill="#22c55e", width=2)
            draw.line([pos_CB, pos_ST_end], fill="#fbbf24", width=3)
        else:
            p = (t - 0.70) / 0.30
            step = ">> 阶段 3/3: 中锋(7)反越位单刀突入禁区，凌空垫射破门入网!"
            st_pos = pos_ST_end
            def1 = def1_end
            def2 = def2_end
            ball_pos = lerp(pos_ST_end, (420, 82), p)
            cb_glow, st_glow = False, True
            ball_size = 0
            draw.line([pos_ST_end, (420, 82)], fill="#ef4444", width=3)
            
        draw_player(draw, pos_CB[0], pos_CB[1], 3, "中卫/出球", True, cb_glow)
        draw_player(draw, st_pos[0], st_pos[1], 7, "中锋(反越位)", True, st_glow)
        draw_player(draw, def1[0], def1[1], "D1", "高位中卫", False)
        draw_player(draw, def2[0], def2[1], "D2", "高位中卫", False)
        draw_player(draw, def_gk[0], def_gk[1], "GK", "门将", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1], ball_size)
        draw_header(draw, "【进攻流派③】纵深越顶反越位突袭 (Over-the-Top Chip)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_08_over_the_top.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# ============================================================
# 9. 流派④ 攻防转换5秒快攻闪击 (Counter-Pressing 5-Second Blitz)
# ============================================================
def make_5s_counter_blitz_gif():
    frames = []
    total_frames = 55
    
    # Positions
    pos_opp_D = (400, 310) # 对方拿球后卫
    pos_W5_start, pos_W5_end = (310, 370), (370, 320) # 边前卫 5 围抢
    pos_W7_start, pos_W7_end = (490, 370), (430, 320) # 前锋 7 夹击
    pos_CM_start, pos_CM_end = (420, 480), (450, 240) # 6号插上
    pos_F7_finish = (370, 140)
    
    def_gk = (420, 95)
    def2 = (490, 220)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.35:
            p = t / 0.35
            step = ">> 阶段 1/3: 丢球 0.5s 内！左翼(5)与前锋(7)就地合围抢断!"
            w5_pos = lerp(pos_W5_start, pos_W5_end, p)
            w7_pos = lerp(pos_W7_start, pos_W7_end, p)
            cm_pos = pos_CM_start
            ball_pos = pos_opp_D
            w5_glow, w7_glow, cm_glow = True, True, False
            draw.line([pos_W5_start, pos_W5_end], fill="#ef4444", width=2)
            draw.line([pos_W7_start, pos_W7_end], fill="#ef4444", width=2)
        elif t < 0.68:
            p = (t - 0.35) / 0.33
            step = ">> 阶段 2/3: 断球立即贴地刺穿直塞插上的中场(6)，打对手立足未稳"
            w5_pos = pos_W5_end
            w7_pos = lerp(pos_W7_end, pos_F7_finish, p*0.6)
            cm_pos = lerp(pos_CM_start, pos_CM_end, p)
            ball_pos = lerp(pos_W5_end, pos_CM_end, p)
            w5_glow, w7_glow, cm_glow = False, True, True
            draw.line([pos_W5_end, pos_CM_end], fill="#fbbf24", width=3)
            draw.line([pos_W7_end, pos_F7_finish], fill="#22c55e", width=2)
        else:
            p = (t - 0.68) / 0.32
            step = ">> 阶段 3/3: 5秒内第3脚传球直插禁区，前锋(7)接球推射空门破门!"
            w5_pos = pos_W5_end
            cm_pos = pos_CM_end
            w7_pos = lerp(lerp(pos_W7_end, pos_F7_finish, 0.6), pos_F7_finish, (p-0.68)/0.32 if p>0.68 else 1.0)
            ball_pos = lerp(pos_CM_end, pos_F7_finish, p) if p < 0.85 else lerp(pos_F7_finish, (420, 82), (p-0.85)/0.15)
            w5_glow, w7_glow, cm_glow = False, True, False
            draw.line([pos_CM_end, pos_F7_finish], fill="#38bdf8", width=2)
            draw.line([pos_F7_finish, (420, 82)], fill="#ef4444", width=3)
            
        draw_player(draw, w5_pos[0], w5_pos[1], 5, "左翼(逼抢)", True, w5_glow)
        draw_player(draw, w7_pos[0], w7_pos[1], 7, "中锋(反击)", True, w7_glow)
        draw_player(draw, cm_pos[0], cm_pos[1], 6, "中场(接应)", True, cm_glow)
        draw_player(draw, pos_opp_D[0], pos_opp_D[1], "D1", "失误后卫", False)
        draw_player(draw, def2[0], def2[1], "D2", "", False)
        draw_player(draw, def_gk[0], def_gk[1], "GK", "门将", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【进攻流派④】攻防转换5秒快攻闪击 (5s Blitz)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_09_5s_counter_blitz.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# ============================================================
# 10. 流派⑤ 立体空战中锋胸部做球 (Target Man Aerial Lay-off)
# ============================================================
def make_target_man_aerial_gif():
    frames = []
    total_frames = 55
    pos_CB = (420, 540) # 中卫起长传
    pos_ST = (420, 270) # 中锋高点
    pos_CM_start, pos_CM_end = (420, 440), (420, 340) # 中场插上爆射
    def1 = (420, 230) # 防守中卫
    def_gk = (420, 95)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.40:
            p = t / 0.40
            step = ">> 阶段 1/3: 后场起高空球避开地面缠斗，直找突前中锋(7)高点"
            ball_pos = lerp(pos_CB, pos_ST, p)
            cm_pos = pos_CM_start
            ball_size = int(math.sin(p * math.pi) * 5)
            draw.line([pos_CB, pos_ST], fill="#fbbf24", width=3)
        elif t < 0.70:
            p = (t - 0.40) / 0.30
            step = ">> 阶段 2/3: 中锋(7)背身扛人胸部稳稳卸球，轻推回做插上的中场(6)"
            cm_pos = lerp(pos_CM_start, pos_CM_end, p)
            ball_pos = lerp(pos_ST, pos_CM_end, p)
            ball_size = 0
            draw.line([pos_ST, pos_CM_end], fill="#38bdf8", width=2)
            draw.line([pos_CM_start, pos_CM_end], fill="#22c55e", width=2)
        else:
            p = (t - 0.70) / 0.30
            step = ">> 阶段 3/3: 中场(6)禁区弧顶迎球不停球直接重炮轰门入网!"
            cm_pos = pos_CM_end
            ball_pos = lerp(pos_CM_end, (420, 82), p)
            ball_size = 0
            draw.line([pos_CM_end, (420, 82)], fill="#ef4444", width=3)
            
        draw_player(draw, pos_CB[0], pos_CB[1], 3, "中卫/长传", True)
        draw_player(draw, pos_ST[0], pos_ST[1], 7, "中锋(支点)", True, True)
        draw_player(draw, cm_pos[0], cm_pos[1], 6, "中场(重炮)", True, True)
        draw_player(draw, def1[0], def1[1], "D", "中卫", False)
        draw_player(draw, def_gk[0], def_gk[1], "GK", "门将", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1], ball_size)
        draw_header(draw, "【进攻流派⑤】立体空战支点胸部做球 (Target Man Lay-off)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_10_target_man_aerial.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# ============================================================
# 11. 流派⑦ 迎球假接真漏 (Dummy / Let-Through)
# ============================================================
def make_dummy_let_through_gif():
    frames = []
    total_frames = 50
    pos_CB = (420, 520) # 后腰
    pos_CM = (420, 330) # 假装接球中场 6
    pos_ST_start, pos_ST_end = (420, 240), (420, 140) # 身后前锋 7
    def_mid = (420, 360) # 贴身防守者
    def_gk = (420, 95)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.45:
            p = t / 0.45
            step = ">> 阶段 1/2: 后腰(4)直塞中场(6)，中场做出迎球接球假动作吸引防守"
            ball_pos = lerp(pos_CB, pos_CM, p)
            st_pos = pos_ST_start
            cm_glow, st_glow = True, False
            draw.line([pos_CB, pos_CM], fill="#38bdf8", width=2)
        else:
            p = (t - 0.45) / 0.55
            step = ">> 阶段 2/2: 中场(6)突然叉腿漏球！防守愣在原地，中锋(7)接球单刀破门!"
            ball_pos = lerp(pos_CM, pos_ST_end, p) if p < 0.8 else lerp(pos_ST_end, (420, 82), (p-0.8)/0.2)
            st_pos = lerp(pos_ST_start, pos_ST_end, p if p < 0.8 else 1.0)
            cm_glow, st_glow = False, True
            draw.line([pos_CM, pos_ST_end], fill="#fbbf24", width=3)
            draw.line([pos_ST_end, (420, 82)], fill="#ef4444", width=2)
            
        draw_player(draw, pos_CB[0], pos_CB[1], 4, "后腰", True)
        draw_player(draw, pos_CM[0], pos_CM[1], 6, "中场(假动作漏球)", True, cm_glow)
        draw_player(draw, st_pos[0], st_pos[1], 7, "中锋(单刀)", True, st_glow)
        draw_player(draw, def_mid[0], def_mid[1], "D", "上抢中卫", False)
        draw_player(draw, def_gk[0], def_gk[1], "GK", "门将", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【进攻流派⑦】迎球假接真漏特种破局 (Dummy Let-Through)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_11_dummy_let_through.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# ============================================================
# 12. 流派⑧ 战术手抛界外球 (Tactical Throw-in Combo)
# ============================================================
def make_tactical_throwin_gif():
    frames = []
    total_frames = 55
    pos_Thrower_start, pos_Thrower_end = (40, 320), (140, 160) # 边卫 2 掷界外球并插上
    pos_ST_start, pos_ST_end = (180, 240), (160, 280) # 前锋 7 迎前回做
    pos_Box = (420, 170) # 中路包抄前锋/中场 6
    def_rb = (120, 300)
    
    for i in range(total_frames):
        img = Image.new("RGB", (W, H))
        draw = ImageDraw.Draw(img)
        draw_pitch(draw)
        t = i / total_frames
        
        if t < 0.35:
            p = t / 0.35
            step = ">> 阶段 1/3: 边卫(2)界外球精准掷向前锋(7)脚下，边卫立即外侧套边前插"
            ball_pos = lerp(pos_Thrower_start, pos_ST_end, p)
            th_pos = lerp(pos_Thrower_start, (pos_Thrower_start[0]+40, pos_Thrower_start[1]-60), p)
            st_pos = lerp(pos_ST_start, pos_ST_end, p)
            draw.line([pos_Thrower_start, pos_ST_end], fill="#38bdf8", width=2)
            draw.line([pos_Thrower_start, pos_Thrower_end], fill="#22c55e", width=2)
        elif t < 0.68:
            p = (t - 0.35) / 0.33
            step = ">> 阶段 2/3: 前锋(7)迎球一脚顺势斜塞给高速套边的边卫(2)下底"
            th_pos = lerp((pos_Thrower_start[0]+40, pos_Thrower_start[1]-60), pos_Thrower_end, p)
            st_pos = pos_ST_end
            ball_pos = lerp(pos_ST_end, pos_Thrower_end, p)
            draw.line([pos_ST_end, pos_Thrower_end], fill="#fbbf24", width=3)
        else:
            p = (t - 0.68) / 0.32
            step = ">> 阶段 3/3: 边卫(2)底线贴地横扫门前，包抄中场(6)抢点破门!"
            th_pos = pos_Thrower_end
            st_pos = pos_ST_end
            ball_pos = lerp(pos_Thrower_end, pos_Box, p)
            draw.line([pos_Thrower_end, pos_Box], fill="#22c55e", width=3)
            
        draw_player(draw, th_pos[0], th_pos[1], 2, "边卫(投掷/插上)", True, True)
        draw_player(draw, st_pos[0], st_pos[1], 7, "前锋(做球)", True)
        draw_player(draw, pos_Box[0], pos_Box[1], 6, "包抄中场", True, True)
        draw_player(draw, def_rb[0], def_rb[1], "D", "防守边卫", False)
        
        draw_ball(draw, ball_pos[0], ball_pos[1])
        draw_header(draw, "【进攻流派⑧】战术手抛界外球三角配合 (Throw-in)", step)
        frames.append(img)
        
    gif_path = os.path.join(out_dir, "anim_12_tactical_throwin.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=65, loop=0)
    print("Generated:", gif_path)

# Execute generators
make_over_the_top_gif()
make_5s_counter_blitz_gif()
make_target_man_aerial_gif()
make_dummy_let_through_gif()
make_tactical_throwin_gif()
print("All new attacking doctrine animated GIFs generated successfully!")
