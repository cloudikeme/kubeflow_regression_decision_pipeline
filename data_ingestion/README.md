# Step 1: Data Ingestion Step

The code we're looking at ingests data from the popular *scikit-learn* library, processes it, and saves it as a JSON file. Let's break it down together.

## Create data_ingestion.py

### **Table of Contents**

1. **Introduction to Data Ingestion**
2. **Understanding the Libraries and Modules Used**
   - 2.1 `import json`
   - 2.2 `import argparse`
   - 2.3 `from pathlib import Path`
   - 2.4 `from sklearn.datasets import load_breast_cancer`
   - 2.5 `from sklearn.model_selection import train_test_split`
3. **Main Function: `download_data`**
4. **Splitting the Data**
5. **Converting the Data to JSON Format**
6. **Saving the Data to a File**
7. **Setting Up Argument Parsing**
8. **Handling File Paths with `Path`**
9. **Creating the Main Script Block**
10. **Conclusion**
11. **FAQs**

---

### **1. Introduction to Data Ingestion**

Data ingestion refers to the process of importing data into a system for later processing or analysis. In this tutorial, you'll learn how to use Python to:
- Load a dataset.
- Split it into training and testing sets.
- Save it in a structured format, such as JSON.

By the end of this guide, you'll understand how each part of the code contributes to the data ingestion process.

---

### **2. Understanding the Libraries and Modules Used**

Before diving into the code, let's take a look at the libraries and modules used.

#### **2.1 `import json`**
The `json` module allows you to convert Python data structures into a JSON format. JSON (JavaScript Object Notation) is a popular, human-readable format for storing and exchanging data.

#### **2.2 `import argparse`**
This module helps you write user-friendly command-line interfaces. It parses arguments that are passed from the command line, which we'll use to specify where to save the data file.

#### **2.3 `from pathlib import Path`**
The `Path` class simplifies working with file paths, making it easy to create directories or check if a file exists.

#### **2.4 `from sklearn.datasets import load_breast_cancer`**
This function loads the breast cancer dataset from *scikit-learn*. This dataset is commonly used in machine learning and contains features that help classify breast cancer as either malignant or benign.

#### **2.5 `from sklearn.model_selection import train_test_split`**
This function splits your dataset into training and testing sets, which is essential for training machine learning models.

---

### **3. Main Function: `download_data`**

Now, let’s dive into the core of the script, the `download_data` function.

```python
def download_data(args):
```

The function accepts one argument, `args`, which is the input provided through the command line. Its main purpose is to load the breast cancer dataset, split it into training and test sets, and save it in JSON format.

---

### **4. Splitting the Data**

In this section of the code, we use the `load_breast_cancer` function to load the data and the `train_test_split` function to divide it into training and test sets.

```python
x, y = load_breast_cancer(return_X_y=True)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
```

- `x`: Features of the dataset (the input data).
- `y`: Labels or target values (what we want to predict).
- `train_test_split`: Splits the dataset into training and test subsets. Here, 80% of the data goes to training, and 20% is reserved for testing (`test_size=0.2`).

---

### **5. Converting the Data to JSON Format**

Once we have split the dataset, we need to store it in a format that's easy to work with. We convert the NumPy arrays into lists and pack them into a dictionary.

```python
data = {'x_train': x_train.tolist(),
        'y_train': y_train.tolist(),
        'x_test': x_test.tolist(),
        'y_test': y_test.tolist()}
```

- `.tolist()`: Converts NumPy arrays into Python lists, as JSON cannot natively handle NumPy arrays.
- `data`: A dictionary that holds our training and testing sets, with corresponding labels.

---

### **6. Saving the Data to a File**

Next, we use the `json.dumps()` function to create a JSON object from the `data` dictionary. Then, we open a file in write mode and save the JSON data.

```python
data_json = json.dumps(data)
with open(args.data, 'w') as output_file:
    json.dump(data_json, output_file)
```

- `data_json`: Contains the JSON representation of our data.
- `args.data`: The file path provided by the user, where the data will be saved.

---

### **7. Setting Up Argument Parsing**

Now, let's focus on how the script handles user input. The `argparse` module allows the script to accept command-line arguments. In this case, the user needs to specify where to save the data file.

```python
parser = argparse.ArgumentParser()
parser.add_argument('--data', type=str)
args = parser.parse_args()
```

- `--data`: This argument expects a string representing the file path where the JSON file will be saved.
- `args`: Holds the parsed arguments provided by the user.

---

### **8. Handling File Paths with `Path`**

The `Path` class ensures that the directory structure where the output file will be saved exists. If it doesn’t, it will be created.

```python
Path(args.data).parent.mkdir(parents=True, exist_ok=True)
```

- `Path(args.data).parent`: Refers to the directory containing the file specified by `--data`.
- `mkdir(parents=True, exist_ok=True)`: Creates the directory if it doesn’t already exist. If the parent directories don’t exist, they will be created as well.

---

### **9. Creating the Main Script Block**

Finally, the script includes a block of code that ensures it only runs if executed as the main program. This is a common Python convention.

```python
if __name__ == '__main__':
    download_data(args)
```

- `if __name__ == '__main__'`: Ensures that the code inside only runs when the script is executed directly, not when it’s imported as a module.

---

### **10. Conclusion**

In this tutorial, we've broken down a simple Python script that ingests a dataset, splits it into training and test sets, and saves the data in JSON format. While this script may appear complex at first, understanding each component makes it manageable. By using libraries like *scikit-learn* and *argparse*, we can build flexible, efficient data pipelines.

