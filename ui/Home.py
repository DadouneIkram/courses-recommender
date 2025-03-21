import streamlit as st
import pandas as pd
import os
import random

st.set_page_config(
  page_title='courses recommender',
  page_icon="📚",
  layout="centered",
  # initial_sidebar_state: InitialSideBarState = "auto"
)

st.markdown("""
## **Welcome to Courses Recommender 📚**

### **Discover Your Next Learning Adventure!**  
Are you passionate about learning but unsure what to dive into next? Our **Courses Recommender App** is here to help! Whether you're looking to upskill in a new area or deepen your knowledge in a specific field, we make it easy to find the right courses tailored to you.

---

## **How It Works**  
1. **Data-Powered Recommendations**:  
   Our app uses advanced recommendation algorithms, including **Apriori**,  **Eclat** and **FP-Growth** to analyze course data and user interactions.

2. **Personalized Suggestions**:  
   Simply select the courses you've already watched, choose a recommendation algorithm, and let our app suggest courses that match your interests and learning journey.

3. **Data Insights**:  
   You can explore the data we used for this app in the [rating](/ratings) and [courses](/courses) pages.

---

## **What’s Inside?**  
- **Visualize Ratings Data** 📊: Gain insights into course ratings and user activity.  
- **Browse Courses** 🎓: Discover the courses in our database, complete with descriptions and IDs.  
- **Get Recommendations** 💡: Select the courses you've watched, choose an algorithm, and unlock personalized course recommendations.

---

## **Start Exploring Now!**  
Navigate through the tabs to explore data, select courses, and find your next big learning adventure!
""")