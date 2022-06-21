import pandas as pd
import streamlit as st
from ._paths import PROCESSED_DATA


@st.cache()
def load_data():
    return pd.read_parquet(PROCESSED_DATA / "random_tracks.parquet")
