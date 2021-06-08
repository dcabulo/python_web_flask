class InitialSetup:
    SECRET_KEY = 'diego12345*'


class DevelopmentConfig(InitialSetup):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Diego12345*@localhost/project_web_course'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
