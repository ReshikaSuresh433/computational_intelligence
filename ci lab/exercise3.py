import pandas as pd
import numpy as np

def calculate_entropy(y):
    _, counts = np.unique(y, return_counts=True)
    probabilities = counts / len(y)
    entropy = -np.sum(probabilities * np.log2(probabilities + 1e-9))  # Adding a small constant to avoid log(0)
    return entropy

def calculate_information_gain(X, y, feature):
    total_entropy = calculate_entropy(y)
    
    feature_values, counts = np.unique(X[:, feature], return_counts=True)
    weighted_entropy = 0
    
    for value, count in zip(feature_values, counts):
        subset_y = y[X[:, feature] == value]
        subset_entropy = calculate_entropy(subset_y)
        weighted_entropy += (count / len(X)) * subset_entropy
    
    info_gain = total_entropy - weighted_entropy
    return info_gain

def calculate_gini_index(X, y, feature):
    feature_values, counts = np.unique(X[:, feature], return_counts=True)
    weighted_gini = 0
    
    for value, count in zip(feature_values, counts):
        subset_y = y[X[:, feature] == value]
        _, subset_counts = np.unique(subset_y, return_counts=True)
        probabilities = subset_counts / len(subset_y)
        gini = 1 - np.sum(probabilities ** 2)
        weighted_gini += (count / len(X)) * gini
    
    return weighted_gini

def find_best_feature(X, y, feature_names):
    num_features = X.shape[1]
    best_feature_info_gain = None
    best_feature_gini_index = None
    best_info_gain = -1
    best_gini_index = float('inf')
    
    entropy_dict = {}
    info_gain_dict = {}
    gini_index_dict = {}
    
    for feature in range(num_features):
        info_gain = calculate_information_gain(X, y, feature)
        gini_index = calculate_gini_index(X, y, feature)
        
        entropy = calculate_entropy(y)
        
        entropy_dict[feature_names[feature]] = entropy
        info_gain_dict[feature_names[feature]] = info_gain
        gini_index_dict[feature_names[feature]] = gini_index
        
        if info_gain > best_info_gain:
            best_info_gain = info_gain
            best_feature_info_gain = feature_names[feature]
        
        if gini_index < best_gini_index:
            best_gini_index = gini_index
            best_feature_gini_index = feature_names[feature]
    
    print(f"Entropy :{entropy}")
    
    print("\nInformation Gain for each attribute:")
    for attr, value in info_gain_dict.items():
        print(f"{attr}: {value}")
    
    print("\nGini Index for each attribute:")
    for attr, value in gini_index_dict.items():
        print(f"{attr}: {value}")
    
    return best_feature_info_gain, best_feature_gini_index

# Get file input from user
file_path = input("Enter the path to the CSV file: ")

# Load data from CSV file
data = pd.read_csv(file_path)
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
feature_names = data.columns[:-1]  # Get feature names

# Find and print the root of the decision tree based on Information Gain and Gini Index
root_feature_info_gain, root_feature_gini_index = find_best_feature(X, y, feature_names)

print("\nRoot of the Decision Tree based on Information Gain:", root_feature_info_gain)
print("Root of the Decision Tree based on Gini Index:", root_feature_gini_index)