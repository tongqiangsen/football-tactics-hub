# -*- coding: utf-8 -*-
import fitz
import os

target_dir = r"C:/Users/Administrator/.gemini/antigravity/brain/030fc641-b9cc-4e72-b4ba-ed21a5a6e35f"
os.makedirs(target_dir, exist_ok=True)

W, H = 1200, 1680

def get_defs():
    return '''
    <defs>
      <!-- Arrow Markers -->
      <marker id="arrowYellow" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto">
        <path d="M0,0 L0,6 L7,3 z" fill="#facc15" />
      </marker>
      
      <marker id="arrowCyan" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto">
        <path d="M0,0 L0,6 L7,3 z" fill="#38bdf8" />
      </marker>

      <marker id="arrowWhite" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto">
        <path d="M0,0 L0,6 L7,3 z" fill="#ffffff" />
      </marker>

      <marker id="arrowRed" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto">
        <path d="M0,0 L0,6 L7,3 z" fill="#ef4444" />
      </marker>

      <marker id="arrowGreen" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto">
        <path d="M0,0 L0,6 L7,3 z" fill="#4ade80" />
      </marker>

      <marker id="arrowOrange" markerWidth="9" markerHeight="9" refX="5" refY="3" orient="auto">
        <path d="M0,0 L0,6 L7,3 z" fill="#fb923c" />
      </marker>

      <!-- Drop Shadows -->
      <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
        <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="0.4"/>
      </filter>
    </defs>
    '''

def get_base_pitch():
    stripes = ""
    st_h = 75
    for i in range(16):
        c = "#2d7f36" if i % 2 == 0 else "#256c2d"
        stripes += f'<rect x="0" y="{120 + i*st_h}" width="{W}" height="{st_h}" fill="{c}" />\n'
    
    lines = '''
    <rect x="60" y="140" width="1080" height="1180" fill="none" stroke="#ffffff" stroke-width="4" stroke-opacity="0.9" rx="4" />
    <line x1="60" y1="730" x2="1140" y2="730" stroke="#ffffff" stroke-width="4" stroke-opacity="0.9" />
    <circle cx="600" cy="730" r="130" fill="none" stroke="#ffffff" stroke-width="4" stroke-opacity="0.9" />
    <circle cx="600" cy="730" r="7" fill="#ffffff" />
    
    <!-- Top Goal Box -->
    <rect x="360" y="140" width="480" height="220" fill="none" stroke="#ffffff" stroke-width="4" stroke-opacity="0.9" />
    <rect x="470" y="90" width="260" height="50" fill="#ffffff" fill-opacity="0.15" stroke="#ffffff" stroke-width="4" />
    <circle cx="600" cy="270" r="6" fill="#ffffff" />
    <path d="M 500 360 A 130 130 0 0 0 700 360" fill="none" stroke="#ffffff" stroke-width="4" stroke-opacity="0.9" />
    
    <!-- Bottom Goal Box -->
    <rect x="360" y="1100" width="480" height="220" fill="none" stroke="#ffffff" stroke-width="4" stroke-opacity="0.9" />
    <rect x="470" y="1320" width="260" height="50" fill="#ffffff" fill-opacity="0.15" stroke="#ffffff" stroke-width="4" />
    <circle cx="600" cy="1190" r="6" fill="#ffffff" />
    <path d="M 500 1100 A 130 130 0 0 1 700 1100" fill="none" stroke="#ffffff" stroke-width="4" stroke-opacity="0.9" />
    
    <!-- Corner Arcs -->
    <path d="M 60 170 A 30 30 0 0 0 90 140" fill="none" stroke="#ffffff" stroke-width="4" stroke-opacity="0.9" />
    <path d="M 1140 170 A 30 30 0 0 1 1110 140" fill="none" stroke="#ffffff" stroke-width="4" stroke-opacity="0.9" />
    <path d="M 60 1290 A 30 30 0 0 1 90 1320" fill="none" stroke="#ffffff" stroke-width="4" stroke-opacity="0.9" />
    <path d="M 1140 1290 A 30 30 0 0 0 1110 1320" fill="none" stroke="#ffffff" stroke-width="4" stroke-opacity="0.9" />
    '''
    return stripes + lines

