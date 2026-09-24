import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

pipeline = joblib.load('flight_pipeline.pkl')

app = FastAPI()

class FlightData(BaseModel):
    destination: str
    source: str
    airline: str
    stops: int
    duration: int
    journey_day: int
    journey_month: int
    dep_hour: int
    dep_min: int
    arrival_hour: int
    arrival_min: int

@app.get("/")
def home():
    return {"message": "The Flight Price Server is Running!"}

@app.post("/predict")
def predict_flight_price(flight_data: FlightData):
    df = pd.DataFrame({'Destination': [flight_data.destination],
         'Source': [flight_data.source],
         'Airline': [flight_data.airline],
         'Total_Stops': [flight_data.stops],
         'Duration': [flight_data.duration],
         'Journey_day': [flight_data.journey_day],
         'Journey_month': [flight_data.journey_month],
         'Dep_hour': [flight_data.dep_hour],
         'Dep_min': [flight_data.dep_min],
         'Arrival_hour': [flight_data.arrival_hour],
         'Arrival_min': [flight_data.arrival_min]
         })
    price = pipeline.predict(df)
    return {'predicted_price': price[0]}



