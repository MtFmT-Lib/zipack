# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-2.0

"""
Package tool
~~~~~~~~~~~~

 Package tool

 File: action.py
 Desc: 支持的动作
 Date: 2023-06-18
 Auth: XiangYang<hinata.hoshino@foxmail.com>

"""
from abc import ABCMeta, abstractmethod


class IAction:
    """
    动作需要实现的接口
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def run(self):
        """
        运行action
        """
        pass
