# 200 为业务正常逻辑
OK = {'code': 200, 'msg': 'ok!'}
STATUS_CODE_ERROR = {'code': 110001, 'msg': 'response 状态码错误'}

# 1 开头  系统问题 code
# 11开头 自定义response错误 code
LOGIN_USER_NOT_EXIST = {'code': 100001, 'msg': "用户不存在"}
LOGIN_USER_IS_ACTIVE = {'code': 100002, 'msg': "用户已停用"}
LOGIN_USER_IS_STAFF = {'code': 100003, 'msg': "用户不能登录admin"}
LOGIN_USER_ACCOUNT_ERROR = {'code': 100004, 'msg': "账号或者密码错误"}
