from functools import reduce
from operator import add

from django.db import connection
from django.utils.deprecation import MiddlewareMixin

__author__ = 'Shafikur Rahman'

import time


class StatsMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        duration = time.time() - request.start_time
        n = len(connection.queries)
        db_queries = len(connection.queries) - n
        if db_queries:
            db_time = reduce(add, [float(q['time'])
                                   for q in connection.queries[n:]])
        else:
            db_time = 0.0

        # and back out python time
        python_time = request.start_time - db_time

        # Add the header.
        python_time = int(python_time * 1000)
        db_time = int(db_time * 1000)
        db_queries = db_queries

        response["X-Total-Time"] = int(duration * 1000)
        response["X-Python-Time"] = int(duration * 1000) - db_time
        response["X-DB-Time"] = db_time
        response["X-DB-Queries"] = db_queries

        return response
