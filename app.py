import streamlit as st
import pandas as pd

# Title of the app
st.title("Excel Sheet Viewer")

# File upload
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx"])

if uploaded_file:
    # Load the uploaded Excel file
    excel_file = pd.ExcelFile(uploaded_file)
    
    # Display all sheet names
    st.write("**Sheet Names:**")
    sheet_names = excel_file.sheet_names
    st.write(sheet_names)

    # Loop through each sheet, clean it, and display
    for sheet_name in sheet_names:
        st.write(f"### Sheet: {sheet_name}")
        
        # Read the sheet into a DataFrame
        df = excel_file.parse(sheet_name)
        
        # Remove 'Unnamed: 0' column if it exists
        if 'Unnamed: 0' in df.columns:
            df = df.drop(columns=['Unnamed: 0'])
        
        # Display the cleaned DataFrame
        st.dataframe(df)

