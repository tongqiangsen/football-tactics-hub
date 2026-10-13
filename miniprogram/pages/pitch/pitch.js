// miniprogram/pages/pitch/pitch.js
let DB = null;
try {
  DB = require('../../utils/tactics_data.js');
} catch (e) {
  try {
    DB = require('../../../data/tactics_data.js');
  } catch (err) {
    console.error("加载 tactics_data.js 失败", err);
  }
}

Page({
  data: {
    formations: {},
    formationKeys: ['1231', '1321', '1331'],
    currentFormationKey: '1231',
    currentFormation: null,
    players: [],
    selectedIndex: 3,
    selectedPlayer: null,
    drawMode: 'drag', // 'drag' | 'pass' | 'run' | 'dribble' | 'press'
    currentScenario: 'standard'
  },

  canvasNode: null,
  ctx: null,
  strokes: [],
  startX: 0,
  startY: 0,
  isDrawing: false,
  boardRect: null,

  // Player dragging state
  activePlayerIndex: -1,
  dragStartX: 0,
  dragStartY: 0,
  origPctX: 0,
  origPctY: 0,
  dragMoved: false,

  onLoad() {
    if (!DB) {
      console.error("战术数据未就绪");
      return;
    }
    const formations = JSON.parse(JSON.stringify(DB.formations || {}));
    const curForm = formations['1231'];
    this.setData({
      formations,
      currentFormation: curForm,
      players: curForm.players,
      selectedPlayer: curForm.players[3]
    });
  },

  onReady() {
    this.initCanvas();
  },

  initCanvas() {
    const query = wx.createSelectorQuery();
    query.select('#pitchCanvas')
      .fields({ node: true, size: true })
      .exec((res) => {
        if (!res || !res[0]) return;
        const canvas = res[0].node;
        const ctx = canvas.getContext('2d');
        const dpr = wx.getSystemInfoSync().pixelRatio || 2;
        canvas.width = res[0].width * dpr;
        canvas.height = res[0].height * dpr;
        ctx.scale(dpr, dpr);

        this.canvasNode = canvas;
        this.ctx = ctx;
        this.redrawCanvas();
      });

    wx.createSelectorQuery().select('#pitchBoard').boundingClientRect((rect) => {
      this.boardRect = rect;
    }).exec();
  },

  onSwitchFormation(e) {
    const key = e.currentTarget.dataset.key;
    const formations = this.data.formations;
    const curForm = formations[key];
    if (!curForm) return;

    this.setData({
      currentFormationKey: key,
      currentFormation: curForm,
      players: curForm.players,
      selectedIndex: 0,
      selectedPlayer: curForm.players[0],
      currentScenario: 'standard'
    });
    this.strokes = [];
    this.redrawCanvas();
  },

  setToolMode(e) {
    const mode = e.currentTarget.dataset.mode;
    this.setData({ drawMode: mode });
  },

  undoStroke() {
    if (this.strokes.length > 0) {
      this.strokes.pop();
      this.redrawCanvas();
    }
  },

  clearBoard() {
    this.strokes = [];
    this.redrawCanvas();
  },

  resetFormation() {
    const origFormations = JSON.parse(JSON.stringify(DB.formations || {}));
    const cur = origFormations[this.data.currentFormationKey];
    this.setData({
      players: cur.players,
      selectedPlayer: cur.players[this.data.selectedIndex] || cur.players[0],
      currentScenario: 'standard'
    });
    this.strokes = [];
    this.redrawCanvas();
  },

  onSelectPlayer(e) {
    if (this.dragMoved) return;
    const idx = e.currentTarget.dataset.index;
    this.setData({
      selectedIndex: idx,
      selectedPlayer: this.data.players[idx]
    });
  },

  // Player Touch Dragging
  onPlayerTouchStart(e) {
    if (this.data.drawMode !== 'drag') return;
    const idx = e.currentTarget.dataset.index;
    const touch = e.touches[0];
    this.activePlayerIndex = idx;
    this.dragStartX = touch.clientX;
    this.dragStartY = touch.clientY;
    this.origPctX = this.data.players[idx].x;
    this.origPctY = this.data.players[idx].y;
    this.dragMoved = false;
  },

  onPlayerTouchMove(e) {
    if (this.activePlayerIndex < 0 || this.data.drawMode !== 'drag' || !this.boardRect) return;
    const touch = e.touches[0];
    const dx = touch.clientX - this.dragStartX;
    const dy = touch.clientY - this.dragStartY;
    if (Math.abs(dx) > 3 || Math.abs(dy) > 3) this.dragMoved = true;

    const deltaPctX = (dx / this.boardRect.width) * 100;
    const deltaPctY = (dy / this.boardRect.height) * 100;

    let newX = Math.max(5, Math.min(95, this.origPctX + deltaPctX));
    let newY = Math.max(5, Math.min(95, this.origPctY + deltaPctY));

    const players = this.data.players;
    players[this.activePlayerIndex].x = Math.round(newX * 10) / 10;
    players[this.activePlayerIndex].y = Math.round(newY * 10) / 10;

    this.setData({
      players,
      selectedPlayer: players[this.activePlayerIndex],
      selectedIndex: this.activePlayerIndex
    });
  },

  onPlayerTouchEnd() {
    this.activePlayerIndex = -1;
  },

  // Canvas Vector Drawing
  onTouchStart(e) {
    if (this.data.drawMode === 'drag') return;
    const touch = e.touches[0];
    const rect = this.boardRect;
    if (!rect) return;
    this.startX = touch.clientX - rect.left;
    this.startY = touch.clientY - rect.top;
    this.isDrawing = true;
  },

  onTouchMove(e) {
    if (!this.isDrawing || this.data.drawMode === 'drag' || !this.boardRect) return;
    const touch = e.touches[0];
    const currX = touch.clientX - this.boardRect.left;
    const currY = touch.clientY - this.boardRect.top;

    this.redrawCanvas();
    this.drawArrow(this.ctx, this.startX, this.startY, currX, currY, this.data.drawMode);
  },

  onTouchEnd(e) {
    if (!this.isDrawing || this.data.drawMode === 'drag') return;
    this.isDrawing = false;
    const touch = e.changedTouches[0];
    if (!this.boardRect) return;
    const endX = touch.clientX - this.boardRect.left;
    const endY = touch.clientY - this.boardRect.top;

    if (Math.hypot(endX - this.startX, endY - this.startY) > 10) {
      this.strokes.push({
        x1: this.startX,
        y1: this.startY,
        x2: endX,
        y2: endY,
        mode: this.data.drawMode
      });
    }
    this.redrawCanvas();
  },

  redrawCanvas() {
    const ctx = this.ctx;
    const canvas = this.canvasNode;
    if (!ctx || !canvas) return;
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    this.strokes.forEach(s => {
      this.drawArrow(ctx, s.x1, s.y1, s.x2, s.y2, s.mode);
    });
  },

  drawArrow(ctx, x1, y1, x2, y2, mode) {
    const headLen = 14;
    const angle = Math.atan2(y2 - y1, x2 - x1);
    ctx.save();

    let color = '#f59e0b';
    let isDashed = false;
    let lineWidth = 3;

    if (mode === 'pass') {
      color = '#f59e0b';
      isDashed = true;
      lineWidth = 3;
    } else if (mode === 'run') {
      color = '#10b981';
      lineWidth = 3.5;
    } else if (mode === 'dribble') {
      color = '#38bdf8';
      lineWidth = 3.5;
    } else if (mode === 'press') {
      color = '#ef4444';
      lineWidth = 4;
      isDashed = true;
    }

    ctx.strokeStyle = color;
    ctx.fillStyle = color;
    ctx.lineWidth = lineWidth;
    ctx.lineCap = 'round';

    if (isDashed) {
      ctx.setLineDash([7, 5]);
    } else {
      ctx.setLineDash([]);
    }

    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();

    ctx.setLineDash([]);
    ctx.beginPath();
    ctx.moveTo(x2, y2);
    ctx.lineTo(x2 - headLen * Math.cos(angle - Math.PI / 6), y2 - headLen * Math.sin(angle - Math.PI / 6));
    ctx.lineTo(x2 - headLen * Math.cos(angle + Math.PI / 6), y2 - headLen * Math.sin(angle + Math.PI / 6));
    ctx.closePath();
    ctx.fill();

    ctx.restore();
  },

  applyScenario(e) {
    const scene = e.currentTarget.dataset.scene;
    this.setData({ currentScenario: scene });
    const rect = this.boardRect;
    if (!rect) return;

    this.strokes = [];

    if (scene === 'high_press') {
      // 3v2 High Press Simulation
      this.strokes.push({ x1: rect.width * 0.5, y1: rect.height * 0.8, x2: rect.width * 0.5, y2: rect.height * 0.55, mode: 'press' });
      this.strokes.push({ x1: rect.width * 0.25, y1: rect.height * 0.7, x2: rect.width * 0.45, y2: rect.height * 0.52, mode: 'pass' });
      wx.showToast({ title: '高位合围推演', icon: 'none' });
    } else if (scene === 'deep_buildup') {
      // GK Buildup
      this.strokes.push({ x1: rect.width * 0.5, y1: rect.height * 0.88, x2: rect.width * 0.25, y2: rect.height * 0.72, mode: 'pass' });
      this.strokes.push({ x1: rect.width * 0.25, y1: rect.height * 0.72, x2: rect.width * 0.5, y2: rect.height * 0.5, mode: 'pass' });
      this.strokes.push({ x1: rect.width * 0.2, y1: rect.height * 0.4, x2: rect.width * 0.2, y2: rect.height * 0.18, mode: 'run' });
      wx.showToast({ title: '门将后场出球三角', icon: 'none' });
    } else if (scene === 'flank_overload') {
      // Flank Overload & Switch
      this.strokes.push({ x1: rect.width * 0.25, y1: rect.height * 0.6, x2: rect.width * 0.8, y2: rect.height * 0.35, mode: 'pass' });
      this.strokes.push({ x1: rect.width * 0.8, y1: rect.height * 0.35, x2: rect.width * 0.5, y2: rect.height * 0.2, mode: 'pass' });
      wx.showToast({ title: '强侧超载弱侧转移', icon: 'none' });
    } else {
      this.resetFormation();
      wx.showToast({ title: '复原标准站位', icon: 'none' });
      return;
    }
    this.redrawCanvas();
  }
});
