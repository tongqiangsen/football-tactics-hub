import pymupdf, os

svg_7v7_1321 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1400" width="1000" height="1400">
  <defs>
    <linearGradient id="fieldGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0a1f14"/>
      <stop offset="50%" stop-color="#0d281a"/>
      <stop offset="100%" stop-color="#08170e"/>
    </linearGradient>
    <marker id="arrowGold" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#fbbf24" />
    </marker>
    <marker id="arrowCyan" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#38bdf8" />
    </marker>
  </defs>

  <!-- Pitch Background -->
  <rect width="1000" height="1400" fill="url(#fieldGrad)"/>
  <rect x="50" y="50" width="900" height="1300" fill="none" stroke="#22c55e" stroke-width="4" stroke-opacity="0.4" rx="16"/>
  <line x1="50" y1="700" x2="950" y2="700" stroke="#22c55e" stroke-width="3" stroke-opacity="0.3" stroke-dasharray="8,8"/>
  <circle cx="500" cy="700" r="120" fill="none" stroke="#22c55e" stroke-width="3" stroke-opacity="0.3"/>
  <rect x="250" y="1100" width="500" height="250" fill="none" stroke="#22c55e" stroke-width="3" stroke-opacity="0.3"/>
  <rect x="350" y="1230" width="300" height="120" fill="none" stroke="#22c55e" stroke-width="3" stroke-opacity="0.3"/>

  <!-- Title Header -->
  <rect x="70" y="70" width="860" height="110" fill="#0f172a" fill-opacity="0.85" rx="12" stroke="#38bdf8" stroke-width="2"/>
  <text x="500" y="120" font-family="sans-serif" font-size="34" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="2">7人制 1-3-2-1 圣诞树稳守反击阵型</text>
  <text x="500" y="155" font-family="sans-serif" font-size="18" fill="#38bdf8" text-anchor="middle">三后卫铁闸 · 双中场双核插上 · 翼卫走廊冲刺</text>

  <!-- Formation Triangles & Mesh -->
  <polygon points="180,920 500,1020 350,680" fill="#38bdf8" fill-opacity="0.07" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
  <polygon points="820,920 500,1020 650,680" fill="#38bdf8" fill-opacity="0.07" stroke="#38bdf8" stroke-width="2" stroke-dasharray="4,4"/>
  <polygon points="500,1020 350,680 650,680" fill="#fbbf24" fill-opacity="0.08" stroke="#fbbf24" stroke-width="2" stroke-dasharray="5,5"/>
  <polygon points="350,680 650,680 500,340" fill="#22c55e" fill-opacity="0.08" stroke="#22c55e" stroke-width="2" stroke-dasharray="5,5"/>
  <polygon points="180,920 350,680 500,340" fill="#38bdf8" fill-opacity="0.04" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>
  <polygon points="820,920 650,680 500,340" fill="#38bdf8" fill-opacity="0.04" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="3,3"/>

  <!-- Tactical Movement Arrows -->
  <path d="M180,900 C150,700 160,500 200,380" fill="none" stroke="#38bdf8" stroke-width="3.5" stroke-dasharray="6,4" marker-end="url(#arrowCyan)"/>
  <path d="M820,900 C850,700 840,500 800,380" fill="none" stroke="#38bdf8" stroke-width="3.5" stroke-dasharray="6,4" marker-end="url(#arrowCyan)"/>
  <path d="M650,650 C620,520 560,420 540,360" fill="none" stroke="#fbbf24" stroke-width="3.5" stroke-dasharray="6,4" marker-end="url(#arrowGold)"/>

  <!-- Players (White Jersey Team) -->
  <circle cx="500" cy="1240" r="28" fill="#f59e0b" stroke="#ffffff" stroke-width="3"/>
  <text x="500" y="1248" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000" text-anchor="middle">1</text>
  <text x="500" y="1285" font-family="sans-serif" font-size="16" font-weight="bold" fill="#fbbf24" text-anchor="middle">门将 (GK)</text>

  <circle cx="180" cy="920" r="26" fill="#ffffff" stroke="#38bdf8" stroke-width="3"/>
  <text x="180" y="927" font-family="sans-serif" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">2</text>
  <text x="180" y="960" font-family="sans-serif" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">左翼卫 (LWB)</text>

  <circle cx="500" cy="1020" r="26" fill="#ffffff" stroke="#38bdf8" stroke-width="3"/>
  <text x="500" y="1027" font-family="sans-serif" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">3</text>
  <text x="500" y="1060" font-family="sans-serif" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">居中中卫 (CB)</text>

  <circle cx="820" cy="920" r="26" fill="#ffffff" stroke="#38bdf8" stroke-width="3"/>
  <text x="820" y="927" font-family="sans-serif" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">4</text>
  <text x="820" y="960" font-family="sans-serif" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">右翼卫 (RWB)</text>

  <circle cx="350" cy="680" r="26" fill="#ffffff" stroke="#22c55e" stroke-width="3"/>
  <text x="350" y="687" font-family="sans-serif" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">5</text>
  <text x="350" y="720" font-family="sans-serif" font-size="15" font-weight="bold" fill="#22c55e" text-anchor="middle">防守中场 (DM/CM1)</text>

  <circle cx="650" cy="680" r="26" fill="#ffffff" stroke="#fbbf24" stroke-width="3"/>
  <text x="650" y="687" font-family="sans-serif" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">6</text>
  <text x="650" y="720" font-family="sans-serif" font-size="15" font-weight="bold" fill="#fbbf24" text-anchor="middle">组织中场 (AM/CM2)</text>

  <circle cx="500" cy="340" r="28" fill="#ffffff" stroke="#ef4444" stroke-width="3"/>
  <text x="500" y="348" font-family="sans-serif" font-size="20" font-weight="bold" fill="#0f172a" text-anchor="middle">7</text>
  <text x="500" y="300" font-family="sans-serif" font-size="16" font-weight="bold" fill="#ef4444" text-anchor="middle">突前支点中锋 (ST)</text>

  <!-- Bottom Tactical Legend Card -->
  <rect x="70" y="1130" width="860" height="200" fill="#0f172a" fill-opacity="0.9" rx="12" stroke="#64748b" stroke-width="1.5"/>
  <text x="95" y="1165" font-family="sans-serif" font-size="20" font-weight="bold" fill="#38bdf8">⚡ 1-3-2-1 阵型核心战术要义：</text>
  <text x="95" y="1200" font-family="sans-serif" font-size="16" fill="#e2e8f0">1. 后防绝对锁死：3中卫+双后腰天然形成 5 人紧凑防守盒，封死中路与肋部，极难被对手打穿。</text>
  <text x="95" y="1235" font-family="sans-serif" font-size="16" fill="#e2e8f0">2. 翼卫纵深走廊：2号/4号翼卫是进攻宽度的唯一来源，丢球回撤成5后卫，反击狂飙提供传中。</text>
  <text x="95" y="1270" font-family="sans-serif" font-size="16" fill="#e2e8f0">3. 双中场梯次分工：5号拖后洗球保护中卫；6号前插做第三人跑位，在中锋做球后完成禁区弧顶爆射。</text>
  <text x="95" y="1305" font-family="sans-serif" font-size="16" fill="#cbd5e1">★ 适用场景：面对整体实力强于自己的对手、防守反击战术、领先保胜局势、场地较宽的7人制球场。</text>