def render_player(cx, cy, num, label, team='white'):
    if team == 'white':
        body_fill = "#ffffff"
        body_stroke = "#0f172a"
        text_color = "#0f172a"
        tag_bg = "#0f172a"
        tag_border = "#38bdf8"
    elif team == 'gk':
        body_fill = "#fbbf24"
        body_stroke = "#78350f"
        text_color = "#0f172a"
        tag_bg = "#0f172a"
        tag_border = "#fbbf24"
    else: # red opponent
        body_fill = "#ef4444"
        body_stroke = "#ffffff"
        text_color = "#ffffff"
        tag_bg = "#7f1d1d"
        tag_border = "#f87171"
    
    return f'''
    <g filter="url(#shadow)">
      <circle cx="{cx}" cy="{cy}" r="34" fill="{body_fill}" stroke="{body_stroke}" stroke-width="4" />
      <text x="{cx}" y="{cy + 10}" font-size="28" font-weight="900" fill="{text_color}" text-anchor="middle" font-family="Arial, 'Microsoft YaHei', sans-serif">{num}</text>
      
      <rect x="{cx - 60}" y="{cy + 42}" width="120" height="30" rx="6" fill="{tag_bg}" stroke="{tag_border}" stroke-width="2.5" />
      <text x="{cx}" y="{cy + 63}" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">{label}</text>
    </g>
    '''

