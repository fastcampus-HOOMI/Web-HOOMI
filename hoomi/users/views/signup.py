from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.contrib import messages
from django.conf import settings


class SignupView(TemplateView):
    template_name = "users/signup.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")

        check_user = authenticate(
            username=username,
            password=password,
        )

        if check_user:
            messages.add_message(
                request,
                messages.ERROR,
                settings.SIGNUP_DUPLICATE_MESSAGE,
            )
            return redirect(reverse("users:login"))

        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            email=username,
            first_name=firstname,
            last_name=lastname,
        )

        return redirect(reverse("users:login"))
