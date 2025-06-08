import streamlit as st

st.title("Hello Faza!")
st.header('Welcome to Faza Web App!')
st.latex('a+b^2 = (a+b)(a-b)')

#button
if st.button('Click Me!'):
    st.write('Button Clicked!')
# checkbox
if st.checkbox('Check Me!'):
    st.write('Checkbox Checked!')
# radio button
option = st.radio('Choose an option:', ['Option 1', 'Option 2', 'Option 3'])
if option == 'Option 1':
    st.write('You selected Option 1')
elif option == 'Option 2':
    st.write('You selected Option 2')
elif option == 'Option 3':
    st.write('You selected Option 3')


name = st.text_input('Enter your name:')
if name:
    st.write(f'Hello, {name}!')

import pandas as pd

# Load data
data = pd.read_csv('iris_data.csv')

import plotly.express as px
fig = px.scatter(data, x='SepalLengthCm', y='SepalWidthCm', color='Species',)
# Display the plot
st.plotly_chart(fig, usecontainer_width=True)
