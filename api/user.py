# coding=utf8

from base import ApiBase
from tornado.gen import coroutine, Return
from service.user import ServiceUser


class ApiUserBase(ApiBase):
    def __init__(self, *args, **kwargs):
        super(ApiUserBase, self).__init__(*args, **kwargs)
        self.srv_user = ServiceUser()


class ApiUser(ApiUserBase):
    @coroutine
    def get(self, user_id):
        data = yield self.srv_user.find_one_by_id(user_id)
        self.json_ok(data)


class ApiUsers(ApiUserBase):
    @coroutine
    def get(self, *args, **kwargs):
        self.json_ok()


class ApiLogin(ApiUserBase):
    @coroutine
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)

        user_id = self.srv_user.find_one_by_username_password(username, password)
        self.set_secure_cookie('user_id', user_id)
        if user_id:
            self.json_ok()
        else:
            self.json_err('用户名或密码错误')


class ApiLogout(ApiUserBase):
    @coroutine
    def post(self):
        self.json_ok()


class ApiRegister(ApiUserBase):
    @coroutine
    def post(self):
        username = self.get_argument('username', None)
        password = self.get_argument('password', None)

        # 用户名是否已经被使用
        data = self.srv_user.find_one_by_username(username)
        if data:
            self.json_err('username: ' + username + '已经被其他人使用了')

        # 注册用户
        data = self.srv_user.create(username, password)
        if data:
            self.json_ok()
        else:
            self.json_err('注册失败')
