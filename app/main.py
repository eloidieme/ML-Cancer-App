import sys
import os
sys.path.append(os.getcwd())

import streamlit as st
import pickle
from model.main import get_clean_data

def add_sidebar():
    st.sidebar.header("Cell Nuclei Measurements")

    data = get_clean_data()
    slider_labels = [(col.split('_')[0].capitalize() + f" ({col.split('_')[1]})", col) for col in data.columns[1:]]

    input_dict = {}

    for label, key in slider_labels:
        input_dict[key] = st.sidebar.slider(
            label,
            min_value=float(data[key].min()),
            max_value=float(data[key].max()),
            value = float(data[key].mean())
        )

    return input_dict



def main():
    st.set_page_config(
        page_title="Brest Cancer Predictor",
        page_icon=":female-doctor:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    input_data = add_sidebar()

    with st.container():
        st.title("Breast Cancer Predictor")
        st.write("Please connect this app to your cytology lab to help diagnose breast cancer from your tissue sample. This app predicts using a machine learning model whether a breast mass is benign or malignant based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the sidebar.")

    col1, col2 = st.columns([4,1])

    with col1:
        st.write("this is column 1")
    with col2:
        st.write("this is column 2")
    

if __name__ == '__main__':
    main()