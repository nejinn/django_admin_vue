export default {
  getLocalInfo: function(item) {
    // 获取localStorage数据
    if (localStorage.getItem(item) === "undefined") {
      return "";
    }
    return localStorage.getItem(item)
      ? JSON.parse(localStorage.getItem(item))
      : "";
  },
  setLocalInfo: function(item, obj) {
    // 存储localStorage数据
    localStorage.setItem(item, JSON.stringify(obj));
  },
  clearLocalInfo: function(item) {
    // 移除localStorage数据
    localStorage.removeItem(item);
  }
};
