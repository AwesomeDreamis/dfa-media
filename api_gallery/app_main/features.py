from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    """Пользовательская пагинация"""
    page_size = 3

    def get_paginated_response(self, data):
        """
        Каким образом выводится информация о пагинации
        :param data: Выводящиеся объекты
        :return: Информация о пагинации
        """
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link(),
            },
            'count': self.page.paginator.count,
            'result': data,
        })
