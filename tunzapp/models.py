from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Profile(models.Model):
    full_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='profile', null=True)

    def __str__(self):
        return self.full_name
    
    
class FinancialNeed(models.Model):
    needs = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return self.needs



class Child(models.Model):
    gender = (
        ('Male','Male'),
        ('Female','Female'),
    )
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='profiles/', default="/default.jpg")
    gender = models.CharField(max_length=50, choices=gender, null=True, blank=True)
    age = models.IntegerField(default=0)
    family_members = models.IntegerField(default=0)
    bio = models.TextField()
    location = models.CharField(max_length=150, blank=True)
    school_grade = models.CharField(max_length=100)
    school = models.CharField(max_length=200)
    class_overall = models.CharField(max_length=100)
    dreams = models.CharField(max_length=255)
    needs = models.ManyToManyField(FinancialNeed)
    fee_amount = models.IntegerField(default=20000)
    donors = models.ManyToManyField('Donor', related_name='contributors')

    def __str__(self):
        return self.last_name

    def remaining_amount(self):
        
        transactions = Donor.objects.filter(child=self)
        total_donations =0
        
        for transaction in transactions:
            total_donations += transaction.amount
            
        return self.fee_amount -total_donations    
    
    def total_transactions(self):
        
        transactions = Donor.objects.filter(child=self)
        
        return len(transactions)



class Donor(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    name= models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    donated_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name   

