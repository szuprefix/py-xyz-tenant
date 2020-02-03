# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals
from celery import shared_task

from celery.utils.log import get_task_logger

log = get_task_logger(__name__)

@shared_task(bind=True, time_limit=600)
def gen_tenant(self, data):
    from .models import Tenant
    Tenant(**data).save()
    return "success"

