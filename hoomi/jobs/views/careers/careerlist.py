from django.views.generic import View
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from django.contrib.auth.mixins import LoginRequiredMixin


class CareerList(LoginRequiredMixin, View):

    login_url = '/login/'

    def get(self, request, *args, **kwargs):

        if request.user.job.id == 1:
            return redirect("jobs:selectjob")

        return render(
                request,
                "jobs/careerlist.html",
                context={}
        )
