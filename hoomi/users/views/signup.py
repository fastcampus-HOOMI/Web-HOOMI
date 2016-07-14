from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse


class SignupView(View):

    def get(self, request, *args, **kwargs):
        return render(
                request,
                "users/signup.html",
                context={}
        )

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")

        # TODO : need to check data revevancy
        user = get_user_model().objects.create_user(
                username=username,
                password=password,
                email=username,
                first_name=firstname,
                last_name=lastname,
        )

        return redirect(reverse("users:login"))
