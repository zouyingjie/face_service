# -*- coding: utf-8 -*-
# __author__ = zouyingjie

from __future__ import division, unicode_literals, print_function
import os

from django.core.management import BaseCommand

from libs.datetimes import datetime_now, datetime_delta, date_to_str
from settings.settings import PROJECT_HOME


class Command(BaseCommand):
    def handle(self, *args, **options):
        # 清理前一天的图片
        now = datetime_now()
        if now.hour != 1:
            return
        yesterday = datetime_delta(now, days=-1)
        path = "%s/data/image/%s*" % (PROJECT_HOME, date_to_str(yesterday.date()))
        shell_command = "rm -rf %s" % path
        os.system(shell_command)
