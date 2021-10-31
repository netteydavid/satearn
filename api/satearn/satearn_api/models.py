from django.db import models
import uuid

# Abstract class representing an account
class Account(models.Model):
    account_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    email = models.CharField(unique=True, max_length=30)

    class Meta:
        abstract = True

# Represents an earner who compelte bounties
class Earner(Account):
    first_name = models.CharField(unique=True, max_length=50)
    last_name = models.CharField(unique=True, max_length=50)
    # This can be websites, Github and Gitlab profile links
    portfolio_links = models.TextField(blank=True)
    # In Satoshis
    balance = models.IntegerField()

# Represents an organization or business making bounties
class Organization(Account):
    name = models.CharField(unique=True, max_length=50)
    # TODO: Add pro feature later

# A task or tasks to be completed by an earner
class Bounty(models.Model):

    # The current status of the bounty
    class Status(models.IntegerChoices):
        # The bounty is available to be signed up for by an earner
        AVAILABLE = 1
        # The bounty is being worked on by an earner
        WORKING = 2
        # The bounty has been completed by an earner, but
        # not paid for by an organization
        COMPLETE = 3
        # The bounty is complete and paid for by an organization
        PAID = 4
        # The bounty has been cancelled by the organization
        CANCELLED = 5

    bounty_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    title = models.CharField(unique=True, max_length=50)
    description = models.TextField(blank=True)
    # In Satoshis
    reward = models.IntegerField()
    created_by = models.ForeignKey(Organization, on_delete=models.CASCADE)
    # Github and Gitlab repository links
    project_link = models.CharField(max_length=50)
    due_date = models.DateTimeField()
    created_on = models.DateTimeField()
    completed_on = models.DateTimeField(null=True)
    earner = models.ForeignKey(Earner, null=True, on_delete=models.SET_NULL)
    status = models.IntegerField(choices=Status.choices)
    # Link to document(s) for the earner to sign
    contracts = models.TextField(blank=True)
