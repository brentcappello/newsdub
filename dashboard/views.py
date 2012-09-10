from django.views.generic import TemplateView, UpdateView
from member.models import MemberProfile
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'






class AccountView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/profile.html'

    def member_view(self):
        self.member = self.request.user.get_profile()
        return self.member

    def get_context_data(self, *args, **kwargs):
        context = super(AccountView, self).get_context_data(*args, **kwargs)
        context['profile'] = self.member_view()
        return context

