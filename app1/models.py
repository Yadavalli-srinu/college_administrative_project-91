from django.db import models

class department_model(models.Model):
    Department = models.CharField(max_length=50)
    Code = models.CharField(max_length=50)

    def __str__(self):
        return self.Department


class hod_model(models.Model):
    Name = models.CharField(max_length=50)
    Department = models.OneToOneField(department_model, on_delete=models.CASCADE)
    Phone = models.BigIntegerField()

    def __str__(self):
        return self.Name


class professor_model(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.BigIntegerField()
    Department = models.ForeignKey(department_model, on_delete=models.CASCADE)
    Subject = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class student_model(models.Model):
    Name = models.CharField(max_length=50)
    Register_id = models.CharField(max_length=50)
    Department = models.ForeignKey(department_model, on_delete=models.CASCADE)
    HOD = models.ForeignKey(hod_model, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name