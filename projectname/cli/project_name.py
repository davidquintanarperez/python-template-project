#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Developer Name'
__authors__ = ['First author name', 'Second author name', 'etc']
__contact__ = 'mail@example.com'
__copyright__ = 'Copyright 2023, David Quintanar Pérez'
__credits__ = ['First author', 'Second author', 'etc']
__date__ = 'YYYY/MM/DD'
__deprecated__ = False
__email__ = 'mail@example.com'
__license__ = 'GPLv3'
__maintainer__ = 'Developer Name'
__status__ = 'Production|Prototype|etc'
__version__ = '0.0.1'

from projectname.core.firtscommand.first_command import FirstCommandExample
from projectname.cli.environment_variables import EnvironmentVariables
from projectname.utils.helpers.logging_helper import LoggingHelper
from projectname.cli.parser import Parser


class ProjectName:
    def __init__(self):
        self.__logging = LoggingHelper.get_logger(logger_name='projectname')

        self.__parser: Parser = Parser()
        self.__arguments: dict = self.__parser.get_arguments()
        self.__command = self.__arguments['command']
        self.__environment_variables: EnvironmentVariables = EnvironmentVariables()
        self.__ENVIRONMENT_VARIABLES: dict = self.__environment_variables.get_environment_variables(
            command=self.__command
        )

        self.__main_flow()

    def __main_flow(self):
        self.__print_banner()

        match self.__command:
            case 'first-command-example':
                FirstCommandExample(arguments=self.__arguments, environment_variables=self.__ENVIRONMENT_VARIABLES)
            case 'second-command-example':
                pass

    def __print_banner(self):
        arguments = [f'{argument_name}: {argument_value}' for argument_name, argument_value in self.__arguments.items()]
        arguments = "\n".join(arguments)

        self.__logging.info(f'''
===========================================================
> Project name
===========================================================

{arguments}

===========================================================

        ''')


if __name__ == '__main__':
    ProjectName()
