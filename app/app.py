import streamlit as st
import pandas as pd
import os

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