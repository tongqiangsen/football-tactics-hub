# ⚽ Football Tactics Hub · 现代足球战术教研交互沙盘与战情中枢

[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](LICENSE)
[![GitHub Repo](https://img.shields.io/badge/GitHub-tongqiangsen%2Ffootball--tactics--hub-181717.svg?logo=github)](https://github.com/tongqiangsen/football-tactics-hub)
[![Zero-Dependency](https://img.shields.io/badge/Frontend-Vanilla_JS_%26_CSS3-blue.svg)](football_tactics_hub.html)
[![Single-File Offline](https://img.shields.io/badge/Deploy-Single--File_Offline-success.svg)](football_tactics_hub.html)
[![Architecture: German Passing System](https://img.shields.io/badge/Doctrine-German_Tactical_System-amber.svg)](README.md)

一套面向现代足球教练员、战术分析师与足球爱好者的**数字化战术沙盘与多媒体教研工作台**。

项目融合欧洲现代传控理念与德国足球传球战术训练体系，提供**全离线、零外部依赖、响应式交互**的单文件战情中枢（Tactical Hub）与全彩战术演练讲义（Tactics Deck），内嵌全量高帧率沙盘战术动图与阵型球员职责时序步进器。

---

## 🌟 核心特性 (Key Features)

### 1. 现代化极简战情中枢 (`football_tactics_hub.html`)
- **超轻量与极速秒开**：纯原生 HTML5/CSS3/Vanilla JS 构建，采用轻量化异步动图解耦架构（HTML 仅约 120KB，较传统 Base64 内嵌方案体积缩减 98%），首屏 10ms 极速呈现，动图按需流式加载；同时保留一键生成纯离线单文件 Bundle 的能力。无需任何 Node.js 构建链或后端服务。
- **三套护眼设计系统**：
  - 🌿 **战术深邃绿**（默认极夜护眼深绿）
  - 📋 **明亮战术白板**（教研会议与日间复盘高对比高清晰度白板）
  - 🌃 **深空暗夜灰**（极简低饱和护眼暗色）
  - 支持快捷键 `T` 一键无缝切换，状态自动持久化至 `localStorage`。
- **专业级排版与视觉降噪**：采用 Linear / Apple HIG 设计语言，建立严谨的 8px 空间基线、清晰字阶与无边框面层次对比，彻底消除视觉杂乱感。

### 2. 8 大现代进攻流派交互矩阵 (Module 02)
- 涵盖**第三人渗透 (Third-Man)**、**弱侧大转移 (Switch Play)**、**身后过顶球 (Over the Top)**、**5秒反击闪电战 (5s Counter-Blitz)**、**高点支点轰炸 (Target Man)**、**倒三角推杆 (Cut-back)**、**漏球假动作 (Dummy)** 与**战术界外球 (Tactical Throw-in)**。
- 支持按渗透传切、快速转换、边路倒三角、定位球与奇袭 4 大场景多维度标签过滤。

### 3. 20 项进攻传球武器库 (Module 03)
- 20 个独立攻防战术武器卡片，**每项武器配备 100% 独立沙盘动图**，涵盖：
  - 纵深刺穿类（贴地直塞、挑传过顶、穿透性激光球等）
  - 边路终结类（下底倒三角、低平速射弧线等）
  - 节奏掌控类（撞墙配合、回敲二过一、重置回流球等）
  - 欺骗与非常规类（假射真传、不看人传球、战术漏球等）
  - 现代门将武器（出击门将穿透性低平长传）
- 配备全屏高清灯箱（Lightbox）与动画逐帧观察。

### 4. 动态战术画板与球员职责时序步进器 (Module 04)
- 支持主流赛制阵型动态热切换：
  - **7人制 1-2-3-1**（传控主导 / 局部三角压迫）
  - **7人制 1-3-2-1**（防守反击 / 中路高韧性锁死）
  - **8人制 1-3-3-1**（边路叠瓦 / 宽度极致展开）
- **全场 22 个战术号位交互看板**：点击球场任意球员节点，动态调取该位置的核心战术使命、接球前/处理时/出球后 **3 步行动规范 (3-Action Guide)**、推荐传球武器库及比赛现场口令。

### 5. 临场破局方案库与 8 大战术口令 (Module 05)
- 针对 4 种典型被动战局（高位逼抢受阻、深度铁桶阵、中场失控、体能临界期）给出立竿见影的破局解法。
- 提炼 8 条通俗有力的场上统一指令（如“别看球，看人背后！”、“转弱侧，空间在对面！”）。

### 6. 20 页全彩互动演示文稿 (`football_tactics_deck.html`)
- 专为更衣室赛前动员、赛后复盘及战术研讨会打造的演示 Deck。
- 支持全屏翻页、快捷导航、主题无缝联动与重点内容同态展现。

---

## 📂 项目结构 (Repository Layout)

```text
Football-Tactics-Hub/
├── football_tactics_hub.html         # [核心] 现代足球战术战情室 (单文件独立离线版)
├── football_tactics_deck.html        # [演示] 20页战术研讨演示文稿 Deck
│
├── build_tactical_hub.py             # 战情室打包编译器 (将动图与组件打包为单文件 HTML)
├── build_full_tactics_deck.py        # 演示讲义编译器 (将讲义内容与资产打包为独立 Deck)
│
├── generate_tactics_gifs.py          # 基础战术沙盘动图生成引擎 (基于 PIL / 60fps 逻辑)
├── generate_missing_weapons_gifs.py  # 进阶攻防武器专属动图生成引擎
│
├── tactics_animations_gif/           # 战术动图核心资产库 (20+ 独立沙盘 GIF)
│   ├── anim_01_third_man.gif
│   ├── anim_02_switch_play.gif
│   ├── anim_w01_through_ball.gif
│   └── ...
│
├── tactics_cards_hd/                 # 高清 4K 战术板切片图 (PNG 格式)
│   ├── card_01_doctrines_8.png
│   ├── card_02_weapons_20.png
│   └── ...
│
├── .gitignore                        # Git 忽略配置 (排除大体积版权 PDF 及编译缓存)
├── LICENSE                           # 开源许可证 (MIT)
└── README.md                         # 项目主说明文档
```

---

## 🚀 快速上手 (Quick Start)

### 方式一：直接在浏览器中打开（推荐）
本项目编译产物 `football_tactics_hub.html` 和 `football_tactics_deck.html` 为**自洽单文件**，无需任何运行环境：
1. 克隆或下载本仓库；
2. 双击 `football_tactics_hub.html` 打开战情室主控台；
3. 双击 `football_tactics_deck.html` 打开交互式战术演示课件。

### 方式二：二次开发与本地重新构建
如需修改战术动图逻辑或扩展全新战术模块，可使用 Python 脚本进行重新渲染与编译：

#### 1. 安装基础依赖
```bash
pip install pillow
```

#### 2. 重新渲染战术沙盘动图
```bash
# 渲染基础流派动图
python generate_tactics_gifs.py

# 渲染武器库专属动图
python generate_missing_weapons_gifs.py
```

#### 3. 编译打包单文件 HTML
```bash
# 编译打包战情中枢
python build_tactical_hub.py

# 编译打包战术演讲课件
python build_full_tactics_deck.py
```

---

## 📚 理论根基与战术文献致敬 (Tactical References)

本项目战术理论与沙盘图解体系汲取并致敬以下经典足球技战术文献：
1. **《足球训练完全图解：德国足球传球战术及训练（全彩图解版）》**
   - 德国足协（DFB）官方青训传球训练法体系；
   - 三角站位原则、身体朝向（Body Orientation）、第一触球（First Touch）与传球权分配。
2. **乔纳森·威尔逊（Jonathan Wilson）《倒转金字塔：足球战术史》 (Inverting The Pyramid)**
   - 空间争夺史、高位压迫反击（Gegenpressing）机制、伪九号与肋部（Half-spaces）空间利用。

*(注：为尊重图书版权并保持 GitHub 仓库精简高效，参考电子书扫描版不纳入 Git 仓库版本控制)*

---

## 🛠️ 开源演进路线图 (Roadmap)

我们计划在后续的 GitHub 版本迭代中持续优化并引入以下功能：

- [ ] **交互式自由战术画板 (Canvas / SVG Drag & Drop)**：支持教练员自由拖拽球员、绘制传跑折线并导出战术板切片。
- [ ] **战术序列动画时间轴编辑器**：允许用户自定义传球帧时序、跑位路径与防守球员响应。
- [ ] **比赛视频与剪辑片段内嵌联动**：支持关联实际比赛视频时间戳（如曼城、皇马、拜仁典型战例）。
- [ ] **多语言国际化 (i18n)**：增加英文（English）与德文（Deutsch）专业术语支持。
- [ ] **移动端手势与平板手写笔优化**：适配 iPad / Android 平板端教练员现场画图体验。

---

## 📄 开源许可证 (License)

本项目采用 [MIT License](LICENSE) 开源。欢迎广大教练员、战术分析师与开发者共同贡献与完善！
