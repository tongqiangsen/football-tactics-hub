// miniprogram/app.js
App({
  globalData: {
    // 媒体资源走云端或 GitHub Pages CDN，解决主包 2MB 限制
    cdnBase: "https://raw.githubusercontent.com/tongqiangsen/football-tactics-hub/main/tactics_animations_gif"
  },
  onLaunch() {
    console.log("⚽ 德国足球战术教研中枢小程序已就绪");
  }
});
