from cef_data_manager import CefDataManager
import streamlit as st


cef_data_manager = CefDataManager()
df = cef_data_manager.get_data()

csv = df.to_csv()

st.dataframe(df)
st.download_button('Press to Download', csv, 'cef.csv')
