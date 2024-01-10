import pandas as pd
import streamlit as st
import base64

# Sample data
df = pd.read_csv("CATEGORY_ADDED-Purchase Register 2020-21.csv")

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
        custom_data = pd.concat([custom_data, pd.DataFrame(['', '']).T], ignore_index=True)
    
        # Add column names in the 7th row
        column_names = filtered_data.columns.tolist()
        custom_data = pd.concat([custom_data, pd.DataFrame([column_names])], ignore_index=True)
    
        # Add data values in the 8th row
        custom_data = pd.concat([custom_data, pd.DataFrame(filtered_data.values, columns=column_names)], ignore_index=True)
    
        # Save to CSV with custom formatting
        csv_data = custom_data.to_csv(index=False, header=False)
    
        b64 = base64.b64encode(csv_data.encode()).decode()
        href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download Filtered Data as CSV</a>'
        st.markdown(href, unsafe_allow_html=True)



# Trigger download automatically when a Vou No is selected
if selected_vou_no:
    download_custom_filtered_data_csv(filtered_data, selected_vou_no)
