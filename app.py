import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="AI-Powered Business Intelligence",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI-Powered Business Intelligence")
st.write("Business analytics dashboard with AI-generated insights.")

# Load data
df = pd.read_csv("data/business_data.csv")

# KPI calculations
total_revenue = df["Revenue"].sum()
total_units = df["Units Sold"].sum()
average_rating = df["Customer Rating"].mean()

# KPI cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Units Sold", f"{total_units:,}")
col3.metric("Avg. Rating", f"{average_rating:.2f}/5")

st.divider()

# Revenue by product
product_data = (
    df.groupby("Product", as_index=False)["Revenue"]
    .sum()
    .sort_values("Revenue", ascending=False)
)

fig_product = px.bar(
    product_data,
    x="Product",
    y="Revenue",
    title="Revenue by Product"
)

st.plotly_chart(fig_product, use_container_width=True)

# Revenue by region
region_data = (
    df.groupby("Region", as_index=False)["Revenue"]
    .sum()
    .sort_values("Revenue", ascending=False)
)

fig_region = px.bar(
    region_data,
    x="Region",
    y="Revenue",
    title="Revenue by Region"
)

st.plotly_chart(fig_region, use_container_width=True)

# AI insights
st.subheader("🤖 AI Business Insights")

best_product = product_data.iloc[0]["Product"]
best_region = region_data.iloc[0]["Region"]

st.info(
    f"AI Insight: **{best_product}** is the highest-revenue product, "
    f"while **{best_region}** is the strongest-performing region."
)

st.success(
    f"Recommendation: Focus marketing and inventory planning on "
    f"**{best_product}** and explore additional opportunities in **{best_region}**."
)

# Data preview
st.subheader("📋 Business Data")
st.dataframe(df, use_container_width=True)