# ==========================================
# CARD 1: 阵型与网格 (1-2-3-1)
# ==========================================
def build_card_1():
    gk = (600, 1220)
    lcb = (300, 1020)
    rcb = (900, 1020)
    cm = (600, 750)
    lm = (180, 520)
    rm = (1020, 520)
    st = (600, 320)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
    {get_defs()}
    <rect width="{W}" height="{H}" fill="#0b131f" />
    {get_base_pitch()}

    <!-- Header Banner -->
    <rect x="0" y="0" width="{W}" height="120" fill="#0f172a" />
    <rect x="60" y="24" width="8" height="72" fill="#38bdf8" rx="4" />
    <text x="85" y="62" font-size="34" font-weight="900" fill="#ffffff" font-family="'Microsoft YaHei', sans-serif">七人制战术图解 01 ｜ 1-2-3-1 阵型与三角支撑网格</text>
    <text x="85" y="96" font-size="18" font-weight="bold" fill="#94a3b8" font-family="'Microsoft YaHei', sans-serif">【主队：白色球衣】 战术哲学：德国足球传球拼图 IQ® ｜ 任何持球点随时保持 2~3 个出球支点</text>

    <!-- Mesh Triangles (Dashed Yellow/Cyan, fill=none) -->
    <g stroke-dasharray="10,8" stroke-width="3.5">
      <polygon points="{gk[0]},{gk[1]} {lcb[0]},{lcb[1]} {rcb[0]},{rcb[1]}" fill="none" stroke="#38bdf8" />
      <polygon points="{lcb[0]},{lcb[1]} {rcb[0]},{rcb[1]} {cm[0]},{cm[1]}" fill="none" stroke="#facc15" />
      <polygon points="{lcb[0]},{lcb[1]} {lm[0]},{lm[1]} {cm[0]},{cm[1]}" fill="none" stroke="#38bdf8" />
      <polygon points="{rcb[0]},{rcb[1]} {rm[0]},{rm[1]} {cm[0]},{cm[1]}" fill="none" stroke="#38bdf8" />
      <polygon points="{lm[0]},{lm[1]} {cm[0]},{cm[1]} {st[0]},{st[1]}" fill="none" stroke="#facc15" />
      <polygon points="{rm[0]},{rm[1]} {cm[0]},{cm[1]} {st[0]},{st[1]}" fill="none" stroke="#facc15" />
    </g>

    <!-- Runs -->
    <path d="M {lm[0]} {lm[1]-50} Q {lm[0]+20} {lm[1]-160} {lm[0]+60} {lm[1]-240}" fill="none" stroke="#ffffff" stroke-width="4.5" stroke-dasharray="8,6" marker-end="url(#arrowWhite)" />
    <rect x="{lm[0]+20}" y="{lm[1]-170}" width="110" height="30" rx="6" fill="#0f172a" fill-opacity="0.8" stroke="#ffffff" stroke-width="1.5" />
    <text x="{lm[0]+75}" y="{lm[1]-150}" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">边路套上</text>

    <path d="M {rm[0]} {rm[1]-50} Q {rm[0]-20} {rm[1]-160} {rm[0]-60} {rm[1]-240}" fill="none" stroke="#ffffff" stroke-width="4.5" stroke-dasharray="8,6" marker-end="url(#arrowWhite)" />
    <rect x="{rm[0]-130}" y="{rm[1]-170}" width="110" height="30" rx="6" fill="#0f172a" fill-opacity="0.8" stroke="#ffffff" stroke-width="1.5" />
    <text x="{rm[0]-75}" y="{lm[1]-150}" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">弱侧插上</text>

    <path d="M {st[0]} {st[1]+50} L {st[0]} {st[1]+120}" fill="none" stroke="#facc15" stroke-width="4.5" stroke-dasharray="8,6" marker-end="url(#arrowYellow)" />
    <rect x="{st[0]+20}" y="{st[1]+75}" width="110" height="30" rx="6" fill="#0f172a" fill-opacity="0.8" stroke="#facc15" stroke-width="1.5" />
    <text x="{st[0]+75}" y="{st[1]+95}" font-size="16" font-weight="bold" fill="#facc15" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">回撤做墙</text>

    <!-- Players -->
    {render_player(gk[0], gk[1], "1", "门将 GK", "gk")}
    {render_player(lcb[0], lcb[1], "2", "左中卫 LCB", "white")}
    {render_player(rcb[0], rcb[1], "3", "右中卫 RCB", "white")}
    {render_player(cm[0], cm[1], "6", "核心中场 CM", "white")}
    {render_player(lm[0], lm[1], "7", "左边中场 LM", "white")}
    {render_player(rm[0], rm[1], "11", "右边中场 RM", "white")}
    {render_player(st[0], st[1], "9", "中锋 ST", "white")}

    <!-- Bottom Instruction Card -->
    <rect x="40" y="1350" width="{W-80}" height="300" rx="16" fill="#0f172a" stroke="rgba(255,255,255,0.3)" stroke-width="2" />
    <text x="80" y="1395" font-size="24" font-weight="900" fill="#38bdf8" font-family="'Microsoft YaHei', sans-serif">📌 各位置核心职责与跑位纪律</text>
    
    <text x="80" y="1440" font-size="19" fill="#f8fafc" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#fbbf24">【中锋 ST #9】</tspan> 进攻压制对方后卫提供纵深；拿球以<tspan fill="#38bdf8">背身一脚做球（撞墙）</tspan>为主，严禁单打粘球。
    </text>
    <text x="80" y="1485" font-size="19" fill="#f8fafc" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#fbbf24">【双边中场 #7 / #11】</tspan> 进攻时必须<tspan fill="#38bdf8">拉开到边线撑开场地宽度</tspan>；防守时主动内收到肋部保护中路。
    </text>
    <text x="80" y="1530" font-size="19" fill="#f8fafc" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#fbbf24">【核心中场 #6】</tspan> 攻防节奏器，永远在持球人侧后方提供安全接应；横向大范围覆盖。
    </text>
    <text x="80" y="1575" font-size="19" fill="#f8fafc" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#fbbf24">【双后卫 #2 / #3】</tspan> 进攻时拉开到大禁区两侧形成出球点；防守时保持<tspan fill="#38bdf8">“一人顶抢、一人拖后保护”</tspan>。
    </text>
    <text x="80" y="1620" font-size="19" font-weight="bold" fill="#4ade80" font-family="'Microsoft YaHei', sans-serif">
      💡 全队铁律：持球人周围必须始终保持至少 2 个传球三角支点，出球后必须立刻跑位！
    </text>
    </svg>'''
    return svg

# ==========================================
# CARD 2: 后场破高压 (Build-up)
# ==========================================
def build_card_2():
    gk = (600, 1220)
    lcb = (260, 1060)
    rcb = (940, 1060)
    cm = (600, 840)
    lm = (180, 560)
    rm = (1020, 560)
    st = (600, 320)

    opp1 = (380, 940)
    opp2 = (780, 920)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
    {get_defs()}
    <rect width="{W}" height="{H}" fill="#0b131f" />
    {get_base_pitch()}

    <!-- Header Banner -->
    <rect x="0" y="0" width="{W}" height="120" fill="#0f172a" />
    <rect x="60" y="24" width="8" height="72" fill="#4ade80" rx="4" />
    <text x="85" y="62" font-size="34" font-weight="900" fill="#ffffff" font-family="'Microsoft YaHei', sans-serif">七人制战术图解 02 ｜ 后场破高压逼抢与门将“+1”出球</text>
    <text x="85" y="96" font-size="18" font-weight="bold" fill="#94a3b8" font-family="'Microsoft YaHei', sans-serif">【实战战术】 门将+双中卫+后腰形成出球菱形 ｜ 面对对手前场紧逼的三大逃生通道</text>

    <!-- Build-up Diamond Zone (fill=none) -->
    <polygon points="{gk[0]},{gk[1]} {lcb[0]},{lcb[1]} {cm[0]},{cm[1]} {rcb[0]},{rcb[1]}" fill="none" stroke="#4ade80" stroke-width="3.5" stroke-dasharray="10,8" />
    
    <rect x="460" y="990" width="280" height="38" rx="8" fill="#0f172a" stroke="#4ade80" stroke-width="2" />
    <text x="600" y="1016" font-size="20" font-weight="bold" fill="#4ade80" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">后场控球菱形 (+1 超载)</text>

    <!-- Route A -->
    <path d="M {gk[0]-40} {gk[1]-20} L {lcb[0]+40} {lcb[1]+20}" fill="none" stroke="#4ade80" stroke-width="5" marker-end="url(#arrowGreen)" />
    <path d="M {lcb[0]} {lcb[1]-50} L {lm[0]+20} {lm[1]+50}" fill="none" stroke="#4ade80" stroke-width="5" marker-end="url(#arrowGreen)" />
    <rect x="90" y="780" width="180" height="34" rx="6" fill="#0f172a" stroke="#4ade80" stroke-width="2" />
    <text x="180" y="804" font-size="17" font-weight="bold" fill="#4ade80" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">路线A：顺线直塞</text>

    <!-- Route B -->
    <path d="M {lcb[0]+45} {lcb[1]} Q {gk[0]-80} {gk[1]-120} {gk[0]-10} {gk[1]-45}" fill="none" stroke="#facc15" stroke-width="5" marker-end="url(#arrowYellow)" />
    <path d="M {gk[0]+20} {gk[1]-35} Q {gk[0]+120} {gk[1]-140} {rcb[0]-35} {rcb[1]}" fill="none" stroke="#facc15" stroke-width="5" marker-end="url(#arrowYellow)" />
    <rect x="510" y="1120" width="180" height="34" rx="6" fill="#0f172a" stroke="#facc15" stroke-width="2" />
    <text x="600" y="1144" font-size="17" font-weight="bold" fill="#facc15" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">路线B：回敲倒弱侧</text>

    <!-- Route C -->
    <path d="M {gk[0]+35} {gk[1]-45} Q {rcb[0]+100} 700 {st[0]+35} {st[1]+60}" fill="none" stroke="#fb923c" stroke-width="5" stroke-dasharray="12,8" marker-end="url(#arrowOrange)" />
    <rect x="850" y="700" width="190" height="34" rx="6" fill="#0f172a" stroke="#fb923c" stroke-width="2" />
    <text x="945" y="724" font-size="17" font-weight="bold" fill="#fb923c" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">路线C：过顶打纵深</text>

    <!-- Opponent Press Arrows -->
    <path d="M {opp1[0]-10} {opp1[1]+30} L {lcb[0]+30} {lcb[1]-35}" fill="none" stroke="#ef4444" stroke-width="4" stroke-dasharray="6,6" marker-end="url(#arrowRed)" />
    <path d="M {opp2[0]+10} {opp2[1]+30} L {rcb[0]-30} {rcb[1]-35}" fill="none" stroke="#ef4444" stroke-width="4" stroke-dasharray="6,6" marker-end="url(#arrowRed)" />

    <!-- Opponents -->
    {render_player(opp1[0], opp1[1], "9", "对方逼抢", "red")}
    {render_player(opp2[0], opp2[1], "10", "对方逼抢", "red")}

    <!-- Players -->
    {render_player(gk[0], gk[1], "1", "门将 GK", "gk")}
    {render_player(lcb[0], lcb[1], "2", "左中卫 LCB", "white")}
    {render_player(rcb[0], rcb[1], "3", "右中卫 RCB", "white")}
    {render_player(cm[0], cm[1], "6", "核心中场 CM", "white")}
    {render_player(lm[0], lm[1], "7", "左边中场 LM", "white")}
    {render_player(rm[0], rm[1], "11", "右边中场 RM", "white")}
    {render_player(st[0], st[1], "9", "中锋 ST", "white")}

    <rect x="40" y="1350" width="{W-80}" height="300" rx="16" fill="#0f172a" stroke="rgba(255,255,255,0.3)" stroke-width="2" />
    <text x="80" y="1395" font-size="24" font-weight="900" fill="#4ade80" font-family="'Microsoft YaHei', sans-serif">🚀 后场破紧逼三原则与逃生口令</text>
    
    <text x="80" y="1440" font-size="19" fill="#f8fafc" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#4ade80">① 路线 A（顺线直推）：</tspan> 双中卫拉开至禁区角外侧接门将传球，若身前有空当，一脚顺给拉边中场。
    </text>
    <text x="80" y="1485" font-size="19" fill="#f8fafc" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#facc15">② 路线 B（回敲倒弱侧）：</tspan> 边后卫受迫绝不勉强转身！<tspan fill="#38bdf8">果断回敲门将</tspan>，门将单触直接转移到弱侧大空当中卫。
    </text>
    <text x="80" y="1530" font-size="19" fill="#f8fafc" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#fb923c">③ 路线 C（过顶致命球）：</tspan> 对手全队上压人盯人时，中卫/门将直接送过顶长传找中锋 #9 冲击身后空当。
    </text>
    <text x="80" y="1585" font-size="19" font-weight="bold" fill="#facc15" font-family="'Microsoft YaHei', sans-serif">
      🗣️ 场上呼应口号：“身后有人一脚回！门将就是多一人！拉开宽度倒弱侧！”
    </text>
    </svg>'''
    return svg

