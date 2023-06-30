
import streamlit as st
from PIL import Image

#look for more information here https://docs.streamlit.io/library/cheatsheet

#adding title
st.title("An Investigation into the Different Aspects of Weather and how they Correlate")

#adding description to your website


# for header use st.header()
st.header("Team Members:") #Add name and what grade you will be going into next school year (2023-24)
st.write("Kate King - Grade 10")
st.write("Belinda Moore - Grade 10")
st.write("Max Swartz - Grade 11")
st.write("Jack Lynch - Grade 11")
st.write("Aarav Vidyarthy - Grade 9")
#Context
st.header("Context to Dataset: ")
st.write("Our data was retrieved from kaggle.com. There are 5,000 rows and 12 columns. Each row represents one hour and the weather events that occurred. The columns state the date and time, a written summary of the weather, the type of precipitation, the temperature, the apparent temperature, the humidity, the wind speed, the wind bearing, the visibility, the cloud cover, the pressure, and a written summary of the weather for the whole day.")
#Hypotheses
st.header("Hypotheses: ")
st.write("1.  Wind bearing does not make an impact on the speed of winds because air pressure, which is not directional, is the main contributor to the speed of wind.")
st.write("2.  The temperature is not a factor in adverse weather occurrences therefore is inconsequential to them.  ") 
st.write("3. Rain will be the most common type of precipitation, because in the past it has rained more each year than it has snowed.")
st.header("Why Is This Important?")
st.write("The weather data set is important because its data can impact the way we view how weather works.")

#Max
st.subheader("Part 1: Are Wind Speed and Wind Bearing Correlated?")
image = Image.open('MaxWeatherGraph.png')
st.image(image, caption='The Scatterplot above exhbits wind speeds and their respective direction for each hour of 9 separate day long trials. Each trial was performed 10 days apart.')

st.write("From the available data, it can be observed that wind bearing Northwest (approximately 315 degrees) generally exhibits the highest speeds. This however, is a weak correlation, as there are many cases where the wind bearing South (approximately 180 degrees) has a stronger speed than the wind bearing Northwest. When considering specific daily wind graphs (not depicted above) almost every day's strongest wind speeds were bearing Northwest. This is enough information to conclude that each day, the winds bearing Northwest are more likely to be the fastest compared to winds from other directions. This, however, is not sufficient enough to prove that wind speed is determined by wind bearing.")

#Kate
st.subheader("Part 2: Average Temperatures")
image = Image.open('download.png')
st.image(image, caption='The Histogram above visualizes the average temperature that the samples were taken at for thousands of hours during the experimental period.')
st.write("The information supplied allows for the conclusion that at temperatures ranging from 0 to 20 degrees celcius, most incliment weather events occur; which is contradictory to the original hypothesis. The graph demonstrates this as the majority of samples (around 60,00) were collected at this range of temperatures. Hence, from the graph it can be concluded that weather events consisting of heavy rain are most likely to occur at temperatures ranging from 0 to 20 degrees celcius. This data, however, does not fully prove that incliment rain events can only occur at these temperatures and further research must be done.")

#Belinda
st.subheader("Part 3: Comparison Between Different Types of Precipitation")
precipImage = Image.open('PrecipPieChart.png')
st.image(precipImage, caption='Precipitation Types')
st.write("This pie chart shows that precipitation in rain form is much more common than precipitation in snow form, which is to be expected due to climate and weather events that have been experienced in the past. This proves our hypothesis. ")
#Jack
st.subheader("Part 4: Correlation Between Visibility and Humidity")
image = Image.open('jackweathergraph.png')
st.image(image, caption='Scatter Plot')
st.write("Looking at the scatter plot the visibility goes down the more humid it is. Foggy is more likely to cause less visibility than mostly cloudly or clear skies, although there are some foggy days where you can still see a decent distance and vice versa for the cloudy days.")
st.write("In short the more humid it is the more likely it will be foggy our cloudy therefore limiting the visibility")
#Aarav
st.subheader("Part 5: Correlation Between Tempeture and Humidity")
image2 = Image.open("fig1.png")
st.image(image2, caption = "Tempeture vs humidity")
st.write("This graph shows how tempeture and humidity stay similar and sometimes differ. You can see vrey small adjustments in humidity and very big adjustments in tempeture. More humidity means rain and snow making it colder.")
