from rest_framework import status


class CleanHtmlException(Exception):
    """Handler for Clean Html Exception"""
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

