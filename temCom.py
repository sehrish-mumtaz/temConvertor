import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit App title
st.title("Temperature Converter")

# Dropdown menu to select conversion type
conversion_type = st.selectbox("Choose Conversion Type:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

# Input field to enter the temperature
temperature = st.number_input("Enter the temperature to convert:")

# Perform the conversion based on the selected type
if st.button("Convert"):
    if conversion_type == "Celsius to Fahrenheit":
        result = celsius_to_fahrenheit(temperature)
        st.success(f"{temperature}°C is equal to {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(temperature)
        st.success(f"{temperature}°F is equal to {result:.2f}°C")
