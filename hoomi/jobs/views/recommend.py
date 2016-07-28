from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from jobs.models import Developer
from jobs.models import Occupation


class RecommendView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, *args, **kwargs):

        return render(
                request,
                "jobs/recommend.html",
                context={}
        )
