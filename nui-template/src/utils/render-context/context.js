const renderContext = {
  loginContext: {
    loginLog: ["BlogAdmin", "NLY"],
    loginBoxMsg: "请输入账号密码登录",
    loginInputPlaceholder: ["账号", "密码"],
    rememberMe: "记住我",
    loginButtom: "登录",
    loginError: {
      title: "登录失败",
      usernameMsg: "用户名不能为空",
      usernameContent: "用户名异常",
      passwordMsg: "密码不能为空",
      passwordContent: "密码异常",
      variant: "danger"
    }
  },
  httpContext: {
    interceptorsErrorTilte: "服务错误",
    interceptorsVariant: "info"
  },
  allUseContext: {
    title: "获取数据出错",
    variant: "primary"
  },
  deleteUserContext: {
    title: "操作成功",
    variant: "success",
    message: "删除用户成功",
    content: "删除成功"
  },
  launchUserContext: {
    title: "操作成功",
    variant: "success",
    message: "启用用户成功",
    content: "启用成功"
  },
  deleteUserMsgBox: {
    message: "请选择至少一个用户",
    variant: "warning",
    title: "操作失败",
    content: "删除失败"
  },
  allUserResetQueryCriteria: {
    message: "重置查询条件",
    variant: "success",
    title: "操作成功",
    content: "重置成功"
  },
  allUserQueryCriteria: {
    message: "查询条件不能全部为空",
    variant: "warning",
    title: "操作失败",
    content: "查询失败"
  },
  userList: {
    usertypeOptions: [
      { value: null, text: "请选择用户类型", disabled: true },
      { value: 1, text: "超级用户" },
      { value: 2, text: "普通用户" }
    ],
    isdeleteOptions: [
      { value: null, text: "请选择是否停用", disabled: true },
      { value: false, text: "未停用" },
      { value: true, text: "已停用" }
    ]
  },
  action: {
    editor: "编辑",
    stop: "停用",
    launch: "启用",
    view: "查看"
  },
  editorUserMsgBox: {
    variant: "warning",
    title: "操作失败",
    content: "编辑用户失败"
  },
  editorUserContext: {
    title: "操作成功",
    variant: "success",
    message: "编辑用户成功",
    content: "编辑成功"
  },
  addUserContext: {
    title: "操作成功",
    variant: "success",
    message: "新增用户成功",
    content: "新增成功"
  }
};

export default renderContext;
