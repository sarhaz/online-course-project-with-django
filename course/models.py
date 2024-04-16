from django.db import models


class Speciality(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/speciality/')
    last_updated = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    class PriceType(models.TextChoices):
        dollars = "Dollars", "$"
        sums = "Sum", "sum"

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='media/course/')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    active_users = models.CharField(default=0)
    price_type = models.CharField(max_length=10, choices=PriceType.choices)
    rating_users = models.CharField(max_length=5)
    last_updated = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)  # Use auto_now_add=True for created date

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/teacher/')
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    x_link = models.URLField(null=True, blank=True)
    l_link = models.URLField(null=True, blank=True)
    m_link = models.URLField(null=True, blank=True)
    last_updated = models.DateField(auto_now=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
