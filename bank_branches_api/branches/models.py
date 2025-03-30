from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Branch(models.Model):
    branch = models.CharField(max_length=200)
    bank = models.ForeignKey(Bank, related_name='branches', on_delete=models.CASCADE)
    ifsc = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return f"{self.branch} - {self.bank.name}"  