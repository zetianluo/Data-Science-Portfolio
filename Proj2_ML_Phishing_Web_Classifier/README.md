# Phishing Website Detection Based on Machine Learning Methods

Phishing attack is the simplest way to obtain sensitive information from innocent users. The target of phishers is to obtain key information, such as username, password, and bank account details. Cyber security officials are now looking for reliable and stable detection techniques to detect phishing sites. This project studies the phishing websites detection technology by extracting and analyzing the characteristics of legal and forged Uniform Resource Locators (URLs) using machine learning approaches, including Logistic Regression, K-nearest Neighbor (KNN), Linear Support Vector Classifier (SVC), Random Forest, Gradient Boosting Decision Tree, and Ada-Boost, and compares their performance with respect to criterions such as accuracy, Root Mean Square Error (RMSE), precision, recall, and F1-score. The results show that ensemble methods, including Gradient Boosting Decision Tree, Random Forest, and Ada Boosting, can achieve much higher detection performance than the other algorithms in terms of all the criteria.

# Dataset

https://www.kaggle.com/xwolf12/malicious-and-benign-websites
Our data comes from the Kaggle platform. The dataset consists of a total of 1708 records, and including two types of data: Benign URL and Phishing URL, which are labeled as ”0” and ”1” respectively. There are 21 features in the original dataset. We preprocessed them and finally selected 16 features. 
In addition, we have done correlation analysis on some of these features.

We use “Type” as y-value for further modeling.
0 - benign, 1 - malicious

# Methods

There are seven models are designed for the research to be trained and fitted to predict the type of given websites. The seven models are random forest classifier, logistic regression, linear SVC, K-Neighbor classifier, Gradient boosting, Decision tree classifier, and Ada-boosting. Each kind of model has different advantages and weaknesses. Thus, after the presentation of models, they would be compared to help us find the best result. 

