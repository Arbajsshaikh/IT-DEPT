import pandas as pd
import streamlit as st
import base64

# Sample data
df = pd.DataFrame({
    'Bill No': ['WMPL/MFG/0553', 'WMPL/MFG/0555', 'WMPL/MFG/702', 'WMPL/MFG/795', 'WMPL/MFG/1002'],
    'Doc. Date': ['22-10-2020', '22-10-2020', '28-11-2020', '11-12-2020', '29-01-2021'],
    'Vou No': ['PW/10', 'PW/04', 'PW/296', 'PW/300', 'PW/730'],
    'Bill Date': ['24-10-2020', '24-10-2020', '30-11-2020', '12-12-2020', '30-01-2021'],
    'Party Name': ['WALMARK MEDITECH PVT.LTD.'] * 5,
    'State': ['Maharashtra'] * 5,
    'City Name': ['NAGPUR'] * 5,
    'Product Name (Overwrite)': ['SUPREME ADULT DIAPER(XL) 10'] * 5,
    'category': [None] * 5,
    'HSN Code': [9619] * 5,
    'Packing': [10] * 5,
    'Qty': [10, 10, 10, 10, 10],
    'Purchase Rate': [480.0, 240.0, 960.0, 480.0, 384.0],
    'Purchase Amt': [96000.0, 48000.0, 192000.0, 96000.0, 76800.0],
    'CGST Amount': [5760.0, 2880.0, 11520.0, 5760.0, 4608.0],
    'SGST Amount': [5760.0, 2880.0, 11520.0, 5760.0, 4608.0],
    'IGST Amount': [None] * 5,
    'Total Amount': [107520.0, 53760.0, 215040.0, 107520.0, 86016.0],
    'Category': ['SURGICAL'] * 5
})

# Create dropdown for Vou No
vou_no_options = df['Vou No'].unique()
selected_vou_no = st.selectbox('Select Vou No:', vou_no_options)

# Filter data based on selected Vou No
filtered_data = df[df['Vou No'] == selected_vou_no]

# Rearrange and rename columns
filtered_data_reordered = filtered_data[['Party Name', 'Bill No', 'Vou No', 'Bill Date', 'Doc. Date'] + [col for col in filtered_data.columns if col not in ['Party Name', 'Bill No', 'Vou No', 'Bill Date', 'Doc. Date']]]

# Display the filtered data with the specified column order and names
st.table(filtered_data_reordered)

# Function to download filtered data as CSV with specified column order and names
def download_filtered_data_csv(data, filename):
    csv_data = data.to_csv(index=False)
    b64 = base64.b64encode(csv_data.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download Filtered Data as CSV</a>'
    st.markdown(href, unsafe_allow_html=True)

# Trigger download automatically when a Vou No is selected
if selected_vou_no:
    download_filtered_data_csv(filtered_data_reordered, selected_vou_no)

