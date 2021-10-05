# Phishing Website Detection Based on Machine Learning Methods

Our project objective is to develop a model to classify the phishing website by recognize key factors.

# Dataset

https://www.kaggle.com/xwolf12/malicious-and-benign-websites
Our data comes from the Kaggle platform. The dataset consists of a total of 1708 records, and including two types of data: Benign URL and Phishing URL, which are labeled as ”0” and ”1” respectively. There are 21 features in the original dataset. We preprocessed them and finally selected 16 features. 
In addition, we have done correlation analysis on some of these features.

We use “Type” as y-value for further modeling.
0 - benign, 1 - malicious

# Experiment

We did EDA and data visualization in the notebook and seven models are designed for the research to be trained and fitted to predict the type of given websites. 

The seven models are random forest classifier, logistic regression, linear SVC, K-Neighbor classifier, Gradient boosting, Decision tree classifier, and Ada-boosting. Each kind of model has different advantages and weaknesses. Thus, after the presentation of models, they would be compared to help us find the best result. 
