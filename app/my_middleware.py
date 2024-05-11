import logging

logger = logging.getLogger(__name__)

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print('hehe', request)
        if 'facebook' in request.path and 'code' in request.GET:
            logger.info('Facebook callback received with code: %s', request.GET['code'])
        response = self.get_response(request)
        return response