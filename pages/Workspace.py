import streamlit as st
from streamlit_elements import elements,mui
st.set_page_config(
    page_title="Workspaces",
    page_icon='icon.png',
)
st.title("Workspace")
st.write("Workspaces connected to tables for visualization and transformation")
st.markdown("<br>",True)

with elements("Workspace_element"):
    with mui.Card(sx={'margin-bottom':'10px','border-radius':'5px'}):
        mui.CardHeader(title="WSP1")
        with mui.CardContent():
            mui.Typography("Description")
        with mui.CardActions():
            mui.Button("Open",color="primary",href="/Dashboard",target="_blank",variant="outlined")
            mui.Button("Edit",color="success")