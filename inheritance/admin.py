from django.contrib import admin
from .models import Abstractbaseclass, Multibaseclass, Multitabel, ProxyBaseclass,Proxyinheritance

# Register your models here.
admin.site.register(Abstractbaseclass)
admin.site.register(Multitabel)
admin.site.register(Multibaseclass)
admin.site.register(Proxyinheritance)
admin.site.register(ProxyBaseclass)