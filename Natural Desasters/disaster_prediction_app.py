import streamlit as st
import pandas as pd
import pickle

# Load the saved models
with open('minmax_scaler2.pkl', 'rb') as file:
    transformer = pickle.load(file)  # use minmax_scaler here

with open('label_encoder2.pkl', 'rb') as file:
    label_encoder = pickle.load(file)

with open('gradient_boosting_model2.pkl', 'rb') as file:
    gradient_boosting_model = pickle.load(file)

# Streamlit user interface
st.title('Disaster Type Prediction')

# Example of user input collection
disaster_subgroup = st.selectbox('Select Disaster Subgroup', options=['Subgroup1', 'Subgroup2', 'Subgroup3'])
country = st.text_input('Enter Country')
region = st.text_input('Enter Region')
continent = st.text_input('Enter Continent')

# When 'Predict' button is clicked
if st.button('Predict'):
    # Create a DataFrame from the inputs
    input_data = pd.DataFrame([[disaster_subgroup, country, region, continent]],
                              columns=['disaster_subgroup', 'country', 'region', 'continent'])
    
    # Encode the inputs
    for column in ['disaster_subgroup', 'country', 'region', 'continent']:
        input_data[column] = label_encoder.transform(input_data[column])

    # Scale the inputs
    input_data_scaled = transformer.transform(input_data)  # use minmax_scaler here

    # Make prediction
    prediction = gradient_boosting_model.predict(input_data_scaled)
    predicted_type = prediction[0]

    # Display the prediction
    st.write(f'Predicted Disaster Type: {predicted_type}')

# Run the Streamlit app by typing in the terminal:
# streamlit run disaster_prediction_app.py