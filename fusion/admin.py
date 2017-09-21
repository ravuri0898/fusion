# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Employee, EmployeeLeaveAuthority, EmployeeLeaveDetails, EmployeeHierarchy, EmployeeLeaveBalance, EmployeeStationLeave, Holidays

admin.site.register(Employee)
admin.site.register(EmployeeLeaveAuthority)
admin.site.register(EmployeeLeaveBalance)
admin.site.register(EmployeeLeaveDetails)
admin.site.register(EmployeeHierarchy)
admin.site.register(EmployeeStationLeave)
admin.site.register(Holidays)
