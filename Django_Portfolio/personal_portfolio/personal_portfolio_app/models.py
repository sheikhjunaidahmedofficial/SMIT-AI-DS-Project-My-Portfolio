from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    intro = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    def __str__(self):
        return self.name


class About(models.Model):
    description = models.TextField()

    def __str__(self):
        return "About Me"


# class Education(models.Model):
#     degree = models.CharField(max_length=150)
#     institute = models.CharField(max_length=200)
#     start_year = models.PositiveIntegerField()
#     end_year = models.PositiveIntegerField()
#     cgpa = models.CharField(max_length=20, blank=True)
#     description = models.TextField(blank=True)

#     def __str__(self):
#         return self.degree

class Education(models.Model):

    EDUCATION_TYPE = [
        ('school', 'School'),
        ('college', 'College'),
        ('university', 'University'),
    ]

    degree = models.CharField(max_length=150)
    institute = models.CharField(max_length=200)

    education_type = models.CharField(
        max_length=15,
        choices=EDUCATION_TYPE,
        default='school'
    )

    start_year = models.PositiveIntegerField()
    end_year = models.PositiveIntegerField()

    cgpa = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    cgpa_scale = models.DecimalField(max_digits=4, decimal_places=2, default=4.00, blank=True, null=True)

    show_grade = models.BooleanField(default=True)
    grade = models.CharField(max_length=10, blank=True)

    show_marks = models.BooleanField(default=True) 

    obtained_marks = models.PositiveIntegerField(blank=True, null=True)
    total_marks = models.PositiveIntegerField(blank=True, null=True)

    description = models.TextField(blank=True)

    @property
    def percentage(self):
        if self.education_type == "university" and self.cgpa and self.cgpa_scale:
            return round((self.cgpa / self.cgpa_scale) * 100)

        if self.obtained_marks and self.total_marks:
            return round((self.obtained_marks / self.total_marks) * 100)

        return None

    def __str__(self):
        return self.degree


class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.PositiveIntegerField(help_text="0 - 100")
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)

    def __str__(self):
        return self.name


class CareerGoal(models.Model):
    description = models.TextField()

    def __str__(self):
        return "Career Goal"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technology = models.CharField(max_length=200)
    project_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name