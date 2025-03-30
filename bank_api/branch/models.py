from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length=255)
    
class Branch(models.Model):
    bank = models.ForeignKey(Bank, related_name="branches", on_delete=models.CASCADE)
    branch = models.CharField(max_length=255)
    ifsc = models.CharField(max_length=20)
    address = models.TextField(default="Unknown")  # Default value added
    city = models.CharField(max_length=100, default="Unknown")
    district = models.CharField(max_length=100, default="Unknown")
    state = models.CharField(max_length=100, default="Unknown")
    bank_name = models.CharField(max_length=255, default="Unknown") 

    class Meta:
        db_table = "branch_branch"

    def __str__(self):
        return f"{self.branch} - {self.city}, {self.state}"
