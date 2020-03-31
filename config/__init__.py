DB_USER = 'root'
DB_PASS = '123456'
DB_HOST = '127.0.0.1'
DB_PORT = 3306
DB_NAME = 'short_url_service'
DB_CHAR = 'utf8'

# mysql://root:123456@127.0.0.1:3306/short_url_service?charset=utf8&autocommit=true
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%d/%s?charset=%s&autocommit=true' % (
    DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME, DB_CHAR)
