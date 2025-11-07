import joblib

# Just type your column names here (same as during training)
encoder_columns = [
    'lead_time', 'arrival_date_week_number', 'arrival_date_day_of_month',
    'stays_in_weekend_nights', 'stays_in_week_nights', 'adults', 'children', 'babies',
    'is_repeated_guest', 'previous_cancellations', 'previous_bookings_not_canceled',
    'required_car_parking_spaces', 'total_of_special_requests', 'adr',
    'hotel_City Hotel', 'hotel_Resort Hotel',
    'arrival_date_month_January', 'arrival_date_month_February', 
    'meal_BB', 'meal_HB', 'meal_SC',
    'market_segment_Online TA', 'market_segment_Offline TA/TO',
    'distribution_channel_TA/TO', 'distribution_channel_Direct',
    'reserved_room_type_A', 'reserved_room_type_D',
    'deposit_type_No Deposit', 'deposit_type_Non Refund',
    'customer_type_Transient', 'customer_type_Group'
]

# Save it properly as a pickle file
joblib.dump(encoder_columns, "encoder_columns.pkl")

print("✅ encoder_columns.pkl created successfully!")
