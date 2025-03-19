import streamlit as st
import random
from timer import pomodoro_timer
from data_handler import log_session, log_pause, get_session_data, get_pause_data
from insights import show_productivity_chart, show_pause_chart
from tips import PRODUCTIVITY_TIPS

st.title("📚 AI-Driven Study Timer & Productivity Tracker")

# Timer options
session_dict = {
    "Pomodoro (25 min)": 25,
    "Short Break (5 min)": 5,
    "Long Break (15 min)": 15
}
session_duration = session_dict[session_type]
# Start Timer Button
if st.button("Start Timer"):
    pomodoro_timer(session_duration, session_type)

# Display productivity trends
st.subheader("📊 Productivity Insights")
show_productivity_chart()

# Display Pause Insights
st.subheader("⏸️ Pause Analysis")
show_pause_chart()

# Random Productivity Tip
st.subheader("💡 AI Productivity Tip")
st.write(random.choice(PRODUCTIVITY_TIPS))
