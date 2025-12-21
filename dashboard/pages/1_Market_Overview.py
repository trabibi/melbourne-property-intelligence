import streamlit as st
import pandas as pd 

from utils.load_data import load_yield_suburb

st.set_page_config(page_title="Market Overview", layout="wide")

st.title("Market Overview")
st.write("Suburb-level rental yield and price context (3 bed houses).")

df = load_yield_suburb()

st.sidebar.header("Filters")

regions = ["All"] + sorted(df["region"].dropna().unique().tolist())
selected_region = st.sidebar.selectbox("Region", regions, index=0)

min_sales = int(st.sidebar.slider("Minimum sales count (price reliability)", 0, 250, 0, 5))

df_f = df.copy()
if selected_region != "All":
    df_f = df_f[df_f["region"] == selected_region]

df_f = df_f[df_f["sales_count"] >= min_sales]

#KPI row 
c1, c2, c3, c4, c5 = st.columns(5)

n_suburbs = df_f["suburb"].nunique()
median_yield = df_f["gross_yield_pct"].median()
mean_median = df_f["gross_yield_pct"].mean()
median_price = df_f["median_price"].median()
median_rent = df_f["median_rent"].median()

c1.metric("Suburbs covered", f"{n_suburbs:,}")
c2.metric("Median gross yield", f"{median_yield:.2f}%")
c3.metric("Average gross yield", f"{"mean_yield":.2f}%")
c4.metric("Median house price", f"${median_price:,.0f}")
c5.metric("Median weekly rent", f"${median_rent:,.0f}")

st.divider()

#Charts for yield distribution + price vs yield 
left, right = st.columns(2) 

with left: 
    st.subheader("Yield distribution")
    st.bar_chart(
        df_f["gross_yield_pct"],
        height=320
    )
    st.caption("Quick view: yields cluster around the mid range; extremes exists but are less common.")

with right: 
    st.subheader("Price vs Yield (Inverse Relationship)")
    scatter_df = df_f[["median_price","gross_yield_pct","suburb"]].copy()
    st.scatter_chart(
        scatter_df,
        x="median_price",
        y="gross_yield_pct",
        height = 320
    )
    st.caption("Higher prices generally compress yields as rents do not scale proportionally.")

#region breakdown 
st.subheader("Regional pattern")

region_summary = (
    df_f.groupby("region",dropna=False).agg(
        suburbs=("suburb","unique"),
        median_yield = ("gross_yield_pct","median"),
        median_price = ("median_price", "median"),
        median_rent = ("median_rent", "median"),
    ).sort_values("median_yield",ascending=False).reset_index()
)

st.dataframe(region_summary.style.format(
    {
        "median_yield": "{:.2f}%",
        "median_price": "${:,.0f}",
        "median_rent": "${:,.0f}",
    }
),use_container_width=True, hide_index=True,)

#top and bottom tables 
st.subheader("Best/Worst yield suburbs (within filter)")

t1,t2 = st.columns(2)

cols = ["region", "suburb","median_price","median_rent","sales_count","gross_yield_pct"]

with t1:
    st.markdown("**Top 10 Yields**")
    top10 = df_f.sort_values("gross_yield_pct",ascending=False).head(10)[cols].copy()
    st.dataframe(
        top10.style.format(
            {
                "median_yield": "{:.2f}%",
                "median_price": "${:,.0f}",
                "median_rent": "${:,.0f}",
            }
        ),
        use_container_width=True, 
        hide_index=True,
    )

with t2:
    st.markdown("**Top 10 Yields**")
    top10 = df_f.sort_values("gross_yield_pct",ascending=True).head(10)[cols].copy()
    st.dataframe(
        top10.style.format(
            {
                "median_yield": "{:.2f}%",
                "median_price": "${:,.0f}",
                "median_rent": "${:,.0f}",
            }
        ),
        use_container_width=True, 
        hide_index=True,
    )

st.divider()

st.info("This page uses gross yield (rent / price) and does not include expenses, vacancy duration, or tax effects.")


