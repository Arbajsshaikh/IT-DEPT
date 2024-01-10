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

# Display custom header names and corresponding values
if not filtered_data.empty:
    st.text('PARTY NAME= ' + filtered_data['Party Name'].iloc[0])
    st.text('PARTY INVOICE NO= ' + filtered_data['Bill No'].iloc[0])
    st.text('PARTY INVOICE DATE= ' + filtered_data['Doc. Date'].iloc[0])
    st.text('GEN PUR NO= ' + filtered_data['Vou No'].iloc[0])
    st.text('GEN PUR DATE= ' + filtered_data['Bill Date'].iloc[0])

    # Display the remaining columns
    st.table(filtered_data.drop(['Party Name', 'Bill No', 'Doc. Date', 'Vou No', 'Bill Date'], axis=1))

    # Function to download custom filtered data as CSV
    def download_custom_filtered_data_csv(filtered_data, filename):
        # Create a dictionary for custom headers and their corresponding values
        custom_headers = {
            'PARTY NAME': filtered_data['Party Name'].iloc[0],
            'PARTY INVOICE NO': filtered_data['Bill No'].iloc[0],
            'PARTY INVOICE DATE': filtered_data['Doc. Date'].iloc[0],
            'GEN PUR NO': filtered_data['Vou No'].iloc[0],
            'GEN PUR DATE': filtered_data['Bill Date'].iloc[0],
        }
    
        # Create a DataFrame for custom headers
        custom_data = pd.DataFrame(list(custom_headers.items()), columns=['Custom Headers', 'Values'])
    
        # Add an empty row
        custom_data = custom_data.append(pd.Series(['', ''], index=custom_data.columns), ignore_index=True)
    
        # Add column names in the 7th row
        column_names = filtered_data.columns.tolist()
        custom_data = custom_data.append(pd.Series(column_names, index=custom_data.columns), ignore_index=True)
    
        # Add data values in the 8th row
        custom_data = custom_data.append(pd.Series(filtered_data.values.flatten(), index=custom_data.columns), ignore_index=True)
    
        # Save to CSV with custom formatting
        csv_data = custom_data.to_csv(index=False, header=False)
    
        b64 = base64.b64encode(csv_data.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download Filtered Data as CSV</a>'
        st.markdown(href, unsafe_allow_html=True)



# Trigger download automatically when a Vou No is selected
if selected_vou_no:
    download_custom_filtered_data_csv(filtered_data, selected_vou_no)

