import logging

logger = logging.getLogger(__name__)


class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = request.META.get('HTTP_X_REQUEST_ID', 'N/A')
        template = "Request | ID: {} | Method: {} | Path: {} | Headers: {}"
        logger.info(template.format(
            request_id,
            request.method,
            request.path,
            dict(request.headers)
        ))

        response = self.get_response(request)

        response_template = "Response | ID: {} | Status: {} | Headers: {}"
        logger.info(response_template.format(
            request_id,
            response.status_code,
            dict(response.headers)
        ))

        return response
