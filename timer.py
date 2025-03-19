import streamlit as st
import time
from data_handler import log_pause

PAUSE_REASONS = ["Phone Distraction", "Social Media", "Urgent Task", "Break", "Other"]

def pomodoro_timer(duration, session_type):
    """Runs a Pomodoro timer with pause functionality."""
    st.write(f"Starting {session_type} session for {duration} minutes...")
    progress_bar = st.progress(0)

    paused = False
    for i in range(duration * 60):  # Convert minutes to seconds
        if st.button("Pause Timer"):
            paused = True
            st.warning("⏸ Timer Paused")
            pause_reason = st.selectbox("Why did you pause?", PAUSE_REASONS)
            if st.button("Resume Timer"):
                paused = False
                log_pause(pause_reason)
                st.success("✅ Resuming Timer...")

        if not paused:
            time.sleep(1)
            progress_bar.progress((i + 1) / (duration * 60))

    st.success(f"{session_type} session completed! 🎉")
