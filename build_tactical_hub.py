# -*- coding: utf-8 -*-
"""
Compile football_tactics_hub.html - Modern Interactive Web Tactical Hub.
Step 2 Delivery:
1. Module 04: Interactive Football Pitch Board & Player Role Cards (互动球场画板)
   - Toggle 7v7 1-2-3-1, 7v7 1-3-2-1, 8v8 1-3-3-1
   - Interactive SVG pitch with clickable player nodes (1~7 / 1~8)
   - Clicking any player triggers live role card update: 3-Action requirements (Pre/Main/Post),
     key passes, tactical duties, matchday callouts, and formation animations!
2. Module 02: 8 Attacking Doctrines Hub with Category Filtering & Clickable Weapon Capsules (流派与武器联动)
   - Category filtering (All, Penetration, Direct/Transition, Flank/Cut-back, Trick/Set-piece)
   - Weapon capsule tags: Clicking any weapon tag pops up a quick weapon modal with GIF and tips!
3. Module 03: 20 Passing Weapons Console with point-and-play multi-GIF switcher (updated with W17 门将穿透性低平球).
4. Integrated Lightbox zoom tool across all tactical animations.
"""

import os, base64, shutil

gif_dir = r"e:\06_Study\书籍\足球\tactics_animations_gif"
art_gif_dir = r"C:\Users\Administrator\.gemini\antigravity\brain\030fc641-b9cc-4e72-b4ba-ed21a5a6e35f\tactics_animations_gif"
os.makedirs(art_gif_dir, exist_ok=True)

def get_gif_b64(name):
    path = os.path.join(gif_dir, name)
    if os.path.exists(path):
        try:
            shutil.copy2(path, os.path.join(art_gif_dir, name))
        except Exception:
            pass
        with open(path, "rb") as f:
            return "data:image/gif;base64," + base64.b64encode(f.read()).decode("ascii")
    return ""

# Doctrines
b64_d01 = get_gif_b64("anim_01_third_man.gif")
b64_d02 = get_gif_b64("anim_02_switch_play.gif")
b64_d03 = get_gif_b64("anim_08_over_the_top.gif")
b64_d04 = get_gif_b64("anim_09_5s_counter_blitz.gif")
b64_d05 = get_gif_b64("anim_10_target_man_aerial.gif")
b64_d06 = get_gif_b64("anim_04_cut_back.gif")
b64_d07 = get_gif_b64("anim_11_dummy_let_through.gif")
b64_d08 = get_gif_b64("anim_12_tactical_throwin.gif")

# 20 Weapons - 100% Dedicated Independent Animations
b64_w01 = get_gif_b64("anim_w01_through_ball.gif")
b64_w02 = get_gif_b64("anim_w02_chipped_through.gif")
b64_w03 = get_gif_b64("anim_04_cut_back.gif")
b64_w04 = get_gif_b64("anim_w04_driven_cross.gif")
b64_w05 = get_gif_b64("anim_03_wall_pass.gif")
b64_w06 = get_gif_b64("anim_w06_layoff_pass.gif")
b64_w07 = get_gif_b64("anim_w07_line_breaking.gif")
b64_w08 = get_gif_b64("anim_01_third_man.gif")
b64_w09 = get_gif_b64("anim_02_switch_play.gif")
b64_w10 = get_gif_b64("anim_w10_channel_pass.gif")
b64_w11 = get_gif_b64("anim_w_cat3_curled.gif")
b64_w12 = get_gif_b64("anim_w12_recycling.gif")
b64_w13 = get_gif_b64("anim_w13_no_look.gif")
b64_w14 = get_gif_b64("anim_w_cat4_fake_shot.gif")
b64_w15 = get_gif_b64("anim_w15_reverse_diagonal.gif")
b64_w16 = get_gif_b64("anim_11_dummy_let_through.gif")
b64_w17 = get_gif_b64("anim_w_cat5_gk_laser.gif")
b64_w18 = get_gif_b64("anim_08_over_the_top.gif")
b64_w19 = get_gif_b64("anim_w19_setpiece_cutback.gif")
b64_w20 = get_gif_b64("anim_12_tactical_throwin.gif")

# Special Combo Animation
b64_combo_w02_w04 = get_gif_b64("anim_w_cat1_chipped.gif")

# Formations
b64_f1231 = get_gif_b64("anim_05_1231_buildup.gif")
b64_f1321 = get_gif_b64("anim_06_1321_counter.gif")
b64_f1331 = get_gif_b64("anim_07_1331_overlap.gif")

