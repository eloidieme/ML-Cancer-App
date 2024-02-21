import streamlit as st
import pandas as pd
import pickle

def main():
    st.set_page_config(
        page_title="Brest Cancer Predictor",
        page_icon=":female-doctor:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.write("Hello world")

if __name__ == '__main__':
    main()