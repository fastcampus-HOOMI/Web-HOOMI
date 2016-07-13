from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.conf import settings


class LoginView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                "users/login.html",
                context={},
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
                username=username,
                password=password,
        )

        if user:
            login(request, user)

            messages.add_message(
                    request,
                    messages.SUCCESS,
                    settings.LOGIN_SUCCESS_MESSAGE,
            )

            return redirect("jobs:job_history")

        messages.add_message(
            request,
            messages.ERROR,
            settings.LOGIN_FAIL_MESSAGE,
        )

        return redirect(reverse("users:login"))
