#!/usr/bin/env python
import pika


class Connection:
    def __init__(self, server_url):
        self.__connection = None
        params = pika.URLParameters(server_url)
        params.socket_timeout = 5
        self.__connection = pika.BlockingConnection(params)
        print(" [x] Created Connection")

    def conn(self):
        return self.__connection

    def __del__(self):
        if self.__connection is not None:
            self.__connection.close()
        self.__connection = None
        print(" [x] Closed Connection")
