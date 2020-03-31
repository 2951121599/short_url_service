from database import db_session
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class UrlModel(Base):
    __bind_key__ = 'short_url_service'
    __tablename__ = 'url_info'

    url_id = Column(Integer, nullable=False, primary_key=True)
    long_url = Column(String(255), nullable=False)
    short_url = Column(String(255), nullable=False)

    @classmethod
    def get_url_by_long_url(cls, long_url):
        """
        根据长链接获取信息
        :return:
        """
        return db_session.query(cls).filter(cls.long_url == long_url).first()

    @classmethod
    def get_url_by_short_url(cls, short_url):
        """
        根据短链接获取信息
        :return:
        """
        return db_session.query(cls).filter(cls.short_url == short_url).first()
