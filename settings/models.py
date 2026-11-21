from django.db import models
from django.conf import settings

# Create your models here.
class Course(models.Model):
    # make choice for category
    CATEGORY_CHOICES = [
        ('frontend', 'Front-End Development'),
        ('backend', 'Back-End Development'),
        ('graphic-design', 'Graphic Design'),
        ('ux-ui', 'UI/UX Design'),
        ('mobile', 'Mobile App Development'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    rating = models.CharField(max_length=10, blank=True, null=True)
    duration = models.CharField(max_length=5, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    lessons = models.PositiveIntegerField(default=10, help_text="Total number of lessons")
    instructor_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title
    
class CourseSection(models.Model):
    course = models.ForeignKey(
    Course,
    on_delete=models.CASCADE,
    related_name='sections'
    )
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['order']

class Lesson(models.Model):
    section = models.ForeignKey(
    CourseSection,
    on_delete=models.CASCADE,
    related_name='lessons'
    )
    title = models.CharField(max_length=200)
    video_url = models.URLField(
        blank=True,
        null=True
    )
    duration = models.CharField(
        max_length=50,
        blank=True
    )
    order = models.PositiveIntegerField(default=1)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['order']
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    full_name = models.CharField(
        max_length=100,
        blank=True
    )
    phone = models.CharField(
        max_length=20,
        blank=True
    )
    location = models.CharField(
        max_length=100,
        blank=True
    )
    bio = models.CharField(
        max_length=500,
        blank=True
    )
    avatar = models.ImageField(
        upload_to='profile_pics/',
        null=True
    )
    create_at = models.DateTimeField(
        auto_now_add=True
    )
    update_at = models.DateTimeField(
        auto_now=True
    )
    def __str__(self):
        return self.user.username
    