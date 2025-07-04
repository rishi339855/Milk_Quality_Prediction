import streamlit as st
import pandas as pd
import numpy as np
import pickle 

# Load the saved model from the file
with open('rf_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
arr = []
tab1, tab2= st.tabs(["Home", "About"])
st.title("MILK QUALITY PREDICTION")
st.subheader("Using Machine learning to predict :red[Milk Quality].",divider='rainbow')
st.divider()
#NAME
st.markdown("<p style='font-size:20px';>Please Enter your name below",unsafe_allow_html=True)
st.text_input("Name", key="name", placeholder="Name", label_visibility="collapsed")
a= (st.session_state.name).upper()
if a:
    st.success(f"Hi {a}, welcome to our website!😇")

# pH and Temperature
container1 = st.container()
with container1:
    col1,col2= st.columns([1,1])
    with col1:
        number1 = st.number_input("pH Value",placeholder="Please Enter pH Value")
        arr.append(number1)
    with col2:
        number2 = st.number_input("Temperature",placeholder="Please Enter Temperature (C)")
        arr.append(number2)
        
st.markdown("<p style='font-size:25px';>Please Enter the following in scale of 0 to 1.",unsafe_allow_html=True)
container2 = st.container()
with container2:
    col3,col4,col5= st.columns([1,1,1])
    with col3:
        number3 = st.number_input("Taste",placeholder="How does it taste?",min_value=0.0, max_value=1.0, step=0.01)
        arr.append(number3)
    with col4:
        number4 = st.number_input("Odor",placeholder="How does it smell?",min_value=0.0, max_value=1.0, step=0.01)
        arr.append(number4)
    with col5:
        number5 = st.number_input("Fat",placeholder="Fat content",min_value=0.0, max_value=1.0, step=0.01)
        arr.append(number5)

container3 = st.container()
with container3:
    col6,col7= st.columns([1,1])
    with col6:
        number6 = st.number_input("Turbidity",placeholder="Turbidity",min_value=0.0, max_value=1.0, step=0.01)
        arr.append(number6)
    with col7:
        number7 = st.number_input("Colour",placeholder="Colour Scale")
        arr.append(number7)
        
    def predict_milk():
        # Create DataFrame with proper feature names to match the training data
        feature_names = ['pH', 'Temprature', 'Taste', 'Odor', 'Fat ', 'Turbidity', 'Colour']
        input_df = pd.DataFrame([arr], columns=feature_names)
        prediction = loaded_model.predict(input_df)
        return prediction[0]  # Extract the single value from the array

but1 = st.button('Predict!',type='primary')
if but1:
    if len(arr)!= 7:
        st.error("Please fill all the details!😅")
    else:
        result = predict_milk()
        if result == 0:
            st.success("MILK GRADE: HIGH QUALITY")
        elif result == 1:
            st.error("MILK GRADE: LOW QUALITY")
        elif result == 2:
            st.success("MILK GRADE: MEDIUM QUALITY")
        else:
            st.warning(f"Unknown prediction value: {result}")
        