</svg>"""

svg_8v8_1331 = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1400" width="1000" height="1400">
  <defs>
    <linearGradient id="fieldGrad8" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#081d14"/>
      <stop offset="50%" stop-color="#0d2b1c"/>
      <stop offset="100%" stop-color="#06160d"/>
    </linearGradient>
    <marker id="arrowGold8" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#fbbf24" />
    </marker>
    <marker id="arrowGreen8" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#22c55e" />
    </marker>
    <marker id="arrowCyan8" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L9,3 z" fill="#38bdf8" />
    </marker>
  </defs>

  <!-- Pitch Background -->
  <rect width="1000" height="1400" fill="url(#fieldGrad8)"/>
  <rect x="50" y="50" width="900" height="1300" fill="none" stroke="#22c55e" stroke-width="4" stroke-opacity="0.4" rx="16"/>
  <line x1="50" y1="700" x2="950" y2="700" stroke="#22c55e" stroke-width="3" stroke-opacity="0.3" stroke-dasharray="8,8"/>
  <circle cx="500" cy="700" r="120" fill="none" stroke="#22c55e" stroke-width="3" stroke-opacity="0.3"/>
  <rect x="250" y="1100" width="500" height="250" fill="none" stroke="#22c55e" stroke-width="3" stroke-opacity="0.3"/>
  <rect x="350" y="1230" width="300" height="120" fill="none" stroke="#22c55e" stroke-width="3" stroke-opacity="0.3"/>

  <!-- Title Header -->
  <rect x="70" y="70" width="860" height="110" fill="#0f172a" fill-opacity="0.85" rx="12" stroke="#22c55e" stroke-width="2"/>
  <text x="500" y="120" font-family="sans-serif" font-size="34" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="2">8人制 1-3-3-1 现代黄金全能阵型</text>
  <text x="500" y="155" font-family="sans-serif" font-size="18" fill="#22c55e" text-anchor="middle">四层三线多三角 · 边路双人搭档 · 攻守全能平衡</text>

  <!-- Multi-Triangle Meshes -->
  <polygon points="200,950 500,1020 200,620" fill="#38bdf8" fill-opacity="0.06" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
  <polygon points="800,950 500,1020 800,620" fill="#38bdf8" fill-opacity="0.06" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
  <polygon points="200,950 500,680 500,1020" fill="#22c55e" fill-opacity="0.06" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="4,4"/>
  <polygon points="800,950 500,680 500,1020" fill="#22c55e" fill-opacity="0.06" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="4,4"/>
  <polygon points="200,620 500,680 500,340" fill="#fbbf24" fill-opacity="0.08" stroke="#fbbf24" stroke-width="2" stroke-dasharray="5,5"/>
  <polygon points="800,620 500,680 500,340" fill="#fbbf24" fill-opacity="0.08" stroke="#fbbf24" stroke-width="2" stroke-dasharray="5,5"/>

  <!-- Tactical Movement Arrows -->
  <path d="M170,920 C130,750 140,550 170,420" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4" marker-end="url(#arrowCyan8)"/>
  <path d="M220,590 C260,520 360,450 420,380" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="5,4" marker-end="url(#arrowGreen8)"/>
  <path d="M780,590 C740,520 640,450 580,380" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="5,4" marker-end="url(#arrowGreen8)"/>
  <path d="M500,650 L500,480" fill="none" stroke="#fbbf24" stroke-width="3.5" stroke-dasharray="6,4" marker-end="url(#arrowGold8)"/>

  <!-- Players (White Jersey Team) -->
  <circle cx="500" cy="1240" r="28" fill="#f59e0b" stroke="#ffffff" stroke-width="3"/>
  <text x="500" y="1248" font-family="sans-serif" font-size="20" font-weight="bold" fill="#000000" text-anchor="middle">1</text>
  <text x="500" y="1285" font-family="sans-serif" font-size="16" font-weight="bold" fill="#fbbf24" text-anchor="middle">门卫 (GK)</text>

  <circle cx="200" cy="950" r="26" fill="#ffffff" stroke="#38bdf8" stroke-width="3"/>
  <text x="200" y="957" font-family="sans-serif" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">2</text>
  <text x="200" y="990" font-family="sans-serif" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">左边后卫 (LB)</text>

  <circle cx="500" cy="1020" r="26" fill="#ffffff" stroke="#38bdf8" stroke-width="3"/>
  <text x="500" y="1027" font-family="sans-serif" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">3</text>
  <text x="500" y="1060" font-family="sans-serif" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">居中中卫 (CB)</text>

  <circle cx="800" cy="950" r="26" fill="#ffffff" stroke="#38bdf8" stroke-width="3"/>
  <text x="800" y="957" font-family="sans-serif" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">4</text>
  <text x="800" y="990" font-family="sans-serif" font-size="15" font-weight="bold" fill="#ffffff" text-anchor="middle">右边后卫 (RB)</text>

  <circle cx="200" cy="620" r="26" fill="#ffffff" stroke="#22c55e" stroke-width="3"/>
  <text x="200" y="627" font-family="sans-serif" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">5</text>
  <text x="200" y="660" font-family="sans-serif" font-size="15" font-weight="bold" fill="#22c55e" text-anchor="middle">左边前卫 (LM)</text>

  <circle cx="500" cy="680" r="26" fill="#ffffff" stroke="#fbbf24" stroke-width="3"/>
  <text x="500" y="687" font-family="sans-serif" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">6</text>
  <text x="500" y="720" font-family="sans-serif" font-size="15" font-weight="bold" fill="#fbbf24" text-anchor="middle">中前卫/核心 (CM)</text>

  <circle cx="800" cy="620" r="26" fill="#ffffff" stroke="#22c55e" stroke-width="3"/>
  <text x="800" y="627" font-family="sans-serif" font-size="18" font-weight="bold" fill="#0f172a" text-anchor="middle">7</text>
  <text x="800" y="660" font-family="sans-serif" font-size="15" font-weight="bold" fill="#22c55e" text-anchor="middle">右边前卫 (RM)</text>

  <circle cx="500" cy="340" r="28" fill="#ffffff" stroke="#ef4444" stroke-width="3"/>
  <text x="500" y="348" font-family="sans-serif" font-size="20" font-weight="bold" fill="#0f172a" text-anchor="middle">8</text>
  <text x="500" y="300" font-family="sans-serif" font-size="16" font-weight="bold" fill="#ef4444" text-anchor="middle">突前中锋 (ST)</text>

  <!-- Bottom Tactical Legend Card -->
  <rect x="70" y="1130" width="860" height="200" fill="#0f172a" fill-opacity="0.9" rx="12" stroke="#64748b" stroke-width="1.5"/>
  <text x="95" y="1165" font-family="sans-serif" font-size="20" font-weight="bold" fill="#22c55e">⚡ 8人制 1-3-3-1 阵型核心战术要义：</text>
  <text x="95" y="1200" font-family="sans-serif" font-size="16" fill="#e2e8f0">1. 边路双人搭档：左路(2+5)与右路(4+7)形成边路双保险，套边(Overlap)与套内(Underlap)随时撕开边路防线。</text>
  <text x="95" y="1235" font-family="sans-serif" font-size="16" fill="#fbbf24" font-weight="bold">2. 黄金中轴核心：CB(3) ➔ CM(6) ➔ ST(8) 贯穿全场中轴，掌控中路控制权与攻防节奏切换。</text>
  <text x="95" y="1270" font-family="sans-serif" font-size="16" fill="#22c55e" font-weight="bold">3. 12+重叠三角网：场上任何一名队员持球，身边均有至少 3 个不同角度的出球接应点，传控容错率极高。</text>
  <text x="95" y="1305" font-family="sans-serif" font-size="16" fill="#cbd5e1">★ 适用场景：标准八人制比赛、控球主导型打法、追求边中结合与高位压迫的进攻型球队。</text>
</svg>"""

