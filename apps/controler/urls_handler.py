import random
import string

from flask import request, make_response, jsonify, redirect
from flask_restful import Resource

from apps.models.url_info import UrlModel
from database import db_session


class UrlsHandler(Resource):

    def post(self):
        """
        获取long_url转换short_url返回
        :return:
        """
        long_url = request.values.get('long_url')
        if not long_url:
            return make_response(jsonify({'error': 'not long_url'}))
        url_obj = None
        try:
            url_obj = UrlModel.get_url_by_long_url(long_url)
        except Exception as e:
            print(e)

        if url_obj:
            short_url = url_obj.short_url
            return make_response(jsonify({'short_url': short_url}))

        short_url = '/short/'
        short_url += ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(6))

        try:
            one_url = UrlModel(long_url=long_url, short_url=short_url)
            db_session.add(one_url)
            db_session.commit()
            print('save url success')
        except Exception as e:
            print('save url error', str(e))
            db_session.rollback()

        # add_url_route(app, short_url)
        return make_response(jsonify({'short_url': short_url}))


def is_exist_url(short_url):
    """
    判断短链接是否存在
    :param short_url:
    :return:
    """
    short_url = '/short/' + short_url
    print('short_url:', short_url)
    url_obj = UrlModel.get_url_by_short_url(short_url)
    if url_obj:
        return url_obj.long_url
    return
