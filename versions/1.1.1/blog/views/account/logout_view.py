# Django imports
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import View


class UserLogoutView(View):
    """
     Logs user out of the dashboard.
    """
    template_name = 'account/logout.html'

    def get(self, request):
        logout(request)
        messages.success(request, "You have successfully logged out.")
        return render(request, self.template_name)

