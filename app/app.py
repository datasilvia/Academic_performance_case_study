import streamlit as st
import pandas as pd
import os

# Load the dataset
#df = pd.read_csv('path_to_your_dataset.csv')

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Path to the image
image_path = os.path.join(current_dir, 'principal.png')

# Streamlit app
st.sidebar.title('Navigation')
option = st.sidebar.selectbox('Select a page:', 
                              ['Home', 'Objectives', 'Methodology', 'Power BI', 'Prediction'])

if option == 'Home':
    st.title('📊 Academic Performance Case Study')
    st.image(image_path, use_column_width=True)
    st.write("""
    Welcome to the Academic Performance Case Study application. 
    Use the navigation menu on the left to explore different sections of the project.
    """)

elif option == 'Objectives':
    st.title('🎯 Objectives')
    st.write("""
    The main objectives of this project are:
    - To analyze the factors affecting students' academic performance.
    - To identify patterns and correlations in the data.
    - To build predictive models to forecast students' performance.
    """)

elif option == 'Methodology':
    st.title('🛠️ Methodology')
    st.write("""
    The methodology followed in this project includes:
    1. Data Collection: Gathering data from various sources.
    2. Data Cleaning: Handling missing values and outliers.
    3. Exploratory Data Analysis (EDA): Visualizing and summarizing the data.
    4. Feature Engineering: Creating new features from existing data.
    5. Model Building: Training machine learning models to predict students' performance.
    6. Model Evaluation: Assessing the performance of the models using various metrics.
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
    st.image(os.path.join(current_dir, 'powerbi_dashboard.png'), use_column_width=True)

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