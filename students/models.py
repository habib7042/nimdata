from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length = 255)
    aqaid_f = models.IntegerField()
    quran_t = models.IntegerField()
    arabic1 = models.IntegerField()
    arabic2 = models.IntegerField()
    bangla = models.IntegerField()
    english = models.IntegerField()
    math = models.IntegerField()
    gen_science = models.IntegerField()
    b_world = models.IntegerField()
    ict = models.IntegerField()
    gpa = models.CharField(max_length= 20)
    gread = models.CharField(max_length= 20)

    def __str__(self):
        return f'{self.roll} {self.name}'