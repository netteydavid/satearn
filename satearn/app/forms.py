from django.forms import ModelForm
from .models import Bounty

class BountyForm(ModelForm):
    class Meta:
        model = Bounty
        fields = ['title', 'description', 'reward', 'due_date']
        localized_fields = ('due_date',)
