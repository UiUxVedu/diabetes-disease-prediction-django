# Diabetes Disease Prediction Web Application

## Project Description

This project is a full-stack web application developed using **Django** and **Machine Learning** to predict the likelihood of diabetes based on medical parameters provided by the user. The application allows users to register, log in securely, enter medical information, and receive a prediction result generated using a trained machine learning model.

The goal of this project is to demonstrate the practical integration of a machine learning model into a web application while maintaining a clean user interface and understandable backend logic. The project focuses on clarity, correctness, and real-world usability rather than over-complexity.

---

## Problem Statement

Diabetes is a long-term medical condition that requires early detection and lifestyle management. Many individuals are unaware of their risk level until symptoms become severe. This project aims to provide a simple system where users can input commonly measured medical values and receive an immediate prediction that indicates whether diabetes is likely.

This application is intended for educational and demonstration purposes and does not replace professional medical diagnosis.

---

## Technologies Used

### Backend

* Python
* Django Framework
* Django Authentication System

### Frontend

* HTML
* CSS
* Bootstrap
* Basic JavaScript for animations

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Support Vector Machine (SVM)

### Database

* SQLite (default Django database)

---

## Machine Learning Model Explanation

The machine learning model is trained using a publicly available diabetes dataset. The following steps are followed:

1. The dataset is loaded and explored to understand feature distribution.
2. Data cleaning and validation are performed.
3. Relevant medical features are selected.
4. The dataset is split into training and testing sets.
5. A Support Vector Machine classifier is trained.
6. Model accuracy and confusion matrix are evaluated.
7. The trained model is saved using joblib and reused in the Django application.

### Input Features Used

* Plasma glucose concentration
* Diastolic blood pressure
* Triceps skinfold thickness
* Serum insulin
* Body mass index (BMI)
* Diabetes pedigree function
* Age

---

## Application Workflow

1. User accesses the home page and reads about the project.
2. User registers an account using username, email, and password.
3. User logs in using secure authentication.
4. After login, the user is redirected to the medical information form.
5. User enters medical data required for prediction.
6. The backend processes the input and sends it to the trained ML model.
7. The model returns a prediction result.
8. The result is displayed clearly on the prediction page.
9. The user can either re-enter data or view lifestyle precautions.

---

## Folder Structure Explanation

```
diab_detect/
│
├── manage.py
│   Django command-line utility for project management
│
├── diab_detect/
│   Project configuration directory
│   ├── settings.py   Project settings and configuration
│   ├── urls.py       Root URL routing
│   └── wsgi.py       Web server gateway interface
│
├── diabdetectapp/
│   Main Django application
│   ├── ml/
│   │   ├── training.py     Machine learning training script
│   │   ├── model.joblib    Saved trained model
│   │   └── diabetes.csv   Dataset used for training
│   │
│   ├── templates/
│   │   HTML templates for frontend pages
│   │
│   ├── views.py
│   │   Contains backend logic and prediction handling
│   │
│   ├── urls.py
│   │   Application-level routing
│   │
│   ├── forms.py
│   │   Django forms for login and registration
│   │
│   └── apps.py
│       Application configuration
│
├── db.sqlite3
│   Local database file
│
├── requirements.txt
│   Python dependencies
│
└── README.md
    Project documentation
```

---

## User Interface Design

The user interface is intentionally kept clean and minimal. Bootstrap is used for layout consistency and responsiveness. Light animations are added using CSS and JavaScript to improve user experience without making the interface overly complex. The design focuses on readability, usability, and clarity.

---

## How to Run the Project Locally

1. Clone the repository from GitHub.
2. Navigate to the project directory.
3. Create and activate a virtual environment.
4. Install dependencies using `pip install -r requirements.txt`.
5. Run database migrations if required.
6. Start the Django server using `python manage.py runserver`.
7. Access the application in the browser.

---

## Limitations

* The prediction is based only on the trained dataset and selected features.
* This project is not intended for clinical use.
* Model performance depends on dataset quality.

---

## Future Enhancements

* Improve model accuracy using additional data and feature engineering.
* Store prediction history per user.
* Add charts and analytics for better insights.
* Deploy the project to a cloud platform.

---

## Conclusion

This project demonstrates a complete end-to-end workflow from data analysis and machine learning model training to web application deployment using Django. It serves as a strong academic and portfolio project that reflects practical skills in backend development, frontend integration, and applied machine learning.
