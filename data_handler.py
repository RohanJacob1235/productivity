import pandas as pd
import datetime

SESSION_FILE = "sessions.csv"
PAUSE_FILE = "pauses.csv"

def log_session(duration, session_type):
    """Logs the session data into a CSV file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {"Date": [timestamp], "Duration (min)": [duration], "Type": [session_type]}
    df = pd.DataFrame(data)

    try:
        df_existing = pd.read_csv(SESSION_FILE)
        df = pd.concat([df_existing, df], ignore_index=True)
    except FileNotFoundError:
        pass

    df.to_csv(SESSION_FILE, index=False)

def get_session_data():
    """Retrieve session data from the CSV file."""
    try:
        df = pd.read_csv(SESSION_FILE)
        return df
    except FileNotFoundError:
        return None

def log_pause(reason):
    """Logs the pause reason into a CSV file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {"Date": [timestamp], "Reason": [reason]}
    df = pd.DataFrame(data)

    try:
        df_existing = pd.read_csv(PAUSE_FILE)
        df = pd.concat([df_existing, df], ignore_index=True)
    except FileNotFoundError:
        pass

    df.to_csv(PAUSE_FILE, index=False)

def get_pause_data():
    """Retrieve pause data from the CSV file."""
    try:
        df = pd.read_csv(PAUSE_FILE)
        return df
    except FileNotFoundError:
        return None