# ==========================================
# CARD 3: 前场三大进攻套路 (Attacking Patterns)
# ==========================================
def build_card_3():
    st = (600, 320)
    lm = (240, 480)
    rm = (960, 480)
    cm = (600, 640)
    lcb = (360, 920)
    rcb = (840, 920)

    opp_cb = (560, 380)
    opp_rb = (320, 420)
    opp_lb = (880, 420)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
    {get_defs()}
    <rect width="{W}" height="{H}" fill="#0b131f" />
    {get_base_pitch()}

    <!-- Header Banner -->
    <rect x="0" y="0" width="{W}" height="120" fill="#0f172a" />
    <rect x="60" y="24" width="8" height="72" fill="#f59e0b" rx="4" />
    <text x="85" y="62" font-size="34" font-weight="900" fill="#ffffff" font-family="'Microsoft YaHei', sans-serif">七人制战术图解 03 ｜ 前场 30 米破密集三大杀手锏</text>
    <text x="85" y="96" font-size="18" font-weight="bold" fill="#94a3b8" font-family="'Microsoft YaHei', sans-serif">【进攻套路】 撞墙二过一 ｜ 第三人下底渗透 ｜ 强侧超载与对角弱侧大转移</text>

    <!-- Pattern 1 -->
    <g>
      <path d="M {lm[0]+35} {lm[1]-20} L {st[0]-45} {st[1]+20}" fill="none" stroke="#facc15" stroke-width="5" marker-end="url(#arrowYellow)" />
      <path d="M {st[0]-35} {st[1]+10} L {lm[0]+120} {lm[1]-180}" fill="none" stroke="#facc15" stroke-width="5" marker-end="url(#arrowYellow)" />
      <path d="M {lm[0]} {lm[1]-45} Q {lm[0]+50} {lm[1]-120} {lm[0]+110} {lm[1]-170}" fill="none" stroke="#ffffff" stroke-width="4.5" stroke-dasharray="8,6" marker-end="url(#arrowWhite)" />
      <rect x="90" y="230" width="180" height="34" rx="6" fill="#0f172a" stroke="#facc15" stroke-width="2" />
      <text x="180" y="254" font-size="17" font-weight="bold" fill="#facc15" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">① 撞墙二过一</text>
    </g>

    <!-- Pattern 2 -->
    <g>
      <path d="M {cm[0]} {cm[1]-45} L {st[0]} {st[1]+48}" fill="none" stroke="#38bdf8" stroke-width="5" marker-end="url(#arrowCyan)" />
      <path d="M {st[0]+25} {st[1]+20} L {st[0]+160} {st[1]-60}" fill="none" stroke="#38bdf8" stroke-width="5" marker-end="url(#arrowCyan)" />
      <path d="M {rm[0]-35} {rm[1]-20} Q {rm[0]-140} {rm[1]-100} {st[0]+150} {st[1]-50}" fill="none" stroke="#ffffff" stroke-width="4.5" stroke-dasharray="8,6" marker-end="url(#arrowWhite)" />
      <rect x="710" y="220" width="180" height="34" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
      <text x="800" y="244" font-size="17" font-weight="bold" fill="#38bdf8" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">② 第三人插肋部</text>
    </g>

    <!-- Pattern 3 -->
    <g>
      <path d="M {lcb[0]-20} {lcb[1]-40} Q 600 500 {rm[0]-25} {rm[1]+50}" fill="none" stroke="#ef4444" stroke-width="5" stroke-dasharray="12,8" marker-end="url(#arrowRed)" />
      <rect x="470" y="540" width="260" height="34" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="2" />
      <text x="600" y="564" font-size="17" font-weight="bold" fill="#ef4444" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">③ 强侧倒脚，大范围转弱侧</text>
    </g>

    {render_player(opp_cb[0], opp_cb[1], "4", "对方中卫", "red")}
    {render_player(opp_rb[0], opp_rb[1], "2", "对方右后卫", "red")}
    {render_player(opp_lb[0], opp_lb[1], "3", "对方左后卫", "red")}

    {render_player(lcb[0], lcb[1], "2", "左中卫 LCB", "white")}
    {render_player(rcb[0], rcb[1], "3", "右中卫 RCB", "white")}
    {render_player(cm[0], cm[1], "6", "核心中场 CM", "white")}
    {render_player(lm[0], lm[1], "7", "左边中场 LM", "white")}
    {render_player(rm[0], rm[1], "11", "右边中场 RM", "white")}
    {render_player(st[0], st[1], "9", "中锋 ST", "white")}

    <rect x="40" y="1350" width="{W-80}" height="300" rx="16" fill="#0f172a" stroke="rgba(255,255,255,0.3)" stroke-width="2" />
    <text x="80" y="1395" font-size="24" font-weight="900" fill="#f59e0b" font-family="'Microsoft YaHei', sans-serif">🎯 前场破密集三大配合要决</text>
    
    <text x="80" y="1440" font-size="19" fill="#f8fafc" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#facc15">① 撞墙配合（One-Two）：</tspan> 边中场交球给中锋后，<tspan fill="#38bdf8">必须无球全速前插</tspan>！中锋不用停球，单触轻推身后。
    </text>
    <text x="80" y="1485" font-size="19" fill="#f8fafc" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#38bdf8">② 第三人跑位（Third-Man）：</tspan> 中场找中锋吸引防守，弱侧边路/后插上中场内切杀入禁区肋部单刀。
    </text>
    <text x="80" y="1530" font-size="19" fill="#f8fafc" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#ef4444">③ 弱侧对角大转移（Switch）：</tspan> 强侧 3 人连续小短传压迫对手防线，突然起脚大对角找完全空置的弱侧边路。
    </text>
    <text x="80" y="1585" font-size="19" font-weight="bold" fill="#facc15" font-family="'Microsoft YaHei', sans-serif">
      💡 终结铁律：传球后严禁站在原地当观众，出球瞬间必须完成 1~2 个后插上接应点！
    </text>
    </svg>'''
    return svg

# ==========================================
# CARD 4: 攻防转换与三动作体系 (Transitions & 3-Action System)
# ==========================================
def build_card_4():
    lost_ball_pos = (400, 480)
    p1 = (350, 520)
    p2 = (450, 430)
    cm = (550, 680)
    lcb = (360, 920)
    rcb = (800, 920)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
    {get_defs()}
    <rect width="{W}" height="{H}" fill="#0b131f" />
    {get_base_pitch()}

    <!-- Header Banner -->
    <rect x="0" y="0" width="{W}" height="120" fill="#0f172a" />
    <rect x="60" y="24" width="8" height="72" fill="#ef4444" rx="4" />
    <text x="85" y="62" font-size="34" font-weight="900" fill="#ffffff" font-family="'Microsoft YaHei', sans-serif">七人制战术图解 04 ｜ 攻防转换铁律与“三动作”实战执行</text>
    <text x="85" y="96" font-size="18" font-weight="bold" fill="#94a3b8" font-family="'Microsoft YaHei', sans-serif">【转换与习惯】 丢球 5 秒就地围抢 ｜ 断球 3 秒垂直推进 ｜ 传球“前-主-后”三动作</text>

    <!-- Top Section: Gegenpress 5s Rule -->
    <g>
      <!-- Pressure Zone Circle (fill=none) -->
      <circle cx="{lost_ball_pos[0]}" cy="{lost_ball_pos[1]}" r="140" fill="none" stroke="#ef4444" stroke-width="3.5" stroke-dasharray="8,6" />
      
      <rect x="{lost_ball_pos[0]-140}" y="{lost_ball_pos[1]-115}" width="280" height="34" rx="6" fill="#0f172a" stroke="#ef4444" stroke-width="2" />
      <text x="{lost_ball_pos[0]}" y="{lost_ball_pos[1]-92}" font-size="18" font-weight="900" fill="#ef4444" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">丢球 5 秒反抢区 (2人合围)</text>
      
      <!-- Ball marker -->
      <circle cx="{lost_ball_pos[0]}" cy="{lost_ball_pos[1]}" r="14" fill="#ffffff" stroke="#000" stroke-width="3" />
      
      <!-- Press Arrows -->
      <path d="M {p1[0]} {p1[1]} L {lost_ball_pos[0]-28} {lost_ball_pos[1]+15}" fill="none" stroke="#facc15" stroke-width="5" marker-end="url(#arrowYellow)" />
      <path d="M {p2[0]} {p2[1]} L {lost_ball_pos[0]+22} {lost_ball_pos[1]-20}" fill="none" stroke="#facc15" stroke-width="5" marker-end="url(#arrowYellow)" />
      
      <path d="M {cm[0]} {cm[1]} L 600 780" fill="none" stroke="#38bdf8" stroke-width="4.5" stroke-dasharray="6,6" marker-end="url(#arrowCyan)" />
      <path d="M {rcb[0]} {rcb[1]} L 680 940" fill="none" stroke="#38bdf8" stroke-width="4.5" stroke-dasharray="6,6" marker-end="url(#arrowCyan)" />
      
      <rect x="520" y="840" width="340" height="34" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="2" />
      <text x="690" y="863" font-size="16" font-weight="bold" fill="#38bdf8" text-anchor="middle" font-family="'Microsoft YaHei', sans-serif">其余人员迅速向中轴线收缩卡位</text>
    </g>

    {render_player(lost_ball_pos[0]+15, lost_ball_pos[1]+10, "10", "对方持球", "red")}
    {render_player(p1[0], p1[1], "7", "就近逼抢", "white")}
    {render_player(p2[0], p2[1], "9", "就近逼抢", "white")}
    {render_player(cm[0], cm[1], "6", "核心中场 CM", "white")}
    {render_player(lcb[0], lcb[1], "2", "左中卫 LCB", "white")}
    {render_player(rcb[0], rcb[1], "3", "右中卫 RCB", "white")}

    <!-- Bottom Instruction Card -->
    <rect x="40" y="1060" width="{W-80}" height="580" rx="16" fill="#0f172a" stroke="rgba(255,255,255,0.3)" stroke-width="2" />
    
    <text x="80" y="1105" font-size="24" font-weight="900" fill="#ef4444" font-family="'Microsoft YaHei', sans-serif">⏱️ 攻防转换黄金时间法则</text>
    <text x="80" y="1145" font-size="19" fill="#f8fafc" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#ef4444">🔴 丢球瞬间（5 秒反抢法则）：</tspan> 离球最近的 2 人立即就地疯抢持球人，其余队员不看球，全速向中轴线回撤落位。
    </text>
    <text x="80" y="1185" font-size="19" fill="#f8fafc" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#4ade80">🟢 断球瞬间（3 秒反击法则）：</tspan> 第一脚绝不横传粘球！直接垂直找前锋 ST #9，或分给弱侧全速插上的边中场。
    </text>

    <!-- 3-Action Box -->
    <rect x="70" y="1220" width="{W-140}" height="280" rx="12" fill="#1e293b" stroke="#38bdf8" stroke-width="2" />
    <text x="95" y="1260" font-size="22" font-weight="900" fill="#38bdf8" font-family="'Microsoft YaHei', sans-serif">🧠 德国足球经典“三动作体系”（养成肌肉记忆）</text>
    
    <text x="95" y="1305" font-size="18" fill="#ffffff" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#facc15">1. 前动作（Pre-Action）：</tspan> 接球前 1 秒<tspan fill="#38bdf8">必须回头观察防守人距离（Scan）</tspan>；保持半侧身开放身体朝向。
    </text>
    <text x="95" y="1350" font-size="18" fill="#ffffff" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#facc15">2. 主要动作（Main Action）：</tspan> 用远离防守队员的脚触球出球；控制球速贴地坚决，眼神可带假动作。
    </text>
    <text x="95" y="1395" font-size="18" fill="#ffffff" font-family="'Microsoft YaHei', sans-serif">
      <tspan font-weight="bold" fill="#facc15">3. 后动作（Post-Action）：</tspan> <tspan fill="#ef4444">严禁出球后站在原地看！</tspan> 0.5 秒内必须二次启动前插、套边或形成保护。
    </text>
    <text x="95" y="1450" font-size="18" font-weight="bold" fill="#4ade80" font-family="'Microsoft YaHei', sans-serif">
      📢 场上核心口令：“接球先看！出球即跑！丢球就抢！断球直塞！”
    </text>
    </svg>'''
    return svg

cards = [
    ("card1_formation_hd.png", build_card_1()),
    ("card2_buildup_hd.png", build_card_2()),
    ("card3_attacking_hd.png", build_card_3()),
    ("card4_transitions_hd.png", build_card_4())
]

for name, svg_code in cards:
    out_path = os.path.join(target_dir, name)
    doc = fitz.open("svg", svg_code.encode("utf-8"))
    pix = doc[0].get_pixmap(dpi=150)
    pix.save(out_path)
    print(f"Successfully rendered: {out_path} ({pix.width}x{pix.height})")

print("ALL_FIXED_AND_RENDERED")
