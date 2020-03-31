from flask_restful import Api
from apps.controler.urls_handler import UrlsHandler

prefix = '/api/v1'


def init_url_route(app):
    """
    初始化所有的路由和hanlder关系
    :param app:
    :return:
    """
    api = Api(app)
    api.add_resource(UrlsHandler, prefix + '/change')
