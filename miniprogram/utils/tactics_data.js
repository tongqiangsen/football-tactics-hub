/**
 * Football Tactics Hub - Core Tactics Data Store
 * Cross-platform data source for Standalone Web, Mobile Viewports, and WeChat Mini Programs.
 */
(function(global) {
  const tacticsData = {
  "metadata": {
    "title": "现代足球战术教研交互沙盘与战情中枢",
    "version": "2.0.0",
    "doctrine": "German Passing System (德系传控战术体系)"
  },
  "foundations": {
    "mistakes": "只看脚下、静态站立等球、单打独斗盲目推进、在密集区以少打多扎堆。",
    "truths": "传球即人际语言；球永远比人跑得快；通过三角站位制造局部 3v2；传向空当而非脚下。",
    "ironRules": [
      "1. 后场中路绝不盲目横传",
      "2. 保持开放半侧身面向前场",
      "3. 接球前 0.5 秒完成盲区扫描"
    ],
    "gridPrinciple": "同一方格内严禁出现两名本方队员；全队保持 5~10 米黄金呼应间距，形成菱形与三角形接应网。"
  },
  "doctrines": [
    {
      "id": "d01",
      "num": "01",
      "title": "流派① · 第三人跑位渗透 (Up-Back-Through)",
      "category": "penetration",
      "tag": "地面渗透破密集",
      "gif": "tactics_animations_gif/anim_01_third_man.gif",
      "steps": "后腰(4)直塞背身中锋(7)[Up] ➔ 中锋回做中场(6)[Back] ➔ 中场顺势直塞高速前插的第三人(5)单刀破门[Through]！",
      "weapons": ["w01", "w06", "w07", "w08"]
    },
    {
      "id": "d02",
      "num": "02",
      "title": "流派② · 强侧超载 ➔ 弱侧 1v1 转移",
      "category": "flank",
      "tag": "宽度调度破铁桶",
      "gif": "tactics_animations_gif/anim_02_switch_play.gif",
      "steps": "强侧左路连续短传吸附防线整体横移 ➔ 中场(6)突然起 30 米大对角斜长传 ➔ 弱侧右翼(7)在巨大无人空当内突入禁区！",
      "weapons": ["w09", "w10", "w11"]
    },
    {
      "id": "d03",
      "num": "03",
      "title": "流派③ · 纵深越顶反越位突袭",
      "category": "transition",
      "tag": "反高位压迫利器",
      "gif": "tactics_animations_gif/anim_08_over_the_top.gif",
      "steps": "对手整体压上高位逼抢身后留 25 米空当 ➔ 中卫(3)送出精准过顶挑传 ➔ 中锋(7)从防守盲区反越位超车单刀垫射破门！",
      "weapons": ["w01", "w02", "w18"]
    },
    {
      "id": "d04",
      "num": "04",
      "title": "流派④ · 攻防转换5秒快攻闪击",
      "category": "transition",
      "tag": "就地反抢闪电战",
      "gif": "tactics_animations_gif/anim_09_5s_counter_blitz.gif",
      "steps": "丢球 0.5s 内边翼(5)与前锋(7)就地合围断球 ➔ 立即刺穿直塞插上中场(6) ➔ 5 秒 3 脚内横推空门得手！",
      "weapons": ["w07", "w17", "w18"]
    },
    {
      "id": "d05",
      "num": "05",
      "title": "流派⑤ · 立体空战中锋胸部做球",
      "category": "penetration",
      "tag": "破中场绞杀支点",
      "gif": "tactics_animations_gif/anim_10_target_man_aerial.gif",
      "steps": "后场起高球避开地面惨烈绞杀 ➔ 突前中锋(7)背身扛人胸部稳卸回做 ➔ 中场(6)禁区弧顶迎球不停球直接重炮轰门！",
      "weapons": ["w02", "w06", "w14"]
    },
    {
      "id": "d06",
      "num": "06",
      "title": "流派⑥ · 禁区底线倒三角终结",
      "category": "flank",
      "tag": "第一进球概率武器",
      "gif": "tactics_animations_gif/anim_04_cut_back.gif",
      "steps": "边锋(7)突至底线迫使门将与防线退缩门线 ➔ 底线发力贴地倒三角推向点球点 ➔ 后插上中场(6)推射大半个空门！",
      "weapons": ["w03", "w04", "w08"]
    },
    {
      "id": "d07",
      "num": "07",
      "title": "流派⑦ · 迎球假接真漏特种破局",
      "category": "setpiece",
      "tag": "节奏欺骗破坏预判",
      "gif": "tactics_animations_gif/anim_11_dummy_let_through.gif",
      "steps": "后腰(4)直塞中场(6) ➔ 中场假装接球瞬间突然叉腿漏球 ➔ 防守完全被假动作扑空，身后的中锋(7)单刀得手！",
      "weapons": ["w13", "w14", "w16"]
    },
    {
      "id": "d08",
      "num": "08",
      "title": "流派⑧ · 战术手抛界外球三角配合",
      "category": "setpiece",
      "tag": "死球重开转反击",
      "gif": "tactics_animations_gif/anim_12_tactical_throwin.gif",
      "steps": "边卫(2)精准掷前锋(7)脚下 ➔ 前锋一脚回敲，边卫高速套边下底 ➔ 底线平抽横扫门前，包抄中场(6)抢点破门！",
      "weapons": ["w03", "w04", "w20"]
    }
  ],
  "weaponCategories": [
    { "id": 1, "name": "分类一：穿透与终结 (W01-W04)" },
    { "id": 2, "name": "分类二：破压与渗透 (W05-W08)" },
    { "id": 3, "name": "分类三：宽度与调度 (W09-W12)" },
    { "id": 4, "name": "分类四：隐蔽与特种 (W13-W16)" },
    { "id": 5, "name": "分类五：现代与死球 (W17-W20)" }
  ],
  "weapons": {
    "1": [
      {
        "id": "w01",
        "num": "W 01",
        "name": "直塞穿透球",
        "en": "Through Ball",
        "tag": "贴地发力 · 刺穿中卫结合部",
        "gif": "tactics_animations_gif/anim_w01_through_ball.gif",
        "desc": "脚内侧或正脚背贴地快速刺穿两条防线之间的结合部空当；给足前锋前插提前量，让队友冲刺接球单刀。",
        "callout": "📢 场上实战口令：“给身后！”"
      },
      {
        "id": "w02",
        "num": "W 02",
        "name": "肋部挑传空当",
        "en": "Chipped Through",
        "tag": "脚尖搓挑 · 越过防线头顶",
        "gif": "tactics_animations_gif/anim_w02_chipped_through.gif",
        "desc": "脚尖快速搓入皮球底部制造回旋，使球迅速跃过密集防守头顶，落入肋部无人区并减速停稳。",
        "callout": "📢 场上实战口令：“挑肋部！”"
      },
      {
        "id": "w03",
        "num": "W 03",
        "name": "底线倒三角回传",
        "en": "Cut-Back Pass",
        "tag": "下底压缩门线 · 推向点球点",
        "gif": "tactics_animations_gif/anim_04_cut_back.gif",
        "desc": "边路下底迫使防守队员与门将退缩门线，随后发力贴地推向点球点到禁区线之间的巨大真空区。",
        "callout": "📢 场上实战口令：“倒三角！”"
      },
      {
        "id": "w04",
        "num": "W 04",
        "name": "贴地横扫传中",
        "en": "Driven Low Cross",
        "tag": "平抽门前走廊 · 抢前点垫射",
        "gif": "tactics_animations_gif/anim_w04_driven_cross.gif",
        "desc": "脚内侧发力平抽门前危险走廊，球速极快，专打后卫转身困难，供前锋抢前点折射或制造乌龙。",
        "callout": "📢 场上实战口令：“前点平抽！”"
      }
    ],
    "2": [
      {
        "id": "w05",
        "num": "W 05",
        "name": "二过一撞墙配合",
        "en": "Wall Pass / 1-2",
        "tag": "传球即启动 · 借墙过人",
        "gif": "tactics_animations_gif/anim_03_wall_pass.gif",
        "desc": "斜传中锋瞬间全速插上，中锋作为“墙”一脚顺势回弹其跑动路线上，瞬间超车防守形成单刀。",
        "callout": "📢 场上实战口令：“撞墙！”"
      },
      {
        "id": "w06",
        "num": "W 06",
        "name": "迎前回敲做球",
        "en": "Lay-off Pass",
        "tag": "背身接应 · 软推二梯队",
        "gif": "tactics_animations_gif/anim_w06_layoff_pass.gif",
        "desc": "前锋迎球背身一脚轻推给面向前场的插上中场，出球要软、球速温和，方便队友迎球不停球直接打门。",
        "callout": "📢 场上实战口令：“回敲！”"
      },
      {
        "id": "w07",
        "num": "W 07",
        "name": "刺穿线形传球",
        "en": "Line-Breaking Laser",
        "tag": "正脚背重炮 · 瞬间刺穿双线",
        "gif": "tactics_animations_gif/anim_w07_line_breaking.gif",
        "desc": "脚背正中发力贴地重炮直塞，像激光一样直接打穿对方锋线与中场线，送至前腰脚下。",
        "callout": "📢 场上实战口令：“穿透线！”"
      },
      {
        "id": "w08",
        "num": "W 08",
        "name": "第三人导向球",
        "en": "Up-Back-Through",
        "tag": "A传B ➔ B敲C ➔ C直塞D",
        "gif": "tactics_animations_gif/anim_01_third_man.gif",
        "desc": "破解密集防守的第一绝技。利用持球人 A 和支点 B 吸引防守，由前瞻者 C 一脚送给盲区杀出的第三人 D。",
        "callout": "📢 场上实战口令：“看第三人！”"
      }
    ],
    "3": [
      {
        "id": "w09",
        "num": "W 09",
        "name": "大范围对角长传",
        "en": "Diagonal Switch",
        "tag": "30米斜长传 · 强侧转弱侧",
        "gif": "tactics_animations_gif/anim_02_switch_play.gif",
        "desc": "脚背内侧搓出 30 米以上高速斜长传，从密集强侧瞬间转移至弱侧空当，制造 1v1 或无人传中。",
        "callout": "📢 场上实战口令：“弱侧弱侧！”"
      },
      {
        "id": "w10",
        "num": "W 10",
        "name": "边线贴地推进球",
        "en": "Channel Pass",
        "tag": "紧贴边线直推 · 边卫连线边锋",
        "gif": "tactics_animations_gif/anim_w10_channel_pass.gif",
        "desc": "边后卫破逼抢的第一选择，紧贴边线外侧贴地直塞，避开中路封堵，直接给边锋启动。",
        "callout": "📢 场上实战口令：“走边线！”"
      },
      {
        "id": "w11",
        "num": "W 11",
        "name": "弧线绕顶传球",
        "en": "Curled Around Block",
        "tag": "外侧强侧旋 · 绕过防守封锁",
        "gif": "tactics_animations_gif/anim_w_cat3_curled.gif",
        "desc": "在中路直线被完全封死时，脚内侧带强侧旋踢出弧线，球绕过防守队员身体外侧进入肋部空当。",
        "callout": "📢 场上实战口令：“绕外侧！”"
      },
      {
        "id": "w12",
        "num": "W 12",
        "name": "回传重新组织球",
        "en": "Recycling / Reset",
        "tag": "拒绝盲目对抗 · 重置进攻面",
        "gif": "tactics_animations_gif/anim_w12_recycling.gif",
        "desc": "前场无突破机会时果断回敲中卫或门将，全队阵型横向展开，重新寻找薄弱防线，绝不死带失误。",
        "callout": "📢 场上实战口令：“回传重来！”"
      }
    ],
    "4": [
      {
        "id": "w13",
        "num": "W 13",
        "name": "不看人隐蔽传球",
        "en": "No-Look Pass",
        "tag": "眼神向左 · 脚腕向右",
        "gif": "tactics_animations_gif/anim_w13_no_look.gif",
        "desc": "身体朝向与视线完全看向左路吸引防守重心，出球瞬间脚腕抖动向右出球，彻底破坏后卫预判。",
        "callout": "📢 场上实战口令：“声东击西！”"
      },
      {
        "id": "w14",
        "num": "W 14",
        "name": "假射真传/节奏差",
        "en": "Fake Shot & Slip",
        "tag": "大动作假射 · 最后一刻分球",
        "gif": "tactics_animations_gif/anim_w_cat4_fake_shot.gif",
        "desc": "大动作假装起脚爆射诱使后卫下铲封堵，在最后一瞬间脚腕轻扣，节奏差隐蔽直塞空当单刀助攻。",
        "callout": "📢 场上实战口令：“假射真分！”"
      },
      {
        "id": "w15",
        "num": "W 15",
        "name": "反向对角塞球",
        "en": "Reverse Diagonal Pass",
        "tag": "打防线横移惯性反方向",
        "gif": "tactics_animations_gif/anim_w15_reverse_diagonal.gif",
        "desc": "横向带球吸附整条防线同步横移，突然逆着防守移动方向送反角直塞，利用对手重心反切破门。",
        "callout": "📢 场上实战口令：“打反向！”"
      },
      {
        "id": "w16",
        "num": "W 16",
        "name": "漏球顺势配合",
        "en": "Dummy / Let-Through",
        "tag": "迎球假动作 · 突然叉腿漏过",
        "gif": "tactics_animations_gif/anim_11_dummy_let_through.gif",
        "desc": "接应球员做出接球假动作吸引后卫上抢，皮球到达身前瞬间叉腿漏过，球顺势滚入单刀区。",
        "callout": "📢 场上实战口令：“漏过来！”"
      }
    ],
    "5": [
      {
        "id": "w17",
        "num": "W 17",
        "name": "门将穿透性低平球",
        "en": "GK Line-Breaking Ground Pass",
        "tag": "门将第7人 · 贴地刺穿双人逼抢线",
        "gif": "tactics_animations_gif/anim_w_cat5_gk_laser.gif",
        "desc": "门将推至大禁区弧顶，脚内侧大力贴地平抽穿透前锋逼抢线，直接连线中场，瞬间瓦解对手高位逼抢。",
        "callout": "📢 场上实战口令：“门将直穿！”"
      },
      {
        "id": "w18",
        "num": "W 18",
        "name": "反击越顶快攻长传",
        "en": "Over-the-Top Counter",
        "tag": "断球不停球 · 直接起身后",
        "gif": "tactics_animations_gif/anim_08_over_the_top.gif",
        "desc": "断球后 0.5 秒内不倒脚，直接送出 30 米半高球越过对手身后，供前锋全速冲刺打立足未稳。",
        "callout": "📢 场上实战口令：“起身后！”"
      },
      {
        "id": "w19",
        "num": "W 19",
        "name": "定位球低平倒三角",
        "en": "Set-piece Short Cross",
        "tag": "战术角球/任意球二过一",
        "gif": "tactics_animations_gif/anim_w19_setpiece_cutback.gif",
        "desc": "角球不盲目起高球争顶，发 2 人战术短传配合突入禁区肋部低平横扫，专门攻破高大后卫防线。",
        "callout": "📢 场上实战口令：“战术角球！”"
      },
      {
        "id": "w20",
        "num": "W 20",
        "name": "战术手抛界外球",
        "en": "Tactical Throw-in",
        "tag": "掷脚下 ➔ 回敲 ➔ 外侧套边",
        "gif": "tactics_animations_gif/anim_12_tactical_throwin.gif",
        "desc": "边卫抛给前锋，前锋顺势一脚回敲，边卫高速套边插下底直接传中，把边线死球变成进攻机会。",
        "callout": "📢 场上实战口令：“界外球一二配合！”"
      }
    ]
  },
  "combo": {
    "id": "combo_w02_w04",
    "title": "W 02 + W 04 · 肋部挑传 + 贴地平抽连招",
    "tag": "综合实战进球连招演示",
    "gif": "tactics_animations_gif/anim_w_cat1_chipped.gif",
    "descTitle": "📌 综合连招实战时序",
    "desc": "中场(4)脚尖搓挑打入左肋空当[W02] ➔ 边锋(5)不停球平抽门前危险走廊[W04] ➔ 中锋(7)高速抢前点垫射破门！",
    "callout": "📢 场上实战口令：“挑肋部” ➔ “前点平抽！”"
  },
  "formations": {
    "1231": {
      "name": "7人制 1-2-3-1 经典压迫传控阵型",
      "tag": "适合控球压迫 / 进攻宽度充足 / 实力占优",
      "animGif": "tactics_animations_gif/anim_05_1231_buildup.gif",
      "players": [
        {
          "num": 1,
          "pos": "GK",
          "name": "门卫 (Goalkeeper)",
          "code": "出球型门将 · 后场+1核心",
          "x": 50,
          "y": 88,
          "duty": "站位推至大禁区弧顶，与双中卫构成 3v2 局部人数优势；主导地面刺穿出球与大禁区外高位扫荡。",
          "pre": "皮球在对方半场时，站位推至禁区外弧顶，观察对方长传反击落点。",
          "main": "接回传球永远向立柱外侧领球；出球发力穿透逼抢线直塞中场。",
          "post": "出球后立即横向移动拉开新接应角度，随时准备再接中卫回敲。",
          "weapons": "W17 门将穿透 · W18 越顶长传",
          "callout": "“门将出球！” / “回传立柱！”"
        },
        {
          "num": 2,
          "pos": "CB",
          "name": "左中卫 (Left Center-Back)",
          "code": "出球中卫 · 破压直塞",
          "x": 28,
          "y": 72,
          "duty": "持球时大范围拉开至左侧肋部，拉扯对方锋线间距；向前送出刺穿直塞，防守时封锁左肋通道。",
          "pre": "接门将球前半侧身面向左路前场，观察中场 4号 与左翼 5号 跑位。",
          "main": "远离前锋逼抢的外侧脚顺势停球，脚内侧发力平推刺穿中路。",
          "post": "出球后保持阵型纵深，绝不上头前压导致身后大片空当。",
          "weapons": "W01 直塞穿透 · W10 边线推进",
          "callout": "“给身前！” / “半侧身！”"
        },
        {
          "num": 3,
          "pos": "CB",
          "name": "右中卫 (Right Center-Back)",
          "code": "出球中卫 · 大范围调度",
          "x": 72,
          "y": 72,
          "duty": "后防出球发起人；负责右路向前推进，在强侧受阻时送出 30 米大对角长传转移至弱侧。",
          "pre": "接球前快速摆头扫描前场右路走廊，保持身体朝向右前方。",
          "main": "一脚触球顺势连停带过，脚背内侧大力长传或低平直塞。",
          "post": "出球后与左中卫保持平行梯次保护，防止被对手单刀偷袭。",
          "weapons": "W07 刺穿线形 · W09 对角长传",
          "callout": "“看弱侧！” / “转过来！”"
        },
        {
          "num": 4,
          "pos": "CM",
          "name": "中前卫 (Central Midfielder)",
          "code": "攻防节拍器 · 阵型心脏",
          "x": 50,
          "y": 50,
          "duty": "全队攻防节奏掌控者；在后场双中卫身前形成接应三角，前场主导第三人跑位直塞与弱侧调度。",
          "pre": "皮球在运动中必须快速回头观察身后防守 2 次，保持半侧身迎球。",
          "main": "远离防守的外侧脚停球转身，一脚出球直塞盲区插上的边锋。",
          "post": "出球后立即二次前插禁区弧顶抢第二落点，或回撤保护中路防区。",
          "weapons": "W01 直塞 · W08 第三人 · W14 假射真传",
          "callout": "“转过来！” / “看第三人！”"
        },
        {
          "num": 5,
          "pos": "LW",
          "name": "左边锋 (Left Winger)",
          "code": "边路爆点 · 下底倒三角",
          "x": 20,
          "y": 34,
          "duty": "进攻拉满左侧宽度；利用速度打边线 1v1 突破，杀至底线送出致命倒三角回传或前点平抽。",
          "pre": "紧贴边线站位压低重心，接球前向防守靠近后突然反向迎球。",
          "main": "顺势将球领向进攻方向，底线发力贴地推向点球点无人区。",
          "post": "传球后立即前冲门前准备补射，丢球后就地封堵边线出球路线。",
          "weapons": "W03 倒三角 · W04 贴地横扫 · W05 撞墙",
          "callout": "“倒三角！” / “走边线！”"
        },
        {
          "num": 6,
          "pos": "RW",
          "name": "右边锋 (Right Winger)",
          "code": "内切射手 · 弱侧终结者",
          "x": 80,
          "y": 34,
          "duty": "强侧转移时的弱侧终结者；在左侧吸附防线时包抄后点，或利用二过一撞墙配合内切破门。",
          "pre": "当球在左侧时，悄悄从后卫盲区向后点幽灵插上。",
          "main": "迎着横传不停球直接推射远角，或顺势扣过滑铲后打门。",
          "post": "出球后迅速内收到禁区肋部，防守时回撤协助右中卫防守。",
          "weapons": "W04 贴地横扫 · W05 撞墙 · W11 弧线",
          "callout": "“后点包抄！” / “撞墙！”"
        },
        {
          "num": 7,
          "pos": "ST",
          "name": "突前中锋 (Striker)",
          "code": "反抢第一发起人 · 支点做球",
          "x": 50,
          "y": 19,
          "duty": "压制对方双中卫；背身扛人胸部卸球回做，前插反越位单刀，并领衔执行全队 5 秒就地反抢。",
          "pre": "压在对方越位线上，防守盲区背身卡位，随时准备启动。",
          "main": "迎球一脚轻推回做给后插上中场，做球要软方便施射。",
          "post": "回做球后立刻转身加速冲向门前抢点，或反身扑抢对方门将。",
          "weapons": "W02 挑传 · W06 迎前回做 · W16 漏球",
          "callout": "“回敲！” / “给身后！”"
        }
      ]
    },
    "1321": {
      "name": "7人制 1-3-2-1 圣诞树稳守反击阵型",
      "tag": "防守铁闸零死角 / 遇强敌 / 客场保胜 / 翼卫双核冲刺",
      "animGif": "tactics_animations_gif/anim_06_1321_counter.gif",
      "players": [
        {
          "num": 1,
          "pos": "GK",
          "name": "门将 (Goalkeeper)",
          "code": "最后一道铁闸 · 反击发起",
          "x": 50,
          "y": 88,
          "duty": "防守指挥官，封堵单刀，得球后 3 秒内大脚长传反击直找突前中锋身后。",
          "pre": "大声指挥三后卫保持紧密间距，观察门前包抄漏洞。",
          "main": "稳稳扑救击球，双手手抛球发动快攻。",
          "post": "呼应全队防线快速前推，保持阵型紧凑。",
          "weapons": "W17 门将穿透 · W18 越顶反击",
          "callout": "“收回来！” / “门将出球！”"
        },
        {
          "num": 2,
          "pos": "LWB",
          "name": "左翼卫 (Left Wing-Back)",
          "code": "边路飞翼 · 往返走廊",
          "x": 18,
          "y": 64,
          "duty": "边路走廊主宰；进攻全速前插下底送倒三角，防守回撤成 5 人防线铁壁。",
          "pre": "观察居中中卫拦截时机，一旦断球立即沿边线全速前插。",
          "main": "底线高速奔跑中脚内侧平抽横扫门前走廊。",
          "post": "进攻被阻立即全速退回本方禁区边线落位。",
          "weapons": "W03 倒三角 · W10 边线推进",
          "callout": "“走外侧！” / “回防！”"
        },
        {
          "num": 3,
          "pos": "CB",
          "name": "居中中卫 (Center-Back)",
          "code": "后防定海神针 · 绝不上抢失位",
          "x": 50,
          "y": 74,
          "duty": "后防统帅；严禁盲目上抢；负责中路补位卡线、解围与断球后第一脚纵向连线中锋。",
          "pre": "时刻观察对方中锋跑位，呼喊两翼翼卫保持横向间距。",
          "main": "果断拦截解围，或脚背发力踢出 35 米精准过顶长传。",
          "post": "出球后稳守禁区弧顶，指挥全队保持平衡。",
          "weapons": "W01 直塞 · W18 越顶长传",
          "callout": "“收紧中路！” / “直接起身后！”"
        },
        {
          "num": 4,
          "pos": "RWB",
          "name": "右翼卫 (Right Wing-Back)",
          "code": "边路飞翼 · 弱侧包抄",
          "x": 82,
          "y": 64,
          "duty": "右路走廊飞翼；在左路反击时高速前插包抄远门柱，防守收缩锁死右肋。",
          "pre": "防守时内收至禁区角保护肋部，反击瞬间外扩拉开宽度。",
          "main": "迎球不停球直接打门或贴地平抽门前。",
          "post": "反抢未果立即后撤与中卫组成链式防线。",
          "weapons": "W04 贴地横扫 · W20 战术界外球",
          "callout": "“压上去！” / “倒三角！”"
        },
        {
          "num": 5,
          "pos": "DM",
          "name": "防守型后腰 (Defensive Midfielder)",
          "code": "中场绞肉机 · 弧顶锁匠",
          "x": 50,
          "y": 52,
          "duty": "锁死禁区弧顶核心危险区；负责扫荡破坏对方直塞，完成安全球回敲或横传分边。",
          "pre": "始终将身体置于球与禁区弧顶之间，观察对方前插球员。",
          "main": "上抢卡位断球，一脚触球软推给身边的 6号 进攻核心。",
          "post": "出球后原地构筑防线第一道屏障，绝不前插失位。",
          "weapons": "W06 迎前回做 · W12 回传重组",
          "callout": "“身后有人！” / “回敲！”"
        },
        {
          "num": 6,
          "pos": "AM",
          "name": "前插组织中场 (Attacking Midfielder)",
          "code": "影子杀手 · 弧顶重炮",
          "x": 50,
          "y": 36,
          "duty": "反击进攻发动机；在中锋背身扛人做球瞬间高速前插到弧顶迎球爆射，或分边翼卫。",
          "pre": "在中锋争顶前观察第二落点，保持半侧身起跑姿态。",
          "main": "迎着回做球不停球直接重炮轰门，或假射真扣分给翼卫。",
          "post": "射门后跟进补射，丢球后就地封堵对方后腰传球路线。",
          "weapons": "W01 直塞 · W08 第三人 · W14 假射真传",
          "callout": "“回敲我打！” / “分两边！”"
        },
        {
          "num": 7,
          "pos": "ST",
          "name": "强力支点中锋 (Target Striker)",
          "code": "高空霸主 · 背身扛人",
          "x": 50,
          "y": 19,
          "duty": "强力背身扛人；接后场长传用胸部或头球稳稳摆渡做球给 6号 或两翼插上的飞翼。",
          "pre": "靠住后卫用后背感受防守重心，起跳争顶抢第一落点。",
          "main": "胸部卸球轻推回做，或脚后跟巧塞两翼跑动路线。",
          "post": "做球后转身前冲禁区，抢前点垫射折射。",
          "weapons": "W02 挑传 · W06 回敲 · W16 假接真漏",
          "callout": "“看身后！” / “回敲！”"
        }
      ]
    },
    "1331": {
      "name": "8人制 1-3-3-1 现代黄金全能阵型",
      "tag": "攻守完美平衡 / 边路双人组套边 / 12+三角传递网",
      "animGif": "tactics_animations_gif/anim_07_1331_overlap.gif",
      "players": [
        {
          "num": 1,
          "pos": "GK",
          "name": "门卫 (Goalkeeper)",
          "code": "现代门卫 · 高位扫荡",
          "x": 50,
          "y": 88,
          "duty": "大禁区弧顶扫荡指挥官；主导 3 后卫地面出球，随时前冲化解对方打身后反击。",
          "pre": "全队压上时推至禁区外弧顶，观察反击空当。",
          "main": "脚内侧大力贴地穿透直塞中场 6号。",
          "post": "出球后拉开新角度随时接回传。",
          "weapons": "W17 门将穿透 · W18 越顶长传",
          "callout": "“门将直穿！” / “转过来！”"
        },
        {
          "num": 2,
          "pos": "LB",
          "name": "左后卫 (Left Back)",
          "code": "边路套边器 · 攻防双能",
          "x": 20,
          "y": 72,
          "duty": "边路屏障；进攻推至中线与 5号 边前卫形成 2v1 外侧套边配合，杀入底线传中。",
          "pre": "边前卫内切时，提前向外侧启动冲刺准备套边。",
          "main": "高速插上接直塞一脚低平球横抽门前。",
          "post": "失球后立即全速回追封堵边路身后。",
          "weapons": "W03 倒三角 · W05 撞墙 · W10 边线",
          "callout": "“外侧套边！” / “倒三角！”"
        },
        {
          "num": 3,
          "pos": "CB",
          "name": "居中中卫 (Center-Back)",
          "code": "后防总指挥 · 大范围调度",
          "x": 50,
          "y": 75,
          "duty": "后防总指挥；前压压缩中场空间；送出 35 米大对角长传转移弱侧。",
          "pre": "保持与两名边后卫的呼应，扫描中场前插点。",
          "main": "脚背内侧大力斜长传，刺穿中路。",
          "post": "出球后保持阵型平衡，防止被反击。",
          "weapons": "W07 刺穿线形 · W09 对角长传",
          "callout": "“看弱侧！” / “收紧！”"
        },
        {
          "num": 4,
          "pos": "RB",
          "name": "右后卫 (Right Back)",
          "code": "右翼屏障 · 套边突击",
          "x": 80,
          "y": 72,
          "duty": "封锁右路通道；与 7号 边前卫打套边二过一，底线送出倒三角。",
          "pre": "观察右边前卫内切时机，突然从外侧全速超车。",
          "main": "一脚触球顺势传中，球速极快。",
          "post": "出球后立即补位右路防线。",
          "weapons": "W03 倒三角 · W04 贴地横扫",
          "callout": "“套边套边！” / “回防！”"
        },
        {
          "num": 5,
          "pos": "LM",
          "name": "左边前卫 (Left Midfielder)",
          "code": "边路爆点 · 内切扯动",
          "x": 22,
          "y": 44,
          "duty": "左路进攻发动机；带球内切吸引边后卫，送出直塞助攻套边的 2号 边卫下底。",
          "pre": "接球前观察 2号 边卫插上位置，保持身体半侧身。",
          "main": "大动作假射诱骗防守，脚腕一扣分给套边插上的边卫。",
          "post": "分球后快速内插禁区点球点包抄倒三角。",
          "weapons": "W05 撞墙 · W14 假射真分",
          "callout": "“走外侧！” / “看身后！”"
        },
        {
          "num": 6,
          "pos": "CM",
          "name": "中场指挥官 (Central Midfielder)",
          "code": "全队大脑 · 第三人主导者",
          "x": 50,
          "y": 48,
          "duty": "全场枢纽；掌控比赛节奏；主导第三人跑位直塞与弱侧调度，禁区外重炮轰门。",
          "pre": "皮球在空中滑行时完成盲区扫描，脑中已定出球方案。",
          "main": "一脚贴地穿透球刺穿防线，助攻前锋单刀。",
          "post": "出球后立即压入禁区弧顶抢第二落点。",
          "weapons": "W01 直塞 · W08 第三人 · W09 弱侧对角",
          "callout": "“看第三人！” / “弱侧弱侧！”"
        },
        {
          "num": 7,
          "pos": "RM",
          "name": "右边前卫 (Right Midfielder)",
          "code": "边路飞翼 · 1v1爆点",
          "x": 78,
          "y": 44,
          "duty": "右路爆点；1v1 突破内切射门或与 4号 边后卫打撞墙配合。",
          "pre": "紧贴边线拉开宽度，接球前反向摆脱。",
          "main": "带球内切射门，或送倒三角回传。",
          "post": "传球后立即包抄后门柱。",
          "weapons": "W03 倒三角 · W05 撞墙 · W10 边线",
          "callout": "“撞墙！” / “倒三角！”"
        },
        {
          "num": 8,
          "pos": "ST",
          "name": "突前全能中锋 (Complete Striker)",
          "code": "终极杀手 · 前插破门",
          "x": 50,
          "y": 20,
          "duty": "牵制双中卫；前插反越位单刀，门前抢点横扫折射破门。",
          "pre": "压在最后一名后卫身后，寻找盲区。",
          "main": "不停球直接推射球门近角死角。",
          "post": "进球后全队合围，丢球就地逼抢。",
          "weapons": "W01 直塞 · W04 贴地横扫 · W16 漏球",
          "callout": "“给身后！” / “回敲！”"
        }
      ]
    }
  },
  "crises": {
    "press": {
      "title": "破局① · 破解高位逼抢与前场贴身合围 (Beat High Press)",
      "tag": "反向诱敌 · 门将穿透打其身后大草原",
      "trap": "【对手陷阱】对手整体阵型前提至我方 30 米区域，严密切断中卫地面前插出球线，逼迫我方在后场失误送单刀。",
      "antidote": "【破局解药】严禁后场盲目大脚！门将积极推至大禁区弧顶充当“第 7 人”，利用【门将穿透性低平球】贴地大力刺穿前锋逼抢线；若对手中卫全线压过半场，拖后中卫立即送出【越顶长传】打其身后 25 米巨大真空区！",
      "weapons": [
        { "id": "w17", "name": "W17 门将穿透性低平球" },
        { "id": "w18", "name": "W18 越顶长传反越位" },
        { "id": "w10", "name": "W10 边线推进球" }
      ],
      "callout": "📢 场上核心口令：“门将直穿！” / “起身后！” / “身后有人！”"
    },
    "bus": {
      "title": "破局② · 撕碎低位铁桶与密集大巴防守 (Break Low Block)",
      "tag": "强侧超载 · 弱侧长传与底线倒三角",
      "trap": "【对手陷阱】全队退缩后场 30 米内收缩成铁桶阵，封死中路直线塞球路线，诱使我方盲目起高球争顶无功而返。",
      "antidote": "【破局解药】严禁在中路密集区强行硬塞！强侧连续快速倒脚（超载 Overload）吸引铁桶阵整体横移，中场突然起 30 米对角长传打向弱侧无人区；边路下底迫使防线退缩门线，坚决送【底线倒三角】回推点球点真空区！",
      "weapons": [
        { "id": "w03", "name": "W03 底线倒三角回传" },
        { "id": "w09", "name": "W09 大范围对角长传" },
        { "id": "w02", "name": "W02 肋部挑传空当" },
        { "id": "w14", "name": "W14 假射真传/节奏差" }
      ],
      "callout": "📢 场上核心口令：“弱侧弱侧！” / “倒三角！” / “挑肋部！”"
    },
    "mid": {
      "title": "破局③ · 突围中场惨烈绞杀与局部人数劣势 (Overcome Midfield Squeeze)",
      "tag": "一脚触球 · 第三人跑位与中锋胸部做球",
      "trap": "【对手陷阱】在中圈弧与两肋囤积重兵，凶狠逼抢第一接球人，只要我方持球停顿或背身护球立即遭遇双人合围断球。",
      "antidote": "【破局解药】全员执行【一脚触球】铁律！严禁持球超过 1 秒。启动【第三人跑位 Up-Back-Through】：后腰直塞前锋，前锋背身一脚回做，中场顺势送盲区第三人单刀；若地面绞杀惨烈，后场直接起半高球连线中锋胸部稳卸回做！",
      "weapons": [
        { "id": "w08", "name": "W08 第三人导向球" },
        { "id": "w06", "name": "W06 迎前回敲做球" },
        { "id": "w05", "name": "W05 二过一撞墙配合" },
        { "id": "w16", "name": "W16 漏球顺势配合" }
      ],
      "callout": "📢 场上核心口令：“看第三人！” / “回敲！” / “转过来！”"
    },
    "late": {
      "title": "破局④ · 终场比分落后与绝境搏杀 (Late Game Blitz Attack)",
      "tag": "就地反抢 · 5秒快攻与战术界外球",
      "trap": "【对手陷阱】对手领先拖延时间，退缩防守或在边线死球区故意制造停顿，打乱我方节奏。",
      "antidote": "【破局解药】丢球 0.5 秒内全队合围就地反抢！断球后 5 秒内 3 脚传递直达门前；充分利用死球机会执行【战术手抛界外球】：边卫掷前锋脚下一脚回敲，边卫套边平抽横扫门前；定位球果断发 2 人配合倒三角！",
      "weapons": [
        { "id": "w04", "name": "W04 贴地横扫传中" },
        { "id": "w20", "name": "W20 战术手抛界外球" },
        { "id": "w19", "name": "W19 定位球低平倒三角" },
        { "id": "w07", "name": "W07 刺穿线形传球" }
      ],
      "callout": "📢 场上核心口令：“前点平抽！” / “界外球一二配合！” / “战术角球！”"
    }
  },
  "callouts": [
    {
      "code": "“转过来！”",
      "en": "Turn!",
      "scene": "接球队员身后 3~5 米无防守人紧逼",
      "act": "严禁习惯性回传！拿球队员必须半侧身顺势领球向前，正面冲击对方防线。"
    },
    {
      "code": "“身后有人！”",
      "en": "Man On!",
      "scene": "对方防守队员贴身紧逼上抢接球人盲区",
      "act": "严禁盲目转身！必须一脚触球顺势回敲，或身体卡位护球借力打力。"
    },
    {
      "code": "“弱侧弱侧！”",
      "en": "Switch!",
      "scene": "强侧通道被对手重兵压缩堵死",
      "act": "全队视线向弱侧转移，中场持球人立即送出 30 米大对角斜长传找空当。"
    },
    {
      "code": "“看第三人！”",
      "en": "Third Man!",
      "scene": "破密集防守，第一接应点被死死盯防",
      "act": "不要传给眼前的暴露点，利用回敲过渡，一脚直塞给从盲区突前插上的第三人。"
    },
    {
      "code": "“门将直穿！”",
      "en": "GK Laser!",
      "scene": "对手双前锋高位逼抢扑中后卫",
      "act": "门将提至弧顶接球，大力贴地平抽穿透前锋逼抢线，直接连线中场。"
    },
    {
      "code": "“起身后！”",
      "en": "Over the Top!",
      "scene": "对手防线全线压上，其身后留 20 米真空区",
      "act": "断球 0.5 秒内不倒脚，拖后中卫直接送半高球越顶长传，前锋反越位超车单刀。"
    },
    {
      "code": "“倒三角！”",
      "en": "Cut Back!",
      "scene": "边锋下底迫使防守队员与门将退缩门线",
      "act": "拒绝盲目起高球争顶！发力贴地推向点球点到禁区线之间的巨大真空区。"
    },
    {
      "code": "“回传重来！”",
      "en": "Recycle!",
      "scene": "边路进攻陷入双人包夹死胡同",
      "act": "拒绝单打独斗盲目对抗失误！果断回敲拖后中卫，全队横向展开重构进攻面。"
    }
  ]
};

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = tacticsData;
  }
  if (typeof window !== 'undefined') {
    window.TACTICS_DATA = tacticsData;
  } else {
    global.TACTICS_DATA = tacticsData;
  }
})(typeof window !== 'undefined' ? window : this);
