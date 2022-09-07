import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as ps
import seaborn as sns
sns.set()
from PIL import Image
pic = Image.open('Sales.jpg')

st.title('Sales Dataset Problem',)
st.header('A data Science Problem from Kaggle')
st.image(pic)



def read_data(data):
    data = pd.read_csv(data).head()
    st.dataframe(data)

st.header('Sales_data')
data= read_data('all_sales_data_1')

st.write('You can download the data by clicking the button below:')

st.download_button(
     label="Download data as CSV",
     data='all_sales_data_1',
     file_name='Sales.csv',
     mime='text/csv',
 )

def download_data(df):
    st.download_button(df)


option = st.selectbox(
    'Pick a question',
    ('What was the best month for sales? How much was earned that month ?',
    'What City had the highest number of sales ?',
    'What product sold the most? Why do you think it sold the most ?')
)

st.write('You have selected: ', option)

def question1(data):
    data = pd.read_csv(data)
    data_question_1= data.groupby(['month'])['Sales'].sum().reset_index(name ='Sales')
    return data_question_1


def question2(data):
    data = pd.read_csv(data)
    data_question_2= data.groupby(['city'])['Sales'].sum().reset_index(name ='Sales')
    return data_question_2

def question4(data):
    data = pd.read_csv(data)
    data_question_4 = data.groupby(['Product'])['Quantity Ordered'].sum().reset_index(name ='Quantity Ordered')
    return data_question_4



data_question_1 = question1('all_sales_data_1')
data_question_2 = question2('all_sales_data_1')
data_question_4 = question4('all_sales_data_1')

def chosen_option_1():
        x = data_question_1['month']
        y= data_question_1['Sales']
        fig, ax = plt.subplots()
        ax.plot(x,y)
        plt.xlabel('Month')
        plt.ylabel('Sales')
        plt.title('Sales by Months')
        st.pyplot(fig)


def chosen_option_2():
        x = data_question_2['city']
        y= data_question_2['Sales']
        fig, ax = plt.subplots()
        ax.plot(x,y)
        plt.xlabel('Cities')
        plt.xticks(x, rotation = 45)
        plt.ylabel('Sales')
        plt.title('Sales by city')
        st.pyplot(fig)

    

def chosen_option_4():
    x = data_question_4['Product']
    y = data_question_4['Quantity Ordered']
    fig, ax = plt.subplots()
    ax.plot(x,y)
    plt.xlabel('Product')
    plt.xticks(x, rotation = 90)
    plt.ylabel('Quantity Ordered')
    st.pyplot(fig)



if option == 'What was the best month for sales? How much was earned that month ?':
    chosen_option_1()
    with st.expander('See explanation'):
        st.write("""
        As you See the best Month for sales is December
        """)

if option == 'What City had the highest number of sales ?':
    chosen_option_2()
    with st.expander('See explanation'):
        st.write("""
        San Francisco is the city that has the highest number of sales
        """)


if option == 'What product sold the most? Why do you think it sold the most ?':
    chosen_option_4()
    with st.expander('See explanation'):
        st.write("""
        AAA Batteries (4-pack) is the product that is sold the most
        """)




