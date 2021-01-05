import http from "../http";
import urlList from "./urlList";

const getInfoBox = (obj, data) => {
  const url = urlList.infoBox;
  http.nlyGetList(url, data).then(
    response => {
      obj.infoBox = response.vd;
      obj.infoBox1 = response.vd1;
    },
    err => {
      http.nlyCheckCode(obj, err);
    }
  );
};

export default {
  getInfoBox
};
