from django import forms

class searchForm(forms.Form):
	name = forms.CharField(label="Enter author name",max_length=100)

