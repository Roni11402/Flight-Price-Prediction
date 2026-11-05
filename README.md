# Flight Price Prediction API

A machine learning REST API that predicts flight prices based on route, airline, and scheduling data.

## Features
The model takes the following inputs to generate a price prediction:
* **Route Details:** Source, destination, airline, and number of stops.
* **Scheduling:** Travel day and month, departure time, arrival time, and total flight duration.

## Tech Stack
* **Machine Learning:** Python, pandas, scikit-learn, Random Forest Regressor.
* **Backend:** FastAPI, Uvicorn

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Roni11402/Flight-Price-Prediction.git
   cd Flight-Price-Prediction
   pip install -r requirements.txt 
   uvicorn main:app --reload 
   ```

2. Open http://127.0.0.1:8000/docs to try the API
