import streamlit as st
from PIL import Image
import requests
st.markdown(
        """
        <style>
        .reportview-container {
            background: url("https://images.unsplash.com/photo-1576502200916-3808e07386a5?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=1046&q=80") no-repeat center fixed;
            background-size: cover;
        }
    .sidebar .sidebar-content {
            background: url("url_goes_here")
        }
        </style>
        """,
        unsafe_allow_html=True
    )
#---------------------------------#
# New feature (make sure to upgrade your streamlit library)
# pip install --upgrade streamlit

#---------------------------------#
# Title

rates = {}
class Currency_convertor:
    rates = {}
    def __init__(self, url):
        data = requests.get(url).json()

        # Extracting only the rates from the json data
        self.rates = data["rates"]

    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        st.header('Currency conversion')

            # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        st.write('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))

#---------------------------------#
# Sidebar + Main panel

if __name__ == "__main__":
    image = Image.open('logo.png')

    st.image(image, width=390)

    st.title('Currency Converter App')
    st.markdown("""
    This app interconverts the value of foreign currencies!
    """)
    st.sidebar.header('Input Options')

    ## Sidebar - Currency price unit
    currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS',
                     'INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD',
                     'THB', 'TRY', 'USD', 'ZAR']
    base_price_unit = st.sidebar.selectbox('Select base currency for conversion', currency_list)
    symbols_price_unit = st.sidebar.selectbox('Select target currency to convert to', currency_list)

    # YOUR_ACCESS_KEY = 'GET YOUR ACCESS KEY FROM fixer.io'
    a="d00c55242d68b504de1b4ec37c6812b6"
    url = str.__add__('http://data.fixer.io/api/latest?access_key=',a)
    c = Currency_convertor(url)
    from_country = base_price_unit
    to_country = symbols_price_unit
    amount = int(st.number_input("enter amount"))

    c.convert(from_country, to_country, amount)

# Retrieving currency data from ratesapi.io
# https://api.ratesapi.io/api/latest?base=AUD&symbols=AUD


#st.write( df.transpose() )


#---------------------------------#
# Abou
