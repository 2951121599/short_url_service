from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config import SQLALCHEMY_DATABASE_URI

# 创建一个配置对象
engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_recycle=3600, echo=True, convert_unicode=True)
# 创建一个会话
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
