from django.shortcuts import render
import joblib
from .forms import DiabetesForm
from .statistics import calculate_statistics, generate_histogram


# Load the model
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'analysisDiabetesRF', 'diabetes_model.pkl')

model = joblib.load(MODEL_PATH)
# [6, 148, 72, 35, 0, 33.6, 0.627, 50],  # Diabetic
# [1, 85, 66, 29, 0, 26.6, 0.351, 31],   # Non-diabetic
# [8, 183, 64, 0, 0, 23.3, 0.672, 32]    # Diabetic

def predict_diabetes(request):
    prediction = None

    if request.method == 'POST':
        form = DiabetesForm(request.POST)
        if form.is_valid():
            # Extract feature inputs
            data = [
                form.cleaned_data['pregnancies'],
                form.cleaned_data['glucose'],
                form.cleaned_data['blood_pressure'],
                form.cleaned_data['skin_thickness'],
                form.cleaned_data['insulin'],
                form.cleaned_data['bmi'],
                form.cleaned_data['dpf'],
                form.cleaned_data['age'],
            ]

            # Predict diabetes
            prediction = model.predict([data])[0]
            prediction = "Diabetic" if prediction == 1 else "Non-Diabetic"
    else:
        form = DiabetesForm()

    return render(request, 'analysisDiabetesRF/predict.html', {'form': form, 'prediction': prediction})

def stats_view(request):
    # Calculate statistics
    stats = calculate_statistics()

    # Generate plot
    plot_path = generate_histogram()
    print('plot path ', plot_path)

    return render(request, 'analysisDiabetesRF/stats.html', {'stats_list': stats, 'plot_path': plot_path})
