from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


class JobHistory(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):

        if request.user.job.id == 1:
            return redirect("jobs:select_job")

        return render(
                request,
                "jobs/jobhistory.html",
                context={}
        )
