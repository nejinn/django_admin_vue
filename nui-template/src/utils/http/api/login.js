import http from "../http";
import urlList from "./urlList";

export default {
  loginPost: function(obj, data) {
    const url = urlList.LoginUrl;
    http.nlyPost(url, data).then(
      response => {
        const { token } = response;
        obj.$store.commit("setLoginUserInfo", token);
        obj.$router.push(obj.$route.query.redirect || "/");
      },
      err => {
        http.nlyCheckCode(obj, err);
      }
    );
  },
  loginGet: function(obj, data) {
    const url = urlList.LoginUrl;
    console.log(url);
    http.nlyGetList(url, data).then(
      response => {
        const { site_title, site_header, title } = response;
        obj.title = title;
        obj.siteTitle = site_title;
        obj.siteHeader = site_header;
        document.title = obj.title + " | " + obj.siteTitle;
      },
      err => {
        http.nlyCheckCode(obj, err);
      }
    );
  }
};
