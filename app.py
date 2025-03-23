import streamlit as st
import pandas as pd

# Load data
def load_data():
    return pd.read_csv("data/mess_ratings.csv")

# Save new rating
def save_rating(name, rating, feedback):
    df = load_data()
    new_entry = pd.DataFrame([[name, rating, feedback]], columns=["Name", "Rating", "Feedback"])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv("data/mess_ratings.csv", index=False)

# ---- 🎨 Custom Styling ----
st.set_page_config(page_title="Hostel Mess Rating", layout="wide")

st.markdown("""
    <style>
    /* Change background */
    .main { background-color: #f4f4f9; }

    /* Center align headings */
    h1 { text-align: center; color: #ff6f00; font-weight: bold; }

    /* Sidebar background & text color */
    section[data-testid="stSidebar"] {
        background-color: #1e3a8a !important; /* Dark Blue */
    }
    
    /* Sidebar Text (Force White) */
    section[data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Change Button Colors */
    .stButton>button {
        background-color: #ff6f00; /* Orange */
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #ff8c42; /* Lighter Orange */
    }

    /* Dataframe Styling */
    .stDataFrame { border-radius: 10px; }

    </style>
""", unsafe_allow_html=True)

# ---- 🏠 App Title ----
st.markdown("<h1>🏠 Hostel Mess Rating System 🍽️</h1>", unsafe_allow_html=True)

# ---- 📌 Sidebar Menu ----
st.sidebar.title("📌 Navigation")
menu = ["⭐ Rate Mess", "📊 View Ratings"]
choice = st.sidebar.radio("Select a page:", menu)

# ---- ⭐ Rating Page ----
if choice == "⭐ Rate Mess":
    st.subheader("⭐ Rate Today's Mess")

    col1, col2 = st.columns([2, 1])
    
    with col1:
        name = st.text_input("Your Name", placeholder="Enter your name here")
        rating = st.slider("Rate (1-5)", 1, 5, 3)
        feedback = st.text_area("Feedback", placeholder="Leave your feedback here")

    with col2:
        try:
            st.image("data/mess_food.jpg", caption="Today's Meal", use_container_width=True)
        except Exception as e:
            st.warning("⚠️ Image not found! Please check if 'mess_food.jpg' exists.")

    if st.button("Submit Rating"):
        if name.strip():
            save_rating(name, rating, feedback)
            st.success("✅ Rating submitted! Thank you for your feedback. 🙌")
        else:
            st.warning("⚠️ Please enter your name before submitting.")

# ---- 📊 Ratings Page ----
elif choice == "📊 View Ratings":
    st.subheader("📊 Overall Ratings")
    
    df = load_data()

    # Display ratings in a column layout
    col1, col2 = st.columns([2, 1])

    with col1:
        st.write("### 📋 Rating Data")
        st.dataframe(df)

    with col2:
        st.write("### 📊 Ratings Breakdown")
        st.bar_chart(df["Rating"].value_counts().sort_index())

    # ✅ View Feedback in Expander
    with st.expander("📖 View Feedback"):
        st.write(df[["Name", "Feedback"]])  # This line was missing!
