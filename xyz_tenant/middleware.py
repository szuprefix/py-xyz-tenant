# -*- coding:utf-8 -*- 
# author = 'denishuang'
from __future__ import unicode_literals

from tenant_schemas import middleware as tm


class TenantMiddleware(tm.TenantMiddleware):

    def hostname_from_request(self, request):
        return request.META.get('TENANT_SUBDOMAIN', '').lower()
