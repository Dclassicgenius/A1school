from django.shortcuts import get_object_or_404, redirect, render
from accounts.forms import UserForm, UserProfileForm
from accounts.models import Account, UserProfile

from categories.models import Category, Subcategory
from quiz.models import Question, Result

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def user_dashboard_view(request):
    context={
    
    'courses':Category.objects.all().count(),
    'questions':Question.objects.all().count(),
    'userprofile':UserProfile.objects.get(user_id=request.user.id),
    }
    return render(request,'user/user_dashboard.html',context)


@login_required(login_url="login")
def quiz_playground(request):
    context={
    
    'courses':Category.objects.all().count(),
    'questions':Question.objects.all().count(),
    'userprofile':UserProfile.objects.get(user_id=request.user.id),
    }
    
    return render(request,'user/quiz_playground.html', context)


def user_marks_view(request):
    courses = Category.objects.all()
    levels = Subcategory.objects.all()
    context = {
        'courses':courses, 
        'levels':levels,
        'userprofile':UserProfile.objects.get(user_id=request.user.id),
    }
    return render(request,'user/user_marks.html', context)


def check_marks_view(request,pk, sk):
    course=Category.objects.get(id=pk)
    level=Subcategory.objects.get(id=sk)
    user = Account.objects.get(id=request.user.id)
    results= Result.objects.all().filter(course=course, level=level).filter(user=user)

    context={
        'results':results,
        'userprofile':UserProfile.objects.get(user_id=request.user.id),
    }

    return render(request,'user/check_marks.html',context)


@login_required(login_url='login')
def edit_profile(request):

    
    userprofile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('edit_profile')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=userprofile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }
    return render(request, 'user/edit_profile.html', context)


@login_required(login_url='login')
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = Account.objects.get(username__exact=request.user.username)

        if new_password == confirm_password:
            success = user.check_password(current_password)
            if success:
                user.set_password(new_password)
                user.save()
                # auth.logout(request)
                messages.success(request, 'Password updated successfully.')
                return redirect('change_password')
            else:
                messages.error(request, 'Please enter valid current password')
                return redirect('change_password')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('change_password')
    return render(request, 'user/change_password.html', context={'userprofile':UserProfile.objects.get(user_id=request.user.id),})
