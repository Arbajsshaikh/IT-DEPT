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
        # Reset the index to ensure both column headers and values start from the first column
        filtered_data = filtered_data.reset_index(drop=True)
    
        # Replace NaN values with empty strings
        filtered_data = filtered_data.fillna('')
    
        # Create a dictionary for custom headers and their corresponding values
        custom_headers = {
            'PARTY NAME': filtered_data['Party Name'].iloc[0],
            'PARTY INVOICE NO': filtered_data['Bill No'].iloc[0],
            'PARTY INVOICE DATE': filtered_data['Doc. Date'].iloc[0],
            'GEN PUR NO': filtered_data['Vou No'].iloc[0],
            'GEN PUR DATE': filtered_data['Bill Date'].iloc[0],
        }
    
        # Create a DataFrame for custom headers
        custom_headers_df = pd.DataFrame(list(custom_headers.items()), columns=['Custom Headers', 'Values'])
    
        # Create a DataFrame for column names and values
        column_names = filtered_data.columns.tolist()
        values_data = filtered_data[column_names].apply(lambda x: [str(val) for val in x])
        data_df = pd.DataFrame(values_data, columns=column_names)
    
        # Remove leading/trailing spaces from the filename
        filename = filename.strip()
    
        # Save to CSV with custom formatting
        with open(f"{filename}.csv", 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Write custom headers
            for i in range(len(custom_headers_df)):
                writer.writerow([custom_headers_df.iloc[i]['Custom Headers'], custom_headers_df.iloc[i]['Values']])
            
            # Add an empty row
            writer.writerow(['', ''])
            
            # Write column names
            writer.writerow(column_names)
            
            # Write values
            for i in range(len(data_df)):
                writer.writerow(data_df.iloc[i])
    
        st.markdown(f'<a href="{filename}.csv" download="{filename}.csv">Download Filtered Data as CSV</a>', unsafe_allow_html=True)






# Trigger download automatically when a Vou No is selected
if selected_vou_no:
    download_custom_filtered_data_csv(filtered_data, selected_vou_no)
