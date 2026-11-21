from django.shortcuts import render, get_object_or_404
from settings.models import Course, Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def home(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    category = request.GET.get('category')
    search_query = request.GET.get('q')
    courses = Course.objects.all()
    category = request.GET.get('category')
    if category:
        courses = Course.objects.filter(category=category)
    else:
        courses = Course.objects.all()

    courses = Course.objects.all()
    if category:
        courses = courses.filter(category=category)

    if search_query:
        courses = courses.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )

    for course in courses:
        total_lessons = 0
        total_duration = 0
        
        sections = course.sections.prefetch_related('lessons').all()
        for section in sections:
            lessons = section.lessons.all()
            total_lessons += lessons.count()
            for lesson in lessons:
                if lesson.duration:
                    total_duration += int(lesson.duration)
        
        course.total_lessons = total_lessons
        course.total_duration = total_duration

    context = {
        'courses': courses,
        'selected_category': category,
        'search_query': search_query,
        'profile': profile,
    }
    return render(request, 'homepage.html', context)

@login_required
def course_list(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    category = request.GET.get('category')
    search_query = request.GET.get('q')

    filter_courses = Course.objects.all()

    if category:
        filter_courses = filter_courses.filter(category=category)

    if search_query:
        filter_courses = filter_courses.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )

    for course in filter_courses:
        total_lessons = 0
        total_duration = 0
        sections = course.sections.prefetch_related('lessons').all()
        for section in sections:
            lessons = section.lessons.all()
            total_lessons += lessons.count()
            for lesson in lessons:
                if lesson.duration:
                    total_duration += int(lesson.duration)
        
        course.total_lessons = total_lessons
        course.total_duration = total_duration

    context = {
        'course_list': filter_courses,
        'selected_category': category,
        'search_query': search_query,
        'profile': profile,
    }
    
    return render(request, 'courses.html', context)

@login_required
def course_detail(request, course_id):
    profile, created = Profile.objects.get_or_create(
        user = request.user
    )
    course = get_object_or_404(Course, pk=course_id)
    sections = course.sections.prefetch_related('lessons').all()

    total_lessons = 0
    total_duration = 0
    
    for section in sections:
        lessons = section.lessons.all()
        total_lessons += lessons.count()
        for lesson in lessons:
            if lesson.duration:
                total_duration += int(lesson.duration)

    related_courses = Course.objects.filter(category=course.category).exclude(id=course.id)[:3]

    context = {
        'profile':profile,
        'course': course,
        'sections': sections,
        'total_lessons': total_lessons,
        'total_duration': total_duration,
        'related_courses': related_courses,
    }
    return render(request, 'course_details.html', context)

@login_required
def about_page(request):
    profile, created = Profile.objects.get_or_create(
        user = request.user
    )
    context = {
        'profile': profile
    }
    return render(request, 'about.html', context)

@login_required
def contact_page(request):
    profile, created = Profile.objects.get_or_create(
        user = request.user
    )
    context = {
        'profile': profile
    }
    return render(request, 'contact.html',  context)