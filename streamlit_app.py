import streamlit
import pandas as pd

streamlit.title('My Parents New Healthy Dinner')

#Breakfast Menu
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
#Breakfast Menu

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

#change index from 0,1,2.. to a specific column or names
my_fruit_list=my_fruit_list.set_index('Fruit')

#Put a list so they can pick fruits
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries']) #added default values ['Avocado','Strawberries']

streamlit.dataframe(my_fruit_list)
