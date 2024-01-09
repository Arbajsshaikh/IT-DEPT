import pandas as pd
import streamlit as st

# Assuming your data is stored in a DataFrame named 'df'
# Replace 'your_data.csv' with the actual file or data source you have

# Example:
df = pd.read_csv("CATEGORY_ADDED-Purchase Register 2020-21.csv")

# Create dropdowns for Bill Date and Party Name
bill_date_options = df['Bill Date'].unique()
party_name_options = df['Party Name'].unique()

# Add a selectbox for Bill Date and Party Name
bill_date = st.selectbox('Select Bill Date:', bill_date_options)
party_name = st.selectbox('Select Party Name:', party_name_options)

# Function to display products based on selected Bill Date and Party Name
def display_products(bill_date, party_name):
    selected_data = df[(df['Bill Date'] == bill_date) & (df['Party Name'] == party_name)]
    products_data = selected_data[selected_columns]
    st.table(products_data)

# Display the products when a button is clicked
if st.button('Show Products'):
    display_products(bill_date, party_name)
