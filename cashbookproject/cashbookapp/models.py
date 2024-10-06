from django.db import models

# Create your models here.
class cash_entry(models.Model):
    name = models.CharField(max_length=256)
    amount = models.IntegerField()
    cash_choices = [
        ('cash_in', 'Cash In'),
        ('cash_out', 'Cash Out')        
    ]
    transaction_type = [
        ('upi', 'UPI'),
        ('cash', 'Cash')
    ]
    transaction_platform = [
        ('phonepe','PhonePe'),
        ('googlepay', 'Google Pay'),
        ('paytm','Paytm'),
    ]
    
    cash_type = models.CharField(max_length=10, choices=cash_choices, default='NULL')
    tran_type = models.CharField(max_length=50, choices=transaction_type, default='NULL')
    tran_plat = models.CharField(max_length=50, choices=transaction_platform, default='NULL')
    def __str__(self):
        return f"{self.name}"
    
