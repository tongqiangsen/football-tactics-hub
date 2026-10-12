# -*- coding: utf-8 -*-
"""
Rebuild football_tactics_deck.html with:
1. Complete embedded dynamic tactical animations (16 GIFs).
2. Built-in interactive Image Lightbox / Zoom Tool:
   - Click any tactical sandbox to open in full screen
   - Mouse wheel zoom in/out (0.6x ~ 3.5x)
   - Click-and-drag pan when zoomed
   - Double-click to toggle 1x / 2x
   - Dedicated zoom controls toolbar (+, -, Reset, Close)
   - ESC key or background click to exit
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

# 8 Attacking Doctrines
b64_third_man    = get_gif_b64("anim_01_third_man.gif")
b64_switch       = get_gif_b64("anim_02_switch_play.gif")
b64_over_the_top = get_gif_b64("anim_08_over_the_top.gif")
b64_5s_counter   = get_gif_b64("anim_09_5s_counter_blitz.gif")
b64_target_man   = get_gif_b64("anim_10_target_man_aerial.gif")
b64_cutback      = get_gif_b64("anim_04_cut_back.gif")
b64_dummy        = get_gif_b64("anim_11_dummy_let_through.gif")
b64_throwin      = get_gif_b64("anim_12_tactical_throwin.gif")

# 5 Weapon Categories
b64_w_cat1       = get_gif_b64("anim_w_cat1_chipped.gif")
b64_w_cat2       = get_gif_b64("anim_03_wall_pass.gif")
b64_w_cat3       = get_gif_b64("anim_w_cat3_curled.gif")
b64_w_cat4       = get_gif_b64("anim_w_cat4_fake_shot.gif")
b64_w_cat5       = get_gif_b64("anim_w_cat5_gk_laser.gif")

# 3 Formations
b64_1231         = get_gif_b64("anim_05_1231_buildup.gif")
b64_1321         = get_gif_b64("anim_06_1321_counter.gif")
b64_1331         = get_gif_b64("anim_07_1331_overlap.gif")

html_template = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>德国传球战术体系与全景实战指南 (16组高帧率动态沙盘·带放大观察镜版)</title>
  <style>
    :root {{
      --bg-dark: #09110e;
      --panel-bg: rgba(15, 23, 42, 0.78);
      --panel-border: rgba(34, 197, 94, 0.25);
      --pitch-green: #10b981;
      --accent-gold: #fbbf24;
      --accent-cyan: #38bdf8;
      --accent-red: #f87171;
      --accent-purple: #c084fc;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
      background-color: var(--bg-dark);
      color: var(--text-main);
      overflow: hidden;
      height: 100vh;
      width: 100vw;
      display: flex;
      flex-direction: column;
    }}

    .topbar {{
      height: 52px;
      background: rgba(10, 20, 15, 0.95);
      border-bottom: 1px solid rgba(34, 197, 94, 0.2);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      z-index: 100;
    }}
    .topbar-title {{
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 0.5px;
      color: #ffffff;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .badge {{
      font-size: 11px;
      padding: 2px 8px;
      border-radius: 4px;
      background: rgba(34, 197, 94, 0.15);
      color: var(--pitch-green);
      border: 1px solid var(--pitch-green);
    }}
    .badge.anim {{
      background: rgba(251, 191, 36, 0.15);
      color: var(--accent-gold);
      border-color: var(--accent-gold);
    }}
    .topbar-controls {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .nav-btn {{
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.15);
      color: #fff;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 13px;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .nav-btn:hover {{
      background: var(--pitch-green);
      color: #000;
      border-color: var(--pitch-green);
    }}

    .deck-container {{
      flex: 1;
      position: relative;
      overflow: hidden;
    }}
    .slide {{
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      opacity: 0;
      visibility: hidden;
      transform: scale(0.98) translateY(10px);
      transition: opacity 0.35s ease, transform 0.35s ease, visibility 0.35s;
      padding: 22px 36px;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
    }}
    .slide.active {{
      opacity: 1;
      visibility: visible;
      transform: scale(1) translateY(0);
      z-index: 10;
    }}

    .slide-header {{
      margin-bottom: 14px;
      border-left: 4px solid var(--pitch-green);
      padding-left: 14px;
    }}
    .slide-subtitle {{
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      color: var(--accent-gold);
      margin-bottom: 3px;
      font-weight: 600;
    }}
    .slide-header h2 {{
      font-size: 24px;
      font-weight: 800;
      color: #ffffff;
    }}

    .slide-body {{
      flex: 1;
      display: grid;
      gap: 18px;
    }}

    .grid-2 {{ grid-template-columns: 1fr 1fr; }}
    .grid-3 {{ grid-template-columns: repeat(3, 1fr); }}
    .grid-4 {{ grid-template-columns: repeat(4, 1fr); }}

    .card {{
      background: var(--panel-bg);
      border: 1px solid var(--panel-border);
      border-radius: 12px;
      padding: 16px 18px;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
      backdrop-filter: blur(12px);
      display: flex;
      flex-direction: column;
    }}
    .card-title {{
      font-size: 16.5px;
      font-weight: 700;
      color: var(--accent-cyan);
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .card-title.gold {{ color: var(--accent-gold); }}
    .card-title.green {{ color: var(--pitch-green); }}
    .card-title.red {{ color: var(--accent-red); }}
    .card-title.purple {{ color: var(--accent-purple); }}

    .card p, .card li {{
      font-size: 13.5px;
      line-height: 1.55;
      color: #cbd5e1;
    }}
    .card ul {{ padding-left: 18px; margin-top: 6px; }}
    .card li {{ margin-bottom: 4px; }}
    .card strong {{ color: #ffffff; }}

    /* Interactive Animation Container with Zoom Hint */
    .anim-container {{
      background: #06150e;
      border: 1px solid rgba(34, 197, 94, 0.4);
      border-radius: 10px;
      padding: 6px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      box-shadow: inset 0 0 20px rgba(0,0,0,0.8);
      overflow: hidden;
      cursor: zoom-in;
      position: relative;
      transition: border-color 0.2s, box-shadow 0.2s;
    }}
    .anim-container:hover {{
      border-color: var(--accent-cyan);
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.35);
    }}
    .anim-container::after {{
      content: '🔍 点击放大观察';
      position: absolute;
      bottom: 12px;
      right: 14px;
      background: rgba(15, 23, 42, 0.85);
      color: #38bdf8;
      font-size: 11px;
      font-weight: 600;
      padding: 3px 8px;
      border-radius: 4px;
      opacity: 0;
      transition: opacity 0.2s, transform 0.2s;
      transform: translateY(4px);
      pointer-events: none;
      border: 1px solid rgba(56, 189, 248, 0.4);
    }}
    .anim-container:hover::after {{
      opacity: 1;
      transform: translateY(0);
    }}
    .anim-container img {{
      max-width: 100%;
      max-height: 100%;
      height: auto;
      border-radius: 6px;
      border: 1px solid rgba(255,255,255,0.1);
      display: block;
    }}

    .weapon-card-compact {{
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 8px;
      padding: 9px 12px;
      margin-bottom: 7px;
      transition: all 0.2s;
    }}
    .weapon-card-compact:hover {{
      border-color: var(--accent-gold);
      background: rgba(30, 41, 59, 0.95);
    }}
    .weapon-num-badge {{
      font-size: 10.5px;
      font-weight: 800;
      padding: 1px 6px;
      border-radius: 3px;
      background: var(--accent-gold);
      color: #000;
      display: inline-block;
      margin-right: 6px;
    }}
    .weapon-name-inline {{
      font-size: 14px;
      font-weight: 700;
      color: #fff;
    }}
    .weapon-desc-compact {{
      font-size: 12px;
      color: #94a3b8;
      margin-top: 3px;
      line-height: 1.45;
    }}

    .matrix-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 13.5px;
    }}
    .matrix-table th {{
      background: rgba(34, 197, 94, 0.2);
      color: var(--pitch-green);
      text-align: left;
      padding: 10px 14px;
      border: 1px solid rgba(255,255,255,0.1);
      font-weight: 700;
    }}
    .matrix-table td {{
      padding: 10px 14px;
      border: 1px solid rgba(255,255,255,0.08);
      color: #cbd5e1;
      line-height: 1.5;
    }}
    .matrix-table tr:nth-child(even) {{
      background: rgba(255,255,255,0.02);
    }}

    .bottombar {{
      height: 48px;
      background: rgba(8, 15, 12, 0.95);
      border-top: 1px solid rgba(255,255,255,0.08);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
      padding: 0 20px;
    }}
    .dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: rgba(255,255,255,0.2);
      cursor: pointer;
      transition: all 0.2s;
    }}
    .dot.active {{
      width: 22px;
      border-radius: 10px;
      background: var(--pitch-green);
      box-shadow: 0 0 10px var(--pitch-green);
    }}

    .callout {{
      background: rgba(56, 189, 248, 0.1);
      border-left: 3px solid var(--accent-cyan);
      padding: 9px 12px;
      border-radius: 0 6px 6px 0;
      font-size: 13px;
      margin-top: 8px;
      color: #e0f2fe;
    }}
    .callout.gold {{
      background: rgba(251, 191, 36, 0.1);
      border-left-color: var(--accent-gold);
      color: #fef3c7;
    }}
    .callout.green {{
      background: rgba(34, 197, 94, 0.1);
      border-left-color: var(--pitch-green);
      color: #dcfce7;
    }}
    .callout.red {{
      background: rgba(248, 113, 113, 0.1);
      border-left-color: var(--accent-red);
      color: #fee2e2;
    }}
    .callout.purple {{
      background: rgba(192, 132, 252, 0.1);
      border-left-color: var(--accent-purple);
      color: #f3e8ff;
    }}

    .hotkey-hint {{
      position: fixed;
      bottom: 58px;
      right: 20px;
      background: rgba(0,0,0,0.6);
      border: 1px solid rgba(255,255,255,0.15);
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 11px;
      color: #94a3b8;
      pointer-events: none;
    }}

    /* Lightbox Modal & Zoom Viewer Styles */
    .lightbox-modal {{
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      background: rgba(4, 10, 8, 0.92);
      backdrop-filter: blur(14px);
      z-index: 9999;
      display: none;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      user-select: none;
    }}
    .lightbox-modal.open {{
      display: flex;
    }}
    .lightbox-controls {{
      position: absolute;
      top: 16px;
      left: 24px;
      right: 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 10001;
    }}
    .lightbox-title-badge {{
      font-size: 15px;
      font-weight: 700;
      color: #fff;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(34, 197, 94, 0.4);
      padding: 6px 18px;
      border-radius: 20px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.5);
    }}
    .lightbox-btn-group {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .lb-btn {{
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #fff;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s;
    }}
    .lb-btn:hover {{
      background: var(--pitch-green);
      color: #000;
      border-color: var(--pitch-green);
    }}
    .lb-btn.close:hover {{
      background: var(--accent-red);
      color: #fff;
      border-color: var(--accent-red);
    }}
    .lightbox-viewport {{
      max-width: 92vw;
      max-height: 84vh;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      cursor: grab;
      position: relative;
    }}
    .lightbox-viewport:active {{
      cursor: grabbing;
    }}
    #lightbox-img {{
      max-width: 100%;
      max-height: 82vh;
      object-fit: contain;
      border-radius: 8px;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.95), 0 0 0 1px rgba(34, 197, 94, 0.35);
      transition: transform 0.08s ease-out;
      transform-origin: center center;
    }}
    .lightbox-hint {{
      position: absolute;
      bottom: 16px;
      font-size: 12px;
      color: #94a3b8;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 4px 14px;
      border-radius: 12px;
      pointer-events: none;
    }}
  </style>
</head>
<body>

  <!-- Top Bar -->
  <div class="topbar">
    <div class="topbar-title">
      <span>⚽ 德国传球战术体系与全景实战指南</span>
      <span class="badge">7人制 / 8人制白队版</span>
      <span class="badge anim">🎬 16组高帧率动态沙盘·带放大镜</span>
    </div>
    <div class="topbar-controls">
      <span id="slide-counter" style="font-size: 13px; color: #94a3b8; margin-right: 8px;">01 / 20</span>
      <button class="nav-btn" onclick="prevSlide()">◀ 上一页 [←]</button>
      <button class="nav-btn" onclick="nextSlide()">下一页 [→] ▶</button>
      <button class="nav-btn" onclick="toggleFullScreen()">全屏 [F]</button>
    </div>
  </div>

  <!-- Deck Slides Container -->
  <div class="deck-container" id="deck-container">

    <!-- SLIDE 01: 封面 -->
    <div class="slide active">
      <div class="slide-header">
        <div class="slide-subtitle">TACTICAL PLAYBOOK · 德国传球战术体系与全景实战指南</div>
        <h2>构建现代球队共同战术语言：从理念、套路、武器到实战阵型</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card" style="justify-content: center;">
          <div class="card-title gold" style="font-size: 22px;">⚽ 献给全队队友的现代足球战术手册</div>
          <p style="font-size: 14px; margin-bottom: 12px;">
            本演示文稿提炼自德国著名战术著作《足球训练完全图解：德国足球传球战术及训练》（皮特·希巴拉 & 汉斯-迪特·波尔 著），专为本队量身定制。
          </p>
          <div class="callout green" style="font-size: 13.5px;">
            <strong>🎯 核心目标：</strong>彻底摆脱各自为战的盲目出球，建立全队统一的<strong>“空间认知”、“跑位预判”与“呼应暗号”</strong>，打出流畅而高效的现代战术足球。
          </div>
          <ul style="margin-top: 12px;">
            <li><strong>三大战术基石：</strong>传球认知变革 · 16格动态网格 · 三动作微观执行体系</li>
            <li><strong>八大实战进攻流派：</strong>涵盖弱侧转移、越顶打击、5秒反抢快攻与底线倒三角（100%全配动图）</li>
            <li><strong>二十项传球武器库：</strong>5大分类各配备高帧率动态演示沙盘与技术要领速查</li>
            <li><strong>三大实战阵型落地：</strong>7人制 1-2-3-1、7人制 1-3-2-1、8人制 1-3-3-1 完整职责卡与阵型抉择</li>
            <li><strong>🔍 放大观察镜：</strong>全套 16 组动态战术沙盘<strong>支持任意点击放大、滚轮缩放与拖拽</strong>！</li>
          </ul>
        </div>
        <div class="card" style="background: rgba(10,30,20,0.85); border-color: var(--pitch-green); justify-content: center; text-align: center;">
          <div style="font-size: 52px; margin-bottom: 12px;">🛡️ ⚡ ⚔️</div>
          <h3 style="font-size: 20px; color: #fff; margin-bottom: 8px;">德国足球“传球拼图 IQ®”体系</h3>
          <p style="font-size: 13.5px; color: #94a3b8; max-width: 420px; margin: 0 auto 16px;">
            “传球不是技术炫耀，而是高智商的团队解题。只要每个人做出正确的预判跑位，进球便水到渠成。”
          </p>
          <div style="display: flex; justify-content: center; gap: 10px;">
            <span class="badge">7人制 1-2-3-1</span>
            <span class="badge">7人制 1-3-2-1</span>
            <span class="badge">8人制 1-3-3-1</span>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 02: 理念变革 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 01 · 战术基石与理念革新</div>
        <h2>传球战术核心理念：从“把球传准”到“调度空间与防线”</h2>
      </div>
      <div class="slide-body grid-3">
        <div class="card">
          <div class="card-title red">❌ 传统业余误区：盲目传球</div>
          <ul>
            <li><strong>误区一：只看脚下。</strong>接到球才抬头看人，防守早已封堵死角。</li>
            <li><strong>误区二：静态站立等球。</strong>站在原地伸脚要球，被防守从身后轻松切断。</li>
            <li><strong>误区三：单打独斗盲目推进。</strong>陷入 1v2 局部劣势仍死带不传，导致致命丢球。</li>
            <li><strong>误区四：以少打多。</strong>强行在中路扎堆硬挤，失误率高达 80%。</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-title green">✅ 现代德国战术：空间与沟通</div>
          <ul>
            <li><strong>真理一：传球即人际语言。</strong>传球速度、旋转与落点是在告诉队友“转身上前”还是“安全回敲”。</li>
            <li><strong>真理二：球永远比人跑得快。</strong>3脚 1~2 触的传球能在 2 秒内横跨半场调动整条防线。</li>
            <li><strong>真理三：以多打少是战术目标。</strong>通过三角站位与局部超载（Overload），永远制造 3v2 或 2v1 优势。</li>
            <li><strong>真理四：传向空当而非脚下。</strong>给队友前插的“提前量”，让队友冲刺接球而非降速接球。</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-title gold">⚡ 全队三大铁律 (Golden Rules)</div>
          <div class="callout gold" style="margin-bottom: 8px;">
            <strong>1. 绝不盲目横传：</strong>后场中路严禁横传，横传一旦被断即直接面对空门！
          </div>
          <div class="callout cyan" style="margin-bottom: 8px;">
            <strong>2. 保持开放身位：</strong>永远半侧身面向前场，视野兼顾皮球与前插队友。
          </div>
          <div class="callout green">
            <strong>3. 0.5秒接球前扫描：</strong>皮球在空中滑行时完成盲区观察，脑中已定出球方案。
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 03: 16区域动态传球网格 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 01 · 空间地图</div>
        <h2>空间掌控：16 区域动态传球网格与全队站位纪律</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title green">📐 动态传球网格（Passing Grid）的核心法则</div>
          <p>将球场划分为 16~20 个战术方块，这是拜仁与德国队掌控球权的核心秘密：</p>
          <ul style="margin-top: 10px;">
            <li><strong>同格不站双人法则：</strong>同一横向或纵向方块内，<strong>严禁站两名本方队员</strong>。扎堆只会帮对手降低防守难度。</li>
            <li><strong>5~10 米黄金互应间距：</strong>距离太近容易被一防二，距离太远传球球速慢容易被截断。</li>
            <li><strong>梯次纵深站位：</strong>无论球在何处，持球人身边必须呈“三角形”或“菱形”展开（1个前突接应点 + 1个横向分球点 + 1个后方安全保护点）。</li>
          </ul>
          <div class="callout cyan">
            <strong>💡 实战警示：</strong>当你发现自己离队友不到 3 米时，立即横向或前向移动到相邻方格拉开空间！
          </div>
        </div>
        <div class="card" style="align-items: center; justify-content: center; background: #06150e;">
          <svg viewBox="0 0 500 350" width="100%" height="100%">
            <rect width="500" height="350" fill="#081d14" rx="8" stroke="#22c55e" stroke-width="2"/>
            <line x1="125" y1="0" x2="125" y2="350" stroke="#22c55e" stroke-width="1" stroke-dasharray="4,4" stroke-opacity="0.5"/>
            <line x1="250" y1="0" x2="250" y2="350" stroke="#22c55e" stroke-width="2" stroke-opacity="0.7"/>
            <line x1="375" y1="0" x2="375" y2="350" stroke="#22c55e" stroke-width="1" stroke-dasharray="4,4" stroke-opacity="0.5"/>
            <line x1="0" y1="87.5" x2="500" y2="87.5" stroke="#22c55e" stroke-width="1" stroke-dasharray="4,4" stroke-opacity="0.5"/>
            <line x1="0" y1="175" x2="500" y2="175" stroke="#22c55e" stroke-width="1" stroke-dasharray="4,4" stroke-opacity="0.5"/>
            <line x1="0" y1="262.5" x2="500" y2="262.5" stroke="#22c55e" stroke-width="1" stroke-dasharray="4,4" stroke-opacity="0.5"/>
            <circle cx="250" cy="175" r="45" fill="none" stroke="#22c55e" stroke-width="1.5" stroke-opacity="0.6"/>
            <text x="62.5" y="48" fill="#94a3b8" font-size="11" text-anchor="middle">左翼前场</text>
            <text x="187.5" y="48" fill="#fbbf24" font-size="11" text-anchor="middle">左肋前场</text>
            <text x="312.5" y="48" fill="#fbbf24" font-size="11" text-anchor="middle">右肋前场</text>
            <text x="437.5" y="48" fill="#94a3b8" font-size="11" text-anchor="middle">右翼前场</text>
            <text x="250" y="180" fill="#38bdf8" font-size="13" font-weight="bold" text-anchor="middle">中场控制核心区</text>
            <polygon points="187.5,130 312.5,220 187.5,220" fill="#38bdf8" fill-opacity="0.2" stroke="#38bdf8" stroke-width="2"/>
            <circle cx="187.5" cy="130" r="10" fill="#fff" stroke="#38bdf8" stroke-width="2"/>
            <circle cx="312.5" cy="220" r="10" fill="#fff" stroke="#38bdf8" stroke-width="2"/>
            <circle cx="187.5" cy="220" r="10" fill="#fff" stroke="#38bdf8" stroke-width="2"/>
          </svg>
        </div>
      </div>
    </div>

    <!-- SLIDE 04: 三动作体系 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 01 · 球员微观行为规范</div>
        <h2>球员微观决策基石：德国“三动作体系” (Pre-Main-Post Actions)</h2>
      </div>
      <div class="slide-body grid-3">
        <div class="card">
          <div class="card-title cyan">1. 前动作 (Pre-Action)</div>
          <div class="slide-subtitle" style="color: #94a3b8;">接球前 0.5 秒的无球准备</div>
          <ul>
            <li><strong>盲区扫描（Scanning）：</strong>接球前快速摆头 2~3 次，看清身后防守队员位置与前场空当。</li>
            <li><strong>半侧身接球（Open Body）：</strong>绝不背对进攻方向！身体朝向边线或斜前方，同时看到来球与对方球门。</li>
            <li><strong>反向摆脱（Counter Run）：</strong>先向防守球员靠近半步压住重心，随后突然反向迎球，拉开 1 米安全距离。</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-title green">2. 主动作 (Main-Action)</div>
          <div class="slide-subtitle" style="color: #94a3b8;">触球瞬间的精准执行</div>
          <ul>
            <li><strong>远离防守脚停球：</strong>用远离防守队员的外侧脚触球，将身体置于球与防守者之间护球。</li>
            <li><strong>顺势连停带过：</strong>停球方向直接对准出球路线或下一个攻击方格，一脚触球即完成摆脱。</li>
            <li><strong>出球精准控速：</strong>穿透球发力给低平快，回做球给软球便于不停球施射。</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-title gold">3. 后动作 (Post-Action)</div>
          <div class="slide-subtitle" style="color: #94a3b8;">出球后 0.5 秒的二次启动</div>
          <ul>
            <li><strong>“传完即动”铁律：</strong>出球后<strong>绝不原地看球</strong>！立即向前插或侧向跑位，做“第三人”。</li>
            <li><strong>丢球就地反抢：</strong>如果传球被断，最近的队员 0.5 秒内就地合围，执行“5秒反抢法则”。</li>
            <li><strong>保护阵型平衡：</strong>插上队员失位时，后方后腰或边卫立即横移补位，防止被反击。</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- SLIDE 05: 8大进攻流派 1 & 2 (含动图) -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 02 · 实战进攻战术流派</div>
        <h2>进攻流派 ① 第三人渗透流 & ② 宽度调度弱侧转移流 (动态沙盘)</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title green">🎬 流派 ① · 第三人跑位渗透 (Up-Back-Through)</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_third_man}" alt="第三人跑位动态演示">
          </div>
          <p><strong>运作逻辑：</strong>后腰(4)直塞背身中锋(7)[Up] ➔ 中锋回做中场(6)[Back] ➔ 中场直塞高速插上的第三人(5)单刀[Through]！</p>
          <div class="callout green" style="font-size: 12.5px;"><strong>调用武器：</strong>Weapon 01 直塞、06 回做、07 激光穿透、08 第三人</div>
        </div>

        <div class="card">
          <div class="card-title cyan">🎬 流派 ② · 强侧超载 ➔ 弱侧 1v1 转移</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_switch}" alt="弱侧转移动态演示">
          </div>
          <p><strong>运作逻辑：</strong>左路连续短传吸附防线整体横移 ➔ 中场(6)突然 30 米斜长传转移弱侧 ➔ 右翼(7)获得大片无人区突入禁区！</p>
          <div class="callout cyan" style="font-size: 12.5px;"><strong>调用武器：</strong>Weapon 09 大对角转移、10 边线推进、11 弧线绕顶</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 06: 8大进攻流派 3 & 4 (含动图) -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 02 · 实战进攻战术流派</div>
        <h2>进攻流派 ③ 纵深越顶身后流 & ④ 攻防转换5秒快攻流 (动态沙盘)</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title gold">🎬 流派 ③ · 纵深越顶与身后打击流 (Over-the-Top Chip)</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_over_the_top}" alt="纵深越顶身后打击动图">
          </div>
          <p><strong>运作逻辑：</strong>对手高位压迫防线推至中线 ➔ 中卫(3)送出 25~35 米精准过顶挑传 ➔ 中锋(7)盲区反越位冲刺单刀破门！</p>
          <div class="callout gold" style="font-size: 12.5px;"><strong>调用武器：</strong>Weapon 01 直塞、02 挑传空当、10 边线推进、18 越顶快攻</div>
        </div>

        <div class="card">
          <div class="card-title red">🎬 流派 ④ · 攻防转换5秒快攻闪击 (Gegenpressing Blitz)</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_5s_counter}" alt="攻防转换5秒反抢快攻动图">
          </div>
          <p><strong>运作逻辑：</strong>丢球 0.5s 内前场双人就地合围断球 ➔ 立即刺穿直塞插上中场(6) ➔ 3脚传球内分给前锋(7)推空门！</p>
          <div class="callout red" style="font-size: 12.5px;"><strong>调用武器：</strong>Weapon 07 激光穿透、17 门将出球、18 越顶快攻、20 界外球</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 07: 8大进攻流派 5 & 6 (含动图) -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 02 · 实战进攻战术流派</div>
        <h2>进攻流派 ⑤ 立体空战支点流 & ⑥ 禁区底线倒三角终结流 (动态沙盘)</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title purple">🎬 流派 ⑤ · 立体空战与支点摆渡流 (Target Man Aerial)</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_target_man}" alt="立体空战中锋胸部做球动图">
          </div>
          <p><strong>运作逻辑：</strong>后场起高球避开中场绞杀 ➔ 突前中锋(7)背身扛人胸部卸球回做 ➔ 后插上中场(6)迎球不停球重炮轰门！</p>
          <div class="callout purple" style="font-size: 12.5px;"><strong>调用武器：</strong>Weapon 02 挑传、06 回做做球、14 假射真传、18 越顶长传</div>
        </div>

        <div class="card">
          <div class="card-title green">🎬 流派 ⑥ · 禁区底线倒三角回传终结 (Cut-Back Finish)</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_cutback}" alt="底线倒三角动态演示">
          </div>
          <p><strong>运作逻辑：</strong>边锋(7)突至底线迫使门将防线退守门线 ➔ 底线发力倒三角推向点球点 ➔ 后插上中场(6)推射大半个空门！</p>
          <div class="callout green" style="font-size: 12.5px;"><strong>调用武器：</strong>Weapon 03 倒三角、04 贴地横扫、08 第三人、14 假射真传</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 08: 8大进攻流派 7 & 8 (含动图) -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 02 · 实战进攻战术流派</div>
        <h2>进攻流派 ⑦ 特种欺骗假动作流 & ⑧ 死球与战术界外球流 (动态沙盘)</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title gold">🎬 流派 ⑦ · 迎球假接真漏特种破局 (Dummy / Let-Through)</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_dummy}" alt="迎球假接真漏动态沙盘">
          </div>
          <p><strong>运作逻辑：</strong>后腰(4)直塞中场(6) ➔ 中场做出接球假动作突然叉腿漏球 ➔ 防守完全扑空，中锋(7)身后接球单刀破门！</p>
          <div class="callout gold" style="font-size: 12.5px;"><strong>调用武器：</strong>Weapon 13 不看人传球、14 假射真传、15 反向对角、16 漏球顺势</div>
        </div>

        <div class="card">
          <div class="card-title cyan">🎬 流派 ⑧ · 战术手抛界外球三角配合 (Tactical Throw-in)</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_throwin}" alt="战术手抛界外球动态沙盘">
          </div>
          <p><strong>运作逻辑：</strong>边卫(2)抛向前锋(7)脚下 ➔ 前锋一脚回敲，边卫高速套边下底 ➔ 底线横扫门前，包抄中场(6)抢点破门！</p>
          <div class="callout cyan" style="font-size: 12.5px;"><strong>调用武器：</strong>Weapon 03 倒三角、04 贴地横扫、19 定位球配合、20 战术界外球</div>
        </div>
      </div>
    </div>

    <!-- SLIDE 09: 20武器 分类一 (含动图) -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 03 · 20 种传球武器精要库</div>
        <h2>武器分类一：穿透与终结类 (Weapons 01-04 · 动态沙盘演示)</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title gold">🎬 分类一代表武器 · 肋部挑传空当 + 贴地横扫传中</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_w_cat1}" alt="分类一武器动图">
          </div>
          <p style="font-size: 12.5px;"><strong>技术要领：</strong>中场(4)脚尖搓挑打入肋部空当[Weapon 02] ➔ 边锋(5)不停球脚内侧发力平抽门前走廊[Weapon 04] ➔ 中锋(7)抢前点垫射破门！</p>
        </div>
        <div class="card" style="justify-content: space-between;">
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 01</span>
            <span class="weapon-name-inline">直塞穿透球 (Through Ball)</span>
            <div class="weapon-desc-compact">贴地发力刺穿双中卫结合部，给足前锋冲刺提前量。口令：“给身后！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 02</span>
            <span class="weapon-name-inline">肋部挑传空当 (Chipped Through)</span>
            <div class="weapon-desc-compact">脚尖搓球底部使球越过防守头顶落入肋部无人区。口令：“挑肋部！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 03</span>
            <span class="weapon-name-inline">底线倒三角回传 (Cut-Back Pass)</span>
            <div class="weapon-desc-compact">下底迫使门将回缩门线，发力推向点球点无人区。口令：“倒三角！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 04</span>
            <span class="weapon-name-inline">贴地横扫传中 (Driven Low Cross)</span>
            <div class="weapon-desc-compact">脚内侧平抽门前危险走廊，抢前点垫射或制造乌龙。口令：“前点平抽！”</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 10: 20武器 分类二 (含动图) -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 03 · 20 种传球武器精要库</div>
        <h2>武器分类二：破压与渗透类 (Weapons 05-08 · 动态沙盘演示)</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title gold">🎬 分类二代表武器 · 二过一撞墙配合动态沙盘 (Wall Pass)</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_w_cat2}" alt="二过一撞墙动图">
          </div>
          <p style="font-size: 12.5px;"><strong>技术要领：</strong>边锋(5)斜传中锋(7)瞬间全速前插绕过防守，中锋一脚顺势回塞跑动线路上完成单刀破门！</p>
        </div>
        <div class="card" style="justify-content: space-between;">
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 05</span>
            <span class="weapon-name-inline">二过一撞墙配合 (Wall Pass)</span>
            <div class="weapon-desc-compact">传球即启动冲刺，中锋做“墙”一脚顺势回塞。口令：“撞墙！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 06</span>
            <span class="weapon-name-inline">迎前回敲做球 (Lay-off)</span>
            <div class="weapon-desc-compact">背身迎球一脚轻推给面向前场的插上队友，做球要软方便施射。</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 07</span>
            <span class="weapon-name-inline">刺穿线形传球 (Line-Breaking Laser)</span>
            <div class="weapon-desc-compact">脚背正中发力贴地重炮，像激光一样瞬间穿透对手锋线或中场线。</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 08</span>
            <span class="weapon-name-inline">第三人跑位导向球 (Up-Back-Through)</span>
            <div class="weapon-desc-compact">A传B、B敲C、C直塞高速插上的第三人D，破密集防守第一神技。</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 11: 20武器 分类三 (含动图) -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 03 · 20 种传球武器精要库</div>
        <h2>武器分类三：宽度与调度类 (Weapons 09-12 · 动态沙盘演示)</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title cyan">🎬 分类三代表武器 · 弧线绕顶传球 + 边线推进</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_w_cat3}" alt="分类三武器动图">
          </div>
          <p style="font-size: 12.5px;"><strong>技术要领：</strong>中路防守极度密集封堵直线通道[Weapon 11] ➔ 中卫(3)拉出外侧强侧旋弧线球 ➔ 绕过防守直连右翼(6)高速长驱直入！</p>
        </div>
        <div class="card" style="justify-content: space-between;">
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 09</span>
            <span class="weapon-name-inline">大范围对角长传 (Diagonal Switch)</span>
            <div class="weapon-desc-compact">脚背内侧搓出 30 米以上斜长传，从强侧瞬间转移至弱侧空当。口令：“弱侧！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 10</span>
            <span class="weapon-name-inline">边线贴地推进球 (Channel Pass)</span>
            <div class="weapon-desc-compact">紧贴边线贴地直推，利用边线空间直接送给边锋启动。口令：“走边线！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 11</span>
            <span class="weapon-name-inline">弧线绕顶传球 (Curled Around Block)</span>
            <div class="weapon-desc-compact">脚内侧带强劲侧旋，球绕过中路防守封堵进入边肋空当。口令：“绕外侧！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 12</span>
            <span class="weapon-name-inline">回传重新组织球 (Recycling / Reset)</span>
            <div class="weapon-desc-compact">前场无机会时果断回传后卫或门将，重置阵型重新寻找攻击面。口令：“回传重来！”</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 12: 20武器 分类四 (含动图) -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 03 · 20 种传球武器精要库</div>
        <h2>武器分类四：隐蔽与特种破局类 (Weapons 13-16 · 动态沙盘演示)</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title gold">🎬 分类四代表武器 · 假射真传/节奏差破局</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_w_cat4}" alt="分类四武器动图">
          </div>
          <p style="font-size: 12.5px;"><strong>技术要领：</strong>前腰(6)弧顶大动作扬腿假射诱使后卫滑铲封堵[Weapon 14] ➔ 瞬间脚腕一扣节奏差隐蔽直塞右肋[Weapon 13] ➔ 中锋(7)单刀远角破门！</p>
        </div>
        <div class="card" style="justify-content: space-between;">
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 13</span>
            <span class="weapon-name-inline">不看人隐蔽传球 (No-Look Pass)</span>
            <div class="weapon-desc-compact">身体朝向和眼神看左，脚腕抖动向右出球，完全破坏对手预判。口令：“声东击西！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 14</span>
            <span class="weapon-name-inline">假射真传/节奏差 (Fake Shot & Slip)</span>
            <div class="weapon-desc-compact">大动作假射骗后卫下铲，在最后一瞬轻推空当插上队友。口令：“假射真分！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 15</span>
            <span class="weapon-name-inline">反向对角塞球 (Reverse Diagonal Pass)</span>
            <div class="weapon-desc-compact">横向带球中利用防线重心横移惯性，突然反方向直塞中路空当。口令：“打反向！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 16</span>
            <span class="weapon-name-inline">漏球顺势配合 (Dummy / Let-Through)</span>
            <div class="weapon-desc-compact">迎球接球假动作突然叉腿漏球，顺势滚给身后插上的第三人。口令：“漏过来！”</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 13: 20武器 分类五 (含动图) -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 03 · 20 种传球武器精要库</div>
        <h2>武器分类五：现代专项与死球类 (Weapons 17-20 · 动态沙盘演示)</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title green">🎬 分类五代表武器 · 门将穿透性低平球破压</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 8px;">
            <img src="{b64_w_cat5}" alt="分类五武器动图">
          </div>
          <p style="font-size: 12.5px;"><strong>技术要领：</strong>门将(1)推至弧顶做第7人[Weapon 17]，大力贴地平抽刺穿双人逼抢线 ➔ 中场(4)半侧身顺势领球送斜长传 ➔ 右翼(6)高速反击破门！</p>
        </div>
        <div class="card" style="justify-content: space-between;">
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 17</span>
            <span class="weapon-name-inline">门将穿透性低平球 (GK Line-Breaking)</span>
            <div class="weapon-desc-compact">门将作为出球核心，大力贴地刺穿前锋逼抢线直连中场。口令：“门将直穿！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 18</span>
            <span class="weapon-name-inline">反击越顶快攻长传 (Over-the-Top Counter)</span>
            <div class="weapon-desc-compact">断球后不停球直接半高球打到前场空旷地带供前锋冲刺。口令：“直接起身后！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 19</span>
            <span class="weapon-name-inline">定位球低平倒三角 (Set-piece Short)</span>
            <div class="weapon-desc-compact">角球/任意球不盲目起高球，发短传配合突入禁区肋部低平横扫。口令：“战术角球！”</div>
          </div>
          <div class="weapon-card-compact">
            <span class="weapon-num-badge">W 20</span>
            <span class="weapon-name-inline">战术手抛界外球 (Tactical Throw-in)</span>
            <div class="weapon-desc-compact">边卫抛给前锋，前锋一脚回敲，边卫高速插上直接传中。口令：“界外球一二配合！”</div>
          </div>
        </div>
      </div>
    </div>

    <!-- SLIDE 14: 7人制 1-2-3-1 (含动图) -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 04 · 阵型与位置职责卡</div>
        <h2>7人制 1-2-3-1 经典压迫传控阵型 & 门将出球破压 (动态沙盘)</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title green">📋 1-2-3-1 各位置核心职责卡 (Role Cards)</div>
          <ul style="font-size: 13px;">
            <li><strong>1号 门将 (GK)：</strong>站位推至禁区外做门卫；与双中卫构成后场 3v2 超载出球。</li>
            <li><strong>2/3号 双中卫 (CB)：</strong>控球时大范围拉开至两侧；负责向前刺穿直塞 4号(CM)。</li>
            <li><strong>4号 中前卫/核心 (CM)：</strong>攻防节拍器；接球前半侧身扫描；主导弱侧大转移与第三人直塞。</li>
            <li><strong>5/6号 双边锋 (LW/RW)：</strong>进攻拉满宽度；打 1v1 突破或与中锋打二过一；防守退守肋部。</li>
            <li><strong>7号 突前中锋 (ST)：</strong>第一反抢发起人；背身做球；斜插盲区反越位与前点破门。</li>
          </ul>
          <div class="callout green" style="font-size: 12px; margin-top: 8px;">
            <strong>★ 核心优势：</strong>中前场压迫极强、边路宽度充足，适合控球主导型打法。
          </div>
        </div>
        <div class="card">
          <div class="card-title gold">🎬 1-2-3-1 后场门将“+1”出球破高位逼抢动态沙盘</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 6px;">
            <img src="{b64_1231}" alt="1-2-3-1 出球动图">
          </div>
          <p style="font-size: 12.5px;"><strong>机制：</strong>门将(1)持球，双中卫(2+3)大范围拉开 ➔ 形成 3v2 破压 ➔ 门将刺穿直塞中场(4) ➔ 中场分边左翼(5)反击！</p>
        </div>
      </div>
    </div>

    <!-- SLIDE 15: 7人制 1-3-2-1 (含动图) -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 04 · 阵型与位置职责卡</div>
        <h2>7人制 1-3-2-1 圣诞树稳守反击阵型 & 翼卫双核冲刺 (动态沙盘)</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title cyan">📋 1-3-2-1 各位置核心职责卡 (Role Cards)</div>
          <ul style="font-size: 13px;">
            <li><strong>1号 门将 (GK)：</strong>防守指挥官，封堵单刀，得球后长传反击直找突前中锋。</li>
            <li><strong>3号 居中中卫 (CB)：</strong>防线定海神针；绝不上抢失位；负责中路补位、解围与长传调度。</li>
            <li><strong>2/4号 左右翼卫 (LWB/RWB)：</strong><strong>边路走廊飞翼</strong>；进攻全速插上下底；防守回撤成 5 人防线。</li>
            <li><strong>5号 防守型后腰 (DM)：</strong>锁死禁区弧顶核心区；负责扫荡拦截与后场第一脚安全出球。</li>
            <li><strong>6号 组织/前插中场 (AM)：</strong><strong>隐藏杀手</strong>；在中锋做球瞬间高速前插到弧顶爆射。</li>
            <li><strong>7号 突前支点中锋 (ST)：</strong>强力背身抗人；胸部卸球回做给 6号 或分边给插上的翼卫。</li>
          </ul>
          <div class="callout cyan" style="font-size: 12px; margin-top: 8px;">
            <strong>★ 核心优势：</strong>中路与肋部防守固若金汤，反击速度极快。
          </div>
        </div>
        <div class="card">
          <div class="card-title gold">🎬 1-3-2-1 圣诞树防守反击与双核冲刺动态沙盘</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 6px;">
            <img src="{b64_1321}" alt="1-3-2-1 防反动图">
          </div>
          <p style="font-size: 12.5px;"><strong>机制：</strong>中卫(3)断球纵向越顶连线中锋(7) ➔ 中锋胸部回做 ➔ 中场(6)弧顶迎球重炮轰门，翼卫(2)高速包抄！</p>
        </div>
      </div>
    </div>

    <!-- SLIDE 16: 8人制 1-3-3-1 (含动图) -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 04 · 阵型与位置职责卡</div>
        <h2>8人制 1-3-3-1 现代黄金全能阵型 & 边路双人组套边 (动态沙盘)</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title gold">📋 1-3-3-1 各位置核心职责卡 (Role Cards)</div>
          <ul style="font-size: 13px;">
            <li><strong>1号 门卫 (GK)：</strong>现代高位门将；大禁区弧顶扫荡；主导 3 后卫的地面出球。</li>
            <li><strong>3号 居中中卫 (CB)：</strong>后防总指挥；前压压缩中场空间；大范围斜长传转移弱侧。</li>
            <li><strong>2/4号 左右边后卫 (LB/RB)：</strong>边路屏障；进攻压至中线与边前卫形成 2v1 套边配合。</li>
            <li><strong>6号 中场指挥官 (CM)：</strong>攻防枢纽；掌控节奏；主导第三人跑位直塞与弱侧调度。</li>
            <li><strong>5/7号 左右边前卫 (LM/RM)：</strong>边路爆点；1v1 突破内切射门或底线送出倒三角。</li>
            <li><strong>8号 突前全能中锋 (ST)：</strong>牵制双中卫；前插反越位单刀；抢前点横扫折射破门。</li>
          </ul>
          <div class="callout gold" style="font-size: 12px; margin-top: 8px;">
            <strong>★ 核心优势：</strong>12+ 重叠三角网，攻守平衡无死角，传控容错率极高。
          </div>
        </div>
        <div class="card">
          <div class="card-title green">🎬 1-3-3-1 边路双人组套边 (Overlap) 动态沙盘</div>
          <div class="anim-container" style="height: 240px; margin-bottom: 6px;">
            <img src="{b64_1331}" alt="1-3-3-1 套边动图">
          </div>
          <p style="font-size: 12.5px;"><strong>机制：</strong>边锋(5)内切吸引后卫 ➔ 边卫(2)外侧套边插上下底 ➔ 底线倒三角横传点球点，中锋(8)推射破门！</p>
        </div>
      </div>
    </div>

    <!-- SLIDE 17: 阵型实战抉择矩阵 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 05 · 临场实战决策</div>
        <h2>三大阵型对比与比赛情境破局决策矩阵</h2>
      </div>
      <div class="slide-body" style="display: flex; flex-direction: column; gap: 14px;">
        <table class="matrix-table">
          <thead>
            <tr>
              <th>阵型架构</th>
              <th>主要优势</th>
              <th>潜在薄弱点</th>
              <th>核心进攻流派与武器</th>
              <th>推荐使用时机</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong style="color: #22c55e;">7人制 1-2-3-1</strong></td>
              <td>前场压迫极强<br>中前场控制力足</td>
              <td>双中卫身后空当大<br>边锋回防要求高</td>
              <td>流派① 渗透 + 流派② 弱侧转移<br>Weapon 01, 05, 08, 09</td>
              <td>主场压迫 / 实力占优 / 必须赢球抢攻</td>
            </tr>
            <tr>
              <td><strong style="color: #38bdf8;">7人制 1-3-2-1</strong></td>
              <td>防线铁闸极稳<br>中路肋部零死角</td>
              <td>进攻宽度依赖翼卫<br>中锋容易孤立</td>
              <td>流派③ 越顶 + 流派④ 5秒快攻<br>Weapon 03, 06, 08, 18</td>
              <td>遇强敌 / 客场作战 / 领先保胜 / 防守反击</td>
            </tr>
            <tr>
              <td><strong style="color: #fbbf24;">8人制 1-3-3-1</strong></td>
              <td>攻守完美平衡<br>边路双人组套边</td>
              <td>单后腰横向覆盖大<br>边后卫插上身后空当</td>
              <td>流派① 渗透 + 流派⑥ 底线倒三角<br>Weapon 03, 04, 07, 08, 10</td>
              <td>标准八人制比赛 / 全场控球主导打法</td>
            </tr>
          </tbody>
        </table>

        <div class="card" style="padding: 12px 18px;">
          <div class="card-title gold" style="font-size: 15px; margin-bottom: 6px;">⚡ 临场破局速查公式：</div>
          <p style="font-size: 13.5px; line-height: 1.6;">
            <strong>遇到对方高位逼抢：</strong>严禁后场盲目出脚 ➔ 启动【门将+1激光传球 + 越顶挑传反越位】<br>
            <strong>遇到对方低位摆铁桶：</strong>严禁中路硬塞 ➔ 启动【强侧超载弱侧大转移 + 底线倒三角 + 假射真传】<br>
            <strong>遇到中场激烈绞杀：</strong>严禁在脚下粘球 ➔ 启动【一脚出球 + 第三人跑位 + 中锋胸部做球】
          </p>
        </div>
      </div>
    </div>

    <!-- SLIDE 18: 守门员革命 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 05 · 关键战术引擎</div>
        <h2>现代足球守门员革命：第 7/8 名场上球员与“+1”出球体系</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title gold">🧤 现代守门员的战术角色重塑</div>
          <p>在莱比锡红牛与德国队战术中，守门员早已不是单纯扑救者，而是<strong>后场进攻发起的绝对第一核心</strong>：</p>
          <ul style="margin-top: 10px;">
            <li><strong>后场天然“+1”优势：</strong>当对方 2 名锋线球员对位逼抢我方 2 名中卫时，门将前压至大禁区弧顶接球，瞬间形成 <strong>3v2 局部人数绝对优势</strong>。</li>
            <li><strong>大禁区外高位扫荡（Sweeper）：</strong>全队压上进攻时，门将站位必须推进至禁区线甚至弧顶外，随时前冲解围对方长传反击。</li>
            <li><strong>双手与双脚兼备的出球大师：</strong>具备双手手抛球发动快攻、脚内侧低平快刺穿中场、以及精准挑传两翼边卫的能力。</li>
          </ul>
        </div>
        <div class="card" style="background: rgba(10,25,20,0.9);">
          <div class="card-title green">📋 守门员实战传球四大守则</div>
          <ol style="padding-left: 18px; font-size: 13.5px; color: #cbd5e1; line-height: 1.6;">
            <li><strong>永远向队友习惯脚出球：</strong>传球必须带速度且贴地，让接球后卫无需调整直接面向前场。</li>
            <li><strong>绝不拖延倒地抱球：</strong>扑救成功后若前场有反击机会，3 秒内起身手抛球或大脚开向边锋身后。</li>
            <li><strong>回传球绝不打向球门正中：</strong>队友回传门将时，必须回传到球门立柱外侧，防范停球失误直接漏入球网。</li>
            <li><strong>出球后立即横向移动接应：</strong>门将出球给中卫后，必须侧向移动拉开新角度，随时准备接中卫的回传安全球。</li>
          </ol>
        </div>
      </div>
    </div>

    <!-- SLIDE 19: 口令手册 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 05 · 场上呼应规范</div>
        <h2>球队实战呼应口令手册：统一全队场上快速沟通暗号</h2>
      </div>
      <div class="slide-body grid-3">
        <div class="card">
          <div class="card-title cyan">📢 接球与身位预警口令</div>
          <ul>
            <li><strong>“转过来！”（Turn）：</strong>接球人身后无人盯防，提示其不要回传，果断转身面向前场推进！</li>
            <li><strong>“有人/身后有人！”（Man On）：</strong>接球人身后有防守队员紧逼，提示其一脚出球或护球。</li>
            <li><strong>“半侧身！”（Open Up）：</strong>接球前提示队友调整脚步，不要背对前场。</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-title gold">📢 战术跑位与配合指令</div>
          <ul>
            <li><strong>“回敲！”（Drop / Lay-off）：</strong>提示前锋一脚把球软推给身后的中场施射。</li>
            <li><strong>“看第三人！”（Third Man）：</strong>提示持球人不要传给眼前的队员，直接塞向盲区插上的第三人。</li>
            <li><strong>“弱侧弱侧！”（Switch）：</strong>强侧遇阻，呼唤持球人一脚大范围对角转移至空当。</li>
            <li><strong>“撞墙！”（One-Two）：</strong>发起二过一配合的起动呼唤。</li>
          </ul>
        </div>
        <div class="card">
          <div class="card-title red">📢 防守与攻防转换口令</div>
          <ul>
            <li><strong>“5秒反抢！”（Press Now）：</strong>丢球瞬间全员高呼，最近 2 人立即包夹围抢。</li>
            <li><strong>“收回来！”（Drop Back）：</strong>反抢未果，全队立即回撤至本方半场 16 格落位。</li>
            <li><strong>“倒三角！”（Cut Back）：</strong>边路下底时禁区中路包抄人员的接应呼喊。</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- SLIDE 20: 总结与行动清单 -->
    <div class="slide">
      <div class="slide-header">
        <div class="slide-subtitle">MODULE 05 · 总结与落地</div>
        <h2>全景行动清单：从日常训练到比赛实战的执行标准</h2>
      </div>
      <div class="slide-body grid-2">
        <div class="card">
          <div class="card-title green">✅ 每名队员的赛前自检清单 (Pre-Match Checklist)</div>
          <ul style="font-size: 13.5px; line-height: 1.6;">
            <li>[ ] <strong>盲区扫描习惯：</strong>皮球在运动中，我是否做到了接球前 0.5s 观察身后与前场？</li>
            <li>[ ] <strong>身位开放意识：</strong>我接球时是否保持半侧身，还是总是死板地背对球门？</li>
            <li>[ ] <strong>同格不扎堆：</strong>在 16 格网格中，我是否拉开了与队友 5~10 米的合理距离？</li>
            <li>[ ] <strong>传完即动：</strong>我出球后是否立即二次启动前插或补位，绝不站在原地看球？</li>
            <li>[ ] <strong>呼应口令：</strong>在场上我是否主动喊出“转过来”、“有人”、“弱侧”帮助队友？</li>
          </ul>
        </div>
        <div class="card" style="background: rgba(10,30,20,0.85); border-color: var(--accent-gold);">
          <div class="card-title gold">🏆 战术进阶与球队寄语</div>
          <p style="font-size: 14px; line-height: 1.6; color: #cbd5e1;">
            “一支优秀的球队，不是靠某一个人的孤胆英雄主义，而是靠 7 或 8 个人在球场上如同精密齿轮般的协同与信任。”
          </p>
          <div class="callout gold" style="margin-top: 14px;">
            <strong>德国传球战术精髓：</strong><br>
            先看纵深，次选分边，最后回传；<br>
            前动作观察，主动作精准，后动作前插！
          </div>
          <p style="font-size: 13px; color: #94a3b8; margin-top: 14px; text-align: center;">
            祝全队队友在接下来的比赛中战术默契飙升，享受传控足球的无尽乐趣！⚽🔥
          </p>
        </div>
      </div>
    </div>

  </div>

  <!-- Bottom Dots Navigation -->
  <div class="bottombar" id="dots-container"></div>
  <div class="hotkey-hint">键盘 ← / → 翻页 | 空格 下一页 | F 全屏 | 点击动图放大</div>

  <!-- Lightbox Modal Overlay (放大观察镜) -->
  <div id="lightbox-modal" class="lightbox-modal" onclick="closeLightbox(event)">
    <div class="lightbox-controls" onclick="event.stopPropagation()">
      <span class="lightbox-title-badge" id="lightbox-title">战术动图放大观察</span>
      <div class="lightbox-btn-group">
        <button class="lb-btn" onclick="zoomIn()">➕ 放大</button>
        <button class="lb-btn" onclick="zoomOut()">➖ 缩小</button>
        <button class="lb-btn" onclick="resetZoom()">⟲ 还原</button>
        <button class="lb-btn close" onclick="closeLightboxDirect()">✕ 关闭 [ESC]</button>
      </div>
    </div>
    <div class="lightbox-viewport" id="lb-viewport" onclick="event.stopPropagation()">
      <img id="lightbox-img" src="" alt="战术放大图">
    </div>
    <div class="lightbox-hint">💡 滚轮平滑缩放 | 鼠标按住拖拽移动 | 双击 1x/2x 切换 | 按 ESC 键关闭</div>
  </div>

  <script>
    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    const dotsContainer = document.getElementById('dots-container');
    const counter = document.getElementById('slide-counter');

    // Lightbox Elements
    const lbModal = document.getElementById('lightbox-modal');
    const lbImg = document.getElementById('lightbox-img');
    const lbTitle = document.getElementById('lightbox-title');
    const lbViewport = document.getElementById('lb-viewport');
    let currentScale = 1;
    let isDragging = false;
    let startX, startY, transX = 0, transY = 0;

    slides.forEach((_, idx) => {{
      const dot = document.createElement('div');
      dot.className = 'dot' + (idx === 0 ? ' active' : '');
      dot.onclick = () => goToSlide(idx);
      dotsContainer.appendChild(dot);
    }});

    const dots = document.querySelectorAll('.dot');

    function updateSlide() {{
      slides.forEach((s, idx) => {{
        s.classList.toggle('active', idx === currentSlide);
      }});
      dots.forEach((d, idx) => {{
        d.classList.toggle('active', idx === currentSlide);
      }});
      counter.innerText = `${{String(currentSlide + 1).padStart(2, '0')}} / ${{String(totalSlides).padStart(2, '0')}}`;
    }}

    function nextSlide() {{
      if (currentSlide < totalSlides - 1) {{
        currentSlide++;
        updateSlide();
      }}
    }}

    function prevSlide() {{
      if (currentSlide > 0) {{
        currentSlide--;
        updateSlide();
      }}
    }}

    function goToSlide(idx) {{
      currentSlide = idx;
      updateSlide();
    }}

    function toggleFullScreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen();
      }} else {{
        if (document.exitFullscreen) {{
          document.exitFullscreen();
        }}
      }}
    }}

    // Lightbox Controller
    function openLightbox(src, title) {{
      lbImg.src = src;
      lbTitle.innerText = title ? `🔍 ${{title}}` : '🔍 战术沙盘放大观察';
      lbModal.classList.add('open');
      resetZoom();
    }}

    function closeLightboxDirect() {{
      lbModal.classList.remove('open');
    }}

    function closeLightbox(e) {{
      if (e.target === lbModal) {{
        closeLightboxDirect();
      }}
    }}

    function applyTransform() {{
      lbImg.style.transform = `scale(${{currentScale}}) translate(${{transX}}px, ${{transY}}px)`;
    }}

    function zoomIn() {{
      currentScale = Math.min(3.8, currentScale + 0.3);
      applyTransform();
    }}

    function zoomOut() {{
      currentScale = Math.max(0.5, currentScale - 0.3);
      applyTransform();
    }}

    function resetZoom() {{
      currentScale = 1.0;
      transX = 0;
      transY = 0;
      applyTransform();
    }}

    // Wheel zoom inside viewport
    lbViewport.addEventListener('wheel', (e) => {{
      e.preventDefault();
      if (e.deltaY < 0) {{
        currentScale = Math.min(3.8, currentScale + 0.18);
      }} else {{
        currentScale = Math.max(0.5, currentScale - 0.18);
      }}
      applyTransform();
    }});

    // Drag to pan
    lbViewport.addEventListener('mousedown', (e) => {{
      isDragging = true;
      startX = e.clientX - transX;
      startY = e.clientY - transY;
    }});
    window.addEventListener('mousemove', (e) => {{
      if (isDragging) {{
        transX = e.clientX - startX;
        transY = e.clientY - startY;
        applyTransform();
      }}
    }});
    window.addEventListener('mouseup', () => {{
      isDragging = false;
    }});

    // Double click to toggle 1x / 2x zoom
    lbViewport.addEventListener('dblclick', () => {{
      if (currentScale > 1.2) {{
        resetZoom();
      }} else {{
        currentScale = 2.0;
        applyTransform();
      }}
    }});

    // Bind click events on all anim-containers
    document.querySelectorAll('.anim-container').forEach(container => {{
      const img = container.querySelector('img');
      if (img) {{
        container.onclick = () => {{
          const cardTitle = container.closest('.card')?.querySelector('.card-title')?.innerText || '动态战术沙盘';
          openLightbox(img.src, cardTitle);
        }};
      }}
    }});

    // Global Keybindings
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        if (lbModal.classList.contains('open')) {{
          closeLightboxDirect();
          return;
        }}
      }}
      // If modal is open, prevent deck page slide
      if (lbModal.classList.contains('open')) {{
        if (e.key === '+' || e.key === '=') zoomIn();
        if (e.key === '-' || e.key === '_') zoomOut();
        if (e.key === '0') resetZoom();
        return;
      }}

      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        nextSlide();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        prevSlide();
      }} else if (e.key.toLowerCase() === 'f') {{
        toggleFullScreen();
      }} else if (e.key === 'Home') {{
        goToSlide(0);
      }} else if (e.key === 'End') {{
        goToSlide(totalSlides - 1);
      }}
    }});

    let touchStartX = 0;
    document.addEventListener('touchstart', (e) => {{
      touchStartX = e.touches[0].clientX;
    }});
    document.addEventListener('touchend', (e) => {{
      if (lbModal.classList.contains('open')) return;
      let touchEndX = e.changedTouches[0].clientX;
      if (touchStartX - touchEndX > 50) nextSlide();
      if (touchEndX - touchStartX > 50) prevSlide();
    }});
  </script>
</body>
</html>
"""

output_workspace = r"e:\06_Study\书籍\足球\football_tactics_deck.html"
output_artifact = r"C:\Users\Administrator\.gemini\antigravity\brain\030fc641-b9cc-4e72-b4ba-ed21a5a6e35f\football_tactics_deck.html"

with open(output_workspace, "w", encoding="utf-8") as f:
    f.write(html_template)

with open(output_artifact, "w", encoding="utf-8") as f:
    f.write(html_template)

print("Rebuilt football_tactics_deck.html with 16 dynamic embedded GIFs & Lightbox Zoom Tool successfully!")
