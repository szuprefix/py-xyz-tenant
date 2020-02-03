# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.dispatch import receiver
from tenant_schemas.signals import post_schema_sync
from tenant_schemas.utils import tenant_context


@receiver(post_schema_sync)
def create_tenant_master(sender, **kwargs):
    from django.contrib.auth.models import User
    tenant = kwargs['tenant']
    with tenant_context(tenant):
        u = User(username='admin', first_name='管理员')
        u.set_password(tenant.schema_name)
        u.save()
        print u