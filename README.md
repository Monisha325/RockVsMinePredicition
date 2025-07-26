# Rock vs Mine Prediction

A **Machine Learning** & **Deep Learning** project to classify sonar signals as either **Rock** or **Mine**.

- **Logistic Regression** & **Random Forest** for baseline comparisons  
- **Deep Neural Network** for improved performance  
- **Streamlit Web App** for real-time predictions  

---

## 1. Project Overview
Sonar signals are used in **underwater exploration**, **robotics**, and **naval defense**.  
This project builds **multiple classification models** (**ML + Deep Learning**) to distinguish between **rocks and mines** and provides an **interactive web interface** for easy predictions.

---

## 2. Project Structure
```bash
rock-vs-mine-prediction/
│
├── data/
│   └── Copy of sonar data.csv           # Dataset
│
├── models/
│   ├── trained_model.sav               # Logistic Regression model
│   └── deep_model.h5                   # Deep Learning model
│
├── notebooks/
│   └── Rock_vs_Mine_Prediction.ipynb    # Data exploration & model training
│
├── src/
│   ├── predictive_system.py            # ML prediction script
│   └── deep_model.py                   # Neural Network training script
│
├── app.py                               # Streamlit app
├── requirements.txt                     # Dependencies
└── README.md                            # Documentation
```
---

## 3. Dataset
- **Source:** UCI Machine Learning Repository  
- **Samples:** 208 sonar reflections  
- **Features:** 60 numerical attributes per sample  
- **Target Classes:**  
  - `R` → Rock  
  - `M` → Mine  

---

## 4. Technologies Used
- **Language:** Python 3.11+  
- **Libraries:**  
  - **Data Handling:** NumPy, Pandas  
  - **ML Models:** Scikit-learn (Logistic Regression, Random Forest)  
  - **Deep Learning:** TensorFlow / Keras  
  - **Visualization:** Matplotlib  
  - **Deployment:** Streamlit  

---

## 5. Models Implemented
### 1. Logistic Regression
Baseline binary classification model.

### 2. Random Forest
An ensemble model for improved handling of complex data.

### 3. Deep Neural Network (Keras)
- **Input layer:** 60 features  
- **Hidden layers:** 2 Dense layers (ReLU activation)  
- **Output layer:** Sigmoid activation (binary classification)  

---

## 6. How to Run
### Step 1: Clone the repository
```bash
git clone https://github.com/Monisha325/RockVsMinePredicition.git
cd RockVsMinePredicition
```

###Step 2: Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # Mac/Linux
venv\Scripts\activate        # Windows
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit app
```bash
streamlit run app.py
```

## 7. Results
Model	Training Accuracy	Test Accuracy
Logistic Regression	83.42%	76.19%
Random Forest	100%	76.19%
Deep Neural Network	96%	80–82%

## 8. Future Enhancements
Deploy the application on Streamlit Cloud / Render for public access
Add hyperparameter tuning for better performance
Use SHAP/LIME for interpretability (understanding model decisions)

## 10.  Live Model Output: Logistic Regression predicting object as Rock (R)
My trained model correctly identifies the object as a Rock based on sonar signal input features.
<img width="1014" height="909" alt="image" src="https://github.com/user-attachments/assets/f5e10e0a-55e7-4619-8045-34332d5b2dc8" />


## 9. Author
Monisha Patnana
(Machine Learning & Deep Learning Enthusiast)
