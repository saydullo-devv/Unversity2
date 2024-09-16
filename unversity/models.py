from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


    def __str__(self):
        return f"{self.first_name},{self.last_name}"


class Subject(models.Model):
    name =  models.CharField(max_length=255)
    # kafedra = models.CharField(max_length=255)
    # teacher =models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    # on_delete-> CASCADE, PROTECT, SET_NULL

    def __str__(self):
        return self.name

class Kafedra(models.Model):
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    kafedra = models.OneToOneField(Kafedra, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name},{self.last_name}"



class Group(models.Model):
    name = models.CharField(max_length=255)
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Faculted(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name