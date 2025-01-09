import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.conf import settings 

def calculate_statistics():
    # Load dataset
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, 'analysisDiabetesRF', 'diabetes.csv')
    print('data path:  ', DATA_PATH)
    data = pd.read_csv(DATA_PATH)
    
    # Calculate statistics
    stats = data.describe().to_dict()
    # Convert the stats dictionary to a list of dictionaries
    stats_list = []
    for stat_name, stat_values in stats.items():
        stat_values['feature'] = stat_name  # Add the feature name as a key
        stats_list.append(stat_values)  # Append the updated dict to the list
    print(stats_list)

    return stats_list



def generate_histogram():
    # Load dataset
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_PATH = os.path.join(BASE_DIR, 'analysisDiabetesRF', 'diabetes.csv')
    # print('data path:  ', DATA_PATH)
    data = pd.read_csv(DATA_PATH)
    
    # Create a histogram of Glucose levels
    plt.figure(figsize=(8, 6))
    sns.histplot(data['Glucose'], bins=30, kde=True)
    plt.title('Distribution of Glucose Levels')
    plt.xlabel('Glucose Level')
    plt.ylabel('Frequency')
    
    # Save the plot to a static folder
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    STATIC_PATH = os.path.join(BASE_DIR, 'static')
    os.makedirs(STATIC_PATH, exist_ok=True)
    output_path = os.path.join(STATIC_PATH, 'glucose_histogram.png')
    
    try:
        plt.savefig(output_path)
        relative_graph_path = os.path.relpath(output_path, start=os.path.join(settings.BASE_DIR, 'static'))
        # print('relative path:  ', relative_graph_path )
        # print('Output path:  ', output_path )
        
        
    except Exception as e:
        print(f"Failed to save graph: {e}")

    
    plt.close()

    return relative_graph_path