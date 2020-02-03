# -*- coding:utf-8 -*-
from __future__ import unicode_literals

APP_STATUS_UNINSTALL = 0
APP_STATUS_INSTALL = 1

CHOICES_APP_STATUS = (
    (APP_STATUS_UNINSTALL, "未安装"),
    (APP_STATUS_INSTALL, "已安装"),
)

CHOICES_APPS = (
    ('school', '学校'),
    ('course', '课程'),
    ('exam', '测验'),
)