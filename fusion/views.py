from django.shortcuts import render, redirect, get_object_or_404
from fusion.forms import *
from fusion.models import *


loginform = LoginForm()

def index(request):
    context = {}

    return render(request, "fusion/general/index1.html", context)
    # return render(request, "fusion/general/index.html", context)


def dashboard(request, emp_id):
    employeePK = emp_id
    dbUser = get_object_or_404(Employee, pk=employeePK)
    userFirstName = str(dbUser.empFirstName)
    userLastName = str(dbUser.empLastName)
    userEmail = str(dbUser.empEmail)
    userDepartment = str(dbUser.empDepartment)
    userDesignation = str(dbUser.empDesignation)

    leave_type = ['Casual Leave', 'Commuted Leave', 'Earned Leave', 'Restricted Holiday', 'Sp. Casual Leave',
                  'Vacation Leave']

    context = {'leave_type': leave_type,
               'employeePK': employeePK,
               'userFirstName': userFirstName,
               'userLastName': userLastName,
               'userEmail': userEmail,
               'userDesignation': userDesignation,
               'userDepartment': userDepartment,
               'loginform': loginform,
               }

    return render(request, "fusion/dashboard/dashboard.html", context)


def profile(request, emp_id):
    employeePK = emp_id
    dbUser = get_object_or_404(Employee, pk=employeePK)
    userFirstName = str(dbUser.empFirstName)
    userLastName = str(dbUser.empLastName)
    userEmail = str(dbUser.empEmail)
    userDepartment = str(dbUser.empDepartment)
    userDesignation = str(dbUser.empDesignation)

    leave_type = ['Casual Leave', 'Commuted Leave', 'Earned Leave', 'Restricted Holiday', 'Sp. Casual Leave',
                  'Vacation Leave']

    context = {'leave_type': leave_type,
               'employeePK': employeePK,
               'userFirstName': userFirstName,
               'userLastName': userLastName,
               'userEmail': userEmail,
               'userDesignation': userDesignation,
               'userDepartment': userDepartment,
               'loginform': loginform,
               }

    return render(request, "fusion/eisModule/profile.html", context)


def leave(request, emp_id):
    employeePK = emp_id
    dbUser = get_object_or_404(Employee, pk=employeePK)
    userFirstName = str(dbUser.empFirstName)
    userLastName = str(dbUser.empLastName)
    userEmail = str(dbUser.empEmail)
    userDepartment = str(dbUser.empDepartment)
    userDesignation = str(dbUser.empDesignation)

    leave_type = ['Casual Leave', 'Commuted Leave', 'Earned Leave', 'Restricted Holiday', 'Sp. Casual Leave',
                  'Vacation Leave']

    context = {'leave_type': leave_type,
               'employeePK': employeePK,
               'userFirstName': userFirstName,
               'userLastName': userLastName,
               'userEmail': userEmail,
               'userDesignation': userDesignation,
               'userDepartment': userDepartment,
               'loginform': loginform,
               }

    return render(request, "fusion/leaveModule/leave.html", context)


def leaveApplicationForm(request):
    if loginform.is_valid():
        dbUser = loginform.clean_message()
        userID = str(dbUser.pk)

        context = {'user_name': userID,
                   'loginform': loginform,
                   'dbUser': dbUser
                   }

        leaveapplicationform = leaveApplicationForm(request.POST)

    return render(request, "fusion/leaveModule/leave.html", context)


def login(request):
    loginform = LoginForm(request.POST)

    if loginform.is_valid():
        dbUser = loginform.clean_message()
        userID = str(dbUser.pk)

        context = {'user_name': userID,
                   'loginform': loginform,
                   'dbUser': dbUser
                   }
        return redirect('/fusion/dashboard/' + context['user_name'], context)

    else:
        context = {'loginform': loginform}
        return render(request, 'fusion/general/login.html', context)


def temp(request):
    return render(request, 'fusion/general/base.html', {})
