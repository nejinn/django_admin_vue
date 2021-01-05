import localstorage from "../../utils/localstorage";

const state = {
  loginToken: localstorage.getLocalInfo("nly-blog-token") || undefined
};

const getters = {
  getLoginToken(state) {
    return state.loginToken;
  }
};

const mutations = {
  setLoginUserInfo(state, payload) {
    state.loginToken = payload;
    localstorage.setLocalInfo("nly-blog-token", payload);
  },
  clearLoginUserInfo(state) {
    state.loginToken = "";
    localstorage.clearLocalInfo("nly-blog-token");
  }
};

const actions = {};

export default {
  state,
  getters,
  mutations,
  actions
};
