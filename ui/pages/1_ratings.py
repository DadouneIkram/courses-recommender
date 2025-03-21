import streamlit as st
import pandas as pd
import os

st.set_page_config(
  page_title='courses recommender',
  page_icon="📚",
  layout="centered",
  # initial_sidebar_state: InitialSideBarState = "auto"
)

# ratings   
data_folder = os.path.join(os.path.dirname(__file__), '..', 'data')
ratings_path = os.path.join(data_folder, 'ratings.csv')

ratings = pd.read_csv(ratings_path)

st.header('📈 data story:')

col1, col2 = st.columns(2)
col1.subheader('ratings head: ')
col1.dataframe(ratings.head())
col2.subheader('ratings tail: ')
col2.dataframe(ratings.tail())

st.markdown('#### 📊 ratings distribution:')
st.bar_chart(ratings['rating'].value_counts())



min_rating = ratings['rating'].min()
max_rating = ratings['rating'].max()
avg_rating = ratings['rating'].mean()
ratings_mode = ratings['rating'].mode()
col1, col2, col3, col4 = st.columns(4)

col1.metric("minimum rating", f'{min_rating} ⭐')
col2.metric("average rating", f'{round(avg_rating, 2)} ⭐')
col3.metric("maximum rating", f'{max_rating} ⭐')
col4.metric("ratings mode", f'{ratings_mode[0]} ⭐')

users_number = ratings['user_id'].nunique()
users_unique_ratings = ratings['rating'].nunique()
missing_vals = ratings.isna().sum().sum()
courses_number = ratings['course_id'].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("number of users", f'{users_number} 🧑')
col2.metric("missing values", f'{missing_vals} ❔')
col3.metric("number of rated courses", f'{courses_number} 📚')
col4.metric("number of unique ratings", f'{users_unique_ratings} ⭐')

st.markdown('### 📊 most active users:')
users_activity = ratings.groupby('user_id')['rating'].count().reset_index()
users_activity.rename(columns={'rating': 'ratings_count'}, inplace=True)
st.bar_chart(users_activity.sort_values(by='ratings_count', ascending=False).head(10).set_index('user_id'), x_label='user_id', y_label='ratings_count')