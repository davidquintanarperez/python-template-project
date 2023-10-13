#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ProjectNameExit(SystemExit):
    def __init__(self, message: str):
        super().__init__(message)
