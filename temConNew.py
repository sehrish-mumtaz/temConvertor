import streamlit as st

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit App title and subtitle
st.title("🌡️ Temperature Converter")
st.subheader("Convert between Celsius and Fahrenheit easily!")

# Sidebar instructions
st.sidebar.header("Instructions")
st.sidebar.write("""
1. Choose the conversion type from the dropdown menu.
2. Enter the temperature you want to convert.
3. Press the 'Convert' button to see the result.
""")

# Sidebar image (for visual interest)
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Thermometer_blue.svg/1200px-Thermometer_blue.svg.png", use_column_width=True)

# Dropdown menu to select conversion type
conversion_type = st.selectbox("Choose Conversion Type:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

# Input field to enter the temperature
temperature = st.number_input("🌡️ Enter the temperature to convert:", format="%.2f")

# Perform the conversion based on the selected type
if st.button("Convert"):
    if conversion_type == "Celsius to Fahrenheit":
        result = celsius_to_fahrenheit(temperature)
        if temperature < 0:
            st.success(f"❄️ {temperature}°C is equal to {result:.2f}°F. It's freezing!")
        elif temperature > 30:
            st.success(f"🔥 {temperature}°C is equal to {result:.2f}°F. It's hot!")
        else:
            st.success(f"{temperature}°C is equal to {result:.2f}°F")
    else:
        result = fahrenheit_to_celsius(temperature)
        if result < 0:
            st.success(f"❄️ {temperature}°F is equal to {result:.2f}°C. It's freezing!")
        elif result > 30:
            st.success(f"🔥 {temperature}°F is equal to {result:.2f}°C. It's hot!")
        else:
            st.success(f"{temperature}°F is equal to {result:.2f}°C")

# Footer for extra information
st.write("##### Developed with 💻 and Streamlit")

