from django.contrib import messages
from django.utils.translation import ugettext
from django.views.generic import UpdateView

from member.forms import ProfileForm
from member.models import MemberProfile

from registration.signals import *


class ProfileView(UpdateView):
    template_name = 'dashboard/profile.html'
    model = MemberProfile
    form_class = ProfileForm
    success_url = "/dashboard/"

    def get(self, *args, **kwargs):
        self.kwargs['pk'] = self.request.user.get_profile().id
        return super(ProfileView, self).get(*args, **kwargs)

    def post(self, *args, **kwargs):
        self.kwargs['pk'] = self.request.user.get_profile().id
        r = super(ProfileView, self).post(*args, **kwargs)
        if 300 < r.status_code < 400:
            messages.success(self.request, ugettext(u"Profile successfully updated."), fail_silently=True)
        return r

