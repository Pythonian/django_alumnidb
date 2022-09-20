from django.db import models
from datetime import date
from django.conf import settings


class Faculty(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    YEAR_RANGE = (
        ('2010-2011', '2010-2011'),
        ('2011-2012', '2011-2012'),
        ('2012-2013', '2012-2013'),
        ('2013-2014', '2013-2014'),
        ('2014-2015', '2014-2015'),
        ('2015-2016', '2015-2016'),
        ('2016-2017', '2016-2017'),
        ('2017-2018', '2017-2018'),
        ('2018-2019', '2018-2019'),
        ('2019-2020', '2019-2020'),
        ('2020-2021', '2020-2021'),
        ('2021-2022', '2021-2022'),
    )

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=150)
    date_of_birth = models.DateField()
    phonenumber = models.CharField(max_length=18)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    about = models.TextField()
    passport = models.ImageField(upload_to='passports')

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    location = models.CharField(max_length=100, blank=True)
    nationality = models.CharField(max_length=100, blank=True)
    year_of_admission = models.CharField(max_length=10, choices=YEAR_RANGE)
    year_of_graduation = models.CharField(max_length=10, choices=YEAR_RANGE)
    post_held = models.CharField(max_length=150, blank=True)
    project_topic = models.CharField(max_length=250, blank=True)
    memorable_moment = models.TextField(blank=True)

    def __str__(self):
        return self.fullname

    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def save_profile(sender, instance, **kwargs):
#     instance.profile.save()
