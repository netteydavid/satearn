from django.forms import ModelForm
from .models import Bounty

class BountyForm(ModelForm):
    class Meta:
        model = Bounty
        fields = ['title', 'category', 'description', 'reward', 'due_date', 'tags']
        localized_fields = ('due_date',)
