from django import forms

class Emp_forms(forms.Form):
    name=forms.CharField(label="name")
    age=forms.IntegerField(label="age")
    dept=forms.CharField(label="dept")
    salary=forms.IntegerField(label="sal")
