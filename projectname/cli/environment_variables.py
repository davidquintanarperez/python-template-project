#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


class EnvironmentVariables:
    def __init__(self):
        self.__environment_variables: dict = dict()

    def get_environment_variables(self, command: str = str()) -> dict:
        match command:
            case 'first-command-example':
                self.__environment_variables['PATH'] = os.environ['PATH']
            case _:
                pass

        return self.__environment_variables
