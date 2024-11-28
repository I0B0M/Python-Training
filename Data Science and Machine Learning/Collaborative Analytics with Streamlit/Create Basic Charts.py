import streamlit as st
import pandas as pd
import numpy  as np
import streamlit as st
import matplotlib.pyplot as plt

col_names = ['column1','column2','column3']

data  = pd.DataFrame(np.random.randint(30, size = (30,3)),columns =col_names)

'line graph:'
st.write(data)
st.line_chart(data)


'bar graph:'
st.write(data)
st.bar_chart(data)

animals = ['cat','cow','dog']
population = [30,150,180]

'pie chart:'
fig, ax = plt.subplots()
ax.pie(population,labels = animals)

st.pyplot(fig)
