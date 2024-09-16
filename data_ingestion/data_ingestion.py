import json
import argparse
from pathlib import Path
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

def download_data(output_path: str, test_size: float = 0.2, random_state: int = 42):
    # Load data from sklearn library
    X, y = load_breast_cancer(return_X_y=True)
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Create data structure to save
    data = {
        'X_train': X_train.tolist(),
        'y_train': y_train.tolist(),
        'X_test': X_test.tolist(),
        'y_test': y_test.tolist()
    }
    
    # Save the data directly as JSON
    with open(output_path, 'w') as output_file:
        json.dump(data, output_file)

def main():
    parser = argparse.ArgumentParser(description="Download and process breast cancer dataset")
    parser.add_argument('--data', type=str, required=True, help="Output file path for the processed data")
    parser.add_argument('--test-size', type=float, default=0.2, help="Proportion of the dataset to include in the test split")
    parser.add_argument('--random-state', type=int, default=42, help="Random state for reproducibility")
    
    args = parser.parse_args()
    
    # Create the output directory if it doesn't exist
    Path(args.data).parent.mkdir(parents=True, exist_ok=True)
    
    # Download and process the data
    download_data(args.data, args.test_size, args.random_state)
    print(f"Data has been successfully processed and saved to {args.data}")

if __name__ == '__main__':
    main()