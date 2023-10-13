#!/usr/bin/env python
# -*- coding: utf-8 -*-
from projectname.utils.helpers.logging_helper import LoggingHelper


class FirstCommandExample:
    def __init__(self, arguments: dict, environment_variables: dict):
        self.__logging = LoggingHelper.get_logger(logger_name='projectname')
        self.__arguments: dict = arguments
        self.__ENVIRONMENT_VARIABLES: dict = environment_variables

        self.__method_example()

    def __method_example(self):
        """

        :return:
        """
        self.__logging.info(f'FirstCommand with arguments "{self.__arguments}" and '
                            f'environment_variables "{self.__ENVIRONMENT_VARIABLES}" ')
