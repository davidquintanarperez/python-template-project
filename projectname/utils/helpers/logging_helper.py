#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging


class LoggingHelper(logging.Formatter):
    @staticmethod
    def get_formats() -> dict:
        """

        :return: Logging formats
        :rtype: dict
        """
        white: str = '\x1b[38;5;7m'
        green = '\x1B[32m'
        yellow = '\x1B[33m'
        red = '\x1B[31m'
        bold_red = '\x1B[31;1m'
        logging_format = '[{asctime}] [{name}] [{filename}:{lineno}] [{levelname}]: {message}'
        # logging_format = '{asctime} - {name} - {filename}:{lineno} - {levelname}: {message}'

        formats = {
            logging.DEBUG: green + logging_format,
            logging.INFO: white + logging_format,
            logging.WARNING: yellow + logging_format,
            logging.ERROR: red + logging_format,
            logging.CRITICAL: bold_red + logging_format
        }

        return formats

    def format(self, record) -> str:
        """

        :param record: Record
        :return: str
        """
        formats: dict = LoggingHelper.get_formats()
        log_fmt = formats.get(record.levelno)
        formatter = logging.Formatter(log_fmt, style='{')

        return formatter.format(record)

    @staticmethod
    def create_logger(logger_name: str) -> logging.getLogger():
        """

        :param logger_name: Logger name
        :type logger_name: str
        :return: Logger
        :rtype: logging.getLogger()
        """
        project_logger = logging.getLogger(logger_name)
        project_logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        ch.setFormatter(LoggingHelper())

        project_logger.addHandler(ch)

        return project_logger

    @staticmethod
    def get_logger(logger_name: str) -> logging.getLogger():
        """

        :param logger_name: Logger name
        :type logger_name: str
        :return: Logger
        :rtype: logging.getLogger()
        """
        if logger_name in logging.Logger.manager.loggerDict.keys():
            project_logger = logging.getLogger(logger_name)
        else:
            project_logger = LoggingHelper.create_logger(logger_name=logger_name)

        return project_logger
