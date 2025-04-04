# Imports
import streamlit as st

# Set up our app
st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("Unit Converter")
st.write("")


conversion_rates = {
    "length": {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "inches": 39.3701,
        "feet": 3.28084,
        "yards": 1.09361,
        "miles": 0.000621371
    },
    "weight": {
        "grams": 1,
        "kilograms": 0.001,
        "pounds": 0.00220462,
        "ounces": 0.035274
    },
    "temperature": {
    "celsius": {
        "fahrenheit": ("(x * 9/5) + 32"),
        "kelvin": "x + 273.15"
    },
    "fahrenheit": {
        "celsius": "(x - 32) * 5/9",
        "kelvin": "((x - 32) * 5/9) + 273.15"
    },
    "kelvin": {
        "celsius": "x - 273.15",
        "fahrenheit": "((x - 273.15) * 9/5) + 32"
    }
},
    "volume": {
        "liters": 1,
        "milliliters": 1000,
        "gallons": 0.264172,
        "cups": 4.22675
    },
    "area": {
        "square_meters": 1,
        "square_kilometers": 1_000_000,
        "hectares": 10_000,
        "acres": 4046.86
    },

}


Unit = st.selectbox("Select the unit to convert", conversion_rates,
placeholder="Select Unit to Convert...",
index=0,
)




col1, col2 = st.columns(2, border=True)

with col1:
    fromUnit = st.selectbox("Select the unit to convert the value from",
    options=list(conversion_rates[Unit].keys()),
    placeholder="From unit...",
    index=None,

)
    toUnit = st.selectbox("Select the unit to convert the value to", conversion_rates[Unit].keys(),
    placeholder="To unit...",
    index=None,
)
    input_value = st.number_input("Enter the value to convert", min_value=0.0, step=1.0)

with col2:
    if st.button("Convert"):
        # Check if input values are valid
        if fromUnit and toUnit and input_value is not None:
            # Handle temperature separately
            if Unit == "temperature":
                expr = conversion_rates["temperature"][fromUnit][toUnit]
                x = input_value
                converted_value = eval(expr)
            else:
                # Regular conversion for length, weight, etc.
                converted_value = input_value * (conversion_rates[Unit][toUnit] / conversion_rates[Unit][fromUnit])
        
            if converted_value is not None:
                st.write(f"Converted value: {converted_value:.2f} {toUnit}")
        else:
            st.write("Please select valid units and enter a value.")







st.write("You selected:", fromUnit, "to", toUnit)
