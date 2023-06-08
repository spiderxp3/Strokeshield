# StrokeShield

StrokeShield is a web application that uses machine learning to predict the risk of heart strokes. The application is built on a Python server and utilizes the RandomForestClassifier algorithm to provide personalized risk assessments based on user input health data.

Check out live demo of the project in the description.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8-blue)](https://www.python.org/downloads/release/python-380/)
[![Flask Version](https://img.shields.io/badge/flask-2.0.1-blue)](https://pypi/project/Flask/)

[![scikit-learn Version](https://img.shields.io/badge/scikit--learn-0.24.2-blue)](https://pypi.org/project/scikit-learn/)
[![Bootstrap Version](https://img.shields.io/badge/bootstrap-5.0.1-blue)](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Stroke%20Prediction%20Dataset-blue)](https://www.kgle.com/fedesoriano/stroke-prediction-dataset)
[![scikit-learn RandomForestClassifier](https://img.shields.io/badge/scikit--learn-RandomForestClassifier-blue)](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)

![5764322](https://github.com/spiderxp3/Strokeshield/assets/91022462/67fcf6c9-9b58-4a29-bdb8-f6b6c88f6685)


## Dataset and Accuracy
- StrokeShield uses the Stroke Prediction Dataset from Kaggle to train and test the RandomForestClassifier algorithm. 
- This dataset includes 5110 records of `patient data`, including demographic information, lifestyle factors, and medical history.
- After preprocessing the data and training the model, StrokeShield achieved an accuracy of 94% on the test set.
- This high accuracy demonstrates the effectiveness of the RandomForestClassifier algorithm in predicting stroke risk based on individual risk factors.

## Features

- User-friendly interface for inputting health data
- Machine learning algorithm for predicting stroke risk
- Personalized risk assessments based on user data
- Proactive prevention strategies for improved heart health
- An accuracy of 94% prediction of required outcome with this approach.

## Installation

1. Clone the repository: `git clone https://github.com/spiderxp3/strokeshield.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the server: `python server.py`
4. Open the application in your web browser: `http://localhost:5000`

## Usage
1. Input your health data into the application
2. Click the "Predict" button to receive your personalized stroke risk assessment
3. Follow the proactive prevention strategies provided by the application to improve your heart health

## Contributing
Contributions to StrokeShield are welcome! If you find a bug or have a feature request, please open an issue on the repository. If you would like to contribute code, please fork the repository and submit a pull request.

## License

StrokeShield is licensed under the MIT License. See `LICENSE` for more information.

## `Acknowledgements`

- RandomForestClassifier algorithm from scikit-learn
- Flask web framework
- Bootstrap CSS framework
