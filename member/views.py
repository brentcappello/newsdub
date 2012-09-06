from django.contrib import messages
from django.utils.translation import ugettext
from django.views.generic import UpdateView, FormView
from django.contrib.auth.models import User
from member.forms import ProfileForm, UserForm
from member.models import MemberProfile
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.forms import PasswordChangeForm

from registration.signals import *


def profileedit(request):
    instance_a = get_object_or_404(MemberProfile, user=request.user)
    instance_b = get_object_or_404(User, pk=request.user.id)

    a = ProfileForm(request.POST or None, instance=instance_a)
    b = UserForm(request.POST or None, instance=instance_b)

    if a.is_valid() and b.is_valid():
        a.save() and b.save()
        return HttpResponseRedirect('/dashboard/')


    return render(request, 'dashboard/profile-edit.html', {
        'form': a,
        'forms': b,
        })

def passchange(request):
    change_password_form = PasswordChangeForm(data=request.POST or None, user=request.user)

    if change_password_form.is_valid():
        change_password_form.save()
        return HttpResponseRedirect('/dashboard/')

    return render(request, 'registration/password_change_form.html', {
        'form':change_password_form,
        })


#def profileedit(request):
#
#    memprof = MemberProfile.objects.get(user=request.user)
#    userprof = User.objects.get(pk=request.user.id)
#
#    a = ProfileForm(instance=memprof)
#    b = UserForm(instance=userprof)
#
#    return render(request, 'dashboard/profile.html', {
#        'form': a,
#        'forms':b,
#        })
