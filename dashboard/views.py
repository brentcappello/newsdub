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

#class DashBoardView(LoginRequiredMixin, TemplateView):
#    pass

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'

    #Just a note: I could have also called the MemberProfile
    #objects directly in the template by using {{ user.get_profile.website }}

    def member_view(self):
        self.member = self.request.user.get_profile()
        return self.member

    def get_context_data(self, *args, **kwargs):
        context = super(DashboardView, self).get_context_data(*args, **kwargs)
        context['profile'] = self.member_view()
        return context



