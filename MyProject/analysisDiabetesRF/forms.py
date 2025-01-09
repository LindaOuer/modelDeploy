from django import forms

class DiabetesForm(forms.Form):
    pregnancies = forms.FloatField(label='Number of Pregnancies')
    glucose = forms.FloatField(label='Glucose Level')
    blood_pressure = forms.FloatField(label='Blood Pressure')
    skin_thickness = forms.FloatField(label='Skin Thickness')
    insulin = forms.FloatField(label='Insulin Level')
    bmi = forms.FloatField(label='BMI')
    dpf = forms.FloatField(label='Diabetes Pedigree Function')
    age = forms.FloatField(label='Age')
