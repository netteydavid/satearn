from django.db import models
from datetime import datetime
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import fields
from django.forms import ModelForm

# Represents a bounty created by a user and completed by another
class Bounty(models.Model):

    # Status constants
    NEW = 'NEW'
    WORKING = 'WORKING'
    COMPLETE = 'COMPLETE'
    CANCELLED = 'CANCELLED'
    # The statuses a bounty can take on
    BOUNTY_STATUS = [
        (NEW, 'New'), 
        (WORKING, 'Working'), 
        (COMPLETE, 'Complete'), 
        (CANCELLED, 'Canceled')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    reward = models.IntegerField()
    due_date = models.DateTimeField()
    created_on = models.DateTimeField(default=datetime.now(), editable=False)
    status = models.CharField(max_length=10, choices=BOUNTY_STATUS, default=NEW)
    assigned_to = models.ForeignKey(
        get_user_model(), 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='assignments', 
        related_query_name='assignment'
    )
    completed_on = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.title

# Represents an invoice created to pay for a bounty
class Invoice(models.Model):
    invoice = models.CharField(max_length=200)
    bounty = models.ForeignKey(Bounty, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(default=datetime.now(), editable=False)

    def __str__(self) -> str:
        return self.invoice

class BountyForm(ModelForm):
    class Meta:
        model = Bounty
        fields = ['title', 'description', 'reward', 'due_date']
        localized_fields = ('due_date',)