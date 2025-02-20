import streamlit as st
import plotly.express as px

st.title("Weather Forcast for the Next Days")
place = st.text_input(label="Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5, help="Select the number of days to forcast")
option = st.selectbox("Select data to view", options=("Temperature", "Sky"))
st.subheader(f"Temperature for the next {days} days in {place}")


def get_data(days):
    date = ["2025-01-01", "2025-01-02", "2025-01-02", "2025-01-03"]
    temperature = [20, 25, 26, 27]
    temperature = [days * i for i in temperature]
    return date, temperature

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x":"Date", "y":"Temperature"})
st.plotly_chart(figure)