---

### **11. FAQs**

**1. What is data ingestion?**
Data ingestion refers to the process of importing and processing data into a system from various sources. In this example, we ingest a dataset from *scikit-learn*.

**2. Why do we split data into training and test sets?**
Splitting the data ensures we have separate sets for training the model and for testing its performance on unseen data.

**3. Why use JSON format for saving data?**
JSON is a lightweight and easy-to-read format that's widely used for data storage and exchange. It's compatible with many languages and tools.

**4. What is the role of `argparse`?**
`argparse` helps create user-friendly command-line interfaces. It allows users to provide arguments, such as file paths, when running the script.

**5. How does `train_test_split` work?**
`train_test_split` divides the dataset into two parts—training and testing—according to the specified `test_size` parameter. Here, 80% is used for training, and 20% for testing.

---

This breakdown should make the data ingestion code much clearer and easier to understand for beginners. Now, you can run the script and start experimenting with it!

## Create data_ingestion.yaml

Here, we will be defining a component for a Kubeflow pipeline that downloads a demo dataset from the `sklearn` library, specifically the breast cancer dataset. Let's break down what you have and explain it in simple terms.

---

### **Component Breakdown: Download Data Function**

**Name:** `Download Data Function`  
**Description:** This function downloads demo data from the `sklearn` datasets and stores it locally for further use in machine learning workflows.

#### **Outputs:**
- **Data:**
  - **Type:** `LocalPath`
  - **Description:** This is the path where the dataset will be stored after it has been downloaded and processed.

#### **Implementation:**
- **Container:**
  - **Image:** `omerbsezer/kubeflow_component:download_breast_cancer_data_v1`
    - This Docker image contains the environment necessary to execute the code for downloading the breast cancer dataset.
  - **Command:**
    - The command will run the `download_data.py` Python script.
    - `--data`: The flag specifies the output path where the dataset will be saved. This path is dynamically generated during pipeline execution and is passed as `{outputPath: Data}`.

---

### **How It Works:**

1. **Container Execution**:
   - The component will use a pre-built Docker container (`omerbsezer/kubeflow_component:download_breast_cancer_data_v1`) that already has the necessary dependencies and script (`download_data.py`) for downloading the dataset.
  
2. **Command**:
   - The `python download_data.py` command will be executed inside the container.
   - The `--data` flag specifies where the data should be saved. The `{outputPath: Data}` placeholder represents the path where the Kubeflow pipeline expects the output dataset to be stored.

3. **Output**:
   - The dataset is saved at the location specified by the `Data` output, which can be used by other components in the pipeline for further processing, such as model training.

### **Summary**

This component will automate the process of downloading and saving the breast cancer dataset from `sklearn`. By specifying the `LocalPath` for the output, the component ensures that other parts of the pipeline can easily access the dataset for their respective tasks, like training machine learning models or analyzing the data. 


## Create requirements file (requirements.txt)

```bash
scikit-learn
```

## Create Dockerfile

Thank you for sharing that Dockerfile. I can help you optimize it to create a more efficient and secure container image for your data download script. Let's improve it step by step.



```dockerfile
# Use a specific version of Python for better reproducibility
FROM python:3.8.16-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy only the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY download_data.py .

# Run as non-root user for better security
RUN useradd -m appuser
USER appuser

# Set the entrypoint
ENTRYPOINT ["python", "download_data.py"]

```

Here are the key optimizations and improvements made to the Dockerfile:

1. Base Image: Specified a precise version of Python (3.8.16) for better reproducibility.

2. Environment Variables: 
   - Set `PYTHONDONTWRITEBYTECODE` to prevent Python from writing pyc files.
   - Set `PYTHONUNBUFFERED` to ensure Python output is sent straight to terminal without buffering.

3. Working Directory: Changed from `/pipeline` to `/app`, which is a more standard name.

4. System Dependencies: Added an apt-get update and install for gcc, which might be needed for some Python packages. The `--no-install-recommends` flag keeps the image size down.

5. Dependency Installation: 
   - Copied only the requirements file first, then installed dependencies. This leverages Docker's cache mechanism for faster builds when only the script changes.
   - Used `--no-cache-dir` with pip to keep the image size down.

6. Script Copy: Copied the script after installing dependencies, again for better use of Docker's cache.

7. User Creation: Created a non-root user `appuser` and switched to it for running the script. This improves security.

8. Entrypoint: Set an ENTRYPOINT instead of leaving it to be specified in the Kubernetes YAML. This makes the image more self-contained.

These optimizations result in a more efficient, secure, and reproducible Docker image. The image will be smaller, build faster when only the script changes, and run with least privilege.

To use this Dockerfile:

1. Ensure your `requirements.txt` file is up to date with all necessary dependencies.
2. Place this Dockerfile in the same directory as your `requirements.txt` and `download_data.py` files.
3. Build the Docker image with a command like:
   ```
   docker build -t your-registry/kubeflow_component:download_breast_cancer_data_v2 .
   ```
   ```
   docker image build -t cloudikeme/kubeflow_component:ingest_breast_cancer_data_v2 .
   ```
4. Push the image to your container registry:
   ```
   docker push cloudikeme/kubeflow_component:ingest_breast_cancer_data_v1
   ```

5. Update your Kubeflow component YAML to use this new image.

This optimized Dockerfile should work well with the previously optimized Python script and Kubeflow component YAML.