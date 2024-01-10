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
    st.text('PARTY NAME : ' + filtered_data['Party Name'].iloc[0])
    st.text('PARTY INVOICE NO : ' + filtered_data['Bill No'].iloc[0])
    st.text('PARTY INVOICE DATE : ' + filtered_data['Doc. Date'].iloc[0])
    st.text('GEN PUR NO : ' + filtered_data['Vou No'].iloc[0])
    st.text('GEN PUR DATE : ' + filtered_data['Bill Date'].iloc[0])

    # Display the remaining columns
    st.table(filtered_data.drop(['Party Name', 'Bill No', 'Doc. Date', 'Vou No', 'Bill Date'], axis=1))

    # Function to download custom filtered data as Excel
    def download_custom_filtered_data_excel(filtered_data, filename):
        # Create a Pandas Excel writer using XlsxWriter as the engine
        excel_writer = pd.ExcelWriter(f"{filename}.xlsx", engine='xlsxwriter')

        # Reset the index to ensure both column headers and values start from the first column
        filtered_data = filtered_data.reset_index(drop=True)

        # Write the DataFrame data to XlsxWriter
        filtered_data.to_excel(excel_writer, sheet_name='Sheet1', index=False, startrow=7, header=False)

        # Close the Pandas Excel writer and output the Excel file
        excel_writer.save()

        # Create download link
        href = f'<a href="{filename}.xlsx" download="{filename}.xlsx">Download Filtered Data as Excel</a>'
        st.markdown(href, unsafe_allow_html=True)

    # Trigger download automatically when a Vou No is selected
    if selected_vou_no:
        download_custom_filtered_data_excel(filtered_data, selected_vou_no)
