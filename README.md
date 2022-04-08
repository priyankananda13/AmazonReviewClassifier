# AmazonReviewClassifier
Given a dataset of Amazon product reviews for the year 2017-2018 for the category Cell Phones and Accessories, create a classifier for the classification of Reviews into Positive, Negative, and Neutral.

## Problem Statement for Machine Learning/NLP:
The problem statement goes as follows:

Given a dataset of Amazon product reviews for the year 2017-2018 for the category Cell Phones and Accessories, do the following tasks:

1. Reading and pre-processing of the dataset.<br>
2. Creating a classifier for the classification of Reviews into Positive, Negative, and Neutral.<br>
3. Creating a Confusion matrix.

## Approach
### 1. Data Preprocessing: <br>
i. The original data in json format is converted to dataframe using Pandas.<br>
ii. From 1-5 range reviews, 1-2 is taken as Negative, 3 as Neutral and 4-5 as Positive.<br>
iii. Balancing the data and the use of text pre-processing techniques.
    
### 2. Model Training: <br>
i. Machine Learning model LinearSVC (Linear Support Vector Classifier) is used.<br>
ii. The model is saved with joblib library. We can directly load this model and get results easily.<br>
iii. Generation of Classification report to understand the model better.<br>
   
   
### 3. Making Predictions:
   The predictions are made using main.py file.


## Model Accuracy
Accuracy: 88%
