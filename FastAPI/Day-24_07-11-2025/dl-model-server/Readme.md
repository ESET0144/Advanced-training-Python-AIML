Project Report: Hotel Booking Cancellation Prediction

This project focuses on predicting hotel booking cancellations using a Deep Learning model built with TensorFlow/Keras.
The model was trained on hotel booking data with 32 input features, including both numerical and categorical variables.
Categorical features were transformed using a OneHotEncoder, saved as encoder_columns.pkl for consistent preprocessing.
The trained model (model.h5) was integrated and deployed using FastAPI for real-time inference.
A user-friendly HTML interface (index.html) was created to collect booking details for prediction.
Upon form submission, data is encoded, processed, and passed to the trained model for prediction.
The output is displayed on a result page, indicating whether a booking is likely to be canceled.
Deployment warnings and compatibility issues with TensorFlow were handled during setup.
The project demonstrates end-to-end deep learning model deployment on a live web server.
🔗 Live Demo: https://dl-model-server-1.onrender.com/