# Academic performance case study

![Cover Image](./images/principal.png)

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/datasilvia/Academic_performance_case_study)
![GitHub forks](https://img.shields.io/github/forks/datasilvia/Academic_performance_case_study)
![GitHub stars](https://img.shields.io/github/stars/datasilvia/Academic_performance_case_study)
![GitHub issues](https://img.shields.io/github/issues/datasilvia/Academic_performance_case_study)
![GitHub pull requests](https://img.shields.io/github/issues-pr/datasilvia/Academic_performance_case_study)


## 🎯 Objectives

The main objectives of this project are:

1. **📊 Analyze Factors Affecting Academic Performance**:
   - Identify and understand the various factors that influence students' academic performance, such as demographics, family background, and study habits.

2. **🔍 Identify Patterns and Correlations**:
   - Use exploratory data analysis (EDA) to uncover patterns and correlations in the data that can provide insights into students' performance.

3. **🤖 Build Predictive Models**:
   - Develop and evaluate machine learning models to predict students' academic performance in Mathematics and Portuguese.

4. **📈 Improve Academic Performance**:
   - Provide actionable insights and recommendations to educators and policymakers to help improve students' academic outcomes.

5. **📚 Contribute to Educational Research**:
   - Contribute to the body of research on educational data analysis and predictive modeling.

## ⚙️ Functionality

The Streamlit application offers the following functionalities:

1. **🏠 Home Page**:
   - Overview of the project, including its objectives and key features.
   - Introduction to the project team and a link to the GitHub repository.

2. **🎯 Objectives**:
   - Detailed description of the project's main goals and expected outcomes.

3. **📊 Power BI**:
   - Interactive visualizations and insights into the dataset using Power BI.
   - Exploration of various aspects of the data, such as the distribution of grades, correlations between variables, and trends over time.

4. **🔮 Prediction**:
   - Allows users to make predictions about students' academic performance in Mathematics and Portuguese.
   - Users can select the subject and input relevant features to obtain predictions.
   - Utilizes two machine learning models:
     - **📐 AdaBoostClassifier** for Mathematics: Combines multiple weak classifiers to create a strong classifier.
     - **📚 BaggingClassifier** for Portuguese: Improves stability and accuracy by training multiple instances of the same classifier on different subsets of the data.
   - Displays the accuracy of the models and visualizes the confusion matrix for each prediction.

5. **📈 Model Evaluation**:
   - Provides detailed evaluation metrics for the machine learning models, including accuracy and confusion matrices.

6. **💻 User Interaction**:
   - Interactive interface for users to input data and obtain predictions.
   - User-friendly design with clear instructions and visual feedback.

These functionalities ensure that the application is both informative and easy to use, providing valuable insights into students' academic performance and helping educators make data-driven decisions.

## 🛠️ Tools Used

The following tools and technologies were used to carry out this project:

- **🐍 Python**: For data exploration and analysis
- **📊 Pandas**: For data manipulation and cleaning
- **📉 Matplotlib and Seaborn**: For data visualization
- **📊 Power BI**: For creating interactive visualizations
- **📓 Jupyter Notebook**: For documenting and presenting the analysis
- **🐙 GitHub**: For version control and collaboration
- **📋 Trello**: For project management
- **🌐 Streamlit**: For building and deploying the interactive web application
- **🤖 Scikit-learn**: For implementing the Machine Learning model

## 🚀 Development Process

The development process of this project was carried out in several key stages, each of which was crucial for the success of the analysis and prediction of students' academic performance. Below are the main stages of the development process:

### 1. 📊 Data Collection
The first stage of the project involved data collection. Data was gathered from various sources, including academic records, student surveys, and demographic information. This data provided a solid foundation for subsequent analysis.

### 2. 🧹 Data Cleaning and Preprocessing
Once the data was collected, an exhaustive data cleaning and preprocessing process was conducted. This included removing null values, handling outliers, and normalizing the data. Additionally, transformations such as encoding categorical variables and creating new features from existing ones were performed.

### 3. 🔍 Exploratory Data Analysis (EDA)
Exploratory Data Analysis (EDA) was a crucial stage for understanding the relationships and patterns in the data. Various visualization techniques and descriptive statistics were used to identify trends, correlations, and potential factors influencing students' academic performance.

### 4. 🛠️ Feature Selection
To improve the accuracy of the prediction models, a feature selection process was carried out. Techniques such as SelectKBest and feature importance analysis were used to identify the most relevant variables for the model.

### 5. 🤖 Building Machine Learning Models
Several machine learning models were built to predict students' academic performance. Different models were applied and evaluated, but the two that achieved the best results were:
- **📐 AdaBoostClassifier**: Used for predicting performance in Mathematics. This model combines multiple weak classifiers to create a strong classifier.
- **📚 BaggingClassifier**: Used for predicting performance in Portuguese. This model improves stability and accuracy by training multiple instances of the same classifier on different subsets of the data.

### 6. 📈 Model Evaluation
The models were evaluated using cross-validation techniques (K-Fold) to ensure their robustness and accuracy. Metrics such as accuracy, confusion matrix, and other relevant metrics were calculated to assess the performance of the models.

### 7. 💻 Implementation and Visualization
Finally, the models were implemented in an interactive application using Streamlit. The application allows users to input data and obtain predictions about students' academic performance. Additionally, interactive visualizations were included to explore the data and model results.

### 8. 🔄 Continuous Improvement
The project was designed with a focus on continuous improvement. The models are monitored and updated regularly to ensure they remain accurate and relevant. Additionally, user feedback is collected to improve the functionality and usability of the application.

This structured and meticulous development process ensured that the project met its objectives and provided valuable insights to improve students' academic performance.

## 📋 Trello Board

In this section, we explain that we used a Kanban board to organize ourselves as a group, distributing and assigning tasks efficiently. This helped us stay organized, set deadlines, and divide the workload effectively.

You can see more details about how we used the Kanban board in the section [Kanban Board for Task Management](https://github.com/datasilvia/Academic_performance_case_study/tree/main/kanban_board).

## 🗂️ Project Structure

## 🌐 Streamlit App

The Streamlit application provides an interactive interface for exploring the dataset and making predictions about students' academic performance. Below are the key features and functionalities of the Streamlit app:

### Key Features

1. **🏠 Home Page**: 
   - Provides an overview of the project, including its objectives and key features.
   - Introduces the project team and provides a link to the GitHub repository.

2. **🎯 Objectives**:
   - Details the main goals of the project, such as analyzing factors affecting academic performance, identifying patterns, and building predictive models.
   - Explains the expected outcomes, including improved academic performance, informed decision-making, and enhanced student support.

3. **📊 Power BI**:
   - Displays interactive visualizations and insights into the dataset using Power BI.
   - Allows users to explore various aspects of the data, such as the distribution of grades, correlations between variables, and trends over time.

4. **🔮 Prediction**:
   - Enables users to make predictions about students' academic performance in Mathematics and Portuguese.
   - Users can select the subject and input relevant features to obtain predictions.
   - The app uses two machine learning models:
     - **📐 AdaBoostClassifier** for Mathematics: Combines multiple weak classifiers to create a strong classifier.
     - **📚 BaggingClassifier** for Portuguese: Improves stability and accuracy by training multiple instances of the same classifier on different subsets of the data.
   - Displays the accuracy of the models and visualizes the confusion matrix for each prediction.

## 📊 PowerBI

## 🤖 Machine Learning Model

In this project, we applied various machine learning models to predict students' academic performance. After evaluating multiple models, we identified two that provided the best results for predicting performance in Mathematics and Portuguese. Below is a detailed description of the models used and the process followed:

### Models Used

1. **📐 AdaBoostClassifier**:
   - **Purpose**: Used for predicting students' performance in Mathematics.
   - **Description**: AdaBoost (Adaptive Boosting) is an ensemble learning method that combines multiple weak classifiers to create a strong classifier. It works by training classifiers sequentially, each trying to correct the errors of its predecessor. The final model is a weighted sum of the individual classifiers.
   - **Implementation**: The AdaBoostClassifier was implemented using the `AdaBoostClassifier` class from the `sklearn.ensemble` module.

2. **📚 BaggingClassifier**:
   - **Purpose**: Used for predicting students' performance in Portuguese.
   - **Description**: Bagging (Bootstrap Aggregating) is another ensemble learning method that improves the stability and accuracy of machine learning algorithms. It works by training multiple instances of the same classifier on different subsets of the training data (created using bootstrapping) and then averaging their predictions.
   - **Implementation**: The BaggingClassifier was implemented using a pipeline that includes feature selection (`SelectKBest`) and the `BaggingClassifier` class from the `sklearn.ensemble` module, with a `DecisionTreeClassifier` as the base estimator.

### Model Training and Evaluation

#### 📐 Mathematics (AdaBoostClassifier)

- **Data Preparation**: The dataset for Mathematics was preprocessed and the relevant features were selected.
- **Training**: The AdaBoostClassifier was trained using the selected features and the target variable (`math_pass`).
- **Evaluation**: The model was evaluated using K-Fold cross-validation to ensure robustness and accuracy. Metrics such as accuracy and confusion matrix were calculated to assess the model's performance.

#### 📚 Portuguese (BaggingClassifier)

- **Data Preparation**: The dataset for Portuguese was preprocessed and the relevant features were selected.
- **Training**: A pipeline was created that included feature selection (`SelectKBest`) and the BaggingClassifier with a `DecisionTreeClassifier` as the base estimator. The pipeline was trained using the selected features and the target variable (`por_pass`).
- **Evaluation**: The model was evaluated using K-Fold cross-validation. Metrics such as accuracy and confusion matrix were calculated to assess the model's performance.

### Results

- **📐 Mathematics (AdaBoostClassifier)**:
  - **Accuracy**: The model achieved a high accuracy in predicting students' performance in Mathematics.
  - **Confusion Matrix**: The confusion matrix provided insights into the model's performance, showing the number of true positives, true negatives, false positives, and false negatives.

- **📚 Portuguese (BaggingClassifier)**:
  - **Accuracy**: The model achieved a high accuracy in predicting students' performance in Portuguese.
  - **Confusion Matrix**: The confusion matrix provided insights into the model's performance, showing the number of true positives, true negatives, false positives, and false negatives.

### Conclusion

The use of **📐 AdaBoostClassifier** for Mathematics and **📚 BaggingClassifier** for Portuguese provided robust and accurate predictions of students' academic performance. These models were selected based on their superior performance compared to other models evaluated during the project. The implementation of these models in an interactive Streamlit application allows educators and researchers to make data-driven decisions to improve students' academic outcomes.

By following a structured development process and leveraging advanced machine learning techniques, this project demonstrates the potential of predictive analytics in the field of education.

## 👥 Project Members

| Name          | Role         | Special Characteristic       | GitHub Profile                          |
|---------------|--------------|------------------------------|-----------------------------------------|
| Silvia Alonso | 🧑‍💻 Data Analyst | 🥇 Expert in data wrangling     | [Silvia Alonso](https://github.com/datasilvia)  |
| Juan Duran    | 🧑‍💻 Data Analyst | 🌐 Skilled in Streamlit      | [Juan Duran](https://github.com/Jotis86)        |
| Ana Pineda    | 🧑‍💻 Data Analyst | 🏆 Spanish Excel Champion       | [Ana Pineda](https://github.com/asdianita)        |
| Andrea Lafarga| 🧑‍💻 Data Analyst | 📊 Expert in data management    | [Andrea Lafarga](https://github.com/AndreaLaHe)|

## 🤝 Collaborations and Suggestions

We welcome collaborations and suggestions! Feel free to open an issue or submit a pull request. 🚀

Thank you for taking the time to explore our project. We hope you find it useful and informative. Your feedback and contributions are invaluable to us, and we look forward to working together to improve and expand this project. 🙌

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Thank you for visiting our repository! If you have any questions or need further assistance, please don't hesitate to reach out. Happy coding! 😊

<br>

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif"/>