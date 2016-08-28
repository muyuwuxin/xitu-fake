from page import index, user, article

router_page = [
    (r'/', index.PageIndex),
    (r'/login', user.PageLogin),
    (r'/register', user.PageRegister),
    (r'/user/(\d+)', user.PageUser),
    (r'/me', user.PageMe),
    (r'/publish', article.PagePublish)
]
