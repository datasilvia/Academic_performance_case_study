import streamlit as st
import pandas as pd
import os
import numpy as np
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import confusion_matrix, accuracy_score
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
#df = pd.read_csv('path_to_your_dataset.csv')

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the images
main_image_path = os.path.join(current_dir, 'principal.png')
sidebar_image_path = os.path.join(current_dir, 'menu.png') 

# Streamlit app
st.sidebar.image(sidebar_image_path, use_column_width=True)
st.sidebar.title('Navigation')
option = st.sidebar.radio('Select a page:', 
                          ['Home', 'Objectives', 'Power BI', 'Prediction'])


# Project Members
st.sidebar.markdown("## Project Members")
st.sidebar.markdown("""
| Name           | Special Characteristic         |
|----------------|--------------------------------|
| Silvia Alonso  | 🥇 Expert in data wrangling     |
| Juan Duran     | 🌐 Skilled in Streamlit         |
| Ana Pineda     | 🏆 Spanish Excel Champion       |
| Andrea Lafarga | 📊 Expert in data management    |
""")

# GitHub Repository Link
st.sidebar.markdown("""
    <style>
    .github-button {
        display: inline-block;
        padding: 10px 20px;
        font-size: 16px;
        color: black;
        background-color: #e0e0e0;
        border: none;
        border-radius: 5px;
        text-align: center;
        text-decoration: none;
    }
    .github-button:hover {
        background-color: #d0d0d0;
    }
    </style>
    <a href="https://github.com/datasilvia/Academic_performance_case_study" class="github-button" target="_blank">GitHub Repository</a>
    """, unsafe_allow_html=True)

# Display the main image at the top of every page
st.image(main_image_path, use_column_width=True)

if option == 'Home':
    #st.title('📊 Academic Performance Analysis')
    st.write("""
    Welcome to the Academic Performance Case Study application. 
    Use the navigation menu on the left to explore different sections of the project.
    """)

    st.header('📋 Project Overview')
    st.write("""
    This project aims to analyze the factors affecting students' academic performance. 
    By exploring various attributes such as demographics, family background, and academic records, 
    we aim to identify patterns and correlations that can help in predicting students' performance.
    """)

    st.header('✨ Key Features')
    st.write("""
    - **🎯 Objectives**: Understand the main goals of the project.
    - **🛠️ Methodology**: Learn about the steps and processes followed in the project.
    - **📊 Power BI**: Explore interactive visualizations and insights.
    - **🔮 Prediction**: Discover the predictive models used to forecast students' performance.
    """)

    st.header('📚 How to Use This App')
    st.write("""
    - 🧭 Navigate through the different sections using the menu on the left.
    - 📄 Each section provides detailed information and insights about the project.
    - 📈 Use the Power BI section to interact with the data visualizations.
    - 🔍 Check the Prediction section to see the models and their predictions.
    """)


elif option == 'Objectives':
    st.title('🎯 Objectives')
    st.write("""
    The main objectives of this project are:
    - **📊 Analyze Factors**: To analyze the factors affecting students' academic performance, including demographics, family background, and academic records.
    - **🔍 Identify Patterns**: To identify patterns and correlations in the data that can provide insights into students' performance.
    - **🔮 Predict Performance**: To build predictive models to forecast students' performance based on the identified factors and patterns.
    - **📈 Improve Outcomes**: To provide actionable insights that can help educators and policymakers improve students' academic outcomes.
    - **🧠 Enhance Understanding**: To enhance the understanding of the various factors that influence academic performance and how they interact with each other.
    - **📚 Support Decision Making**: To support data-driven decision making in educational institutions by providing reliable predictions and insights.
    """)

    st.header('📋 Detailed Goals')
    st.write("""
    - **📥 Data Collection**: Gather comprehensive data from various sources to ensure a robust analysis.
    - **🧹 Data Cleaning**: Handle missing values, outliers, and inconsistencies to prepare the data for analysis.
    - **🔍 Exploratory Data Analysis (EDA)**: Visualize and summarize the data to uncover initial insights and patterns.
    - **🛠️ Feature Engineering**: Create new features from existing data to improve the predictive power of the models.
    - **🤖 Model Building**: Train various machine learning models to predict students' performance.
    - **📊 Model Evaluation**: Assess the performance of the models using metrics such as accuracy, precision, recall, and F1-score.
    - **🚀 Deployment**: Deploy the best-performing model to provide real-time predictions and insights.
    - **🔄 Continuous Improvement**: Continuously monitor and improve the models to ensure they remain accurate and relevant.
    """)

    st.header('🌟 Expected Outcomes')
    st.write("""
    - **📈 Improved Academic Performance**: By understanding the factors that influence performance, educators can implement targeted interventions to help students succeed.
    - **📊 Informed Decision Making**: Educational institutions can make data-driven decisions to allocate resources effectively and improve student outcomes.
    - **👩‍🏫 Enhanced Student Support**: Provide personalized support to students based on their unique needs and circumstances.
    - **🏛️ Policy Development**: Inform policy development at the institutional and governmental levels to create a supportive learning environment.
    - **📚 Research Contributions**: Contribute to the body of research on educational data analysis and predictive modeling.
    """)


