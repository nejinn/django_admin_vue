const ApiBaseUrl = "/nui_admin";

export default {
  LoginUrl: `${ApiBaseUrl}/login/`,
  getSidebar: `${ApiBaseUrl}/sidebar/`,
  getUserList: `${ApiBaseUrl}user/list`,
  checkUsername: `${ApiBaseUrl}user/check_username`,
  addUser: `${ApiBaseUrl}user/add_user`,
  deleteUser: `${ApiBaseUrl}user/delete_user`,
  deleteUserList: `${ApiBaseUrl}user/delete_user_list`,
  launchUser: `${ApiBaseUrl}user/recover_user`,
  infoBox: `${ApiBaseUrl}dashboard`,
  editorUser: `${ApiBaseUrl}user/editor`
};
