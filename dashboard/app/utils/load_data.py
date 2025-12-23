from __future__ import annotations
from pathlib import Path
import pandas as pd
import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = PROJECT_ROOT / "data" / "processed"

if not DATA_DIR.exists():
    raise FileNotFoundError(f"DATA_DIR not found: {DATA_DIR}")

@st.cache_data(show_spinner=False)
def load_yield_suburb() -> pd.DataFrame:
    path = DATA_DIR / "suburb_house_rental_yield.csv"
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return pd.read_csv(path)

@st.cache_data(show_spinner=False)
def load_rate_spreads() -> pd.DataFrame:
    path = DATA_DIR / "suburb_yield_rate_spreads.csv"
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return pd.read_csv(path)

@st.cache_data(show_spinner=False)
def load_yield_demand_lga() -> pd.DataFrame:
    path = DATA_DIR / "yield_demand_lga_2025.csv"
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return pd.read_csv(path)

@st.cache_data(show_spinner=False)
def load_demand_band_summary() -> pd.DataFrame:
    path = DATA_DIR / "yield_demand_band_summary.csv"
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    return pd.read_csv(path)