elif option == 'Power BI':
    st.title('📊 Power BI')
    st.write("""
    The Power BI dashboard provides interactive visualizations and insights into the dataset. 
    You can explore various aspects of the data, such as:
    - Distribution of students' grades.
    - Correlation between different variables.
    - Trends and patterns in the data.
    """)
    #st.image(os.path.join(current_dir, 'powerbi_dashboard.png'), use_column_width=True)

elif option == 'Prediction':
    st.title('🔮 Prediction')
    st.write("""
    The prediction section involves building and evaluating machine learning models to forecast students' performance.
    The models used include:
    - Linear Regression
    - Decision Trees
    - Random Forest
    - Support Vector Machines (SVM)
    """)

    # Cargar los datos desde el archivo CSV
    data_path = os.path.join(current_dir, 'df_limpito_EDA.csv')
    data = pd.read_csv(data_path)

    # Cargar y mostrar los DataFrames tratados para cada asignatura
    math_data_path = os.path.join(current_dir, 'ML_Math.csv')
    portuguese_data_path = os.path.join(current_dir, 'ML_Portuguese.csv')

    math_data = pd.read_csv(math_data_path)
    portuguese_data = pd.read_csv(portuguese_data_path)


    # Seleccionar la asignatura a predecir 
    st.markdown("### Select the subject to predict:")
    subject = st.radio('', ['Mathematics', 'Portuguese'], index=0, horizontal=True)

    # Definir las características y la variable objetivo
    X = math_data[['school_GP', 'age', 'address_urban', 'Medu', 'Fedu', 'studytime', 'failures', 'freetime', 'Dalc', 'Walc']]
    y = math_data['math_pass']

    # Inicializar el clasificador
    modelo = AdaBoostClassifier(random_state=42)

    # Configurar K-Fold
    kf = KFold(n_splits=5, shuffle=True, random_state=42)

    # Crear arrays para almacenar las predicciones y valores reales
    y_pred_total = np.array([])
    y_real_total = np.array([])

    # Ejecutar K-Fold
    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        modelo.fit(X_train, y_train)
        y_pred = modelo.predict(X_test)

        # Almacenar las predicciones y los valores reales
        y_pred_total = np.concatenate([y_pred_total, y_pred])
        y_real_total = np.concatenate([y_real_total, y_test])

    # Mostrar la precisión del modelo
    accuracy = accuracy_score(y_real_total, y_pred_total)
    st.write(f'Accuracy of the Model: {accuracy:.3f}')

    # Pedir al usuario que ingrese los valores de las características
    st.write("### Enter the values for the following features to make a prediction:")
    school_GP = st.selectbox('🏫 School (GP=1, Other=0):', [0, 1])
    age = st.number_input('🎂 Age:', min_value=15, max_value=22, value=17)
    address_urban = st.selectbox('🏡 Address (Urban=1, Rural=0):', [0, 1])
    Medu = st.number_input('👩‍🎓 Mother\'s Education (0-4):', min_value=0, max_value=4, value=2)
    Fedu = st.number_input('👨‍🎓 Father\'s Education (0-4):', min_value=0, max_value=4, value=2)
    studytime = st.number_input('📚 Study Time (1-4):', min_value=1, max_value=4, value=2)
    failures = st.number_input('❌ Failures (0-3):', min_value=0, max_value=3, value=0)
    freetime = st.number_input('🕒 Free Time (1-5):', min_value=1, max_value=5, value=3)
    Dalc = st.number_input('🍷 Workday Alcohol Consumption (1-5):', min_value=1, max_value=5, value=1)
    Walc = st.number_input('🍻 Weekend Alcohol Consumption (1-5):', min_value=1, max_value=5, value=2)

    # Crear un DataFrame con los valores ingresados
    input_data = pd.DataFrame({
        'school_GP': [school_GP],
        'age': [age],
        'address_urban': [address_urban],
        'Medu': [Medu],
        'Fedu': [Fedu],
        'studytime': [studytime],
        'failures': [failures],
        'freetime': [freetime],
        'Dalc': [Dalc],
        'Walc': [Walc]
    })

    # Hacer la predicción
    prediction = modelo.predict(input_data)
    st.write(f'### The predicted math pass status is: {"🎉 Pass" if prediction[0] == 1 else "❌ Fail"}')