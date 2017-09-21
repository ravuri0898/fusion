from django.db import models
from django.core.urlresolvers import reverse

# TODO: These lists are not complete fully!

LEAVETYPE = (
    ('CL', 'Casual Leave'),
    ('COL', 'Commuted Leave'),
    ('EL', 'Earned Leave'),
    ('RH', 'Restricted Holiday'),
    ('SCL', 'Special Casual Leave'),
    ('VL', 'Vacation Leave'),
)

DESIGNATION = (
    ('driver', 'Driver'),
    ('ja', 'Junior Assistant'),
    ('sa', 'Senior Assistant'),
    ('jt', 'Junior Technician'),
    ('st', 'Senior Technician'),
    ('ar', 'Assistant Registrar'),
    ('dr', 'Deputy Registrar'),
    ('rr', 'Registrar'),
    ('Research Engineer', 'Research Engineer'),
    ('Assistant Professor', 'Assistant Professor'),
    ('Associate Professor', 'Associate Professor'),
    ('Professor', 'Professor'),
)

DEPARTMENT = (
    ('iwd', 'IWD'),
    ('et', 'Establishment'),
    ('library', 'Library'),
    ('pc', 'Placement Cell'),
    ('acad', 'Academics'),
    ('ns', 'Natural Science'),
    ('cse', 'CSE'),
    ('ece', 'ECE'),
    ('me', 'ME'),
    ('otd', 'Office of Dean'),
    ('fna', 'Finance and Accounts'),
    ('directorate', 'Directorate'),
)

AUTHDESIGNATION = (
    ('rr', 'Registrar'),
    ('director', 'Director'),
    ('ccc', 'Coordinator Computer Center'),
    ('wi', 'Workshop In-charge'),
    ('headns', 'HOD NS'),
    ('hodcse', 'HOD CSE'),
    ('hodece', 'HOD ECE'),
    ('hodme', 'HOD ME'),
    ('deanacad', 'Dean Academics'),
    ('deanstudents', 'Dean Students'),
    ('deanRSPC', 'Dean RSPC'),
)


class Employee(models.Model):
    empFirstName = models.CharField(max_length=36)
    empLastName = models.CharField(max_length=36)
    empEmail = models.CharField(max_length=36, unique=True)
    empPassword = models.CharField(max_length=36, null=False, default='pass')
    empDesignation = models.CharField(max_length=36, choices=DESIGNATION)
    empDepartment = models.CharField(max_length=36, choices=DEPARTMENT)

    def __str__(self):
        return self.empFirstName + "." + self.empLastName + "." + self.empEmail + "." + self.empPassword + "." + self.empDesignation + "." + self.empDepartment


class EmployeeLeaveBalance(models.Model):
    empID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    empCL = models.IntegerField()
    empCOL = models.IntegerField()
    empEL = models.IntegerField()
    empRH = models.IntegerField()
    empSCL = models.IntegerField()
    empVL = models.IntegerField()


class EmployeeLeaveDetails(models.Model):
    empID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    empLeaveType = models.CharField(max_length=5)
    empLeaveFrom = models.DateField()
    empLeaveTo = models.DateField()
    empLeaveDuration = models.IntegerField()
    empLeaveStatus = models.IntegerField(default=0)
    # Rejected: -1, Approved: 1, Pending: 0


class EmployeeStationLeave(models.Model):
    empLeaveID = models.ForeignKey(EmployeeLeaveDetails, on_delete=models.CASCADE)
    empStationLeave = models.BooleanField(default=False)
    empStationAddress = models.CharField(max_length=150)


class EmployeeLeaveAuthority(models.Model):
    authID = models.IntegerField(primary_key=True, auto_created=True)
    authDesignation = models.CharField(max_length=18, choices=AUTHDESIGNATION)
    authHeadID = models.ForeignKey(Employee, related_name='ELA_authHeadID')
    authActingID = models.ForeignKey(Employee, null=True, related_name='ELA_authActingID')
    empActingAuthStatus = models.BooleanField(default=False)


class EmployeeHierarchy(models.Model):
    empID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # For CL/RH:
    empHeadAuthID1 = models.ForeignKey(EmployeeLeaveAuthority, related_name='EH_empAuthID1')
    # For Other types of Leaves:
    empHeadAuthID2 = models.ForeignKey(EmployeeLeaveAuthority, related_name='EH_empAuthID2')


class Holidays(models.Model):
    HolidayType = models.CharField(max_length=3)
    HolidayFrom = models.DateField()
    HolidayTo = models.DateField()
