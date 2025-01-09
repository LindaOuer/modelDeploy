from django.shortcuts import render
from .ml_model import train_model, generate_graphs
from sklearn.datasets import load_iris
import os

# View to handle input and results
def predict(request):
    model, target_names, report, confusion = train_model()
    # graph_path = generate_graphs()
    #print(f"Resolved path for saving graph: {graph_path}")

    
    context = {"report": report, "confusion": confusion, "target_names": target_names,}

    if request.method == "POST":
        # Get features from user input
        features = [
            float(request.POST["sepal_length"]),
            float(request.POST["sepal_width"]),
            float(request.POST["petal_length"]),
            float(request.POST["petal_width"]),
        ]
        prediction = model.predict([features])
        graph_path = generate_graphs()
        # file_exists = os.path.isfile(graph_path)  
        
        
        context["prediction"] = target_names[prediction[0]]
        context["graph_path"] = graph_path

        #print(f"Resolved path for saving graph: {graph_path}")
        

    return render(request, "analysis/predict.html", context)
