import pandas as pd
import streamlit as st
import base64

# Assuming your data is stored in a DataFrame named 'df'
# Replace 'your_data.csv' with the actual file or data source you have

# Example:
df = pd.read_csv('CATEGORY_ADDED-Purchase Register 2020-21.csv')

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

# Trigger download automatically when a Vou No is selected
if selected_vou_no:
    download_filtered_data_csv(filtered_data, selected_vou_no)
