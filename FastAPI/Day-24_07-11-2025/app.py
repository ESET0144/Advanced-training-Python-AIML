import os
#os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # suppress TF logs

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import tensorflow as tf
import pandas as pd
import numpy as np
import joblib

# Initialize FastAPI
app = FastAPI()
templates = Jinja2Templates(directory="template")

# Load model and encoder metadata
model = tf.keras.models.load_model("model.h5")
encoder_info = joblib.load("encoder_columns.pkl")  # Columns from training after encoding

# Define your feature groups
features_num = [
    "lead_time", "arrival_date_week_number", "arrival_date_day_of_month",
    "stays_in_weekend_nights", "stays_in_week_nights", "adults", "children",
    "babies", "is_repeated_guest", "previous_cancellations",
    "previous_bookings_not_canceled", "required_car_parking_spaces",
    "total_of_special_requests", "adr"
]

features_cat = [
    "hotel", "arrival_date_month", "meal", "market_segment",
    "distribution_channel", "reserved_room_type", "deposit_type", "customer_type"
]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    hotel: str = Form(...),
    lead_time: float = Form(...),
    arrival_date_year: int = Form(...),
    arrival_date_month: str = Form(...),
    arrival_date_week_number: int = Form(...),
    arrival_date_day_of_month: int = Form(...),
    stays_in_weekend_nights: int = Form(...),
    stays_in_week_nights: int = Form(...),
    adults: int = Form(...),
    children: float = Form(...),
    babies: int = Form(...),
    meal: str = Form(...),
    market_segment: str = Form(...),
    distribution_channel: str = Form(...),
    is_repeated_guest: int = Form(...),
    previous_cancellations: int = Form(...),
    previous_bookings_not_canceled: int = Form(...),
    reserved_room_type: str = Form(...),
    deposit_type: str = Form(...),
    customer_type: str = Form(...),
    adr: float = Form(...),
    required_car_parking_spaces: int = Form(...),
    total_of_special_requests: int = Form(...)
):
    # Construct input data as DataFrame
    input_dict = {
        "hotel": [hotel],
        "lead_time": [lead_time],
        "arrival_date_year": [arrival_date_year],
        "arrival_date_month": [arrival_date_month],
        "arrival_date_week_number": [arrival_date_week_number],
        "arrival_date_day_of_month": [arrival_date_day_of_month],
        "stays_in_weekend_nights": [stays_in_weekend_nights],
        "stays_in_week_nights": [stays_in_week_nights],
        "adults": [adults],
        "children": [children],
        "babies": [babies],
        "meal": [meal],
        "market_segment": [market_segment],
        "distribution_channel": [distribution_channel],
        "is_repeated_guest": [is_repeated_guest],
        "previous_cancellations": [previous_cancellations],
        "previous_bookings_not_canceled": [previous_bookings_not_canceled],
        "reserved_room_type": [reserved_room_type],
        "deposit_type": [deposit_type],
        "customer_type": [customer_type],
        "adr": [adr],
        "required_car_parking_spaces": [required_car_parking_spaces],
        "total_of_special_requests": [total_of_special_requests],
    }

    df_input = pd.DataFrame(input_dict)

    # One-hot encode categorical columns (same as training)
    df_encoded = pd.get_dummies(df_input, columns=features_cat)

    # Align with training columns
    for col in encoder_info:  # encoder_info is list of all columns used in training
        if col not in df_encoded.columns:
            df_encoded[col] = 0  # Add missing column

    df_encoded = df_encoded[encoder_info]  # Reorder columns exactly as training

    # Predict
    prediction = model.predict(df_encoded)
    predicted_class = int(prediction[0][0] > 0.5)

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "predicted_class": predicted_class,
            "prediction_prob": float(prediction[0][0]),
        },
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
