import logging

logging.basicConfig(filename='access.log', level=logging.INFO)


class RequestLoggerMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        log_message = f"{request.path}"
        logging.info(log_message)
        response = self.get_response(request)
        return response
