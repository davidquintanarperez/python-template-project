#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

from projectname.utils.helpers.validate_helper import ValidateHelper


class Parser:
    def __init__(self):
        self.__parser: argparse.ArgumentParser = Parser.create_parser()
        self.__sub_parser = self.__crete_sub_parser()

        self.__create_commands()
        self.__validate_arguments()

    @staticmethod
    def create_parser() -> argparse.ArgumentParser:
        """

        :return: ArgumentParser
        :rtype: argparse.ArgumentParser
        """
        parser: argparse.ArgumentParser = argparse.ArgumentParser(
            prog='Project Name',
            description='What the program does.',
            epilog='Text at the bottom of help (parser).'
        )

        return parser

    def __crete_sub_parser(self):
        """

        :return: SubParser
        :rtype: argparse._SubParser
        """
        sub_parser = self.__parser.add_subparsers(
            title='command',
            description='Valid subcommands.',
            dest='command',
            required=False,
            help='Valid subcommands.'
        )

        return sub_parser

    def __create_firs_command(self) -> None:
        """

        :return: Nothing
        :rtype: None
        """
        first_command = self.__sub_parser.add_parser(
            'first-command-example',
            help='Help of command.',
            description='Description of command.'
        )

        first_command.add_argument(
            '--argument_example',
            default='example_value',
            type=str,
            required=True,
            help='Text at the bottom of help (argument).'
        )

    def __create_second_command(self) -> None:
        """

        :return: Nothing
        :rtype: None
        """
        first_command = self.__sub_parser.add_parser(
            'second-command-example',
            help='Help of command.',
            description='Description of command.'
        )

        first_command.add_argument(
            '--argument_example',
            default='example_value',
            type=str,
            required=False,
            help='Text at the bottom of help (argument).'
        )

    def __create_commands(self) -> None:
        """

        :return: Nothing
        :rtype: None
        """
        self.__create_firs_command()
        self.__create_second_command()

    def __validate_arguments(self) -> None:
        """

        :return: Nothing
        :rtype: None
        """
        arguments: argparse.Namespace = self.__parser.parse_args()

        for argument_name, argument_value in vars(arguments).items():
            ValidateHelper.validate_argument(argument_name=argument_name, argument_value=argument_value)

    def get_arguments(self) -> dict:
        """

        :return: Arguments
        :rtype: dict
        """
        return vars(self.__parser.parse_args())
