from django.contrib.auth.mixins import LoginRequiredMixin


class LoginRequiredMixin(LoginRequiredMixin):
    # TODO : pupup message need login

    login_url = '/login/'
