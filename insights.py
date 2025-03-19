import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_handler import get_session_data, get_pause_data

def show_productivity_chart():
    """Displays a chart of past sessions."""
    df = get_session_data()
    
    if df is None:
        st.write("No session data available yet.")
        return

    df["Date"] = pd.to_datetime(df["Date"])
    df.sort_values(by="Date", inplace=True)

    fig, ax = plt.subplots()
    ax.plot(df["Date"], df["Duration (min)"], marker='o', linestyle='-')
    ax.set_title("📊 Productivity Trend")
    ax.set_xlabel("Date")
    ax.set_ylabel("Session Duration (min)")
    ax.grid(True)

    st.pyplot(fig)

def show_pause_chart():
    """Displays a pie chart of pause reasons."""
    df = get_pause_data()
    
    if df is None:
        st.write("No pause data available yet.")
        return

    pause_counts = df["Reason"].value_counts()

    fig, ax = plt.subplots()
    ax.pie(pause_counts, labels=pause_counts.index, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'green', 'purple', 'orange'])
    ax.set_title("⏸️ Reasons for Pausing")

    st.pyplot(fig)
