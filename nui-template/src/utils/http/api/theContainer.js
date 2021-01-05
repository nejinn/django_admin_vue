import http from "../http";
import urlList from "./urlList";
import RenderContext from "../../../utils/render-context/context";

export default {
  getSidebar: function(obj, data) {
    const url = urlList.getSidebar;
    http.nlyGetList(url, data).then(
      response => {
        const { user_info, app_list } = response;
        obj.userInfo = user_info;
        obj.userSidebar = app_list;
      },
      err => {
        if (!http.nlyCheckCode(obj, err)) {
          const { code, msg } = err;
          const toastVnode = {
            title: RenderContext.allUseContext.title,
            message: msg,
            content: code,
            variant: RenderContext.allUseContext.variant
          };
          obj.$toast(obj, toastVnode);
        }
      }
    );
  }
};
