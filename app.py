import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Zomato Data Analysis", layout="wide")

st.title("🍽️ Zomato Dataset Analysis")

# Upload file
uploaded_file = st.file_uploader("Upload Zomato Dataset (Excel/CSV)", type=["csv", "xlsx"])

if uploaded_file is not None:
    
    # Read file
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    st.subheader("📊 Dataset Preview")
    st.dataframe(data.head())

    # Shape
    st.subheader("📏 Dataset Shape")
    st.write("Rows:", data.shape[0], "Columns:", data.shape[1])

    # Missing values
    st.subheader("❗ Missing Values")
    st.write(data.isnull().sum())

    # Column selection
    st.subheader("🔍 Select Column for Analysis")
    column = st.selectbox("Choose column", data.columns)

    # Value counts
    st.subheader("📊 Value Counts")
    st.write(data[column].value_counts().head(10))

    # Plot
    st.subheader("📈 Visualization")

    if data[column].dtype == "object":
        fig, ax = plt.subplots()
        data[column].value_counts().head(10).plot(kind='bar', ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    else:
        fig, ax = plt.subplots()
        sns.histplot(data[column], kde=True, ax=ax)
        st.pyplot(fig)

    # Correlation heatmap (only numeric)
    st.subheader("🔥 Correlation Heatmap")

    numeric_data = data.select_dtypes(include=['number'])

    if not numeric_data.empty:
        fig, ax = plt.subplots()
        sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
    else:
        st.warning("No numeric columns available")

else:
    st.info("Please upload your dataset to start analysis")
