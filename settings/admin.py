from django.contrib import admin
from .models import Course, CourseSection, Lesson, Profile

# Register your models here.
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

class CourseSectionInline(admin.TabularInline):
    model = CourseSection
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')
    inlines = [CourseSectionInline]

@admin.register(CourseSection)
class CourseSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    inlines = [LessonInline]

admin.site.register(Lesson)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'full_name',
        'phone',
        'location',
        'create_at'
    ]
    search_fields = [
        'user__username',
        'full_name',
        'phone'
    ]