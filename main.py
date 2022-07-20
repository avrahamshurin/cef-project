from io import BytesIO
from cef_data_manager import CefDataManager
from datetime import datetime
import streamlit as st
import pandas as pd

def get_file_name(extension):
    return "{}{}.{}".format('screener_summary', datetime.now().strftime('%y%m%d'), extension)

cef_data_manager = CefDataManager()
df = cef_data_manager.get_data()

in_memory_fp = BytesIO()
with (pd.ExcelWriter(in_memory_fp, engine='xlsxwriter', engine_kwargs={'options': {'strings_to_numbers': True}})) as writer:
    df.to_excel(writer, index=False)

excel = in_memory_fp.getvalue()
csv = df.to_csv(index=False)

st.dataframe(df)
st.download_button('Download as CSV', csv, get_file_name('csv'))
st.download_button('Download as Excel', excel, get_file_name('xlsx'))