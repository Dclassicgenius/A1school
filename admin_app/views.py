from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from accounts.forms import UserForm, UserProfileForm
from django.contrib import messages


from accounts.models import Account, UserProfile
from admin_app.forms import QuestionForm, UpdateQuestionForm
from categories.models import Category, Subcategory
from quiz.models import Question, Result

# Create your views here.


def admin_dashboard(request):
    user_all = Account.objects.all()
    users =  user_all.exclude(is_superuser=True).count()

    context={
    'users':users,
    'courses':Category.objects.all().count(),
    'questions':Question.objects.all().count(),
    }
    return render(request, "admin/admin.html", context)

def admin_user_view(request):
    dict={
    'users':Account.objects.all().exclude(is_superuser=True).count(),
    }
    return render(request,'admin/admin_user.html',context=dict)


def admin_view_user_view(request):
    users= UserProfile.objects.all()
    return render(request,'admin/admin_view_users.html',{'users':users})

def admin_update_user(request, pk):
    
    userprofile = get_object_or_404(UserProfile, id=pk)
    user = Account.objects.get(id=userprofile.user_id)
    
    print(userprofile)
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            
            return redirect('admin_view_user_view')
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=userprofile)
    context = {
        'userprofile':userprofile,
        'user_form': user_form,
        'profile_form': profile_form,
        'userprofile': userprofile,
    }

   
    return render(request, 'admin/admin_update_user.html', context)


def admin_delete_user(request,pk):
    user=UserProfile.objects.get(id=pk)
    student = Account.objects.get(id=user.user_id)
    student.delete()
    user.delete()
    return redirect('admin_user_view')

def admin_view_user_marks_view(request):
    users= Account.objects.all().exclude(is_superuser=True)
    return render(request,'admin/admin_view_user_marks.html',{'users':users})

def admin_view_marks_view(request,pk):
    courses = Category.objects.all()
    level = Subcategory.objects.all()
    response =  render(request,'admin/admin_view_marks.html',{'courses':courses, 'level':level})
    response.set_cookie('user_id',str(pk))
    return response

def admin_check_marks_view(request,pk,sk):
    course = Category.objects.get(id=pk)
    level = Subcategory.objects.get(id=sk)
    user_id = request.COOKIES.get('user_id')
    user= Account.objects.get(id=user_id)

    results= Result.objects.all().filter(course=course, level=level).filter(user=user)
    return render(request,'admin/admin_check_marks.html',{'results':results})



def admin_question_view(request):
    
    return render(request,'admin/admin_questions.html')

def admin_view_question_view(request):
    courses=Category.objects.all()
    levels=Subcategory.objects.all()

    context =  {
        'courses':courses,
        'levels':levels,
    
    }
    return render(request,'admin/admin_view_question.html', context)


@login_required(login_url="login")
def admin_add_questions(request):
    questionForm=QuestionForm()
    if request.method=='POST':
        questionForm=QuestionForm(request.POST)
        if questionForm.is_valid():
            question=questionForm.save(commit=False)
            course=Category.objects.get(id=request.POST.get('courseID'))
            level=Subcategory.objects.get(id=request.POST.get('levelID'))
            question.course=course
            question.level=level
            question.save()     
        else:
            print("form is invalid")
        return redirect('admin_question_view')
    return render(request,'admin/add_questions.html',{'questionForm':questionForm})



def view_question_view(request, pk, sk):
    course=Category.objects.get(id=pk)
    level=Subcategory.objects.get(id=sk)
    questions=Question.objects.all().filter(course=course, level=level)
    context =  {
        'course':course,
        'level':level,
        'questions':questions,
    }
    
    return render(request,'admin/view_question.html', context)


def delete_question_view(request,pk):
    questions=Question.objects.get(id=pk)
    questions.delete()
    return redirect('admin_question_view')


def update_question(request, pk):
    obj = get_object_or_404(Question, id = pk)
    if request.method == 'POST':
        questionForm = UpdateQuestionForm(request.POST or None, instance = obj)
        if questionForm.is_valid():
            questionForm.save()
            return redirect('admin_question_view')
    else:
        questionForm = QuestionForm(instance=obj)
    context = {
        'questionForm': questionForm,
        'obj':obj,
        
    }
    return render(request, 'admin/update_question.html', context)

def playground(request):
    return render(request, 'admin/playground.html')

def admin_quiz(request):
    return render(request, 'admin/admin_quiz_playground.html')