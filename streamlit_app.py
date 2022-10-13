import streamlit as st


import home, article, contact, visualize

st.title('Heart related deaths in Football')

PAGELIST = {
    "Home": home,
    "Article": article,
    "Contact Me": contact,
    "Visualizations":visualize
}


selection_default = st.sidebar.radio("Please select an option", list(PAGELIST.keys()))
page = PAGELIST[selection_default]
page.app()