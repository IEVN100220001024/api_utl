class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'emi'
    MYSQL_PASSWORD = '123'
    MYSQL_DB = 'api_utl'

config={
    'development': DevelopmentConfig
}