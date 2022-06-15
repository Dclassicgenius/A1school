from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from accounts.models import Account

from categories.models import Category, Subcategory
from quiz import models as QMODEL
from quiz.models import Question, Result

# Create your views here.

@login_required(login_url="login")
def html(request):
    course_html = get_object_or_404(Category, category_name='HTML')

    level = Subcategory.objects.all()
    context = {
        'course_html':course_html,
        'level':level,
    }

    return render(request, 'quizzes/html.html', context)


@login_required(login_url="login")
def css(request):
    course_css = get_object_or_404(Category, category_name='CSS')

    level = Subcategory.objects.all()
    context = {
        'course_css':course_css,
        'level':level,
    }

    return render(request, 'quizzes/css.html', context)
    

@login_required(login_url="login")
def js(request):
    course_js = get_object_or_404(Category, category_name='JS')

    level = Subcategory.objects.all()
    context = {
        'course_js':course_js,
        'level':level,
    }

    return render(request, 'quizzes/js.html', context)


@login_required(login_url="login")
def take_test(request, pk, sk):
    
    course= Category.objects.get(id=pk)
    level = Subcategory.objects.get(id=sk)
    total_questions=Question.objects.all().filter(course=course, level=level).count()
    questions_all=Question.objects.all().filter(course=course, level=level)
    total_marks=0
    for q in questions_all:
        total_marks=total_marks + q.marks
    
    context = {
        'total_questions':total_questions,
        'total_marks':total_marks,
        'level':level,
        'course':course,
    }
    
    return render(request,'quizzes/take_test.html', context)

@login_required(login_url="login")
def start_test(request, pk, sk):
    course= Category.objects.get(id=pk)
    level = Subcategory.objects.get(id=sk)
    questions=Question.objects.all().filter(course=course, level=level)

    if request.method=='POST':
        pass

    context = {'course':course,'questions':questions, 'level':level}

    response= render(request,'quizzes/questions.html', context)
    response.set_cookie('level_id',level.id)
    response.set_cookie('course_id',course.id)

    return response


# def result(request, course_id, level_id):
#     if request.COOKIES.get('level_id') is not None and request.COOKIES.get('course_id') is not None:
#         level_id = request.COOKIES.get('level_id')
#         course_id = request.COOKIES.get('course_id')

#         course = Category.objects.get(id=course_id)
#         level=Subcategory.objects.get(id=level_id)
        
#         score=0
#         total_marks=0
#         questions=Question.objects.all().filter(level=level, course=course)

#         for i in range(len(questions)):
            
#             total_marks = total_marks + questions[i].marks
#             selected_ans = request.COOKIES.get(str(i+1))
#             print(selected_ans)
#             actual_answer = questions[i].answer
#             if selected_ans == actual_answer:
#                 score = score + questions[i].marks
        
        
#         user = Account.objects.get(id=request.user.id)
        
#         # result = QMODEL.Result()
#         # result.marks=score
#         # result.course=course
#         # result.level=level
#         # result.user=user
#         # result.save()
#         results= Result.objects.all().filter(level=level, course=course).filter(user=user)

#         return render(request,'quizzes/results.html',{'total_marks':total_marks, 'course':course, 'level':level, 'result':results,})


def feedback(request, course_id, level_id):
    if request.COOKIES.get('level_id') is not None and request.COOKIES.get('course_id') is not None:
        level_id = request.COOKIES.get('level_id')
        course_id = request.COOKIES.get('course_id')
        questions=request.COOKIES.get('questions')

        course = Category.objects.get(id=course_id)
        level=Subcategory.objects.get(id=level_id)
        
        score=0
        total_marks=0
        user_ans = []
        questions=Question.objects.all().filter(level=level, course=course)

        for i in range(len(questions)):
            
            total_marks = total_marks + questions[i].marks
            selected_ans = request.COOKIES.get(str(i+1))
            user_ans.append(selected_ans)
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                score = score + questions[i].marks
        
        percentage = (score/total_marks)*100

        user = Account.objects.get(id=request.user.id)
        
        result = QMODEL.Result()
        result.marks=score
        result.course=course
        result.level=level
        result.user=user
        result.save()
        results= Result.objects.all().filter(level=level, course=course).filter(user=user)
        context = {
            'questions':questions,
            'results':results, 
            'total_marks':total_marks, 
            'course':course, 
            'level':level,
            'user_ans':user_ans,
            'zipped':zip(questions, user_ans),
            'percentage':percentage,
            'score':score,
        }

        return render(request,'quizzes/feedback.html', context)
