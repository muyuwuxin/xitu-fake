from page import index, user

router_page = [
    (r'/', index.PageIndex),
    (r'/login', user.PageLogin),
    (r'/register', user.PageRegister)
]