artifact_dir = r"C:\Users\Administrator\.gemini\antigravity\brain\030fc641-b9cc-4e72-b4ba-ed21a5a6e35f"
os.makedirs(artifact_dir, exist_ok=True)

# 7v7 1-3-2-1
svg_path_1321 = os.path.join(artifact_dir, "card_7v7_1321.svg")
png_path_1321 = os.path.join(artifact_dir, "card_7v7_1321_hd.png")
with open(svg_path_1321, "w", encoding="utf-8") as f:
    f.write(svg_7v7_1321)

doc = pymupdf.open(svg_path_1321)
pix = doc[0].get_pixmap(dpi=300)
pix.save(png_path_1321)
print("Generated 7v7 1-3-2-1 HD Card successfully:", png_path_1321)

# 8v8 1-3-3-1
svg_path_1331 = os.path.join(artifact_dir, "card_8v8_1331.svg")
png_path_1331 = os.path.join(artifact_dir, "card_8v8_1331_hd.png")
with open(svg_path_1331, "w", encoding="utf-8") as f:
    f.write(svg_8v8_1331)

doc = pymupdf.open(svg_path_1331)
pix = doc[0].get_pixmap(dpi=300)
pix.save(png_path_1331)
print("Generated 8v8 1-3-3-1 HD Card successfully:", png_path_1331)
