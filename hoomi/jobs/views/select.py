from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class SelectView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = request.user

        if user.job_id != 1:
            return render(
                request,
                "jobs/main.html",
                context={}
            )
        return redirect("jobs:select")

    def post(self, request, *args, **kwargs):
        user = request.user

        user.job_id = 2
        user.developer_set.create(
            skills=request.POST.getlist("list[]"),
            interest_company=[],
            theme=1,
        )
        user.save()
        return redirect("jobs:main")
