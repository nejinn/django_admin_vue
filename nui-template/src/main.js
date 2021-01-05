import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "nly-adminlte-vue/dist/adminlte/css/adminlte.css";
import "nly-adminlte-vue/dist/adminlte/fontawesome-free/css/all.css";
import "nly-adminlte-vue/dist/adminlte/icon/iconfont.css";
import "nly-adminlte-vue/dist/nly-adminlte-vue.css";
import "./assets/open-iconic/font/css/open-iconic-bootstrap.css";
import { NlyAdminlteVue, NlyAdminlteVueIcons } from "nly-adminlte-vue";
Vue.use(NlyAdminlteVue);
Vue.use(NlyAdminlteVueIcons);

import "./assets/static/css/blog-icon/iconfont.css";
import "./assets/static/css/font.css";
import "./assets/static/css/blog-icon/iconfont.js";
import "./assets/static/css/custom.css";

import Toast from "./utils/toast";
import Api from "./utils/http";
Vue.prototype.$toast = Toast;
Vue.prototype.$api = Api;

Vue.config.productionTip = false;

// import HighchartsVue from "highcharts-vue";
// Vue.use(HighchartsVue);

router.beforeEach((to, from, next) => {
  // 判断跳转的路由是否需要登录
  if (to.meta.login) {
    // vuex.state判断token是否存在
    if (store.state.login.loginToken) {
      next(); // 已登录
    } else {
      next({
        path: "/login",
        query: { redirect: to.fullPath } // 将跳转的路由path作为参数，登录成功后跳转到该路由
      });
    }
  } else {
    // document.title = "NLY Adminlte Vue" + "-" + to.meta.title;
    next();
  }
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
