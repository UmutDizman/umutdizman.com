from django import forms
from .models import Inquiry

LOCKABLE = {"starter", "business", "pro"}

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["name", "email", "phone", "package", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": " "}),
            "email": forms.EmailInput(attrs={"placeholder": " "}),
            "phone": forms.TextInput(attrs={"placeholder": " "}),
            "package": forms.Select(),  # select'e placeholder gerekmiyor
            "message": forms.Textarea(attrs={"rows": 5, "placeholder": " "}),
        }

    def __init__(self, *args, preset_package=None, **kwargs):
        super().__init__(*args, **kwargs)

        if preset_package in LOCKABLE:
            self.fields["package"].initial = preset_package
            self.fields["package"].disabled = True
        
        
    def clean_package(self):
        if self.fields["package"].disabled:
            return self.initial.get("package")
        return self.cleaned_data.get("package")