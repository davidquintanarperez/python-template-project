#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

from projectname.utils.constants.parser_constants import *
from projectname.utils.helpers.logging_helper import LoggingHelper
from projectname.utils.helpers.system_exit_helper import ProjectNameExit


class ValidateHelper:

    @staticmethod
    def validate_argument(argument_name: str, argument_value: str):
        logging = LoggingHelper.get_logger(logger_name='projectname')

        match argument_name:
            case 'argument_example':
                if not re.fullmatch(pattern=argument_example_regex, string=argument_value):
                    logging.info(argument_example_message)
                    raise ProjectNameExit(argument_example_message)
