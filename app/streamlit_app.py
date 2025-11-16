import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Antibiotic Resistance Dashboard", layout="wide")
st.title("🧫 Multi-Drug Resistance Dashboard")

uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")

    if 'resistant' in df.columns:
        st.subheader("Resistance Distribution")
        fig = px.histogram(df, x='resistant', color='resistant', title='Resistance Status Distribution')
        st.plotly_chart(fig, use_container_width=True)

    if 'bacteria' in df.columns and 'antibiotic' in df.columns:
        st.subheader("Top 10 Bacteria Resistance Patterns")
        top_bacteria = df['bacteria'].value_counts().nlargest(10).index
        fig2 = px.histogram(df[df['bacteria'].isin(top_bacteria)], x='bacteria', color='resistant',
                            title='Top 10 Bacteria Resistance Patterns')
        st.plotly_chart(fig2, use_container_width=True)
else:
    st.info("Please upload a CSV file to begin analysis.")
