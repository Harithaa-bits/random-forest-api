# Model Experimentation and Packaging (M3)

## Project Overview
This project involves training a Random Forest model, performing hyperparameter tuning, and packaging the model using Flask and Docker for deployment.


## 1. Hyperparameter Tuning Results

### **Best Parameters:**
The best parameters identified through `GridSearchCV` are:
- `n_estimators`: 100
- `max_depth`: 10
- `min_samples_split`: 2

### **Test Accuracy:**
The accuracy of the model on the test data is **95.3%**.


## 2. Model Packaging
The best-performing model was packaged using:
- **Flask** for creating a REST API.
- **Docker** for containerizing the application.


## 3. How to Run the Application

### Step 1: Run Locally
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
