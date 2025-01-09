import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.conf import settings 

# Load Iris dataset
def train_model():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target)
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Train Logistic Regression model
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    
    # Test the model
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, target_names=iris.target_names)
    confusion = confusion_matrix(y_test, y_pred)
    
    return model, iris.target_names, report, confusion


def generate_graphs():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target

    # Pairplot
    sns.pairplot(df, hue='species', palette='Set2')
    
    # Save image to static folder
    static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    os.makedirs(static_dir, exist_ok=True)
    graph_path = os.path.join(static_dir, "pairplot.png")
    try:
        plt.savefig(graph_path)
        relative_graph_path = os.path.relpath(graph_path, start=os.path.join(settings.BASE_DIR, 'static'))
        
    except Exception as e:
        print(f"Failed to save graph: {e}")

    plt.close()

    return relative_graph_path