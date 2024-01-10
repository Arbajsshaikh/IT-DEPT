import pandas as pd
import streamlit as st
import base64

# Assuming your data is stored in a DataFrame named 'df'
# Replace 'your_data.csv' with the actual file or data source you have

# Example:
df = pd.DataFrame({
    'Bill No': ['WMPL/MFG/0553', 'WMPL/MFG/0555'],
    'Doc. Date': ['22-10-2020', '22-10-2020'],
    'Vou No': ['PW/10', 'PW/04'],
    'Bill Date': ['24-10-2020', '24-10-2020'],
    'Party Name': ['WALMARK MEDITECH PVT.LTD.', 'WALMARK MEDITECH PVT.LTD.'],
    'State': ['Maharashtra', 'Maharashtra'],
    'City Name': ['NAGPUR', 'NAGPUR'],
    'Product Name (Overwrite)': ['SUPREME ADULT DIAPER(XL) 10', 'SUPREME ADULT DIAPER(XL) 10'],
    'category': [None, None],
    'HSN Code': [9619, 9619],
    'Packing': [10, 10],
    'Qty': [10, 10],
    'Purchase Rate': [480.0, 240.0],
    'Purchase Amt': [96000.0, 48000.0],
    'CGST Amount': [5760.0, 2880.0],
    'SGST Amount': [5760.0, 2880.0],
    'IGST Amount': [None, None],
    'Total Amount': [107520.0, 53760.0],
    'Category': ['SURGICAL', 'SURGICAL']
})

# Create dropdown for Vou No
vou_no_options = df['Vou No'].unique()
selected_vou_no = st.selectbox('Select Vou No:', vou_no_options)

# Filter data based on selected Vou No
filtered_data = df[df['Vou No'] == selected_vou_no]

# Display the filtered data
st.table(filtered_data)

# Function to download filtered data as CSV
def download_filtered_data_csv(data, filename):
    csv_data = data.to_csv(index=False)
    b64 = base64.b64encode(csv_data.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download Filtered Data as CSV</a>'
    st.markdown(href, unsafe_allow_html=True)

# Download button
if st.button('Download Filtered Data as CSV'):
    download_filtered_data_csv(filtered_data, selected_vou_no)
