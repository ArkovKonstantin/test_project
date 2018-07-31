from django import forms

from app.models import Point, PointType


class PointCreateForm(forms.ModelForm):
    class Meta:
        model = Point
        exclude = ['']

class PointTypeCreateForm(forms.ModelForm):
    class Meta:
        model = PointType
        exclude = ['']