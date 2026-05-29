☁️ LIVE WEATHER DASHBOARD

A real-time weather tracking web application built with Python and Streamlit. This project demonstrates backend API integration, secure data handling, and modern UI deployment.


🚀 LIVE DEMO

(https://emwangi-weather.streamlit.app/)

🛠️ TECHNOLOGIES AND FRAMEWORKS USED

Python 3: Core application logic.

Streamlit: Frontend framework for building the interactive web UI.

OpenWeatherMap API: Real-time weather data integration.

Git/GitHub: Version control and repository management.

Streamlit Community Cloud: CI/CD and cloud hosting.



💡 KEY FEATURES:

Real-Time Data: Fetches live temperature, feels like temperature, humidity, and weather conditions for any global city.

Secure Architecture: API keys are protected using environment variables (dotenv) locally and encrypted secrets in production.

Responsive UI: Clean, modern dashboard design with dynamic metric cards.

Error Handling: Hanldes invalid city inputs and API connection errors with user-friendly alerts.


⚙️ LOCAL INSTALLATION:

To run this project locally on your machine:

CLONE THE REPOSITORY:
git clone [https://github.com/Emwangi47/weather-app-python.git](https://github.com/Emwangi47/weather-app-python.git)


NAVIGATE TO PROJECT DIRECTORY:
cd weather-app-python


INSTALL THE REQUIRED DEPENDENCIES:
pip install -r requirements.txt


CREATE .env FILE IN ROOT DIRECTORY AND ADD OPEN WEATHER API KEY:
API_KEY=your_api_key_here


RUN STREAMLIT APP:
streamlit run weather.py