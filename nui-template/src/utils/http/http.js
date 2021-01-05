import axios from "axios";
import store from "../../store";
// import qs from "qs";
import router from "../../router";

axios.defaults.timeout = 50000;
axios.defaults.baseURL = "http://127.0.0.1:8000";

// http request 拦截器
axios.interceptors.request.use(
  config => {
    if (store.state.login.loginToken) {
      config.headers.Authorization = `nui ${store.getters.getLoginToken}`;
    }
    // if (Object.prototype.toString.call(config.data) != "[object FormData]") {
    //   if (config.method == "post") {
    //     config.data = qs.stringify(config.data);
    //     config.headers["Content-Type"] = "application/x-www-form-urlencoded";
    //   }
    // } else {
    //   if (config.method == "post") {
    //     config.data = qs.stringify(config.data);
    //     config.headers["Content-Type"] = "multipart/form-data";
    //   }
    // }

    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

axios.interceptors.response.use(
  response => {
    const dataAxios = response.data;
    const { ret, data } = dataAxios;
    const { code } = ret;
    if (code === undefined) {
      return dataAxios;
    } else {
      switch (code) {
        case 200:
          return data;
        default:
          return Promise.reject(ret);
      }
    }
  },
  error => {
    const ret = {};
    if (error && error.response) {
      switch (error.response.status) {
        case 400:
          ret.code = 400;
          ret.msg = "请求错误";
          return Promise.reject(ret);
        case 401:
          router.push({
            path: "/login",
            query: { redirect: router.currentRoute.fullPath }
          });
          store.commit("clearLoginUserInfo");
          ret.code = 401;
          ret.msg = "请重新登录";
          return Promise.reject(ret);
        case 403:
          ret.code = 403;
          ret.msg = "没有权限";
          return Promise.reject(ret);
        case 404:
          router.push({
            path: "/404"
          });
          ret.code = 404;
          ret.msg = "没有找到资源";
          return Promise.reject(ret);
        case 408:
          ret.code = 408;
          ret.msg = "请求超时";
          return Promise.reject(ret);
        case 500:
          router.push({
            path: "/500"
          });
          ret.code = 500;
          ret.msg = "服务器内部错误";
          return Promise.reject(ret);
        case 501:
          ret.code = 501;
          ret.msg = "服务未实现";
          return Promise.reject(ret);
        case 502:
          ret.code = 502;
          ret.msg = "网关错误";
          return Promise.reject(ret);
        case 503:
          router.push({
            path: "/500"
          });
          ret.code = 503;
          ret.msg = "服务不可用";
          return Promise.reject(ret);
        case 504:
          ret.code = 504;
          ret.msg = "网关超时";
          return Promise.reject(ret);
        case 505:
          ret.code = 505;
          ret.msg = "HTTP版本不受支持";
          return Promise.reject(ret);
        default:
          ret.code = 600;
          ret.msg = "未知错误";
          return Promise.reject(ret);
      }
    } else {
      router.push({
        path: "/500"
      });
      ret.code = 503;
      ret.msg = "服务不可用";
      return Promise.reject(ret);
    }
  }
);

export default {
  nlyGetList: function(url, params = {}) {
    /**
     * 封装get list方法，获取数据列表
     * 可带 搜索条件，页码，每页数量数据
     * demo url 127.0.0.1:8000/api/project/?page=1&size=10&name=33
     * @param url
     * @param data
     * @returns {Promise}
     */
    return new Promise((resolve, reject) => {
      axios
        .get(url, {
          params: params
        })
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });
  },
  nlyGetDetail: function(url, id) {
    /**
     * 封装get detail方法,获取数据详情
     * 不带params和data，带id
     * demo url 127.0.0.1:8000/api/project/detail/1/
     * @param url
     * @param id
     * @returns {Promise}
     */
    return new Promise((resolve, reject) => {
      axios
        .get(url + id + "/")
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });
  },
  nlyPost: function(url, data = {}) {
    /**
     * 封装post请求，创建数据
     * demo url 127.0.0.1:8000/api/project/create/
     * @param url
     * @param data
     * @returns {Promise}
     */
    return new Promise((resolve, reject) => {
      axios
        .post(url, data)
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });
  },
  nlyUpdateFile: function(url, data = {}, config = {}) {
    /**
     * 封装post请求，创建数据
     * demo url 127.0.0.1:8000/api/project/create/
     * @param url
     * @param data
     * @returns {Promise}
     */
    return new Promise((resolve, reject) => {
      axios
        .post(url, data, config)
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });
  },
  nlyPatch: function(url, data = {}) {
    /**
     * 封装patch请求
     * @param url
     * @param data
     * @returns {Promise}
     */
    return new Promise((resolve, reject) => {
      axios
        .patch(url, data)
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });
  },
  nlyUpDate: function(url, id, data) {
    /**
     * 封装put请求，更新，修改数据，假删除数据等
     * 带data，带id
     * demo url 127.0.0.1:8000/api/project/1/
     * @param url
     * @param data
     * @returns {Promise}
     */
    return new Promise((resolve, reject) => {
      axios
        .put(url + id + "/", data)
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });
  },
  nlyUpDateNoId: function(url, data) {
    /**
     * 封装put请求，更新，修改数据，假删除数据等
     * 带data
     * demo url 127.0.0.1:8000/api/project/1/
     * @param url
     * @param data
     * @returns {Promise}
     */
    return new Promise((resolve, reject) => {
      axios
        .put(url, data)
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });
  },
  nlyDelete: function(url, id) {
    /**
     * 封装delete请求，删除数据
     * 带id
     * demo url 127.0.0.1:8000/api/project/delete/1/
     * @param url
     * @param data
     * @returns {Promise}
     */
    return new Promise((resolve, reject) => {
      axios
        .delete(url + id + "/")
        .then(response => {
          resolve(response);
        })
        .catch(err => {
          reject(err);
        });
    });
  },
  nlyCheckCode: function(obj, ret) {
    const codeArray = [400, 403, 408, 500, 501, 502, 503, 504, 505, 600];
    const { code, msg } = ret;

    if (code == 100002) {
      obj.$router.push({
        path: "/login",
        query: { redirect: router.currentRoute.fullPath }
      });
      store.commit("clearLoginUserInfo");
      return true;
    }

    if (codeArray.indexOf(code) === -1) {
      const toastVnode = {
        title: "操作失败",
        message: msg,
        content: code,
        variant: "danger"
      };
      obj.$toast(obj, toastVnode);
      return true;
    }

    if (code === 401 || code === 404 || code === 500 || code === 503) {
      return true;
    }
    return false;
  }
};
