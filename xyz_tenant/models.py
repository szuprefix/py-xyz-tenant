# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from tenant_schemas.models import TenantMixin
from . import choices
from django.db import models
from xyz_util import modelutils

class Tenant(TenantMixin):
    class Meta:
        verbose_name_plural = verbose_name = '租户'

    name = models.CharField('名称', max_length=128)
    auto_create_schema = True

    def __unicode__(self):
        return self.name


class App(models.Model):
    class Meta:
        verbose_name_plural = verbose_name = "应用"
        unique_together = ('tenant', 'name')

    tenant = models.ForeignKey(Tenant, verbose_name=Tenant._meta.verbose_name, related_name="apps")
    name = models.CharField("名字", max_length=64, db_index=True, choices=choices.CHOICES_APPS)
    status = models.PositiveSmallIntegerField("状态", choices=choices.CHOICES_APP_STATUS,
                                              default=choices.APP_STATUS_INSTALL)
    settings = modelutils.JSONField('配置')
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    modify_time = models.DateTimeField("修改时间", auto_now=True)

    def __unicode__(self):
        return "%s 应用 %s" % (self.tenant, self.name)


