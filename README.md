# Diabetes Detection using Machine Learning Techniques

This project focuses on developing a web application that utilizes various machine learning techniques to predict the presence or absence of diabetes in patients. The application is implemented using Flask, a popular web framework in Python.

Diabetes is a chronic disease that affects millions of people worldwide. Early detection of diabetes can significantly improve patient outcomes and help in managing the disease effectively. This project aims to provide a convenient and accessible tool for diabetes detection using machine learning algorithms.

The web application allows users to input relevant medical information, such as glucose levels, blood pressure, insulin, and body mass index (BMI), and predicts the likelihood of having diabetes. By employing different machine learning techniques, we can compare their performance and accuracy in predicting diabetes.

# Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* HTML/CSS

### Installation

To set up the project locally, follow these steps:

Clone the repository to your local machine.
Ensure you have Python 3.x installed on your system.
Install the required Python dependencies using the following command:
```pip install -r requirements.txt```


After completing the installation, navigate to the project directory.
Launch the Flask application by running the following command:

```python app.py```
Open your web browser and go to http://localhost:5000 to access the application.
Enter the necessary medical information into the form and submit it for diabetes prediction.
The application will process the input using various machine learning models and display the prediction results.
Machine Learning Techniques

This project utilizes the following machine learning techniques for diabetes detection:

Logistic Regression
Decision Tree
Support Vector Machines (SVM)
Artificial Neural Networks (ANN)
Naive Bayes
Each technique employs different algorithms and approaches to predict diabetes. The web application compares the results from these techniques to evaluate their performance and provide accurate predictions.

### Dataset

The project employs a dataset containing medical information of patients, such as glucose levels, blood pressure, insulin, BMI, etc. The dataset is used to train and evaluate the machine learning models. The application utilizes the diabetes.csv file included in the project.

### Model Training

The machine learning models are trained using the diabetes.csv dataset. The dataset is preprocessed to handle missing values, normalize the features, and split into training and testing sets. The models are trained on the training set and evaluated on the testing set to measure their performance.

### Web Application

The web application is developed using Flask, a lightweight web framework in Python. Flask provides a simple and efficient way to create web applications. The application presents a user-friendly interface where users can input their medical information and obtain a diabetes prediction. The Flask server processes the input and utilizes the trained machine learning models to generate predictions, which are then displayed to the user.
