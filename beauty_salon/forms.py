from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class AuthenticationForm(forms.Form):
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            "autofocus": True,
            'class': 'contacts__form_iunput',
            'placeholder': '+7(999)999--99-99',
            }
        )
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'type':"number",
            'class':"tipsPopup__form_inputNum popup__input",
            'placeholder': "0",
            'min': 1,
            'max': 9
            }
        ),
    )
    password2 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'type':"number",
            'class':"tipsPopup__form_inputNum popup__input",
            'placeholder': "0",
            'min': 1,
            'max': 9
            }
        ),
    )
    password3 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'type':"number",
            'class':"tipsPopup__form_inputNum popup__input",
            'placeholder': "0",
            'min': 1,
            'max': 9
            }
        ),
    )
    password4 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            "autocomplete": "current-password",
            'type':"number",
            'class':"tipsPopup__form_inputNum popup__input",
            'placeholder': "0",
            'min': 1,
            'max': 9
            }
        ),
    )