html_code = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>德国足球战术战情室 · 现代传球体系交互中枢 (Tactical Hub · Step 2)</title>
  <style>
    :root {{
      --bg-app: #0a0e0c;
      --bg-sidebar: #0f1512;
      --bg-surface: #141c18;
      --bg-subsurface: #1a2420;
      --border-subtle: rgba(255, 255, 255, 0.07);
      --border-focus: rgba(16, 185, 129, 0.4);
      --pitch-green: #10b981;
      --accent-gold: #f59e0b;
      --accent-cyan: #38bdf8;
      --accent-red: #ef4444;
      --accent-purple: #a855f7;
      --text-main: #f8fafc;
      --text-sub: #94a3b8;
      --text-muted: #64748b;
      --tab-bg: #18221d;
      --tab-color: #94a3b8;
      --shadow-card: 0 4px 20px -2px rgba(0, 0, 0, 0.35);
      --shadow-float: 0 12px 32px -4px rgba(0, 0, 0, 0.5);
      --bg-dark: var(--bg-app);
      --bg-card: var(--bg-surface);
      --bg-card-inner: var(--bg-subsurface);
      --border-color: var(--border-subtle);
      --border-sub: var(--border-subtle);
      --border-hover: var(--border-focus);
    }}

    /* Light Eye-friendly Tactical Whiteboard Theme (战术白板) */
    body.theme-light {{
      --bg-app: #f4f6f5;
      --bg-sidebar: #e9eeea;
      --bg-surface: #ffffff;
      --bg-subsurface: #f1f5f2;
      --border-subtle: rgba(0, 0, 0, 0.07);
      --border-focus: rgba(4, 120, 87, 0.4);
      --pitch-green: #047857;
      --accent-gold: #b45309;
      --accent-cyan: #0369a1;
      --accent-red: #dc2626;
      --accent-purple: #7e22ce;
      --text-main: #0f172a;
      --text-sub: #334155;
      --text-muted: #64748b;
      --tab-bg: #e2e8f0;
      --tab-color: #475569;
      --shadow-card: 0 4px 15px rgba(0, 0, 0, 0.04);
      --shadow-float: 0 12px 28px rgba(0, 0, 0, 0.1);
      --bg-dark: var(--bg-app);
      --bg-card: var(--bg-surface);
      --bg-card-inner: var(--bg-subsurface);
      --border-color: var(--border-subtle);
      --border-sub: var(--border-subtle);
      --border-hover: var(--border-focus);
    }}
    body.theme-light .main-content {{ background: var(--bg-app); }}
    body.theme-light .sidebar {{ background: var(--bg-sidebar); border-right-color: var(--border-subtle); }}
    body.theme-light .sidebar-header {{ border-bottom-color: var(--border-subtle); }}
    body.theme-light .sidebar-footer {{ border-top-color: var(--border-subtle); }}
    body.theme-light .topbar {{ background: rgba(244, 246, 245, 0.95); border-bottom-color: var(--border-subtle); }}
    body.theme-light .nav-item:hover {{ background: rgba(4, 120, 87, 0.08); color: #0f172a; }}
    body.theme-light .nav-item.active {{ background: rgba(4, 120, 87, 0.12); color: #047857; }}
    body.theme-light .weapon-select-card.active {{ border-color: var(--pitch-green); background: rgba(4, 120, 87, 0.06); }}

    /* Warm Sepia Eye-friendly Theme (羊皮纸暖阳护眼) */
    body.theme-sepia {{
      --bg-app: #f5f0e4;
      --bg-sidebar: #eae2d1;
      --bg-surface: #fdfaf3;
      --bg-subsurface: #f3ece0;
      --border-subtle: rgba(180, 145, 90, 0.2);
      --border-focus: rgba(4, 120, 87, 0.4);
      --pitch-green: #047857;
      --accent-gold: #b45309;
      --accent-cyan: #0369a1;
      --accent-red: #b91c1c;
      --accent-purple: #6b21a8;
      --text-main: #1c1917;
      --text-sub: #44403c;
      --text-muted: #78716c;
      --tab-bg: #eadfcb;
      --tab-color: #57534e;
      --shadow-card: 0 4px 15px rgba(180, 145, 90, 0.08);
      --shadow-float: 0 12px 28px rgba(180, 145, 90, 0.15);
      --bg-dark: var(--bg-app);
      --bg-card: var(--bg-surface);
      --bg-card-inner: var(--bg-subsurface);
      --border-color: var(--border-subtle);
      --border-sub: var(--border-subtle);
      --border-hover: var(--border-focus);
    }}
    body.theme-sepia .main-content {{ background: var(--bg-app); }}
    body.theme-sepia .sidebar {{ background: var(--bg-sidebar); border-right-color: var(--border-subtle); }}
    body.theme-sepia .sidebar-header {{ border-bottom-color: var(--border-subtle); }}
    body.theme-sepia .sidebar-footer {{ border-top-color: var(--border-subtle); }}
    body.theme-sepia .topbar {{ background: rgba(245, 240, 228, 0.96); border-bottom-color: var(--border-subtle); }}
    body.theme-sepia .nav-item:hover {{ background: rgba(4, 120, 87, 0.08); color: #1c1917; }}
    body.theme-sepia .nav-item.active {{ background: rgba(4, 120, 87, 0.14); color: #047857; border-color: transparent; }}
    body.theme-sepia .weapon-select-card.active {{ border-color: #047857; background: rgba(4, 120, 87, 0.08); }}

    /* 3-Theme Switcher Palette */
    .theme-palette-group {{
      display: inline-flex;
      align-items: center;
      background: var(--bg-subsurface);
      padding: 3px;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
      gap: 2px;
    }}
    .theme-btn {{
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 5px 10px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .theme-btn:hover {{
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.06);
    }}
    body.theme-light .theme-btn:hover,
    body.theme-sepia .theme-btn:hover {{
      background: rgba(0, 0, 0, 0.05);
    }}
    .theme-btn.active {{
      background: var(--pitch-green);
      color: #fff;
      font-weight: 600;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
      background-color: var(--bg-app);
      color: var(--text-main);
      overflow-x: hidden;
      height: 100vh;
      display: flex;
      font-feature-settings: "cv02", "cv03", "cv04", "cv11";
      -webkit-font-smoothing: antialiased;
      transition: background-color 0.25s, color 0.25s;
    }}

    /* Left Sidebar */
    .sidebar {{
      width: 260px;
      background: var(--bg-sidebar);
      border-right: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      z-index: 50;
      transition: background-color 0.25s, border-color 0.25s;
    }}
    .sidebar-header {{
      padding: 20px 18px;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .sidebar-title {{
      font-size: 15px;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
      letter-spacing: -0.01em;
    }}
    .sidebar-subtitle {{
      font-size: 11px;
      color: var(--pitch-green);
      margin-top: 4px;
      font-weight: 600;
      letter-spacing: 0.06em;
      opacity: 0.9;
    }}

    .nav-menu {{
      flex: 1;
      padding: 16px 10px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      overflow-y: auto;
    }}
    .nav-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 12px;
      border-radius: 8px;
      color: var(--text-muted);
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
      border: 1px solid transparent;
    }}
    .nav-item:hover {{
      background: var(--bg-subsurface);
      color: var(--text-main);
    }}
    .nav-item.active {{
      background: var(--bg-surface);
      color: var(--pitch-green);
      font-weight: 600;
      border-color: var(--border-subtle);
      box-shadow: 0 1px 4px rgba(0, 0, 0, 0.15);
    }}
    .nav-badge {{
      font-size: 10.5px;
      padding: 2px 7px;
      border-radius: 6px;
      background: var(--bg-subsurface);
      color: var(--text-muted);
      border: 1px solid var(--border-subtle);
      font-weight: 500;
    }}
    .nav-item.active .nav-badge {{
      background: rgba(16, 185, 129, 0.15);
      color: var(--pitch-green);
      border-color: rgba(16, 185, 129, 0.3);
      font-weight: 600;
    }}

    .sidebar-footer {{
      padding: 14px 18px;
      border-top: 1px solid var(--border-subtle);
      font-size: 12px;
      color: var(--text-muted);
    }}

    /* Main Content Area */
    .main-content {{
      flex: 1;
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow-y: auto;
      background: var(--bg-app);
      transition: background-color 0.25s;
    }}

    /* Top Utility Bar */
    .topbar {{
      height: 56px;
      background: var(--bg-app);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 28px;
      position: sticky;
      top: 0;
      z-index: 40;
    }}
    .current-view-title {{
      font-size: 14.5px;
      font-weight: 600;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .view-tag {{
      font-size: 11px;
      font-weight: 600;
      padding: 2px 8px;
      border-radius: 6px;
      background: var(--bg-subsurface);
      color: var(--pitch-green);
      border: 1px solid var(--border-subtle);
    }}
    .top-actions {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .btn-action {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 6px 13px;
      border-radius: 7px;
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .btn-action:hover {{
      background: var(--bg-subsurface);
      border-color: var(--border-focus);
    }}

    /* Content Views */
    .view-container {{
      padding: 24px 32px 60px;
      display: none;
      animation: fadeIn 0.2s ease-out;
    }}
    .view-container.active {{
      display: block;
    }}
    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(4px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .section-header {{
      margin-bottom: 22px;
      padding-bottom: 12px;
      border-bottom: 1px solid var(--border-subtle);
    }}
    .section-header h2 {{
      font-size: 19px;
      font-weight: 700;
      color: var(--text-main);
      letter-spacing: -0.01em;
    }}
    .section-header p {{
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 4px;
      line-height: 1.5;
    }}

    /* Card System */
    .grid-2 {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; }}
    .grid-4 {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }}

    .card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 18px 20px;
      box-shadow: var(--shadow-card);
      transition: border-color 0.15s, box-shadow 0.15s;
    }}
    .card p, .card li {{
      color: var(--text-sub);
      font-size: 13px;
      line-height: 1.6;
    }}
    .card strong {{
      color: var(--text-main);
      font-weight: 600;
    }}
    .card:hover {{
      border-color: var(--border-focus);
    }}
    .card-title {{
      font-size: 14.5px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .card-title.gold {{ color: var(--accent-gold); }}
    .card-title.green {{ color: var(--pitch-green); }}
    .card-title.purple {{ color: var(--accent-purple); }}
    .card-title.red {{ color: var(--accent-red); }}

    /* ========================================================
       MODULE 04: INTERACTIVE PITCH & ROLE CARDS (STEP 2 核心)
       ======================================================== */
    .formation-nav {{
      display: flex;
      gap: 8px;
      margin-bottom: 18px;
    }}
    .formation-tab-btn {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .formation-tab-btn:hover {{
      background: var(--bg-subsurface);
      color: var(--text-main);
    }}
    .formation-tab-btn.active {{
      background: var(--bg-subsurface);
      border-color: var(--pitch-green);
      color: var(--pitch-green);
      font-weight: 600;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }}

    .pitch-workbench {{
      display: grid;
      grid-template-columns: 54% 46%;
      gap: 20px;
      align-items: start;
    }}

    .pitch-container {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 16px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
    }}
    .pitch-header-info {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}
    .pitch-title {{
      font-size: 14.5px;
      font-weight: 700;
      color: var(--text-main);
    }}
    .pitch-badge {{
      font-size: 11px;
      padding: 2px 8px;
      border-radius: 5px;
      background: rgba(245, 158, 11, 0.12);
      color: var(--accent-gold);
      border: 1px solid rgba(245, 158, 11, 0.25);
      font-weight: 600;
    }}

    .pitch-board {{
      position: relative;
      background: #071911;
      border: 1px solid rgba(16, 185, 129, 0.25);
      border-radius: 8px;
      height: 480px;
      overflow: hidden;
      box-shadow: inset 0 0 35px rgba(0, 0, 0, 0.7);
    }}
    body.theme-light .pitch-board {{
      background: #15452d;
      border-color: #047857;
    }}
    body.theme-sepia .pitch-board {{
      background: #133e28;
      border-color: #047857;
    }}
    /* Realistic Pitch Markings */
    .pitch-marking {{
      position: absolute;
      border-color: rgba(255, 255, 255, 0.22);
      border-style: solid;
      pointer-events: none;
    }}
    .pitch-half-line {{
      top: 50%; left: 0; width: 100%; height: 1px;
      border-top-width: 1.5px;
    }}
    .pitch-center-circle {{
      top: 50%; left: 50%; width: 104px; height: 104px;
      transform: translate(-50%, -50%);
      border-width: 1.5px;
      border-radius: 50%;
    }}
    .pitch-center-spot {{
      top: 50%; left: 50%; width: 6px; height: 6px;
      transform: translate(-50%, -50%);
      background: rgba(255, 255, 255, 0.35);
      border-radius: 50%;
    }}
    .pitch-penalty-top {{
      top: 0; left: 50%; width: 190px; height: 90px;
      transform: translateX(-50%);
      border-width: 0 1.5px 1.5px 1.5px;
    }}
    .pitch-penalty-bottom {{
      bottom: 0; left: 50%; width: 190px; height: 90px;
      transform: translateX(-50%);
      border-width: 1.5px 1.5px 0 1.5px;
    }}

    /* Interactive Player Dot Node */
    .player-node {{
      position: absolute;
      width: 36px;
      height: 36px;
      transform: translate(-50%, -50%);
      border-radius: 50%;
      background: #ffffff;
      border: 2px solid #0f172a;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 3px 10px rgba(0, 0, 0, 0.5);
      transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.2s ease;
      z-index: 10;
    }}
    .player-node:hover {{
      transform: translate(-50%, -50%) scale(1.1);
      box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.4), 0 4px 12px rgba(0, 0, 0, 0.6);
    }}
    .player-node.active {{
      transform: translate(-50%, -50%) scale(1.16);
      border-color: #ffffff;
      background: var(--pitch-green);
      box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.5), 0 6px 16px rgba(0, 0, 0, 0.6);
      z-index: 12;
    }}
    .player-node-num {{
      font-size: 13.5px;
      font-weight: 800;
      color: #0f172a;
      line-height: 1;
      transition: color 0.15s;
    }}
    .player-node.active .player-node-num {{
      color: #ffffff;
    }}
    .player-node-label {{
      position: absolute;
      bottom: -17px;
      font-size: 10px;
      font-weight: 700;
      color: #f1f5f9;
      background: rgba(15, 23, 42, 0.85);
      padding: 1px 5px;
      border-radius: 3px;
      border: 1px solid rgba(255, 255, 255, 0.15);
      white-space: nowrap;
      pointer-events: none;
      transition: all 0.15s;
    }}
    .player-node.active .player-node-label {{
      color: #000;
      background: var(--pitch-green);
      border-color: var(--pitch-green);
      font-weight: 800;
    }}

    /* Pitch Bottom Controls */
    .pitch-footer-controls {{
      margin-top: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: var(--bg-subsurface);
      padding: 9px 12px;
      border-radius: 8px;
      font-size: 12px;
      border: 1px solid var(--border-subtle);
    }}

    /* Right Role Card */
    .role-card-deck {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 20px 22px;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-card);
    }}
    .role-card-head {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 12px;
      margin-bottom: 14px;
    }}
    .role-card-title {{
      font-size: 17px;
      font-weight: 700;
      color: var(--text-main);
      letter-spacing: -0.01em;
    }}
    .role-card-code {{
      font-size: 12px;
      color: var(--accent-gold);
      font-weight: 600;
      margin-top: 2px;
    }}
    .role-duty-block {{
      background: var(--bg-subsurface);
      border-left: 3px solid var(--pitch-green);
      padding: 10px 14px;
      border-radius: 0 8px 8px 0;
      font-size: 13px;
      color: var(--text-main);
      line-height: 1.6;
      margin-bottom: 16px;
    }}

    /* Tactical Timeline Stepper (Replacing bulky box-in-a-box) */
    .timeline-stepper {{
      display: flex;
      flex-direction: column;
      position: relative;
      padding-left: 20px;
      margin-bottom: 18px;
    }}
    .timeline-stepper::before {{
      content: '';
      position: absolute;
      left: 7px;
      top: 12px;
      bottom: 24px;
      width: 2px;
      background: var(--border-subtle);
    }}
    .stepper-item {{
      position: relative;
      padding-bottom: 14px;
    }}
    .stepper-item:last-child {{
      padding-bottom: 0;
    }}
    .stepper-dot {{
      position: absolute;
      left: -20px;
      top: 3px;
      width: 16px;
      height: 16px;
      border-radius: 50%;
      background: var(--bg-surface);
      border: 2px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s;
    }}
    .stepper-dot::after {{
      content: '';
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--text-muted);
    }}
    .stepper-item.pre .stepper-dot {{ border-color: var(--pitch-green); }}
    .stepper-item.pre .stepper-dot::after {{ background: var(--pitch-green); }}
    .stepper-item.main .stepper-dot {{ border-color: var(--accent-gold); }}
    .stepper-item.main .stepper-dot::after {{ background: var(--accent-gold); }}
    .stepper-item.post .stepper-dot {{ border-color: var(--pitch-green); }}
    .stepper-item.post .stepper-dot::after {{ background: var(--pitch-green); }}
    .stepper-header {{
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 4px;
    }}
    .stepper-tag {{
      font-size: 11.5px;
      font-weight: 700;
    }}
    .stepper-item.pre .stepper-tag {{ color: var(--pitch-green); }}
    .stepper-item.main .stepper-tag {{ color: var(--accent-gold); }}
    .stepper-item.post .stepper-tag {{ color: var(--pitch-green); }}
    .stepper-timing {{
      font-size: 11px;
      color: var(--text-muted);
    }}
    .stepper-desc {{
      font-size: 13px;
      line-height: 1.55;
      color: var(--text-sub);
    }}

    /* Backward compatibility for action-row */
    .three-action-group {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-bottom: 16px;
    }}
    .action-row {{
      background: var(--bg-subsurface);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 10px 12px;
    }}
    .action-row-title {{
      font-size: 11.5px;
      font-weight: 700;
      margin-bottom: 3px;
    }}
    .action-row.pre .action-row-title {{ color: var(--pitch-green); }}
    .action-row.main .action-row-title {{ color: var(--accent-gold); }}
    .action-row.post .action-row-title {{ color: var(--pitch-green); }}
    .action-row-desc {{
      font-size: 12.5px;
      color: var(--text-sub);
      line-height: 1.5;
    }}

    .role-meta-row {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-top: 4px;
    }}
    .role-meta-box {{
      background: var(--bg-subsurface);
      border-radius: 8px;
      padding: 10px 12px;
      border: 1px solid var(--border-subtle);
    }}
    .role-meta-label {{
      font-size: 11px;
      color: var(--text-muted);
      font-weight: 600;
      margin-bottom: 3px;
    }}
    .role-meta-val {{
      font-size: 12.5px;
      color: var(--text-main);
      font-weight: 600;
      line-height: 1.4;
    }}

    /* ========================================================
       MODULE 02: DOCTRINES WITH WEAPON CAPSULES (STEP 2 核心)
       ======================================================== */
    .doctrine-filter-bar {{
      display: flex;
      gap: 8px;
      margin-bottom: 18px;
      flex-wrap: wrap;
    }}
    .doctrine-filter-btn {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 18px;
      font-size: 12px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .doctrine-filter-btn:hover {{
      background: var(--bg-subsurface);
      color: var(--text-main);
    }}
    .doctrine-filter-btn.active {{
      background: var(--bg-subsurface);
      border-color: var(--pitch-green);
      color: var(--pitch-green);
      font-weight: 600;
    }}

    .doctrine-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-card);
      transition: border-color 0.15s;
    }}
    .doctrine-card:hover {{ border-color: var(--border-focus); }}
    .doctrine-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}
    .doctrine-card-title {{
      font-size: 15px;
      font-weight: 700;
      color: var(--text-main);
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .doctrine-tag {{
      font-size: 10.5px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 5px;
      background: rgba(56, 189, 248, 0.1);
      color: var(--accent-cyan);
      border: 1px solid rgba(56, 189, 248, 0.2);
    }}

    .doctrine-anim-box {{
      background: #000;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
      position: relative;
      cursor: zoom-in;
      overflow: hidden;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .doctrine-anim-box img {{
      width: 100%;
      height: auto;
      max-height: 240px;
      object-fit: contain;
      display: block;
    }}
    .doctrine-anim-box::after {{
      content: '🔍 点击全屏放大';
      position: absolute;
      bottom: 8px;
      right: 10px;
      background: rgba(15, 23, 42, 0.85);
      color: #fff;
      font-size: 10.5px;
      padding: 3px 7px;
      border-radius: 4px;
      opacity: 0;
      transition: opacity 0.15s;
      pointer-events: none;
      border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    .doctrine-anim-box:hover::after {{ opacity: 1; }}

    .doctrine-steps-list {{
      font-size: 12.5px;
      line-height: 1.6;
      color: var(--text-sub);
      margin-bottom: 12px;
    }}

    /* Clickable Weapon Pills Inside Doctrine */
    .doctrine-weapons-group {{
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
      margin-top: auto;
      padding-top: 10px;
      border-top: 1px solid var(--border-subtle);
    }}
    .doctrine-weapon-pill {{
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 6px;
      background: var(--bg-subsurface);
      color: var(--text-main);
      border: 1px solid var(--border-subtle);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .doctrine-weapon-pill:hover {{
      background: rgba(245, 158, 11, 0.15);
      border-color: var(--accent-gold);
      color: var(--accent-gold);
    }}

    /* ========================================================
       MODULE 03: WEAPON CONSOLE STYLES
       ======================================================== */
    .category-tabs {{
      display: flex;
      gap: 8px;
      margin-bottom: 18px;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 10px;
      flex-wrap: wrap;
    }}
    .cat-tab-btn {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 7px 15px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .cat-tab-btn:hover {{
      background: var(--bg-subsurface);
      color: var(--text-main);
    }}
    .cat-tab-btn.active {{
      background: var(--bg-subsurface);
      border-color: var(--pitch-green);
      color: var(--pitch-green);
      font-weight: 600;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }}
    .weapon-console-grid {{
      display: grid;
      grid-template-columns: 55% 45%;
      gap: 20px;
      align-items: start;
    }}
    .player-deck {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 16px;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
    }}
    .player-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}
    .player-title {{
      font-size: 15px;
      font-weight: 700;
      color: var(--text-main);
    }}
    .player-tag {{
      font-size: 11px;
      padding: 2px 8px;
      border-radius: 5px;
      background: rgba(56, 189, 248, 0.1);
      color: var(--accent-cyan);
      border: 1px solid rgba(56, 189, 248, 0.2);
      font-weight: 600;
    }}
    .anim-display {{
      background: #000;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
      position: relative;
      cursor: zoom-in;
      overflow: hidden;
      min-height: 360px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}
    .anim-display img {{
      width: 100%;
      height: auto;
      max-height: 400px;
      object-fit: contain;
      display: block;
    }}
    .anim-display::after {{
      content: '🔍 点击全屏放大观察';
      position: absolute;
      bottom: 10px;
      right: 12px;
      background: rgba(15, 23, 42, 0.85);
      color: #fff;
      font-size: 11px;
      font-weight: 500;
      padding: 3px 8px;
      border-radius: 4px;
      opacity: 0;
      transition: opacity 0.15s;
      pointer-events: none;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }}
    .anim-display:hover::after {{ opacity: 1; }}

    .player-switcher-bar {{
      margin-top: 10px;
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
      background: var(--bg-subsurface);
      padding: 6px;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
    }}
    .switcher-pill {{
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-muted);
      padding: 5px 10px;
      border-radius: 6px;
      font-size: 11.5px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .switcher-pill:hover {{
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.05);
    }}
    .switcher-pill.active {{
      background: var(--bg-surface);
      border-color: var(--pitch-green);
      color: var(--pitch-green);
      font-weight: 600;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
    }}

    .player-details {{
      margin-top: 12px;
      background: var(--bg-subsurface);
      border-radius: 8px;
      padding: 12px 14px;
      border-left: 3px solid var(--accent-gold);
    }}
    .player-details-title {{
      font-size: 12.5px;
      font-weight: 700;
      color: var(--accent-gold);
      margin-bottom: 4px;
    }}
    .player-details-desc {{
      font-size: 12.5px;
      color: var(--text-sub);
      line-height: 1.55;
    }}

    .weapon-list-container {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .weapon-select-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 13px 15px;
      cursor: pointer;
      transition: all 0.15s ease;
      position: relative;
    }}
    .weapon-select-card:hover {{
      border-color: var(--border-focus);
      transform: translateX(3px);
    }}
    .weapon-select-card.active {{
      border-color: var(--pitch-green);
      background: rgba(16, 185, 129, 0.08);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }}
    .weapon-card-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 5px;
    }}
    .weapon-name {{
      font-size: 14px;
      font-weight: 700;
      color: var(--text-main);
    }}
    .weapon-en {{
      font-size: 11px;
      color: var(--text-muted);
    }}
    .weapon-body {{
      font-size: 12.5px;
      color: var(--text-sub);
      line-height: 1.5;
    }}
    .weapon-callout {{
      margin-top: 6px;
      display: inline-block;
      font-size: 11px;
      padding: 2px 7px;
      border-radius: 4px;
      background: var(--bg-subsurface);
      color: var(--pitch-green);
      border: 1px solid var(--border-subtle);
    }}

    /* Lightbox Modal */
    .lightbox-modal {{
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: rgba(10, 14, 12, 0.94);
      backdrop-filter: blur(16px);
      z-index: 9999;
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      user-select: none;
    }}
    .lightbox-modal.open {{ display: flex; }}
    .lightbox-controls {{
      position: absolute;
      top: 16px; left: 24px; right: 24px;
      display: flex; justify-content: space-between; align-items: center;
      z-index: 10001;
    }}
    .lightbox-title-badge {{
      font-size: 14px; font-weight: 600; color: #fff;
      background: rgba(20, 28, 24, 0.9);
      border: 1px solid var(--border-subtle);
      padding: 6px 16px; border-radius: 20px;
    }}
    .lb-btn {{
      background: rgba(20, 28, 24, 0.9);
      border: 1px solid var(--border-subtle);
      color: #fff; padding: 6px 14px; border-radius: 6px;
      font-size: 12px; font-weight: 500; cursor: pointer; transition: all 0.15s ease;
    }}
    .lb-btn:hover {{ background: var(--pitch-green); color: #000; border-color: var(--pitch-green); }}
    .lb-btn.close:hover {{ background: var(--accent-red); color: #fff; border-color: var(--accent-red); }}
    .lightbox-viewport {{
      max-width: 92vw; max-height: 84vh;
      display: flex; align-items: center; justify-content: center;
      overflow: hidden; cursor: grab;
    }}
    .lightbox-viewport:active {{ cursor: grabbing; }}
    #lightbox-img {{
      max-width: 100%; max-height: 82vh; object-fit: contain;
      border-radius: 8px; box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95);
      transition: transform 0.08s ease-out;
    }}
    .lightbox-hint {{
      position: absolute; bottom: 16px; font-size: 11.5px; color: #94a3b8;
      background: rgba(20, 28, 24, 0.85); padding: 4px 14px;
      border-radius: 12px; border: 1px solid var(--border-subtle);
    }}

    /* Weapon Quick Pop-up Modal */
    .weapon-modal-overlay {{
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
      z-index: 10000;
      display: none;
      align-items: center;
      justify-content: center;
    }}
    .weapon-modal-overlay.open {{ display: flex; }}
    .weapon-modal-card {{
      background: var(--bg-surface);
      color: var(--text-main);
      border: 1px solid var(--border-focus);
      border-radius: 14px;
      padding: 22px;
      width: 500px;
      max-width: 90vw;
      box-shadow: var(--shadow-float);
      animation: popIn 0.2s ease-out;
    }}
    @keyframes popIn {{
      from {{ transform: scale(0.95); opacity: 0; }}
      to {{ transform: scale(1); opacity: 1; }}
    }}
    .weapon-modal-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }}
    .weapon-modal-btn-close {{
      background: var(--bg-subsurface);
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 4px 10px; border-radius: 6px; cursor: pointer;
    }}

    /* ========================================================
       MODULE 05: MATCHDAY CRISIS SOLVER & CODES (STEP 3 核心)
       ======================================================== */
    .crisis-tabs {{
      display: flex;
      gap: 8px;
      margin-bottom: 18px;
      flex-wrap: wrap;
    }}
    .crisis-tab-btn {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      padding: 8px 16px;
      border-radius: 20px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .crisis-tab-btn:hover {{
      background: var(--bg-subsurface);
      color: var(--text-main);
    }}
    .crisis-tab-btn.active {{
      background: rgba(239, 68, 68, 0.12);
      border-color: var(--accent-red);
      color: var(--accent-red);
      font-weight: 700;
    }}
    .crisis-dashboard-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 22px;
      display: grid;
      grid-template-columns: 1.15fr 0.85fr;
      gap: 24px;
      box-shadow: var(--shadow-card);
      margin-bottom: 24px;
    }}
    .crisis-callout-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 14px 16px;
      transition: all 0.15s ease;
      box-shadow: var(--shadow-card);
    }}
    .crisis-callout-card:hover {{
      border-color: var(--border-focus);
      transform: translateY(-2px);
    }}
  </style>
</head>
<body>

  <!-- Left Sidebar Navigation -->
  <aside class="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-title">⚽ 德国战术战情室</div>
      <div class="sidebar-subtitle">TACTICAL COMMAND HUB · 7v7 / 8v8</div>
    </div>
    <nav class="nav-menu">
      <div class="nav-item" onclick="switchView('view-foundations')">
        <span>📐 01. 战术基石与网格</span>
        <span class="nav-badge">理念</span>
      </div>
      <div class="nav-item" onclick="switchView('view-doctrines')">
        <span>⚔️ 02. 八大实战进攻流派</span>
        <span class="nav-badge">武器联动</span>
      </div>
      <div class="nav-item" onclick="switchView('view-weapons')">
        <span>🎯 03. 20项传球武器点播台</span>
        <span class="nav-badge" style="background: var(--pitch-green); color:#000;">点播台</span>
      </div>
      <div class="nav-item active" onclick="switchView('view-formations')">
        <span>📋 04. 阵型与球员职责卡</span>
        <span class="nav-badge" style="background: var(--accent-gold); color:#000;">互动球场</span>
      </div>
      <div class="nav-item" onclick="switchView('view-decisions')">
        <span>⚡ 05. 临场破局与口令手册</span>
        <span class="nav-badge">决策</span>
      </div>
    </nav>
    <div class="sidebar-footer">
      <div style="font-weight: 700; color: var(--pitch-green); font-size: 13px;">⚽ 现代足球传球战术教研室</div>
      <div style="font-size: 11px; margin-top: 3px; opacity: 0.85;">《足球训练完全图解》研学转化中枢</div>
    </div>
  </aside>

  <!-- Main Content Area -->
  <main class="main-content">

    <!-- Top Utility Bar -->
    <header class="topbar">
      <div class="current-view-title" id="topbar-title">
        <span>📋 模块 04 · 阵型架构与球员职责卡</span>
        <span class="view-tag">互动球场画板版</span>
      </div>
      <div class="top-actions">
        <!-- 3-Theme Palette Switcher -->
        <div class="theme-palette-group">
          <button class="theme-btn active" id="btn-theme-dark" onclick="setTheme('dark')" title="深色战术 (温润墨绿)">🌙 战术夜间</button>
          <button class="theme-btn" id="btn-theme-sepia" onclick="setTheme('sepia')" title="羊皮纸暖色 (柔和护眼)">📖 暖阳护眼</button>
          <button class="theme-btn" id="btn-theme-light" onclick="setTheme('light')" title="战术白板 (清晰明快)">☀️ 战术白板</button>
        </div>
        <button class="btn-action" onclick="toggleFullscreen()">⛶ 全屏显示</button>
      </div>
    </header>

    <!-- VIEW 04: 阵型架构与球员职责卡 (STEP 2 核心交付物) -->
    <div id="view-formations" class="view-container active">
      <div class="section-header">
        <h2>模块 04 · 阵型架构与互动球场画板 (Interactive Pitch Board)</h2>
        <p>在左侧战术板上<strong>点击任意球员号码（如 4号后腰、7号前锋）</strong>，右侧立即切换该位置的攻防使命、三动作行为规范及配套战术跑位！</p>
      </div>

      <!-- Formation Switcher Tabs -->
      <div class="formation-nav">
        <button class="formation-tab-btn active" onclick="switchFormation('1231')">7人制 1-2-3-1 (经典压迫传控)</button>
        <button class="formation-tab-btn" onclick="switchFormation('1321')">7人制 1-3-2-1 (圣诞树稳守反击)</button>
        <button class="formation-tab-btn" onclick="switchFormation('1331')">8人制 1-3-3-1 (黄金全能阵型)</button>
      </div>

      <!-- Pitch Workbench (Left: Interactive Pitch, Right: Active Player Role Card) -->
      <div class="pitch-workbench">

        <!-- Left Interactive Pitch Board -->
        <div class="pitch-container">
          <div class="pitch-header-info">
            <div class="pitch-title" id="pitch-formation-title">7人制 1-2-3-1 经典压迫传控阵型</div>
            <div class="pitch-badge" id="pitch-formation-tag">适合控球压迫 / 实力占优</div>
          </div>

          <!-- The Pitch Canvas with Clickable Player Nodes -->
          <div class="pitch-board" id="interactive-pitch">
            <!-- Markings -->
            <div class="pitch-marking pitch-half-line"></div>
            <div class="pitch-marking pitch-center-circle"></div>
            <div class="pitch-marking pitch-center-spot"></div>
            <div class="pitch-marking pitch-penalty-top"></div>
            <div class="pitch-marking pitch-penalty-bottom"></div>

            <!-- Dynamic Player Nodes will be injected here by JS -->
            <div id="pitch-players-layer"></div>
          </div>

          <div class="pitch-footer-controls">
            <span style="color: var(--text-muted);">💡 提示：点击场上球员圆点查看职责卡</span>
            <button class="btn-action" onclick="openFormationAnimLightbox()" style="font-size: 11.5px; padding: 4px 10px;">
              🎬 查看阵型跑位沙盘动图
            </button>
          </div>
        </div>

        <!-- Right Active Player Role Card Deck -->
        <div class="role-card-deck">
          <div class="role-card-head">
            <div>
              <div class="role-card-title" id="role-title">4号 中前卫/核心节拍器</div>
              <div class="role-card-code" id="role-code">Central Midfielder (CM) · 攻防枢纽</div>
            </div>
            <span class="weapon-badge" id="role-num-badge">No. 4</span>
          </div>

          <div class="role-duty-block" id="role-duty">
            全队攻防节奏掌控者；负责在双中卫身前构建安全接应三角形，主导弱侧大范围调度与第三人反越位直塞。
          </div>

          <!-- Tactical Timeline Stepper -->
          <div class="timeline-stepper">
            <div class="stepper-item pre">
              <div class="stepper-dot"></div>
              <div class="stepper-header">
                <span class="stepper-tag">01. 接球前预判</span>
                <span class="stepper-timing">Pre-Action · 提前0.5秒观察</span>
              </div>
              <div class="stepper-desc" id="role-pre">保持半侧身面向前场边线，皮球滑行中完成身后防守盲区扫描2次，拒绝死板背对球门。</div>
            </div>
            <div class="stepper-item main">
              <div class="stepper-dot"></div>
              <div class="stepper-header">
                <span class="stepper-tag">02. 触球主动作</span>
                <span class="stepper-timing">Main-Action · 精准执行出球</span>
              </div>
              <div class="stepper-desc" id="role-main">用远离逼抢脚外侧顺势领球摆脱；一脚触球即完成控球转向，出球低平快。</div>
            </div>
            <div class="stepper-item post">
              <div class="stepper-dot"></div>
              <div class="stepper-header">
                <span class="stepper-tag">03. 出球后衔接</span>
                <span class="stepper-timing">Post-Action · 传完即动二次接应</span>
              </div>
              <div class="stepper-desc" id="role-post">出球后立即二次启动前插接应或横移保护防线肋部空当；丢球0.5秒内就地反抢。</div>
            </div>
          </div>

          <div class="role-meta-row">
            <div class="role-meta-box">
              <div class="role-meta-label">🛠️ 核心传球武器</div>
              <div class="role-meta-val" id="role-weapons">W01直塞 · W08第三人 · W09对角</div>
            </div>
            <div class="role-meta-box">
              <div class="role-meta-label">📢 专属呼应口令</div>
              <div class="role-meta-val" id="role-callout">“转过来！” / “看第三人！”</div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- VIEW 02: 八大流派 (STEP 2: 带武器胶囊联动) -->
    <div id="view-doctrines" class="view-container">
      <div class="section-header">
        <h2>模块 02 · 八大实战进攻流派全景沙盘 (Doctrines Hub)</h2>
        <p>全套 8 大进攻流派高帧率沙盘演示；<strong>点击卡片下方的武器胶囊标签</strong>可直接弹出对应武器的微观脚法要领！</p>
      </div>

      <!-- Category Filter Pills -->
      <div class="doctrine-filter-bar">
        <button class="doctrine-filter-btn active" onclick="filterDoctrines('all')">全部 8 大流派</button>
        <button class="doctrine-filter-btn" onclick="filterDoctrines('penetration')">地面渗透组</button>
        <button class="doctrine-filter-btn" onclick="filterDoctrines('transition')">转换与越顶组</button>
        <button class="doctrine-filter-btn" onclick="filterDoctrines('flank')">边路与终结组</button>
        <button class="doctrine-filter-btn" onclick="filterDoctrines('setpiece')">特种与死球组</button>
      </div>

      <div class="grid-2" id="doctrines-grid">

        <!-- 流派 1 -->
        <div class="doctrine-card" data-category="penetration">
          <div class="doctrine-card-header">
            <div class="doctrine-card-title">🎬 流派① · 第三人跑位渗透 (Up-Back-Through)</div>
            <span class="doctrine-tag">地面渗透破密集</span>
          </div>
          <div class="doctrine-anim-box" onclick="openCustomLightbox('{b64_d01}', '流派① 第三人跑位渗透')">
            <img src="{b64_d01}" alt="流派①">
          </div>
          <div class="doctrine-steps-list">
            <strong>时序逻辑：</strong>后腰(4)直塞背身中锋(7)[Up] ➔ 中锋回做中场(6)[Back] ➔ 中场顺势直塞高速前插的第三人(5)单刀破门[Through]！
          </div>
          <div class="doctrine-weapons-group">
            <span style="font-size: 11px; color: var(--text-muted); margin-right:4px;">调用武器:</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w01')">W01 直塞穿透</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w06')">W06 迎前回做</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w07')">W07 刺穿线形</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w08')">W08 第三人导向</span>
          </div>
        </div>

        <!-- 流派 2 -->
        <div class="doctrine-card" data-category="flank">
          <div class="doctrine-card-header">
            <div class="doctrine-card-title">🎬 流派② · 强侧超载 ➔ 弱侧 1v1 转移</div>
            <span class="doctrine-tag">宽度调度破铁桶</span>
          </div>
          <div class="doctrine-anim-box" onclick="openCustomLightbox('{b64_d02}', '流派② 强侧超载弱侧转移')">
            <img src="{b64_d02}" alt="流派②">
          </div>
          <div class="doctrine-steps-list">
            <strong>时序逻辑：</strong>强侧左路连续短传吸附防线整体横移 ➔ 中场(6)突然起 30 米大对角斜长传 ➔ 弱侧右翼(7)在巨大无人空当内突入禁区！
          </div>
          <div class="doctrine-weapons-group">
            <span style="font-size: 11px; color: var(--text-muted); margin-right:4px;">调用武器:</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w09')">W09 对角长传</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w10')">W10 边线推进</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w11')">W11 弧线绕顶</span>
          </div>
        </div>

        <!-- 流派 3 -->
        <div class="doctrine-card" data-category="transition">
          <div class="doctrine-card-header">
            <div class="doctrine-card-title">🎬 流派③ · 纵深越顶反越位突袭</div>
            <span class="doctrine-tag">反高位压迫利器</span>
          </div>
          <div class="doctrine-anim-box" onclick="openCustomLightbox('{b64_d03}', '流派③ 纵深越顶身后打击')">
            <img src="{b64_d03}" alt="流派③">
          </div>
          <div class="doctrine-steps-list">
            <strong>时序逻辑：</strong>对手整体压上高位逼抢身后留 25 米空当 ➔ 中卫(3)送出精准过顶挑传 ➔ 中锋(7)从防守盲区反越位超车单刀垫射破门！
          </div>
          <div class="doctrine-weapons-group">
            <span style="font-size: 11px; color: var(--text-muted); margin-right:4px;">调用武器:</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w01')">W01 直塞穿透</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w02')">W02 肋部挑传</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w18')">W18 越顶快攻</span>
          </div>
        </div>

        <!-- 流派 4 -->
        <div class="doctrine-card" data-category="transition">
          <div class="doctrine-card-header">
            <div class="doctrine-card-title">🎬 流派④ · 攻防转换5秒快攻闪击</div>
            <span class="doctrine-tag">就地反抢闪电战</span>
          </div>
          <div class="doctrine-anim-box" onclick="openCustomLightbox('{b64_d04}', '流派④ 攻防转换5秒快攻')">
            <img src="{b64_d04}" alt="流派④">
          </div>
          <div class="doctrine-steps-list">
            <strong>时序逻辑：</strong>丢球 0.5s 内边翼(5)与前锋(7)就地合围断球 ➔ 立即刺穿直塞插上中场(6) ➔ 5 秒 3 脚内横推空门得手！
          </div>
          <div class="doctrine-weapons-group">
            <span style="font-size: 11px; color: var(--text-muted); margin-right:4px;">调用武器:</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w07')">W07 刺穿线形</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w17')">W17 门将穿透</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w18')">W18 越顶长传</span>
          </div>
        </div>

        <!-- 流派 5 -->
        <div class="doctrine-card" data-category="penetration">
          <div class="doctrine-card-header">
            <div class="doctrine-card-title">🎬 流派⑤ · 立体空战中锋胸部做球</div>
            <span class="doctrine-tag">破中场绞杀支点</span>
          </div>
          <div class="doctrine-anim-box" onclick="openCustomLightbox('{b64_d05}', '流派⑤ 空战支点胸部做球')">
            <img src="{b64_d05}" alt="流派⑤">
          </div>
          <div class="doctrine-steps-list">
            <strong>时序逻辑：</strong>后场起高球避开地面惨烈绞杀 ➔ 突前中锋(7)背身扛人胸部稳卸回做 ➔ 中场(6)禁区弧顶迎球不停球直接重炮轰门！
          </div>
          <div class="doctrine-weapons-group">
            <span style="font-size: 11px; color: var(--text-muted); margin-right:4px;">调用武器:</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w02')">W02 肋部挑传</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w06')">W06 迎前回做</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w14')">W14 假射真传</span>
          </div>
        </div>

        <!-- 流派 6 -->
        <div class="doctrine-card" data-category="flank">
          <div class="doctrine-card-header">
            <div class="doctrine-card-title">🎬 流派⑥ · 禁区底线倒三角终结</div>
            <span class="doctrine-tag">第一进球概率武器</span>
          </div>
          <div class="doctrine-anim-box" onclick="openCustomLightbox('{b64_d06}', '流派⑥ 禁区底线倒三角')">
            <img src="{b64_d06}" alt="流派⑥">
          </div>
          <div class="doctrine-steps-list">
            <strong>时序逻辑：</strong>边锋(7)突至底线迫使门将与防线退缩门线 ➔ 底线发力贴地倒三角推向点球点 ➔ 后插上中场(6)推射大半个空门！
          </div>
          <div class="doctrine-weapons-group">
            <span style="font-size: 11px; color: var(--text-muted); margin-right:4px;">调用武器:</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w03')">W03 底线倒三角</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w04')">W04 贴地横扫</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w08')">W08 第三人导向</span>
          </div>
        </div>

        <!-- 流派 7 -->
        <div class="doctrine-card" data-category="setpiece">
          <div class="doctrine-card-header">
            <div class="doctrine-card-title">🎬 流派⑦ · 迎球假接真漏特种破局</div>
            <span class="doctrine-tag">节奏欺骗破坏预判</span>
          </div>
          <div class="doctrine-anim-box" onclick="openCustomLightbox('{b64_d07}', '流派⑦ 迎球假接真漏')">
            <img src="{b64_d07}" alt="流派⑦">
          </div>
          <div class="doctrine-steps-list">
            <strong>时序逻辑：</strong>后腰(4)直塞中场(6) ➔ 中场假装接球瞬间突然叉腿漏球 ➔ 防守完全被假动作扑空，身后的中锋(7)单刀得手！
          </div>
          <div class="doctrine-weapons-group">
            <span style="font-size: 11px; color: var(--text-muted); margin-right:4px;">调用武器:</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w13')">W13 不看人传球</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w14')">W14 假射真传</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w16')">W16 漏球顺势</span>
          </div>
        </div>

        <!-- 流派 8 -->
        <div class="doctrine-card" data-category="setpiece">
          <div class="doctrine-card-header">
            <div class="doctrine-card-title">🎬 流派⑧ · 战术手抛界外球三角配合</div>
            <span class="doctrine-tag">死球重开转反击</span>
          </div>
          <div class="doctrine-anim-box" onclick="openCustomLightbox('{b64_d08}', '流派⑧ 战术手抛界外球')">
            <img src="{b64_d08}" alt="流派⑧">
          </div>
          <div class="doctrine-steps-list">
            <strong>时序逻辑：</strong>边卫(2)精准掷前锋(7)脚下 ➔ 前锋一脚回敲，边卫高速套边下底 ➔ 底线平抽横扫门前，包抄中场(6)抢点破门！
          </div>
          <div class="doctrine-weapons-group">
            <span style="font-size: 11px; color: var(--text-muted); margin-right:4px;">调用武器:</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w03')">W03 倒三角</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w04')">W04 贴地横扫</span>
            <span class="doctrine-weapon-pill" onclick="popWeaponModal('w20')">W20 战术界外球</span>
          </div>
        </div>

      </div>
    </div>

    <!-- VIEW 03: 20 传球武器点播台 (保持顶级交互) -->
    <div id="view-weapons" class="view-container">
      <div class="section-header">
        <h2>模块 03 · 20 种传球武器点播台 (Interactive Weapon Console)</h2>
        <p>支持单个武器独立点播！点击右侧任意武器卡片，左侧战术屏幕立即切换该武器的专属动图与微动作要领。</p>
      </div>

      <!-- Category Switcher Tabs -->
      <div class="category-tabs">
        <button class="cat-tab-btn active" onclick="switchCategory(1)">分类一：穿透与终结 (W01-W04)</button>
        <button class="cat-tab-btn" onclick="switchCategory(2)">分类二：破压与渗透 (W05-W08)</button>
        <button class="cat-tab-btn" onclick="switchCategory(3)">分类三：宽度与调度 (W09-W12)</button>
        <button class="cat-tab-btn" onclick="switchCategory(4)">分类四：隐蔽与特种 (W13-W16)</button>
        <button class="cat-tab-btn" onclick="switchCategory(5)">分类五：现代与死球 (W17-W20)</button>
      </div>

      <div class="weapon-console-grid">
        <!-- Left Tactical Sandbox Player -->
        <div class="player-deck">
          <div class="player-header">
            <div class="player-title" id="player-title">W 01 · 直塞穿透球 (Through Ball)</div>
            <div class="player-tag" id="player-tag">贴地发力 · 刺穿中卫结合部</div>
          </div>
          <div class="anim-display" onclick="openPlayerLightbox()">
            <img id="player-gif" src="{b64_w01}" alt="武器演示动图">
          </div>
          <div class="player-switcher-bar" id="category-pills"></div>
          <div class="player-details">
            <div class="player-details-title" id="player-details-title">📌 技术要领与微观执行</div>
            <div class="player-details-desc" id="player-details-desc">
              脚内侧或正脚背贴地快速刺穿两条防线之间的空当；给足前锋前插提前量，让队友不降速领球单刀。
            </div>
            <div style="margin-top: 6px; font-size: 12px; color: var(--accent-cyan);" id="player-callout">
              📢 场上实战口令：“给身后！”
            </div>
          </div>
        </div>

        <!-- Right Weapon Select Cards -->
        <div class="weapon-list-container" id="weapon-cards-list"></div>
      </div>
    </div>

    <!-- VIEW 01: 战术基石 -->
    <div id="view-foundations" class="view-container">
      <div class="section-header">
        <h2>模块 01 · 战术基石与空间地图</h2>
        <p>德国足球传球战术认知变革、16 格空间网格纪律与球员微观“三动作体系”。</p>
      </div>
      <div class="grid-3" style="margin-bottom: 24px;">
        <div class="card">
          <div class="card-title red">❌ 传统业余误区</div>
          <p>只看脚下、静态站立等球、单打独斗盲目推进、在密集区以少打多扎堆。</p>
        </div>
        <div class="card">
          <div class="card-title green">✅ 现代德国战术真理</div>
          <p>传球即人际语言；球永远比人跑得快；通过三角站位制造局部 3v2；传向空当而非脚下。</p>
        </div>
        <div class="card">
          <div class="card-title gold">⚡ 全队三大铁律</div>
          <p>1. 后场中路绝不盲目横传<br>2. 保持开放半侧身面向前场<br>3. 接球前 0.5 秒完成盲区扫描</p>
        </div>
      </div>
      <div class="card">
        <div class="card-title green">📐 16 区域动态传球网格与同格不站双人法则</div>
        <p style="font-size: 13.5px; margin-bottom: 12px;">同一方格内严禁出现两名本方队员；全队保持 5~10 米黄金呼应间距，形成菱形与三角形接应网。</p>
        <div style="max-width: 650px; margin: 0 auto; background: var(--bg-subsurface); border: 1px solid var(--border-subtle); padding: 14px; border-radius: 10px;">
          <svg viewBox="0 0 500 280" width="100%">
            <rect width="500" height="280" fill="#071911" rx="6" stroke="var(--pitch-green)" stroke-width="1.5"/>
            <line x1="125" y1="0" x2="125" y2="280" stroke="var(--pitch-green)" stroke-opacity="0.35" stroke-dasharray="4,4"/>
            <line x1="250" y1="0" x2="250" y2="280" stroke="var(--pitch-green)" stroke-opacity="0.6" stroke-width="1.5"/>
            <line x1="375" y1="0" x2="375" y2="280" stroke="var(--pitch-green)" stroke-opacity="0.35" stroke-dasharray="4,4"/>
            <line x1="0" y1="70" x2="500" y2="70" stroke="var(--pitch-green)" stroke-opacity="0.35" stroke-dasharray="4,4"/>
            <line x1="0" y1="140" x2="500" y2="140" stroke="var(--pitch-green)" stroke-opacity="0.6" stroke-width="1.5"/>
            <line x1="0" y1="210" x2="500" y2="210" stroke="var(--pitch-green)" stroke-opacity="0.35" stroke-dasharray="4,4"/>
            <circle cx="250" cy="140" r="40" fill="none" stroke="var(--pitch-green)" stroke-opacity="0.6" stroke-width="1.5"/>
            <text x="250" y="144" fill="#f8fafc" font-size="11.5" font-weight="600" text-anchor="middle">中场控制核心区 (菱形接应)</text>
          </svg>
        </div>
      </div>
    </div>

    <!-- VIEW 05: 临场破局速查与呼应暗号 (STEP 3: 交互化破局引擎) -->
    <div id="view-decisions" class="view-container">
      <div class="section-header">
        <h2>模块 05 · 临场破局速查与呼应暗号 (Matchday Crisis Solver)</h2>
        <p>面对高位逼抢、低位铁桶与中场绞杀的实时交互式战术解药；点击场景即时获取破局组合拳与实战暗号。</p>
      </div>

      <!-- Crisis Scenario Switcher Tabs -->
      <div class="crisis-tabs">
        <button class="crisis-tab-btn active" onclick="switchCrisis('press')">🚨 破局① · 破解高位逼抢与贴身合围</button>
        <button class="crisis-tab-btn" onclick="switchCrisis('bus')">🧱 破局② · 撕碎低位铁桶与密集大巴</button>
        <button class="crisis-tab-btn" onclick="switchCrisis('mid')">⚔️ 破局③ · 突围中场惨烈绞杀与人荒</button>
        <button class="crisis-tab-btn" onclick="switchCrisis('late')">⏱️ 破局④ · 终场比分落后绝境反扑</button>
      </div>

      <!-- Crisis Prescription Dashboard -->
      <div class="crisis-dashboard-card" id="crisis-dashboard-content">
        <!-- Rendered by JS -->
      </div>

      <!-- Team Communication Codes Cheatsheet -->
      <div style="margin-top: 30px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
          <h3 style="font-size: 17px; color: var(--text-main); font-weight: 800; display: flex; align-items: center; gap: 8px;">
            📢 全队 8 大赛场呼应暗号速查盘 (8 Core Communication Codes)
          </h3>
          <span style="font-size: 12px; color: var(--pitch-green); font-weight: 600;">全队语言统一 · 消除 0.5 秒犹豫时延</span>
        </div>

        <div class="grid-4" id="callouts-grid">
          <!-- Rendered by JS -->
        </div>
      </div>
    </div>

  </main>

  <!-- Global Lightbox Zoom Viewer -->
  <div id="lightbox-modal" class="lightbox-modal" onclick="closeLightbox(event)">
    <div class="lightbox-controls" onclick="event.stopPropagation()">
      <span class="lightbox-title-badge" id="lightbox-title">战术动图放大观察</span>
      <div style="display: flex; gap: 8px;">
        <button class="lb-btn" onclick="zoomIn()">➕ 放大</button>
        <button class="lb-btn" onclick="zoomOut()">➖ 缩小</button>
        <button class="lb-btn" onclick="resetZoom()">⟲ 还原</button>
        <button class="lb-btn close" onclick="closeLightboxDirect()">✕ 关闭 [ESC]</button>
      </div>
    </div>
    <div class="lightbox-viewport" id="lb-viewport" onclick="event.stopPropagation()">
      <img id="lightbox-img" src="" alt="战术放大图">
    </div>
    <div class="lightbox-hint">💡 滚轮缩放 | 按住拖拽平移 | 双击切换 1x/2x | ESC 退出</div>
  </div>

  <!-- Quick Weapon Pop-up Modal (From Doctrine Pills) -->
  <div id="weapon-modal" class="weapon-modal-overlay" onclick="closeWeaponModal(event)">
    <div class="weapon-modal-card" onclick="event.stopPropagation()">
      <div class="weapon-modal-head">
        <div>
          <span class="weapon-badge" id="wmodal-num">W 01</span>
          <strong style="font-size: 17px; margin-left: 8px; color: var(--text-main);" id="wmodal-name">直塞穿透球</strong>
        </div>
        <button class="weapon-modal-btn-close" onclick="closeWeaponModalDirect()">✕</button>
      </div>
      <div class="anim-display" style="min-height: 220px; max-height: 240px; margin-bottom: 12px;">
        <img id="wmodal-gif" src="" alt="武器动图" style="max-height: 230px;">
      </div>
      <div style="font-size: 13px; color: var(--text-sub); line-height: 1.55; margin-bottom: 12px;" id="wmodal-desc"></div>
      <div style="display: flex; justify-content: space-between; align-items: center;">
        <span style="font-size: 12px; color: var(--accent-cyan);" id="wmodal-callout"></span>
        <button class="btn-action" onclick="jumpToWeaponFromModal()" style="font-size: 11.5px; padding: 4px 10px;">
          前往武器点播台查看 →
        </button>
      </div>
    </div>
  </div>

  <script>
    // ==========================================
    // 1. Formation Database (22 Players Total)
    // ==========================================
    const formationDatabase = {{
      '1231': {{
        name: '7人制 1-2-3-1 经典压迫传控阵型',
        tag: '适合控球压迫 / 进攻宽度充足 / 实力占优',
        animGif: '{b64_f1231}',
        players: [
          {{
            num: 1, pos: 'GK', name: '门卫 (Goalkeeper)', code: '出球型门将 · 后场+1核心',
            x: 50, y: 88,
            duty: '站位推至大禁区弧顶，与双中卫构成 3v2 局部人数优势；主导地面刺穿出球与大禁区外高位扫荡。',
            pre: '皮球在对方半场时，站位推至禁区外弧顶，观察对方长传反击落点。',
            main: '接回传球永远向立柱外侧领球；出球发力穿透逼抢线直塞中场。',
            post: '出球后立即横向移动拉开新接应角度，随时准备再接中卫回敲。',
            weapons: 'W17 门将穿透 · W18 越顶长传',
            callout: '“门将出球！” / “回传立柱！”'
          }},
          {{
            num: 2, pos: 'CB', name: '左中卫 (Left Center-Back)', code: '出球中卫 · 破压直塞',
            x: 28, y: 72,
            duty: '持球时大范围拉开至左侧肋部，拉扯对方锋线间距；向前送出刺穿直塞，防守时封锁左肋通道。',
            pre: '接门将球前半侧身面向左路前场，观察中场 4号 与左翼 5号 跑位。',
            main: '远离前锋逼抢的外侧脚顺势停球，脚内侧发力平推刺穿中路。',
            post: '出球后保持阵型纵深，绝不上头前压导致身后大片空当。',
            weapons: 'W01 直塞穿透 · W10 边线推进',
            callout: '“给身前！” / “半侧身！”'
          }},
          {{
            num: 3, pos: 'CB', name: '右中卫 (Right Center-Back)', code: '出球中卫 · 大范围调度',
            x: 72, y: 72,
            duty: '后防出球发起人；负责右路向前推进，在强侧受阻时送出 30 米大对角长传转移至弱侧。',
            pre: '接球前快速摆头扫描前场右路走廊，保持身体朝向右前方。',
            main: '一脚触球顺势连停带过，脚背内侧大力长传或低平直塞。',
            post: '出球后与左中卫保持平行梯次保护，防止被对手单刀偷袭。',
            weapons: 'W07 刺穿线形 · W09 对角长传',
            callout: '“看弱侧！” / “转过来！”'
          }},
          {{
            num: 4, pos: 'CM', name: '中前卫 (Central Midfielder)', code: '攻防节拍器 · 阵型心脏',
            x: 50, y: 50,
            duty: '全队攻防节奏掌控者；在后场双中卫身前形成接应三角，前场主导第三人跑位直塞与弱侧调度。',
            pre: '皮球在运动中必须快速回头观察身后防守 2 次，保持半侧身迎球。',
            main: '远离防守的外侧脚停球转身，一脚出球直塞盲区插上的边锋。',
            post: '出球后立即二次前插禁区弧顶抢第二落点，或回撤保护中路防区。',
            weapons: 'W01 直塞 · W08 第三人 · W14 假射真传',
            callout: '“转过来！” / “看第三人！”'
          }},
          {{
            num: 5, pos: 'LW', name: '左边锋 (Left Winger)', code: '边路爆点 · 下底倒三角',
            x: 20, y: 34,
            duty: '进攻拉满左侧宽度；利用速度打边线 1v1 突破，杀至底线送出致命倒三角回传或前点平抽。',
            pre: '紧贴边线站位压低重心，接球前向防守靠近后突然反向迎球。',
            main: '顺势将球领向进攻方向，底线发力贴地推向点球点无人区。',
            post: '传球后立即前冲门前准备补射，丢球后就地封堵边线出球路线。',
            weapons: 'W03 倒三角 · W04 贴地横扫 · W05 撞墙',
            callout: '“倒三角！” / “走边线！”'
          }},
          {{
            num: 6, pos: 'RW', name: '右边锋 (Right Winger)', code: '内切射手 · 弱侧终结者',
            x: 80, y: 34,
            duty: '强侧转移时的弱侧终结者；在左侧吸附防线时包抄后点，或利用二过一撞墙配合内切破门。',
            pre: '当球在左侧时，悄悄从后卫盲区向后点幽灵插上。',
            main: '迎着横传不停球直接推射远角，或顺势扣过滑铲后打门。',
            post: '出球后迅速内收到禁区肋部，防守时回撤协助右中卫防守。',
            weapons: 'W04 贴地横扫 · W05 撞墙 · W11 弧线',
            callout: '“后点包抄！” / “撞墙！”'
          }},
          {{
            num: 7, pos: 'ST', name: '突前中锋 (Striker)', code: '反抢第一发起人 · 支点做球',
            x: 50, y: 19,
            duty: '压制对方双中卫；背身扛人胸部卸球回做，前插反越位单刀，并领衔执行全队 5 秒就地反抢。',
            pre: '压在对方越位线上，防守盲区背身卡位，随时准备启动。',
            main: '迎球一脚轻推回做给后插上中场，做球要软方便施射。',
            post: '回做球后立刻转身加速冲向门前抢点，或反身扑抢对方门将。',
            weapons: 'W02 挑传 · W06 迎前回做 · W16 漏球',
            callout: '“回敲！” / “给身后！”'
          }}
        ]
      }},
      '1321': {{
        name: '7人制 1-3-2-1 圣诞树稳守反击阵型',
        tag: '防守铁闸零死角 / 遇强敌 / 客场保胜 / 翼卫双核冲刺',
        animGif: '{b64_f1321}',
        players: [
          {{
            num: 1, pos: 'GK', name: '门将 (Goalkeeper)', code: '最后一道铁闸 · 反击发起',
            x: 50, y: 88,
            duty: '防守指挥官，封堵单刀，得球后 3 秒内大脚长传反击直找突前中锋身后。',
            pre: '大声指挥三后卫保持紧密间距，观察门前包抄漏洞。',
            main: '稳稳扑救击球，双手手抛球发动快攻。',
            post: '呼应全队防线快速前推，保持阵型紧凑。',
            weapons: 'W17 门将穿透 · W18 越顶反击',
            callout: '“收回来！” / “门将出球！”'
          }},
          {{
            num: 2, pos: 'LWB', name: '左翼卫 (Left Wing-Back)', code: '边路飞翼 · 往返走廊',
            x: 18, y: 64,
            duty: '边路走廊主宰；进攻全速前插下底送倒三角，防守回撤成 5 人防线铁壁。',
            pre: '观察居中中卫拦截时机，一旦断球立即沿边线全速前插。',
            main: '底线高速奔跑中脚内侧平抽横扫门前走廊。',
            post: '进攻被阻立即全速退回本方禁区边线落位。',
            weapons: 'W03 倒三角 · W10 边线推进',
            callout: '“走外侧！” / “回防！”'
          }},
          {{
            num: 3, pos: 'CB', name: '居中中卫 (Center-Back)', code: '后防定海神针 · 绝不上抢失位',
            x: 50, y: 74,
            duty: '后防统帅；严禁盲目上抢；负责中路补位卡线、解围与断球后第一脚纵向连线中锋。',
            pre: '时刻观察对方中锋跑位，呼喊两翼翼卫保持横向间距。',
            main: '果断拦截解围，或脚背发力踢出 35 米精准过顶长传。',
            post: '出球后稳守禁区弧顶，指挥全队保持平衡。',
            weapons: 'W01 直塞 · W18 越顶长传',
            callout: '“收紧中路！” / “直接起身后！”'
          }},
          {{
            num: 4, pos: 'RWB', name: '右翼卫 (Right Wing-Back)', code: '边路飞翼 · 弱侧包抄',
            x: 82, y: 64,
            duty: '右路走廊飞翼；在左路反击时高速前插包抄远门柱，防守收缩锁死右肋。',
            pre: '防守时内收至禁区角保护肋部，反击瞬间外扩拉开宽度。',
            main: '迎球不停球直接打门或贴地平抽门前。',
            post: '反抢未果立即后撤与中卫组成链式防线。',
            weapons: 'W04 贴地横扫 · W20 战术界外球',
            callout: '“压上去！” / “倒三角！”'
          }},
          {{
            num: 5, pos: 'DM', name: '防守型后腰 (Defensive Midfielder)', code: '中场绞肉机 · 弧顶锁匠',
            x: 50, y: 52,
            duty: '锁死禁区弧顶核心危险区；负责扫荡破坏对方直塞，完成安全球回敲或横传分边。',
            pre: '始终将身体置于球与禁区弧顶之间，观察对方前插球员。',
            main: '上抢卡位断球，一脚触球软推给身边的 6号 进攻核心。',
            post: '出球后原地构筑防线第一道屏障，绝不前插失位。',
            weapons: 'W06 迎前回做 · W12 回传重组',
            callout: '“身后有人！” / “回敲！”'
          }},
          {{
            num: 6, pos: 'AM', name: '前插组织中场 (Attacking Midfielder)', code: '影子杀手 · 弧顶重炮',
            x: 50, y: 36,
            duty: '反击进攻发动机；在中锋背身扛人做球瞬间高速前插到弧顶迎球爆射，或分边翼卫。',
            pre: '在中锋争顶前观察第二落点，保持半侧身起跑姿态。',
            main: '迎着回做球不停球直接重炮轰门，或假射真扣分给翼卫。',
            post: '射门后跟进补射，丢球后就地封堵对方后腰传球路线。',
            weapons: 'W01 直塞 · W08 第三人 · W14 假射真传',
            callout: '“回敲我打！” / “分两边！”'
          }},
          {{
            num: 7, pos: 'ST', name: '强力支点中锋 (Target Striker)', code: '高空霸主 · 背身扛人',
            x: 50, y: 19,
            duty: '强力背身扛人；接后场长传用胸部或头球稳稳摆渡做球给 6号 或两翼插上的飞翼。',
            pre: '靠住后卫用后背感受防守重心，起跳争顶抢第一落点。',
            main: '胸部卸球轻推回做，或脚后跟巧塞两翼跑动路线。',
            post: '做球后转身前冲禁区，抢前点垫射折射。',
            weapons: 'W02 挑传 · W06 回敲 · W16 假接真漏',
            callout: '“看身后！” / “回敲！”'
          }}
        ]
      }},
      '1331': {{
        name: '8人制 1-3-3-1 现代黄金全能阵型',
        tag: '攻守完美平衡 / 边路双人组套边 / 12+三角传递网',
        animGif: '{b64_f1331}',
        players: [
          {{
            num: 1, pos: 'GK', name: '门卫 (Goalkeeper)', code: '现代门卫 · 高位扫荡',
            x: 50, y: 88,
            duty: '大禁区弧顶扫荡指挥官；主导 3 后卫地面出球，随时前冲化解对方打身后反击。',
            pre: '全队压上时推至禁区外弧顶，观察反击空当。',
            main: '脚内侧大力贴地穿透直塞中场 6号。',
            post: '出球后拉开新角度随时接回传。',
            weapons: 'W17 门将穿透 · W18 越顶长传',
            callout: '“门将直穿！” / “转过来！”'
          }},
          {{
            num: 2, pos: 'LB', name: '左后卫 (Left Back)', code: '边路套边器 · 攻防双能',
            x: 20, y: 72,
            duty: '边路屏障；进攻推至中线与 5号 边前卫形成 2v1 外侧套边配合，杀入底线传中。',
            pre: '边前卫内切时，提前向外侧启动冲刺准备套边。',
            main: '高速插上接直塞一脚低平球横抽门前。',
            post: '失球后立即全速回追封堵边路身后。',
            weapons: 'W03 倒三角 · W05 撞墙 · W10 边线',
            callout: '“外侧套边！” / “倒三角！”'
          }},
          {{
            num: 3, pos: 'CB', name: '居中中卫 (Center-Back)', code: '后防总指挥 · 大范围调度',
            x: 50, y: 75,
            duty: '后防总指挥；前压压缩中场空间；送出 35 米大对角长传转移弱侧。',
            pre: '保持与两名边后卫的呼应，扫描中场前插点。',
            main: '脚背内侧大力斜长传，刺穿中路。',
            post: '出球后保持阵型平衡，防止被反击。',
            weapons: 'W07 刺穿线形 · W09 对角长传',
            callout: '“看弱侧！” / “收紧！”'
          }},
          {{
            num: 4, pos: 'RB', name: '右后卫 (Right Back)', code: '右翼屏障 · 套边突击',
            x: 80, y: 72,
            duty: '封锁右路通道；与 7号 边前卫打套边二过一，底线送出倒三角。',
            pre: '观察右边前卫内切时机，突然从外侧全速超车。',
            main: '一脚触球顺势传中，球速极快。',
            post: '出球后立即补位右路防线。',
            weapons: 'W03 倒三角 · W04 贴地横扫',
            callout: '“套边套边！” / “回防！”'
          }},
          {{
            num: 5, pos: 'LM', name: '左边前卫 (Left Midfielder)', code: '边路爆点 · 内切扯动',
            x: 22, y: 44,
            duty: '左路进攻发动机；带球内切吸引边后卫，送出直塞助攻套边的 2号 边卫下底。',
            pre: '接球前观察 2号 边卫插上位置，保持身体半侧身。',
            main: '大动作假射诱骗防守，脚腕一扣分给套边插上的边卫。',
            post: '分球后快速内插禁区点球点包抄倒三角。',
            weapons: 'W05 撞墙 · W14 假射真分',
            callout: '“走外侧！” / “看身后！”'
          }},
          {{
            num: 6, pos: 'CM', name: '中场指挥官 (Central Midfielder)', code: '全队大脑 · 第三人主导者',
            x: 50, y: 48,
            duty: '全场枢纽；掌控比赛节奏；主导第三人跑位直塞与弱侧调度，禁区外重炮轰门。',
            pre: '皮球在空中滑行时完成盲区扫描，脑中已定出球方案。',
            main: '一脚贴地穿透球刺穿防线，助攻前锋单刀。',
            post: '出球后立即压入禁区弧顶抢第二落点。',
            weapons: 'W01 直塞 · W08 第三人 · W09 弱侧对角',
            callout: '“看第三人！” / “弱侧弱侧！”'
          }},
          {{
            num: 7, pos: 'RM', name: '右边前卫 (Right Midfielder)', code: '边路飞翼 · 1v1爆点',
            x: 78, y: 44,
            duty: '右路爆点；1v1 突破内切射门或与 4号 边后卫打撞墙配合。',
            pre: '紧贴边线拉开宽度，接球前反向摆脱。',
            main: '带球内切射门，或送倒三角回传。',
            post: '传球后立即包抄后门柱。',
            weapons: 'W03 倒三角 · W05 撞墙 · W10 边线',
            callout: '“撞墙！” / “倒三角！”'
          }},
          {{
            num: 8, pos: 'ST', name: '突前全能中锋 (Complete Striker)', code: '终极杀手 · 前插破门',
            x: 50, y: 20,
            duty: '牵制双中卫；前插反越位单刀，门前抢点横扫折射破门。',
            pre: '压在最后一名后卫身后，寻找盲区。',
            main: '不停球直接推射球门近角死角。',
            post: '进球后全队合围，丢球就地逼抢。',
            weapons: 'W01 直塞 · W04 贴地横扫 · W16 漏球',
            callout: '“给身后！” / “回敲！”'
          }}
        ]
      }}
    }};

    let currentFormationKey = '1231';
    let currentSelectedPlayerIdx = 3; // Default select CM (No. 4)

    // Switch Formation in Module 04
    function switchFormation(formKey) {{
      currentFormationKey = formKey;
      currentSelectedPlayerIdx = (formKey === '1331' ? 5 : 3); // default CM
      
      // Update tab buttons active state
      document.querySelectorAll('.formation-tab-btn').forEach((btn, idx) => {{
        const keys = ['1231', '1321', '1331'];
        btn.classList.toggle('active', keys[idx] === formKey);
      }});

      renderInteractivePitch();
    }}

    // Render the SVG Pitch and Player Nodes
    function renderInteractivePitch() {{
      const form = formationDatabase[currentFormationKey];
      document.getElementById('pitch-formation-title').innerText = form.name;
      document.getElementById('pitch-formation-tag').innerText = form.tag;

      const layer = document.getElementById('pitch-players-layer');
      let nodesHtml = '';
      form.players.forEach((p, idx) => {{
        const isActive = idx === currentSelectedPlayerIdx;
        nodesHtml += `
          <div class="player-node ${{isActive ? 'active' : ''}}" style="left: ${{p.x}}%; top: ${{p.y}}%;" onclick="selectFormationPlayer(${{idx}})">
            <span class="player-node-num">${{p.num}}</span>
            <span class="player-node-label">${{p.pos}}</span>
          </div>
        `;
      }});
      layer.innerHTML = nodesHtml;

      renderPlayerRoleCard(form.players[currentSelectedPlayerIdx]);
    }}

    // Select Player Node on the pitch
    function selectFormationPlayer(idx) {{
      currentSelectedPlayerIdx = idx;
      const form = formationDatabase[currentFormationKey];
      
      document.querySelectorAll('.player-node').forEach((node, i) => {{
        node.classList.toggle('active', i === idx);
      }});

      renderPlayerRoleCard(form.players[idx]);
    }}

    // Update Right Role Card Content
    function renderPlayerRoleCard(p) {{
      if (!p) return;
      document.getElementById('role-title').innerText = `${{p.num}}号 ${{p.name}}`;
      document.getElementById('role-code').innerText = p.code;
      document.getElementById('role-num-badge').innerText = `No. ${{p.num}}`;
      document.getElementById('role-duty').innerText = p.duty;
      document.getElementById('role-pre').innerText = p.pre;
      document.getElementById('role-main').innerText = p.main;
      document.getElementById('role-post').innerText = p.post;
      document.getElementById('role-weapons').innerText = p.weapons;
      document.getElementById('role-callout').innerText = p.callout;
    }}

    function openFormationAnimLightbox() {{
      const form = formationDatabase[currentFormationKey];
      openCustomLightbox(form.animGif, form.name + ' · 战术跑位沙盘');
    }}

    // ==========================================
    // 2. Module 02 Doctrine Filtering & Quick Modals
    // ==========================================
    function filterDoctrines(category) {{
      document.querySelectorAll('.doctrine-filter-btn').forEach(btn => {{
        btn.classList.toggle('active', btn.getAttribute('onclick').includes(category));
      }});

      document.querySelectorAll('.doctrine-card').forEach(card => {{
        if (category === 'all' || card.getAttribute('data-category') === category) {{
          card.style.display = 'flex';
        }} else {{
          card.style.display = 'none';
        }}
      }});
    }}

    let pendingJumpWeaponId = null;
    function popWeaponModal(weaponId) {{
      // Find weapon in database
      let foundWeapon = null;
      let foundCat = 1;
      let foundIdx = 0;
      for (let c = 1; c <= 5; c++) {{
        const list = weaponDatabase[c] || [];
        for (let i = 0; i < list.length; i++) {{
          if (list[i].id === weaponId) {{
            foundWeapon = list[i];
            foundCat = c;
            foundIdx = i;
            break;
          }}
        }}
        if (foundWeapon) break;
      }}

      if (!foundWeapon) return;

      pendingJumpWeaponId = {{ cat: foundCat, idx: foundIdx }};
      document.getElementById('wmodal-num').innerText = foundWeapon.num;
      document.getElementById('wmodal-name').innerText = `${{foundWeapon.name}} (${{foundWeapon.en}})`;
      document.getElementById('wmodal-gif').src = foundWeapon.gif;
      document.getElementById('wmodal-desc').innerText = foundWeapon.desc;
      document.getElementById('wmodal-callout').innerText = foundWeapon.callout;

      document.getElementById('weapon-modal').classList.add('open');
    }}

    function closeWeaponModalDirect() {{
      document.getElementById('weapon-modal').classList.remove('open');
    }}

    function closeWeaponModal(e) {{
      if (e.target === document.getElementById('weapon-modal')) closeWeaponModalDirect();
    }}

    function jumpToWeaponFromModal() {{
      closeWeaponModalDirect();
      if (pendingJumpWeaponId) {{
        switchView('view-weapons');
        switchCategory(pendingJumpWeaponId.cat);
        selectWeapon(pendingJumpWeaponId.idx);
      }}
    }}

    // ==========================================
    // 3. Database of 20 Passing Weapons (Module 03) - 100% Dedicated Animations
    // ==========================================
    const weaponDatabase = {{
      1: [
        {{
          id: "w01",
          num: "W 01",
          name: "直塞穿透球",
          en: "Through Ball",
          tag: "贴地发力 · 刺穿中卫结合部",
          gif: "{b64_w01}",
          desc: "脚内侧或正脚背贴地快速刺穿两条防线之间的结合部空当；给足前锋前插提前量，让队友冲刺接球单刀。",
          callout: "📢 场上实战口令：“给身后！”"
        }},
        {{
          id: "w02",
          num: "W 02",
          name: "肋部挑传空当",
          en: "Chipped Through",
          tag: "脚尖搓挑 · 越过防线头顶",
          gif: "{b64_w02}",
          desc: "脚尖快速搓入皮球底部制造回旋，使球迅速跃过密集防守头顶，落入肋部无人区并减速停稳。",
          callout: "📢 场上实战口令：“挑肋部！”"
        }},
        {{
          id: "w03",
          num: "W 03",
          name: "底线倒三角回传",
          en: "Cut-Back Pass",
          tag: "下底压缩门线 · 推向点球点",
          gif: "{b64_w03}",
          desc: "边路下底迫使防守队员与门将退缩门线，随后发力贴地推向点球点到禁区线之间的巨大真空区。",
          callout: "📢 场上实战口令：“倒三角！”"
        }},
        {{
          id: "w04",
          num: "W 04",
          name: "贴地横扫传中",
          en: "Driven Low Cross",
          tag: "平抽门前走廊 · 抢前点垫射",
          gif: "{b64_w04}",
          desc: "脚内侧发力平抽门前危险走廊，球速极快，专打后卫转身困难，供前锋抢前点折射或制造乌龙。",
          callout: "📢 场上实战口令：“前点平抽！”"
        }}
      ],
      2: [
        {{
          id: "w05",
          num: "W 05",
          name: "二过一撞墙配合",
          en: "Wall Pass / 1-2",
          tag: "传球即启动 · 借墙过人",
          gif: "{b64_w05}",
          desc: "斜传中锋瞬间全速插上，中锋作为“墙”一脚顺势回弹其跑动路线上，瞬间超车防守形成单刀。",
          callout: "📢 场上实战口令：“撞墙！”"
        }},
        {{
          id: "w06",
          num: "W 06",
          name: "迎前回敲做球",
          en: "Lay-off Pass",
          tag: "背身接应 · 软推二梯队",
          gif: "{b64_w06}",
          desc: "前锋迎球背身一脚轻推给面向前场的插上中场，出球要软、球速温和，方便队友迎球不停球直接打门。",
          callout: "📢 场上实战口令：“回敲！”"
        }},
        {{
          id: "w07",
          num: "W 07",
          name: "刺穿线形传球",
          en: "Line-Breaking Laser",
          tag: "正脚背重炮 · 瞬间刺穿双线",
          gif: "{b64_w07}",
          desc: "脚背正中发力贴地重炮直塞，像激光一样直接打穿对方锋线与中场线，送至前腰脚下。",
          callout: "📢 场上实战口令：“穿透线！”"
        }},
        {{
          id: "w08",
          num: "W 08",
          name: "第三人导向球",
          en: "Up-Back-Through",
          tag: "A传B ➔ B敲C ➔ C直塞D",
          gif: "{b64_w08}",
          desc: "破解密集防守的第一绝技。利用持球人 A 和支点 B 吸引防守，由前瞻者 C 一脚送给盲区杀出的第三人 D。",
          callout: "📢 场上实战口令：“看第三人！”"
        }}
      ],
      3: [
        {{
          id: "w09",
          num: "W 09",
          name: "大范围对角长传",
          en: "Diagonal Switch",
          tag: "30米斜长传 · 强侧转弱侧",
          gif: "{b64_w09}",
          desc: "脚背内侧搓出 30 米以上高速斜长传，从密集强侧瞬间转移至弱侧空当，制造 1v1 或无人传中。",
          callout: "📢 场上实战口令：“弱侧弱侧！”"
        }},
        {{
          id: "w10",
          num: "W 10",
          name: "边线贴地推进球",
          en: "Channel Pass",
          tag: "紧贴边线直推 · 边卫连线边锋",
          gif: "{b64_w10}",
          desc: "边后卫破逼抢的第一选择，紧贴边线外侧贴地直塞，避开中路封堵，直接给边锋启动。",
          callout: "📢 场上实战口令：“走边线！”"
        }},
        {{
          id: "w11",
          num: "W 11",
          name: "弧线绕顶传球",
          en: "Curled Around Block",
          tag: "外侧强侧旋 · 绕过防守封锁",
          gif: "{b64_w11}",
          desc: "在中路直线被完全封死时，脚内侧带强侧旋踢出弧线，球绕过防守队员身体外侧进入肋部空当。",
          callout: "📢 场上实战口令：“绕外侧！”"
        }},
        {{
          id: "w12",
          num: "W 12",
          name: "回传重新组织球",
          en: "Recycling / Reset",
          tag: "拒绝盲目对抗 · 重置进攻面",
          gif: "{b64_w12}",
          desc: "前场无突破机会时果断回敲中卫或门将，全队阵型横向展开，重新寻找薄弱防线，绝不死带失误。",
          callout: "📢 场上实战口令：“回传重来！”"
        }}
      ],
      4: [
        {{
          id: "w13",
          num: "W 13",
          name: "不看人隐蔽传球",
          en: "No-Look Pass",
          tag: "眼神向左 · 脚腕向右",
          gif: "{b64_w13}",
          desc: "身体朝向与视线完全看向左路吸引防守重心，出球瞬间脚腕抖动向右出球，彻底破坏后卫预判。",
          callout: "📢 场上实战口令：“声东击西！”"
        }},
        {{
          id: "w14",
          num: "W 14",
          name: "假射真传/节奏差",
          en: "Fake Shot & Slip",
          tag: "大动作假射 · 最后一刻分球",
          gif: "{b64_w14}",
          desc: "大动作假装起脚爆射诱使后卫下铲封堵，在最后一瞬间脚腕轻扣，节奏差隐蔽直塞空当单刀助攻。",
          callout: "📢 场上实战口令：“假射真分！”"
        }},
        {{
          id: "w15",
          num: "W 15",
          name: "反向对角塞球",
          en: "Reverse Diagonal Pass",
          tag: "打防线横移惯性反方向",
          gif: "{b64_w15}",
          desc: "横向带球吸附整条防线同步横移，突然逆着防守移动方向送反角直塞，利用对手重心反切破门。",
          callout: "📢 场上实战口令：“打反向！”"
        }},
        {{
          id: "w16",
          num: "W 16",
          name: "漏球顺势配合",
          en: "Dummy / Let-Through",
          tag: "迎球假动作 · 突然叉腿漏过",
          gif: "{b64_w16}",
          desc: "接应球员做出接球假动作吸引后卫上抢，皮球到达身前瞬间叉腿漏过，球顺势滚入单刀区。",
          callout: "📢 场上实战口令：“漏过来！”"
        }}
      ],
      5: [
        {{
          id: "w17",
          num: "W 17",
          name: "门将穿透性低平球",
          en: "GK Line-Breaking Ground Pass",
          tag: "门将第7人 · 贴地刺穿双人逼抢线",
          gif: "{b64_w17}",
          desc: "门将推至大禁区弧顶，脚内侧大力贴地平抽穿透前锋逼抢线，直接连线中场，瞬间瓦解对手高位逼抢。",
          callout: "📢 场上实战口令：“门将直穿！”"
        }},
        {{
          id: "w18",
          num: "W 18",
          name: "反击越顶快攻长传",
          en: "Over-the-Top Counter",
          tag: "断球不停球 · 直接起身后",
          gif: "{b64_w18}",
          desc: "断球后 0.5 秒内不倒脚，直接送出 30 米半高球越过对手身后，供前锋全速冲刺打立足未稳。",
          callout: "📢 场上实战口令：“起身后！”"
        }},
        {{
          id: "w19",
          num: "W 19",
          name: "定位球低平倒三角",
          en: "Set-piece Short Cross",
          tag: "战术角球/任意球二过一",
          gif: "{b64_w19}",
          desc: "角球不盲目起高球争顶，发 2 人战术短传配合突入禁区肋部低平横扫，专门攻破高大后卫防线。",
          callout: "📢 场上实战口令：“战术角球！”"
        }},
        {{
          id: "w20",
          num: "W 20",
          name: "战术手抛界外球",
          en: "Tactical Throw-in",
          tag: "掷脚下 ➔ 回敲 ➔ 外侧套边",
          gif: "{b64_w20}",
          desc: "边卫抛给前锋，前锋顺势一脚回敲，边卫高速套边插下底直接传中，把边线死球变成进攻机会。",
          callout: "📢 场上实战口令：“界外球一二配合！”"
        }}
      ]
    }};

    let currentCategory = 1;
    let currentWeaponIndex = 0;

    // View Navigation
    function switchView(viewId) {{
      document.querySelectorAll('.view-container').forEach(v => v.classList.remove('active'));
      document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
      
      const targetView = document.getElementById(viewId);
      if (targetView) targetView.classList.add('active');

      const titleMap = {{
        'view-foundations': '📐 模块 01 · 战术基石与空间地图',
        'view-doctrines': '⚔️ 模块 02 · 八大实战进攻流派全景沙盘',
        'view-weapons': '🎯 模块 03 · 20 种传球武器点播台',
        'view-formations': '📋 模块 04 · 阵型架构与球员职责卡 (互动球场)',
        'view-decisions': '⚡ 模块 05 · 临场破局速查与呼应暗号'
      }};
      document.getElementById('topbar-title').innerHTML = `<span>${{titleMap[viewId] || '战情室'}}</span>`;
      
      const navItems = document.querySelectorAll('.nav-item');
      if (viewId === 'view-foundations') navItems[0].classList.add('active');
      if (viewId === 'view-doctrines') navItems[1].classList.add('active');
      if (viewId === 'view-weapons') navItems[2].classList.add('active');
      if (viewId === 'view-formations') navItems[3].classList.add('active');
      if (viewId === 'view-decisions') navItems[4].classList.add('active');
    }}

    // Switch Category Tabs in Module 03
    function switchCategory(catNum) {{
      currentCategory = catNum;
      currentWeaponIndex = 0;
      
      document.querySelectorAll('.cat-tab-btn').forEach((btn, idx) => {{
        btn.classList.toggle('active', idx + 1 === catNum);
      }});

      renderWeaponConsole();
    }}

    // Render the active Category in Module 03
    function renderWeaponConsole() {{
      const weapons = weaponDatabase[currentCategory] || [];
      const cardsContainer = document.getElementById('weapon-cards-list');
      const pillsContainer = document.getElementById('category-pills');

      let cardsHtml = '';
      weapons.forEach((w, idx) => {{
        const isActive = idx === currentWeaponIndex;
        cardsHtml += `
          <div class="weapon-select-card ${{isActive ? 'active' : ''}}" onclick="selectWeapon(${{idx}})">
            <div class="weapon-card-head">
              <span class="weapon-badge">${{w.num}}</span>
              <span class="weapon-en">${{w.en}}</span>
            </div>
            <div class="weapon-name">${{w.name}}</div>
            <div class="weapon-body">${{w.desc}}</div>
            <div class="weapon-callout">${{w.callout}}</div>
          </div>
        `;
      }});
      cardsContainer.innerHTML = cardsHtml;

      let pillsHtml = '';
      weapons.forEach((w, idx) => {{
        const isActive = idx === currentWeaponIndex;
        pillsHtml += `
          <button class="switcher-pill ${{isActive ? 'active' : ''}}" onclick="selectWeapon(${{idx}})">
            ${{w.num}} ${{w.name}}
          </button>
        `;
      }});
      if (currentCategory === 1) {{
        pillsHtml += `<button class="switcher-pill" onclick="selectCombo()">★ 挑传+平抽连招</button>`;
      }}
      pillsContainer.innerHTML = pillsHtml;

      updatePlayerContent(weapons[currentWeaponIndex]);
    }}

    function selectWeapon(idx) {{
      currentWeaponIndex = idx;
      const weapons = weaponDatabase[currentCategory];
      const selected = weapons[idx];
      
      document.querySelectorAll('.weapon-select-card').forEach((c, i) => {{
        c.classList.toggle('active', i === idx);
      }});
      document.querySelectorAll('.switcher-pill').forEach((p, i) => {{
        p.classList.toggle('active', i === idx);
      }});

      updatePlayerContent(selected);
    }}

    function selectCombo() {{
      document.querySelectorAll('.weapon-select-card').forEach(c => c.classList.remove('active'));
      document.querySelectorAll('.switcher-pill').forEach(p => p.classList.remove('active'));
      event.target.classList.add('active');

      document.getElementById('player-title').innerText = "W 02 + W 04 · 肋部挑传 + 贴地平抽连招";
      document.getElementById('player-tag').innerText = "综合实战进球连招演示";
      document.getElementById('player-gif').src = "{b64_combo_w02_w04}";
      document.getElementById('player-details-title').innerText = "📌 综合连招实战时序";
      document.getElementById('player-details-desc').innerText = "中场(4)脚尖搓挑打入左肋空当[W02] ➔ 边锋(5)不停球平抽门前危险走廊[W04] ➔ 中锋(7)高速抢前点垫射破门！";
      document.getElementById('player-callout').innerText = "📢 场上实战口令：“挑肋部” ➔ “前点平抽！”";
    }}

    function updatePlayerContent(w) {{
      if (!w) return;
      document.getElementById('player-title').innerText = `${{w.num}} · ${{w.name}} (${{w.en}})`;
      document.getElementById('player-tag').innerText = w.tag;
      document.getElementById('player-gif').src = w.gif;
      document.getElementById('player-details-title').innerText = "📌 技术要领与微动作规范";
      document.getElementById('player-details-desc').innerText = w.desc;
      document.getElementById('player-callout').innerText = w.callout;
    }}

    // Lightbox Controls
    const lbModal = document.getElementById('lightbox-modal');
    const lbImg = document.getElementById('lightbox-img');
    const lbTitle = document.getElementById('lightbox-title');
    const lbViewport = document.getElementById('lb-viewport');
    let currentScale = 1;
    let isDragging = false;
    let startX, startY, transX = 0, transY = 0;

    function openPlayerLightbox() {{
      const currentGif = document.getElementById('player-gif').src;
      const currentTitle = document.getElementById('player-title').innerText;
      openCustomLightbox(currentGif, currentTitle);
    }}

    function openCustomLightbox(src, title) {{
      lbImg.src = src;
      lbTitle.innerText = `🔍 ${{title || '战术动态沙盘'}}`;
      lbModal.classList.add('open');
      resetZoom();
    }}

    function closeLightboxDirect() {{ lbModal.classList.remove('open'); }}
    function closeLightbox(e) {{ if (e.target === lbModal) closeLightboxDirect(); }}

    function applyTransform() {{
      lbImg.style.transform = `scale(${{currentScale}}) translate(${{transX}}px, ${{transY}}px)`;
    }}

    function zoomIn() {{ currentScale = Math.min(3.8, currentScale + 0.3); applyTransform(); }}
    function zoomOut() {{ currentScale = Math.max(0.5, currentScale - 0.3); applyTransform(); }}
    function resetZoom() {{ currentScale = 1; transX = 0; transY = 0; applyTransform(); }}

    lbViewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      if (e.deltaY < 0) currentScale = Math.min(3.8, currentScale + 0.18);
      else currentScale = Math.max(0.5, currentScale - 0.18);
      applyTransform();
    }});

    lbViewport.addEventListener('mousedown', (e) => {{
      isDragging = true; startX = e.clientX - transX; startY = e.clientY - transY;
    }});
    window.addEventListener('mousemove', (e) => {{
      if (isDragging) {{ transX = e.clientX - startX; transY = e.clientY - startY; applyTransform(); }}
    }});
    window.addEventListener('mouseup', () => {{ isDragging = false; }});

    lbViewport.addEventListener('dblclick', () => {{
      if (currentScale > 1.2) resetZoom();
      else {{ currentScale = 2.0; applyTransform(); }}
    }});

    function toggleFullscreen() {{
      if (!document.fullscreenElement) document.documentElement.requestFullscreen();
      else if (document.exitFullscreen) document.exitFullscreen();
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        if (lbModal.classList.contains('open')) closeLightboxDirect();
        if (document.getElementById('weapon-modal').classList.contains('open')) closeWeaponModalDirect();
      }}
    }});

    // ==========================================
    // 4. Module 05: Crisis Database & Callouts (STEP 3 核心)
    // ==========================================
    const crisisDatabase = {{
      'press': {{
        title: '破局① · 破解高位逼抢与前场贴身合围 (Beat High Press)',
        tag: '反向诱敌 · 门将穿透打其身后大草原',
        trap: '【对手陷阱】对手整体阵型前提至我方 30 米区域，严密切断中卫地面前插出球线，逼迫我方在后场失误送单刀。',
        antidote: '【破局解药】严禁后场盲目大脚！门将积极推至大禁区弧顶充当“第 7 人”，利用【门将穿透性低平球】贴地大力刺穿前锋逼抢线；若对手中卫全线压过半场，拖后中卫立即送出【越顶长传】打其身后 25 米巨大真空区！',
        weapons: [
          {{ id: 'w17', name: 'W17 门将穿透性低平球' }},
          {{ id: 'w18', name: 'W18 越顶长传反越位' }},
          {{ id: 'w10', name: 'W10 边线推进球' }}
        ],
        callout: '📢 场上核心口令：“门将直穿！” / “起身后！” / “身后有人！”'
      }},
      'bus': {{
        title: '破局② · 撕碎低位铁桶与密集大巴防守 (Break Low Block)',
        tag: '强侧超载 · 弱侧长传与底线倒三角',
        trap: '【对手陷阱】全队退缩后场 30 米内收缩成铁桶阵，封死中路直线塞球路线，诱使我方盲目起高球争顶无功而返。',
        antidote: '【破局解药】严禁在中路密集区强行硬塞！强侧连续快速倒脚（超载 Overload）吸引铁桶阵整体横移，中场突然起 30 米对角长传打向弱侧无人区；边路下底迫使防线退缩门线，坚决送【底线倒三角】回推点球点真空区！',
        weapons: [
          {{ id: 'w03', name: 'W03 底线倒三角回传' }},
          {{ id: 'w09', name: 'W09 大范围对角长传' }},
          {{ id: 'w02', name: 'W02 肋部挑传空当' }},
          {{ id: 'w14', name: 'W14 假射真传/节奏差' }}
        ],
        callout: '📢 场上核心口令：“弱侧弱侧！” / “倒三角！” / “挑肋部！”'
      }},
      'mid': {{
        title: '破局③ · 突围中场惨烈绞杀与局部人数劣势 (Overcome Midfield Squeeze)',
        tag: '一脚触球 · 第三人跑位与中锋胸部做球',
        trap: '【对手陷阱】在中圈弧与两肋囤积重兵，凶狠逼抢第一接球人，只要我方持球停顿或背身护球立即遭遇双人合围断球。',
        antidote: '【破局解药】全员执行【一脚触球】铁律！严禁持球超过 1 秒。启动【第三人跑位 Up-Back-Through】：后腰直塞前锋，前锋背身一脚回做，中场顺势送盲区第三人单刀；若地面绞杀惨烈，后场直接起半高球连线中锋胸部稳卸回做！',
        weapons: [
          {{ id: 'w08', name: 'W08 第三人导向球' }},
          {{ id: 'w06', name: 'W06 迎前回敲做球' }},
          {{ id: 'w05', name: 'W05 二过一撞墙配合' }},
          {{ id: 'w16', name: 'W16 漏球顺势配合' }}
        ],
        callout: '📢 场上核心口令：“看第三人！” / “回敲！” / “转过来！”'
      }},
      'late': {{
        title: '破局④ · 终场比分落后与绝境搏杀 (Late Game Blitz Attack)',
        tag: '就地反抢 · 5秒快攻与战术界外球',
        trap: '【对手陷阱】对手领先拖延时间，退缩防守或在边线死球区故意制造停顿，打乱我方节奏。',
        antidote: '【破局解药】丢球 0.5 秒内全队合围就地反抢！断球后 5 秒内 3 脚传递直达门前；充分利用死球机会执行【战术手抛界外球】：边卫掷前锋脚下一脚回敲，边卫套边平抽横扫门前；定位球果断发 2 人配合倒三角！',
        weapons: [
          {{ id: 'w04', name: 'W04 贴地横扫传中' }},
          {{ id: 'w20', name: 'W20 战术手抛界外球' }},
          {{ id: 'w19', name: 'W19 定位球低平倒三角' }},
          {{ id: 'w07', name: 'W07 刺穿线形传球' }}
        ],
        callout: '📢 场上核心口令：“前点平抽！” / “界外球一二配合！” / “战术角球！”'
      }}
    }};

    const calloutsDatabase = [
      {{ code: '“转过来！”', en: 'Turn!', scene: '接球队员身后 3~5 米无防守人紧逼', act: '严禁习惯性回传！拿球队员必须半侧身顺势领球向前，正面冲击对方防线。' }},
      {{ code: '“身后有人！”', en: 'Man On!', scene: '对方防守队员贴身紧逼上抢接球人盲区', act: '严禁盲目转身！必须一脚触球顺势回敲，或身体卡位护球借力打力。' }},
      {{ code: '“弱侧弱侧！”', en: 'Switch!', scene: '强侧通道被对手重兵压缩堵死', act: '全队视线向弱侧转移，中场持球人立即送出 30 米大对角斜长传找空当。' }},
      {{ code: '“看第三人！”', en: 'Third Man!', scene: '破密集防守，第一接应点被死死盯防', act: '不要传给眼前的暴露点，利用回敲过渡，一脚直塞给从盲区突前插上的第三人。' }},
      {{ code: '“门将直穿！”', en: 'GK Laser!', scene: '对手双前锋高位逼抢扑中后卫', act: '门将提至弧顶接球，大力贴地平抽穿透前锋逼抢线，直接连线中场。' }},
      {{ code: '“起身后！”', en: 'Over the Top!', scene: '对手防线全线压上，其身后留 20 米真空区', act: '断球 0.5 秒内不倒脚，拖后中卫直接送半高球越顶长传，前锋反越位超车单刀。' }},
      {{ code: '“倒三角！”', en: 'Cut Back!', scene: '边锋下底迫使防守队员与门将退缩门线', act: '拒绝盲目起高球争顶！发力贴地推向点球点到禁区线之间的巨大真空区。' }},
      {{ code: '“回传重来！”', en: 'Recycle!', scene: '边路进攻陷入双人包夹死胡同', act: '拒绝单打独斗盲目对抗失误！果断回敲拖后中卫，全队横向展开重构进攻面。' }}
    ];

    let currentCrisisKey = 'press';

    function switchCrisis(crisisKey) {{
      currentCrisisKey = crisisKey;
      document.querySelectorAll('.crisis-tab-btn').forEach(btn => {{
        btn.classList.toggle('active', btn.getAttribute('onclick').includes(crisisKey));
      }});
      renderCrisisDashboard();
    }}

    function renderCrisisDashboard() {{
      const c = crisisDatabase[currentCrisisKey];
      if (!c) return;
      const container = document.getElementById('crisis-dashboard-content');
      
      let weaponsHtml = '';
      c.weapons.forEach(w => {{
        weaponsHtml += `<span class="doctrine-weapon-pill" onclick="popWeaponModal('${{w.id}}')">${{w.name}}</span> `;
      }});

      container.innerHTML = `
        <div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
            <div style="font-size: 18px; font-weight: 800; color: var(--text-main);">${{c.title}}</div>
            <span class="doctrine-tag" style="background: rgba(248,113,113,0.15); color: var(--accent-red); border-color: rgba(248,113,113,0.3);">${{c.tag}}</span>
          </div>
          <div style="font-size: 13.5px; line-height: 1.6; color: var(--accent-red); font-weight: 600; margin-bottom: 14px; background: rgba(239,68,68,0.08); padding: 10px 14px; border-radius: 8px; border-left: 3px solid var(--accent-red);">
            ${{c.trap}}
          </div>
          <div style="font-size: 13.5px; line-height: 1.7; color: var(--text-sub);">
            ${{c.antidote}}
          </div>
        </div>
        <div style="border-left: 1px solid var(--border-sub); padding-left: 20px; display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <div style="font-size: 13px; font-weight: 800; color: var(--accent-gold); margin-bottom: 10px;">
              🛠️ 核心推荐破局武器 (点击查看要领):
            </div>
            <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px;">
              ${{weaponsHtml}}
            </div>
          </div>
          <div style="background: rgba(16,185,129,0.08); border: 1px solid rgba(16,185,129,0.25); border-radius: 8px; padding: 12px 14px;">
            <div style="font-size: 13.5px; font-weight: 800; color: var(--pitch-green); line-height: 1.5;">
              ${{c.callout}}
            </div>
          </div>
        </div>
      `;
    }}

    function renderCalloutsGrid() {{
      const container = document.getElementById('callouts-grid');
      let html = '';
      calloutsDatabase.forEach(co => {{
        html += `
          <div class="crisis-callout-card">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 6px;">
              <span style="font-size: 16px; font-weight: 900; color: var(--accent-cyan);">${{co.code}}</span>
              <span style="font-size: 11px; color: var(--text-muted); font-weight: 600;">${{co.en}}</span>
            </div>
            <div style="font-size: 12px; color: var(--accent-gold); font-weight: 700; margin-bottom: 6px;">
              🎯 触发：${{co.scene}}
            </div>
            <div style="font-size: 12px; color: var(--text-sub); line-height: 1.5;">
              ${{co.act}}
            </div>
          </div>
        `;
      }});
      container.innerHTML = html;
    }}

    // 3-Theme Switcher & Storage
    function setTheme(themeName) {{
      document.body.classList.remove('theme-light', 'theme-sepia');
      if (themeName === 'light') {{
        document.body.classList.add('theme-light');
      }} else if (themeName === 'sepia') {{
        document.body.classList.add('theme-sepia');
      }}
      localStorage.setItem('tactics_theme', themeName);
      updateThemeButtons(themeName);
    }}

    function updateThemeButtons(currentTheme) {{
      document.querySelectorAll('.theme-btn').forEach(btn => btn.classList.remove('active'));
      const activeBtn = document.getElementById('btn-theme-' + currentTheme);
      if (activeBtn) activeBtn.classList.add('active');
    }}

    function initTheme() {{
      const savedTheme = localStorage.getItem('tactics_theme') || 'dark';
      setTheme(savedTheme);
    }}

    // Initialize Components
    initTheme();
    renderWeaponConsole();
    renderInteractivePitch();
    renderCrisisDashboard();
    renderCalloutsGrid();
  </script>
</body>
</html>
"""

# Write to workspace and artifacts
out_workspace = r"e:\06_Study\书籍\足球\football_tactics_hub.html"
out_artifact = r"C:\Users\Administrator\.gemini\antigravity\brain\030fc641-b9cc-4e72-b4ba-ed21a5a6e35f\football_tactics_hub.html"

with open(out_workspace, "w", encoding="utf-8") as f:
    f.write(html_code)

with open(out_artifact, "w", encoding="utf-8") as f:
    f.write(html_code)

print("Generated football_tactics_hub.html Step 2 successfully!")
