# End-to-End MLOps Pipeline — Pet Adoption Prediction

A production-grade, end-to-end MLOps pipeline built with OOP Python, 
MLflow, TensorFlow, Docker, and GCP Cloud Run.

## Overview
Predicts the likelihood of pet adoption based on shelter features. 
Designed as a fully reproducible MLOps system covering data ingestion 
through live model serving with automated CI/CD.

## Key Features
- **MLflow experiment tracking & model registry** — all runs logged, 
  artifacts versioned, best model promoted via model registry
- **OOP Python pipeline** — modular design using service-layer and 
  factory patterns for preprocessing, feature engineering, and training
- **TensorFlow model training** — neural network with GridSearchCV 
  hyperparameter tuning and cross-validation
- **Docker + Flask inference API** — containerized REST endpoint 
  serving real-time predictions
- **GCP Cloud Run deployment** — serverless, auto-scaling model serving 
  with Google Cloud Logging
- **CI/CD via GitHub Actions** — automated test, build, and deploy 
  pipeline on every push
- **Model validation** — validate_model.py and test_api.py for 
  automated quality gates before deployment

## Tech Stack
Python (OOP) · TensorFlow · scikit-learn · MLflow · Flask · Docker · 
GCP Cloud Run · GitHub Actions · pandas · NumPy
Key Features

    Dataset: Pet adoption dataset containing features like pet type, breed, age, size, health, vaccination status, and adoption fee.
    Data Preprocessing:
        Handling missing values.
        Normalization of numerical data (e.g., age, weight, adoption fee).
        One-hot encoding for categorical features.
    Feature Engineering:
        Created additional features such as ShelterTimeCategory and HealthVaccStatus.
    Model Development:
        Developed a neural network and a Random Forest model.
        Hyperparameter tuning using GridSearchCV.
    Model Deployment:
        Flask API serving a pre-trained Random Forest model.
        Dockerized application deployed on Google Cloud Run.
    Model Monitoring:
        Integrated Google Cloud Logging for monitoring and debugging.
        Automated CI/CD pipeline using GitHub Actions.

Project Structure

    accuracyperdata.py: Logs model accuracy and other performance metrics. 

app.yaml: Configuration file for deploying the Flask app on Google App Engine.
Dockerfile: Defines the environment for building and deploying the application.
inspect_pickle.py: Inspects the saved model file (.pkl) and aligns input data for predictions.
mylogging.py: Sets up Google Cloud Logging for the application. requirements.txt: Lists the dependencies required for the project. test_api.py: Contains test cases for validating the Flask API's functionality. validate_model.py: Validates the model predictions against sample data.

    README.md: Documentation of the project.

Installation and Setup

    Clone the Repository:

git clone https://github.com/your-repo/pet-adoption-prediction.git
cd pet-adoption-prediction

Install Dependencies:

pip install -r requirements.txt

Run Flask API:

    python app.py

    Test API: Use test_api.py to validate predictions.

Deployment

    Dockerize:
        Build the Docker image:

docker build -t pet-adoption-api .

Run the Docker container:

        docker run -p 5000:5000 pet-adoption-api

    Deploy on Google Cloud:
        Push the Docker image to Google Container Registry.
        Deploy the container on Google Cloud Run or App Engine using app.yaml.

Monitoring

    Google Cloud Logging tracks API requests and model performance.
    CI/CD pipeline ensures automated testing and deployment.

Technologies Used

    Languages: Python
    Libraries: Flask, scikit-learn, pandas, joblib
    Tools: Docker, Google Cloud Platform, GitHub Actions

Future Enhancements

    Improve model accuracy with additional data or features.
    Enhance the web API with additional endpoints for analytics.
    Implement real-time model updates using continuous retraining.
