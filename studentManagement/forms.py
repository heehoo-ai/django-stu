from django import forms

from .models import StudentInformationModel

class StudentInformationModelForm(forms.ModelForm):
    def clean_phone(self):
        cleaned_data = self.cleaned_data['stu_phone']
        if not cleaned_data.isdigit():
            raise forms.ValidationError('必须是数字！')
        return int(cleaned_data)

    class Meta:
        model = StudentInformationModel
        fields = (
            'stu_id',
            'stu_name',
            'stu_phone',
            'str_addr',
            'stu_faculty',
            'stu_major',
        )



