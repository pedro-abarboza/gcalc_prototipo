from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User, Permission, Group

class CustomUserChangeForm(UserChangeForm):
    user_permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.SelectMultiple,
        required=False
    )
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.SelectMultiple,
        required=False
    )

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                'is_active', 'date_joined', 'last_login', 'user_permissions', 'groups']
    
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['user_permissions'].initial = self.instance.user_permissions.all()
            self.fields['groups'].initial = self.instance.groups.all()



class GroupForm(forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.SelectMultiple,
        required=False
    )

    class Meta():
        model = Group
        fields = ['name', 'permissions']
    
    def __init__(self, *args, **kwargs):
        super(GroupForm, self).__init__(*args, **kwargs)
        if self.initial:
            self.fields['permissions'].initial = self.instance.permissions.all()




