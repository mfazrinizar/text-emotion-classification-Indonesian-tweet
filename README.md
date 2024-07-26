# Text Emotion Classification in Indonesian Public Opinion Tweet

Four traditional machine learning classifiers were evaluated for their performance in classifying emotions in Indonesian public opinion tweets. Below are the results of each classifier, including their accuracy, F1 score, and confusion matrix. The product in in form of prediction model is saved into /models.

## Traditional Machine Learning Classifiers

### 1. Naive Bayes

#### Result:
1. Accuracy: 43.79%
2. F1 Score: 43.79
3. Confusion Matrix:
   
|     |  0 |  1 |  2 |  3 |  4 |  5 |
|-----|----|----|----|----|----|----|
| 0   | 67 |  0 |  0 |  0 | 289|  0 |
| 1   |  0 | 32 |  1 |  0 | 248|  0 |
| 2   |  0 |  1 | 171|  3 | 210|  0 |
| 3   |  0 |  0 |  2 | 29 | 185|  0 |
| 4   |  3 |  0 |  6 |  0 | 580|  0 |
| 5   |  0 |  0 |  2 |  0 | 244| 51 |

![image](https://github.com/user-attachments/assets/bdd761da-32ae-4d50-abbc-c52ab575ab4a)

### 2. Random Forest

#### Result:
1. Accuracy: 68.13%
2. F1 Score: 68.13
3. Confusion Matrix:
   
|     |  0 |  1 |  2 |  3 |  4 |  5 |
|-----|----|----|----|----|----|----|
| 0   | 239|  5 |  6 | 23 | 79 |  4 |
| 1   | 10 | 203|  5 | 12 | 48 |  3 |
| 2   | 16 | 13 | 253| 31 | 59 | 13 |
| 3   |  4 |  4 |  7 | 165| 34 |  2 |
| 4   | 43 | 29 | 38 | 30 | 417| 32 |
| 5   | 11 |  9 | 10 | 12 | 85 | 170|

![image](https://github.com/user-attachments/assets/a97babc1-66af-4422-bb98-c5e231f3cd04)

### 3. Logistic Regression
#### Result:
1. Accuracy: 65.87%
2. F1 Score: 65.87
3. Confusion Matrix:
   
|     |  0 |  1 |  2 |  3 |  4 |  5 |
|-----|----|----|----|----|----|----|
| 0   | 202|  3 |  4 | 14 | 130|  3 |
| 1   |  5 | 178|  3 |  3 | 91 |  1 |
| 2   | 10 | 13 | 241| 23 | 88 | 10 |
| 3   |  3 |  3 | 10 | 146| 53 |  1 |
| 4   | 28 | 21 | 24 | 18 | 478| 20 |
| 5   |  7 |  7 |  6 | 11 | 112| 154|

![image](https://github.com/user-attachments/assets/52bc0afe-475f-42b2-b941-21fce2724195)

### 4. Linear Support Vector

#### Result:
1. Accuracy: 70.95%
2. F1 Score: 70.95
3. Confusion Matrix:
   
|     |  0 |  1 |  2 |  3 |  4 |  5 |
|-----|----|----|----|----|----|----|
| 0   | 202|  3 |  4 | 14 | 130|  3 |
| 1   |  5 | 178|  3 |  3 | 91 |  1 |
| 2   | 10 | 13 | 241| 23 | 88 | 10 |
| 3   |  3 |  3 | 10 | 146| 53 |  1 |
| 4   | 28 | 21 | 24 | 18 | 478| 20 |
| 5   |  7 |  7 |  6 | 11 | 112| 154|

![image](https://github.com/user-attachments/assets/5d82095f-50c7-4b90-9c3d-68eb9b403cf7)

## Summary

- The Linear Support Vector classifier outperformed the other classifiers with the highest accuracy and F1 score of 70.95%.
- The Random Forest classifier also showed strong performance with an accuracy of 68.13%.
- The Logistic Regression classifier achieved a moderate accuracy of 65.87%.
- The Naive Bayes classifier had the lowest performance with an accuracy of 43.79%.
#### The confusion matrices provide detailed insights into the classification results, showing the distribution of true positives, false positives, true negatives, and false negatives for each classifier.
