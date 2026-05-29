import streamlit as st
import urllib.request
import urllib.parse
import json
import os
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# --- Page Setup ---
st.set_page_config(page_title="Weather App", page_icon="☁️", layout="centered")

# --- Clean Professional Background ---
def set_clean_background():
    """Injects custom CSS for a modern, clean gradient background."""
    page_bg = """
    <style>
    /* Subtle blue-to-white gradient background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        color: #1e1e1e; /* Dark text for contrast */
    }
    
    /* Make the top header transparent */
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }
    
    /* Style the metric boxes to look like cards */
    [data-testid="metric-container"] {
        background-color: white;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)

# Apply the background immediately
set_clean_background()

# --- Main App Logic ---
def get_weather():
    st.title("☁️ Live Weather Tracker")
    st.write("Welcome! Type a city below to get real-time weather data.")

    api_key = os.getenv("API_KEY")
    
    if not api_key:
        st.error("Error: API_KEY not found. Please check your .env file.")
        return

    city = st.text_input("Enter a city name:", placeholder="e.g. Chicago, London, Nairobi")
    
    if st.button("Check Weather"):
        if city:
            encoded_city = urllib.parse.quote(city)
            url = f"http://api.openweathermap.org/data/2.5/weather?q={encoded_city}&appid={api_key}&units=imperial"
            
            try:
                response = urllib.request.urlopen(url)
                data = json.loads(response.read())
                
                # Extract the data
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                humidity = data['main']['humidity']
                description = data['weather'][0]['description'].title()
                
                # --- Displaying Data ---
                st.success(f"Current weather for {city.title()}")
                
                # Metrics automatically get the "card" styling from our CSS above
                col1, col2, col3 = st.columns(3)
                col1.metric("Temperature", f"{temp} °F")
                col2.metric("Feels Like", f"{feels_like} °F")
                col3.metric("Humidity", f"{humidity} %")
                
                st.info(f"**Conditions:** {description}")
                
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    st.error("City not found. Please check the spelling and try again.")
                elif e.code == 401:
                    st.error("Invalid API Key. Please check your .env file.")
                else:
                    st.error(f"An error occurred: {e}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
        else:
            st.warning("Please enter a city name first.")

if __name__ == "__main__":
    get_weather()