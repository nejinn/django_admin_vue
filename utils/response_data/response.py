from rest_framework.response import Response
from utils.response_msg.server_msg import STATUS_CODE_ERROR, OK


class ResponseDate(object):
    STATUS_TYPE = [
        100, 101, 200, 201, 202, 203, 204, 205, 206, 207, 208,
        226, 300, 301, 302, 303, 304, 305, 306, 307, 308, 400,
        401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411,
        412, 413, 414, 415, 416, 417, 418, 422, 423, 424, 426,
        428, 429, 431, 451, 500, 501, 502, 503, 504, 505, 506,
        507, 508, 509, 510, 511]

    def __init__(self):
        pass

    @classmethod
    def json_data(cls, data=None, service_type=OK, status=200):
        """
        返回 response 格式化
        :param service_type: ret 内容
        :param data: 返回data内容
        :param status: 返回http状态码
        :return:
        """
        result = {
            'ret': service_type,
        }

        if status not in cls.STATUS_TYPE:
            result['ret'] = STATUS_CODE_ERROR
        if isinstance(data, (dict, list)):
            result['data'] = data

        return Response(data=result, status=status)
