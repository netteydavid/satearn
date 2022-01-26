from unicodedata import category
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

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

    # Category Constants
    ART = 'ART'
    WRITING = 'WRITING'
    AUDIO = 'AUDIO'
    TECH = 'TECHNOLOGY'
    VIDEO = 'VIDEO'
    BUSINESS = 'BUSINESS'
    LIFESTYLE = 'LIFESTYLE'
    EDUCATION = 'EDUCATION'
    MISC = 'MISC'
    # The categories a bounty can have
    CATEGORIES = [
        (MISC, 'Miscellaneous'),
        (ART, 'Visual Arts'),
        (AUDIO, 'Audio and Music'),
        (BUSINESS, 'Business and Marketing'),
        (EDUCATION, 'Education'),
        (LIFESTYLE, 'Lifestyle'),
        (TECH, 'Technology'),
        (VIDEO, 'Video and Editing'),
        (WRITING, 'Writing and Literature'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=CATEGORIES, default=MISC)
    reward = models.IntegerField()
    due_date = models.DateTimeField()
    created_on = models.DateTimeField(default=datetime.now(), editable=False)
    status = models.CharField(max_length=10, choices=BOUNTY_STATUS, default=NEW)
    assigned_to = models.ForeignKey(
        get_user_model(), 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='assignments', 
        related_query_name='assignment'
    )
    completed_on = models.DateTimeField(null=True, blank=True)
    tags = models.TextField(max_length=500, blank=True)

    #TODO: Bounty categories

    def __str__(self) -> str:
        return self.title

# Represents an invoice created to pay for a bounty
class Invoice(models.Model):
    invoice = models.CharField(max_length=200)
    bounty = models.ForeignKey(Bounty, on_delete=models.SET_NULL, null=True)
    created_on = models.DateTimeField(default=datetime.now(), editable=False)

    def __str__(self) -> str:
        return self.invoice

class Application(models.Model):
    bounty = models.ForeignKey(Bounty, on_delete=models.SET_NULL, null=True)
    applicant = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_on = models.DateTimeField(default=datetime.now(), editable=False)