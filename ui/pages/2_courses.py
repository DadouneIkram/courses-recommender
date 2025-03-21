import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(
  page_title='courses recommender',
  page_icon="📚",
  layout="centered",
  # initial_sidebar_state: InitialSideBarState = "auto"
)

# # courses
data_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

# Construct file paths
all_courses_path = os.path.join(data_folder, 'all_courses.csv')
rated_courses_path = os.path.join(data_folder, 'rated_courses.csv')
ratings_courses_path = os.path.join(data_folder, 'ratings_courses.csv')

# Load datasets
all_courses = pd.read_csv(all_courses_path)
rated_courses = pd.read_csv(rated_courses_path)
ratings_courses = pd.read_csv(ratings_courses_path)

st.header('📈 data story:')

st.warning('within our datasets, we have the set of all courses, from it we extracted only the rated ones which are the ones we are interested in.')

# all courses
st.subheader('∀ all courses:')

st.markdown('##### all courses head: ')
st.dataframe(all_courses.head())
st.markdown('##### all courses tail: ')
st.dataframe(all_courses.tail())

col1, col2, col3 = st.columns(3)

all_courses_number = all_courses['course_id'].nunique()
all_courses_missing_vals = all_courses.isna().sum().sum()
all_courses_duplicated_vals = all_courses.duplicated().sum()

col1.metric("number of courses", f'{all_courses_number} 📚')
col2.metric("missing values", f'{all_courses_missing_vals} ❔')
col3.metric("number of duplicates", f'{all_courses_duplicated_vals} 🗐')

# rated courses  
st.subheader('∃ only rated courses:')

st.markdown('##### rated courses head: ')
st.dataframe(all_courses.head())
st.markdown('##### rated courses tail: ')
st.dataframe(all_courses.tail())

col1, col2, col3 = st.columns(3)

rated_courses_number = rated_courses['course_id'].nunique()
rated_courses_missing_vals = rated_courses.isna().sum().sum()
rated_courses_duplicated_vals = rated_courses.duplicated().sum()

col1.metric("number of courses", f'{rated_courses_number} 📚')
col2.metric("missing values", f'{rated_courses_missing_vals} ❔')
col3.metric("number of duplicates", f'{rated_courses_duplicated_vals} 🗐')

courses_ratings_summery = ratings_courses.groupby(by='course_id')['rating'].agg(['mean', 'count']).reset_index().rename(columns={'mean': 'average_rating', 'count': 'ratings_count'}).merge(rated_courses)

st.subheader('rated courses summery: ')
st.dataframe(courses_ratings_summery.head())

best_rated_courses = courses_ratings_summery.sort_values(by='average_rating', ascending=False).head(10)
worst_rated_courses = courses_ratings_summery.sort_values(by='average_rating').head(10)
most_rated_courses = courses_ratings_summery.sort_values(by='ratings_count',  ascending=False).head(10)

fig = px.bar(best_rated_courses, x='title', y='average_rating', orientation='v', title='Best Rated Courses')
st.plotly_chart(fig)

fig = px.bar(worst_rated_courses, x='title', y='average_rating', orientation='v', title='Worst Rated Courses')
st.plotly_chart(fig)

fig = px.bar(most_rated_courses, x='title', y='ratings_count', orientation='v', title='Most Rated Courses')
st.plotly_chart(fig)