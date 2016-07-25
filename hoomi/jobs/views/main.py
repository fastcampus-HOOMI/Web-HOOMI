from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class MainView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        user = request.user

        if user.job_id == 1:
            return render(
                request,
                "jobs/select.html",
                context={},
            )

        context = {
            "name": "HeoJinHan",
            "birth": "1989.10.29",
            "email": "hjh5488@gmail.com",
        }

        return render(
            request,
            "jobs/main2.html",
            context=context,
        )
