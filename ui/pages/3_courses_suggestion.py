import os
import streamlit as st
import pandas as pd
import pickle
from models.fp_growth import fp_growth_recommend
from models.apriori import apriori_recommend
from mlxtend.frequent_patterns import fpgrowth, association_rules

st.set_page_config(
    page_title='Courses Recommender',
    page_icon="📚",
    layout="centered",
)

# Get the correct path to the data folder
data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

# Use caching to load data and rules
@st.cache_data
def load_data():
    clean_user_with_courses_path = os.path.join(data_folder, 'clean_user_with_courses.csv')
    rated_courses_path = os.path.join(data_folder, 'rated_courses.csv')
    fp_growth_rules_path = os.path.join(data_folder, 'fp_growth_association_rules.csv')
    apriori_rules_path = os.path.join(data_folder, 'apriori_association_rules.csv')

    clean_user_with_courses = pd.read_csv(clean_user_with_courses_path)
    rated_courses = pd.read_csv(rated_courses_path)
    fp_growth_rules = pd.read_csv(fp_growth_rules_path)
    apriori_rules = pd.read_csv(apriori_rules_path)
    
    return clean_user_with_courses, rated_courses, fp_growth_rules, apriori_rules

clean_user_with_courses, rated_courses, fp_growth_rules, apriori_rules = load_data()

# UI
st.title('Explore New Courses 📚')

selected_titles = st.multiselect(
    "# Select the courses you've watched",
    rated_courses['title'], 
    help="Select the courses you have completed to get tailored recommendations.",
)

selected_ids = rated_courses[rated_courses['title'].isin(selected_titles)]['course_id'].to_list()

algorithm = st.selectbox(
    "Choose an algorithm for recommendations:",
    ["apriori", "eclat", "fp_growth"],
    help="Choose the algorithm you prefer for generating course recommendations."
)

if st.button("Get Recommendations"):
    if algorithm == 'apriori':
        recommendations = apriori_recommend(apriori_rules, selected_ids)
    elif algorithm == 'eclat':
        pass  # Implement Eclat if needed
    else:
        recommendations = fp_growth_recommend(fp_growth_rules, selected_ids)

    if recommendations:
        recommended_courses = rated_courses[rated_courses['course_id'].isin(recommendations)]['title'].tolist()
        st.write("Recommended courses:", recommended_courses)
    else:
        st.write("No recommendations found.")
