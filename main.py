import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forcast for the Next Days")
place = st.text_input(label="Place: ")
days = st.slider("Forcast Days", min_value=1, max_value=5, help="Select the number of days to forcast")
option = st.selectbox("Select data to view", options=("Temperature", "Sky"))
st.subheader(f"Temperature for the next {days} days in {place}")


if place:
    data = get_data(place, days)
    dates = [i['dt_txt'] for i in data]

    if option == "Temperature":
        temperature = [i['main']['temp'] for i in data]
        temperature = [i/10 for i in temperature]

        figure = px.line(x=dates, y=temperature, labels={"x":"Date", "y":"Temperature"})
        st.plotly_chart(figure)


    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png","Rain": "images/rain.png", "Snow": "images/snow.png"}
        weather_condition = [i['weather'] for i in data]
        weather_condition = [i[0]['main'] for i in weather_condition]
        print(weather_condition)
        weather_images = [images[condition] for condition in weather_condition]
        st.image(weather_images, width=100)
        [st.write(date) for date in dates]

    # if option == "Sky":
    #     sky_type = [i['weather'][0]['description'] for i in data]
    #     weather_icon = [f"https://openweathermap.org/img/wn/{i['weather'][0]['icon']}.png" for i in data]
    #     for i, image in enumerate(weather_icon):
    #         st.image(image, width=100)
    #         st.write(sky_type[i])
    #         st.write(dates[i], ln=0)
