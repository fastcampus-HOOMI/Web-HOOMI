from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, TemplateView
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.http import JsonResponse

from jobs.models import Resume
from users.models import User


class AjaxableResponseMixin(object):
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        response = super(AjaxableResponseMixin, self).form_invalid(form)

        if self.request.is_ajax():
            return JsonResponse(form.errors, status=400)
        else:
            return response


class ResumeCreateView(LoginRequiredMixin,
                       AjaxableResponseMixin,
                       CreateView):
    template_name = "jobs/main2.html"
    model = Resume
    fields = [
        "github_profile",
        "name",
        "user_image",
        "detail_job",

        "timeline_name",
        "timeline_job",
        "timeline_description",

        "profile_name",
        "profile_email",
        "profile_address",
        "profile_blog",

        "experiences",
        "educations",
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()

        return redirect("jobs:main")


class ResumeMypageView(LoginRequiredMixin, TemplateView):

    template_name = "profile/user_profile.html"

    def get_context_data(self, **kwargs):
        data = {
            "user": self.request.user.resume_set.first()
        }
        return data
