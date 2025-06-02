class DevConfig(object):
    DEBUG = True
    TESTING = True
    SWAGGER_TITLE = "API 文档"
    SWAGGER_DESC = "此处是描述内容"
    SWAGGER_HOST = "127.0.0.1:5000"


class ProdConfig(object):
    DEBUG = False
    TESTING = False
    SWAGGER_TITLE = "API 文档"
    SWAGGER_DESC = "此处是描述内容"
    SWAGGER_HOST = "xxxx.com"
