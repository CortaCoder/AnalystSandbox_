import streamlit as st
from st_aggrid import AgGrid
import pandas as pd

st.header("Create a Chart")

DATA = [
        { "taste": "fruity", "chardonay": 93, "carmenere": 61, "syrah": 114 },
        { "taste": "bitter", "chardonay": 91, "carmenere": 37, "syrah": 72 },
        { "taste": "heavy", "chardonay": 56, "carmenere": 95, "syrah": 99 },
        { "taste": "strong", "chardonay": 64, "carmenere": 90, "syrah": 30 },
        { "taste": "sunny", "chardonay": 119, "carmenere": 94, "syrah": 103 },
    ]

chart_data=pd.DataFrame(data=DATA,columns=['chardonay', 'carmenere', 'syrah' ])


crForm=st.form(key="chartCreate")
view=crForm.text_input("Enter Dataset JSON")
submit=crForm.form_submit_button("Save")

st.header("Preview")
viz,dat=st.tabs(["ChartView","DataView"])

with viz:
    st.line_chart(chart_data)

with dat:
    AgGrid(chart_data)