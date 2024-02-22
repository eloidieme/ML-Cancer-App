import sys
import os
sys.path.append(os.getcwd())

import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from model.main import get_clean_data
import warnings
warnings.filterwarnings('ignore')

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

    min_vals = {key : float(data[key].min()) for _, key in slider_labels}
    max_vals = {key : float(data[key].max()) for _, key in slider_labels}

    return input_dict, min_vals, max_vals

def get_radar_chart(input_data, min_vals, max_vals):
    categories = sorted(list(set([key.split('_')[0].capitalize() for key in input_data.keys()])))

    def _get_values_array(name : str):
        return np.array([input_data[key] for key in sorted(input_data.keys()) if name in key]),\
               np.array([min_vals[key] for key in sorted(input_data.keys()) if name in key]),\
               np.array([max_vals[key] for key in sorted(input_data.keys()) if name in key])

    def _get_normalized_values_array(name : str):
        arr, minv, maxv = _get_values_array(name)
        norm_arr = (arr - minv) / (maxv - minv)
        return norm_arr
    
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=_get_normalized_values_array('mean'),
        theta=categories,
        fill='toself',
        name='Mean'
    ))
    fig.add_trace(go.Scatterpolar(
        r=_get_normalized_values_array('se'),
        theta=categories,
        fill='toself',
        name='Standard Error'
    ))
    fig.add_trace(go.Scatterpolar(
        r=_get_normalized_values_array('worst'),
        theta=categories,
        fill='toself',
        name='Worst'
    ))

    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0, 1]
        )),
    showlegend=True
    )

    return fig

def add_predictions(input_data):
    model = pickle.load(open('model/model.pkl', 'rb'))
    scaler = pickle.load(open("model/scaler.pkl", "rb"))

    input_array = np.array(list(input_data.values())).reshape(1, -1)
    input_array_scaled = scaler.transform(input_array)

    prediction = model.predict(input_array_scaled)

    st.subheader("Cell cluster prediction")
    st.write("The cell cluster is:")

    if prediction[0]:
        st.write("Malignant")
    else:
        st.write("Benign")

    st.write("Probability of being benign: ", model.predict_proba(input_array_scaled)[0][0])
    st.write("Probability of being malignant: ", model.predict_proba(input_array_scaled)[0][1])
    st.write("This app can assist medical professionals in making a diagnosis, but should not be used as a substitute for a professional diagnosis.")
    st.write("This app was made for learning purposes only, not for real use.")


def main():
    st.set_page_config(
        page_title="Brest Cancer Predictor",
        page_icon=":female-doctor:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    input_data, min_vals, max_vals = add_sidebar()

    with st.container():
        st.title("Breast Cancer Predictor")
        st.write("Please connect this app to your cytology lab to help diagnose breast cancer from your tissue sample. This app predicts using a machine learning model whether a breast mass is benign or malignant based on the measurements it receives from your cytosis lab. You can also update the measurements by hand using the sliders in the sidebar.")

    col1, col2 = st.columns([4,1])

    with col1:
        radar_chart = get_radar_chart(input_data, min_vals, max_vals)
        st.plotly_chart(radar_chart)
    with col2:
        add_predictions(input_data)
    

if __name__ == '__main__':
    main()