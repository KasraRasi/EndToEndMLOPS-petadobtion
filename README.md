# mlops
 This project is a comprehensive end-to-end machine learning pipeline . The project involves selecting a dataset, training a machine learning model using TensorFlow, creating a robust model training pipeline, deploying the model, monitoring its performance, and following best practices in machine learning development.the project is an end-to-end machine learning solution designed to predict the likelihood of pet adoption based on various features.
Overview

 The project focuses on building a robust machine learning pipeline, deploying it as a web service, and monitoring its performance.
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
