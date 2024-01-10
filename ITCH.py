import pandas as pd
import streamlit as st
import base64

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

# Define the columns to display
selected_columns = ['Product Name (Overwrite)', 'Category', 'HSN Code', 'Packing', 'Qty', 'Purchase Rate', 'Purchase Amt', 'CGST Amount', 'SGST Amount', 'IGST Amount', 'Total Amount']

# Function to display products based on selected Bill Date and Party Name
def display_products(bill_date, party_name):
    selected_data = df[(df['Bill Date'] == bill_date) & (df['Party Name'] == party_name)]
    products_data = selected_data[selected_columns]
    st.table(products_data)

# Function to download filtered data
def download_filtered_data(data, filename):
    csv_data = data.to_csv(index=False)
    b64 = base64.b64encode(csv_data.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download Filtered Data</a>'
    st.markdown(href, unsafe_allow_html=True)

# Display the products when a button is clicked
if st.button('Show Products'):
    display_products(bill_date, party_name)
    # Download button
    download_filtered_data(selected_data, f'{party_name}_{bill_date}')
