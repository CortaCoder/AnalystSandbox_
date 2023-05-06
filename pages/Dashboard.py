import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_elements import elements, dashboard, mui, nivo
from st_aggrid import AgGrid
import pandas as pd


# data
DATA = [{"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 180.4605}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 4.7331}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 6.208799999999999}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 33.7027}, {"Walmart": 20.0, "BestBuy": 3.51, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 41.15, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 0.54, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 4.95, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 4.14, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 11.89, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.187435, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 189.70999999996496, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 142.7399999999692, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 1.114003122552, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 8.89, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 13.7672568756, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 2.16, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 32.05, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 10.59, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 36.85938, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 2.49, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 2.6400000000283, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 386.1142}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 4.2377}, {"Walmart": 19.3761393064, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 110.77, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 7.929999999992369, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 11.23}, {"Walmart": 20.0, "BestBuy": 108.17999999999586, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 5.3363}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 70.7124}, {"Walmart": 20.0, "BestBuy": 2.24, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 37.140000000127614, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 27.329699999999995}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 11.1622}, {"Walmart": 20.0, "BestBuy": 22.909999999879886, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 26.3099}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 22.318035, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 30.776517, "Target": 20.0}, {"Walmart": 21.23404638075, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 4.40257896, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 21.295347, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 72.7776}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 19.2066}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 1.0196}, {"Walmart": 20.0, "BestBuy": 24.44, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 71.87, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 104.14, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 153.67000000001212, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 9.83000000002916, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 172.01000000002875, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 192.1, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 4.84, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 4.74, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 116.22000000008028, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 527.3437}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 29.16000000007404, "Costco": 20.0, "Target": 20.0}, {"Walmart": 13.90228, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 36.5474}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 37.9178}, {"Walmart": 20.0, "BestBuy": 13.48, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 44.16, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 0.99, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 40.79, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 389.01, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 27.59, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 40.46, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 102.1289}, {"Walmart": 9.79, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 5.1809}, {"Walmart": 20.0, "BestBuy": 13.7, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 12.02, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 4.99, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 24.81, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 11.31, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 8.6417}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 27.47, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 5.2602}, {"Walmart": 22.0903, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 86.1873}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 4.1333}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 5.3839}, {"Walmart": 6.54, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 7.76, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 41.8116690296, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 7.469999999999998, "Costco": 20.0, "Target": 20.0}, {"Walmart": 5.3, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 10.65, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 98.1116}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 9.013}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 130.0597}, {"Walmart": 0.98, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 2.89, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 141.46118699999997, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 95.67, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 210.2899999999694, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 29.42, "Target": 20.0}, {"Walmart": 12.42, "BestBuy": 20.0, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 532.22, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}, {"Walmart": 20.0, "BestBuy": 26.31, "Chuckys": 20.0, "Costco": 20.0, "Target": 20.0}]

BDATA = [{"COUNTRY_NAME": "Spain", "STORE": "Costco", "UNITS": 5, "AMOUNT": 22.318035}, {"COUNTRY_NAME": "Colombia", "STORE": "Target", "UNITS": 2, "AMOUNT": 1.3672}, {"COUNTRY_NAME": "Hungary", "STORE": "BestBuy", "UNITS": 2, "AMOUNT": 9.879999999999999}, {"COUNTRY_NAME": "Finland", "STORE": "Walmart", "UNITS": 1, "AMOUNT": 14.370897}, {"COUNTRY_NAME": "Finland", "STORE": "BestBuy", "UNITS": 4, "AMOUNT": 22.06999999998078}, {"COUNTRY_NAME": "Denmark", "STORE": "Chuckys", "UNITS": 1, "AMOUNT": 7.91}, {"COUNTRY_NAME": "United Arab Emirates", "STORE": "BestBuy", "UNITS": 24, "AMOUNT": 61.86}, {"COUNTRY_NAME": "Costa Rica", "STORE": "BestBuy", "UNITS": 1, "AMOUNT": 4.99}, {"COUNTRY_NAME": "Spain", "STORE": "Costco", "UNITS": 4, "AMOUNT": 7.414488}, {"COUNTRY_NAME": "Italy", "STORE": "Target", "UNITS": 12, "AMOUNT": 53.0026}, {"COUNTRY_NAME": "Netherlands", "STORE": "BestBuy", "UNITS": 34, "AMOUNT": 246.08999999993264}, {"COUNTRY_NAME": "Chile", "STORE": "Target", "UNITS": 3, "AMOUNT": 2.6116}, {"COUNTRY_NAME": "Denmark", "STORE": "Walmart", "UNITS": 1, "AMOUNT": 2.5765079724}, {"COUNTRY_NAME": "Greece", "STORE": "Target", "UNITS": 6, "AMOUNT": 39.1512}, {"COUNTRY_NAME": "United Kingdom", "STORE": "BestBuy", "UNITS": 156, "AMOUNT": 738.8600000002039}, {"COUNTRY_NAME": "Australia", "STORE": "Chuckys", "UNITS": 2, "AMOUNT": 8.030000000059179}, {"COUNTRY_NAME": "Qatar", "STORE": "BestBuy", "UNITS": 3, "AMOUNT": 7.97}, {"COUNTRY_NAME": "Mexico", "STORE": "Target", "UNITS": 14, "AMOUNT": 85.4609}, {"COUNTRY_NAME": "Bahrain", "STORE": "BestBuy", "UNITS": 2, "AMOUNT": 5.98}, {"COUNTRY_NAME": "Argentina", "STORE": "Walmart", "UNITS": 2, "AMOUNT": 8.29916379162}, {"COUNTRY_NAME": "Spain", "STORE": "BestBuy", "UNITS": 26, "AMOUNT": 104.91999999998917}, {"COUNTRY_NAME": "Switzerland", "STORE": "Chuckys", "UNITS": 4, "AMOUNT": 37.62}, {"COUNTRY_NAME": "United States", "STORE": "Target", "UNITS": 84, "AMOUNT": 437.66}, {"COUNTRY_NAME": "Chile", "STORE": "Chuckys", "UNITS": 2, "AMOUNT": 4.14}, {"COUNTRY_NAME": "Bulgaria", "STORE": "BestBuy", "UNITS": 8, "AMOUNT": 33.18}, {"COUNTRY_NAME": "Switzerland", "STORE": "Chuckys", "UNITS": 4, "AMOUNT": 12.4}, {"COUNTRY_NAME": "Netherlands", "STORE": "Target", "UNITS": 12, "AMOUNT": 30.3912}, {"COUNTRY_NAME": "South Africa", "STORE": "BestBuy", "UNITS": 1, "AMOUNT": 4.29}, {"COUNTRY_NAME": "South Africa", "STORE": "Target", "UNITS": 5, "AMOUNT": 98.90070000000001}, {"COUNTRY_NAME": "Turkey", "STORE": "Walmart", "UNITS": 14, "AMOUNT": 33.552084468412}, {"COUNTRY_NAME": "Brazil", "STORE": "BestBuy", "UNITS": 19, "AMOUNT": 49.95}, {"COUNTRY_NAME": "United States", "STORE": "BestBuy", "UNITS": 82, "AMOUNT": 372.96}, {"COUNTRY_NAME": "Mexico", "STORE": "Target", "UNITS": 21, "AMOUNT": 98.2917}, {"COUNTRY_NAME": "Peru", "STORE": "BestBuy", "UNITS": 2, "AMOUNT": 19.98}, {"COUNTRY_NAME": "Argentina", "STORE": "Chuckys", "UNITS": 8, "AMOUNT": 19.92}, {"COUNTRY_NAME": "Cyprus", "STORE": "BestBuy", "UNITS": 4, "AMOUNT": 5.79}, {"COUNTRY_NAME": "Hungary", "STORE": "BestBuy", "UNITS": 2, "AMOUNT": 13.549999999999997}, {"COUNTRY_NAME": "Bahrain", "STORE": "BestBuy", "UNITS": 2, "AMOUNT": 1.98}, {"COUNTRY_NAME": "Mexico", "STORE": "BestBuy", "UNITS": 1, "AMOUNT": 5.79}, {"COUNTRY_NAME": "United Kingdom", "STORE": "BestBuy", "UNITS": 82, "AMOUNT": 393.65000000004136}, {"COUNTRY_NAME": "Poland", "STORE": "Chuckys", "UNITS": 5, "AMOUNT": 18.82}, {"COUNTRY_NAME": "Germany", "STORE": "BestBuy", "UNITS": 121, "AMOUNT": 611.4099999999656}, {"COUNTRY_NAME": "Luxembourg", "STORE": "BestBuy", "UNITS": 1, "AMOUNT": 10.59999999997986}, {"COUNTRY_NAME": "Canada", "STORE": "Walmart", "UNITS": 2, "AMOUNT": 3.87}, {"COUNTRY_NAME": "Turkey", "STORE": "Walmart", "UNITS": 3, "AMOUNT": 5.337422334294}, {"COUNTRY_NAME": "Slovakia", "STORE": "BestBuy", "UNITS": 1, "AMOUNT": 21.21}, {"COUNTRY_NAME": "Chile", "STORE": "BestBuy", "UNITS": 7, "AMOUNT": 22.53}, {"COUNTRY_NAME": "United States", "STORE": "Walmart", "UNITS": 8, "AMOUNT": 79.70999999999998}, {"COUNTRY_NAME": "Kuwait", "STORE": "BestBuy", "UNITS": 6, "AMOUNT": 12.94}, {"COUNTRY_NAME": "Netherlands", "STORE": "Costco", "UNITS": 4, "AMOUNT": 13.273638}, {"COUNTRY_NAME": "United Kingdom", "STORE": "Walmart", "UNITS": 3, "AMOUNT": 9.55479}, {"COUNTRY_NAME": "Czech Republic", "STORE": "BestBuy", "UNITS": 4, "AMOUNT": 26.57}, {"COUNTRY_NAME": "France", "STORE": "Target", "UNITS": 34, "AMOUNT": 142.5843}, {"COUNTRY_NAME": "Hong Kong", "STORE": "Target", "UNITS": 1, "AMOUNT": 2.2934}, {"COUNTRY_NAME": "Argentina", "STORE": "Walmart", "UNITS": 2, "AMOUNT": 5.34455480611}, {"COUNTRY_NAME": "Mexico", "STORE": "BestBuy", "UNITS": 4, "AMOUNT": 9.82}, {"COUNTRY_NAME": "United Kingdom", "STORE": "Walmart", "UNITS": 4, "AMOUNT": 10.99588}, {"COUNTRY_NAME": "Canada", "STORE": "Chuckys", "UNITS": 1, "AMOUNT": 1.13}, {"COUNTRY_NAME": "Croatia", "STORE": "BestBuy", "UNITS": 3, "AMOUNT": 25.98}, {"COUNTRY_NAME": "United Arab Emirates", "STORE": "Target", "UNITS": 2, "AMOUNT": 3.13}, {"COUNTRY_NAME": "Bahrain", "STORE": "BestBuy", "UNITS": 5, "AMOUNT": 6.25}, {"COUNTRY_NAME": "Ireland", "STORE": "Chuckys", "UNITS": 1, "AMOUNT": 7.1499999999505}, {"COUNTRY_NAME": "Turkey", "STORE": "BestBuy", "UNITS": 9, "AMOUNT": 50.17}, {"COUNTRY_NAME": "Australia", "STORE": "Chuckys", "UNITS": 1, "AMOUNT": 6.0400000000314}, {"COUNTRY_NAME": "Hungary", "STORE": "BestBuy", "UNITS": 3, "AMOUNT": 25.7}, {"COUNTRY_NAME": "United States", "STORE": "Target", "UNITS": 106, "AMOUNT": 565.87}, {"COUNTRY_NAME": "Poland", "STORE": "Walmart", "UNITS": 9, "AMOUNT": 31.985888913225}, {"COUNTRY_NAME": "Greece", "STORE": "BestBuy", "UNITS": 12, "AMOUNT": 26.929999999922096}, {"COUNTRY_NAME": "Turkey", "STORE": "Walmart", "UNITS": 9, "AMOUNT": 16.93}, {"COUNTRY_NAME": "United Kingdom", "STORE": "Costco", "UNITS": 12, "AMOUNT": 88.98428}, {"COUNTRY_NAME": "Japan", "STORE": "Costco", "UNITS": 1, "AMOUNT": 6.842081777751336}, {"COUNTRY_NAME": "United States", "STORE": "Target", "UNITS": 113, "AMOUNT": 807.4099999999999}, {"COUNTRY_NAME": "France", "STORE": "BestBuy", "UNITS": 74, "AMOUNT": 388.2700000001111}, {"COUNTRY_NAME": "Mexico", "STORE": "BestBuy", "UNITS": 7, "AMOUNT": 17.33}, {"COUNTRY_NAME": "United States", "STORE": "Walmart", "UNITS": 5, "AMOUNT": 133.52}, {"COUNTRY_NAME": "Turkey", "STORE": "Target", "UNITS": 7, "AMOUNT": 6.0027}, {"COUNTRY_NAME": "Portugal", "STORE": "Walmart", "UNITS": 2, "AMOUNT": 3.69}, {"COUNTRY_NAME": "France", "STORE": "Walmart", "UNITS": 1, "AMOUNT": 1.054647}, {"COUNTRY_NAME": "Italy", "STORE": "Walmart", "UNITS": 1, "AMOUNT": 1.054647}, {"COUNTRY_NAME": "Kuwait", "STORE": "BestBuy", "UNITS": 16, "AMOUNT": 50.84}, {"COUNTRY_NAME": "Sweden", "STORE": "BestBuy", "UNITS": 7, "AMOUNT": 57.44}, {"COUNTRY_NAME": "Hong Kong", "STORE": "Target", "UNITS": 3, "AMOUNT": 12.384399999999998}, {"COUNTRY_NAME": "Ireland", "STORE": "BestBuy", "UNITS": 14, "AMOUNT": 157.8200000001184}, {"COUNTRY_NAME": "Chile", "STORE": "BestBuy", "UNITS": 2, "AMOUNT": 12.95}, {"COUNTRY_NAME": "United States", "STORE": "BestBuy", "UNITS": 77, "AMOUNT": 360.85}, {"COUNTRY_NAME": "Switzerland", "STORE": "BestBuy", "UNITS": 20, "AMOUNT": 179.55}, {"COUNTRY_NAME": "Brazil", "STORE": "Chuckys", "UNITS": 2, "AMOUNT": 4.03}, {"COUNTRY_NAME": "Japan", "STORE": "Costco", "UNITS": 4, "AMOUNT": 25.137213487825555}, {"COUNTRY_NAME": "Turkey", "STORE": "BestBuy", "UNITS": 14, "AMOUNT": 31.16}, {"COUNTRY_NAME": "Czech Republic", "STORE": "BestBuy", "UNITS": 3, "AMOUNT": 34.55}, {"COUNTRY_NAME": "Canada", "STORE": "Chuckys", "UNITS": 2, "AMOUNT": 6.46}, {"COUNTRY_NAME": "Colombia", "STORE": "Chuckys", "UNITS": 2, "AMOUNT": 4.14}, {"COUNTRY_NAME": "Romania", "STORE": "BestBuy", "UNITS": 10, "AMOUNT": 30.91}, {"COUNTRY_NAME": "South Africa", "STORE": "BestBuy", "UNITS": 3, "AMOUNT": 2.49}, {"COUNTRY_NAME": "Slovakia", "STORE": "BestBuy", "UNITS": 1, "AMOUNT": 5.29}, {"COUNTRY_NAME": "Italy", "STORE": "BestBuy", "UNITS": 47, "AMOUNT": 221.14000000006945}, {"COUNTRY_NAME": "Greece", "STORE": "BestBuy", "UNITS": 4, "AMOUNT": 23.57000000000607}, {"COUNTRY_NAME": "Finland", "STORE": "Walmart", "UNITS": 3, "AMOUNT": 10.514511}, {"COUNTRY_NAME": "Saudi Arabia", "STORE": "Chuckys", "UNITS": 5, "AMOUNT": 17.45}, {"COUNTRY_NAME": "South Africa", "STORE": "Target", "UNITS": 4, "AMOUNT": 11.0025}]

LDATA = [{"id": "Walmart", "data": [{"x": "2023-03-09", "y": 1}]}, {"id": "BestBuy", "data": [{"x": "2023-03-04", "y": 2}, {"x": "2023-03-04", "y": 30}, {"x": "2023-03-04", "y": 9}, {"x": "2023-03-06", "y": 12}, {"x": "2023-03-07", "y": 4}, {"x": "2023-03-09", "y": 2}]}, {"id": "Chuckys", "data": [{"x": "2023-03-07", "y": 2}, {"x": "2023-03-08", "y": 2}, {"x": "2023-03-09", "y": 2}]}, {"id": "Costco", "data": [{"x": "2023-03-06", "y": 3}]}, {"id": "Target", "data": [{"x": "2023-03-06", "y": 1}, {"x": "2023-03-08", "y": 20}]}]







st.write("Description")

create_page=st.button("Create a Chart")

if create_page:
    switch_page("CreateChart")

with elements("dashboard"):
    layout = [
           # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
        dashboard.Item("create_item", 0, 0, 1, 1),
        dashboard.Item("first_item", 1, 0, 8, 8),
        dashboard.Item("second_item", 0, 0, 2, 2),
        dashboard.Item("third_item", 0, 0, 2, 2),
        ]
       # Next, create a dashboard layout using the 'with' syntax. It takes the layout
       # as first parameter, plus additional properties you can find in the GitHub links below.# If you want to retrieve updated layout values as the user move or resize dashboard items,
       # you can pass a callback to the onLayoutChange event parameter.

    def handle_layout_change(updated_layout):
            # You can save the layout in a file, or do anything you want with it.
            # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
        print(updated_layout)

    with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
        with mui.Card(key="first_element"):
            nivo.Radar(
                data=DATA,
                keys=["Walmart","BestBuy","Chuckys","Costco","Target"],
                valueFormat=">-.2f",
                margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
                borderColor={"from": "color"},
                gridLabelOffset=36,
                dotSize=10,
                dotColor={"theme": "background"},
                dotBorderWidth=2,
                motionConfig="wobbly",
                legends=[
                    {
                        "anchor": "top-left",
                        "direction": "column",
                        "translateX": -50,
                        "translateY": -40,
                        "itemWidth": 80,
                        "itemHeight": 20,
                        "itemTextColor": "#999",
                        "symbolSize": 12,
                        "symbolShape": "circle",
                        "effects": [
                            {
                                "on": "hover",
                                "style": {
                                    "itemTextColor": "#000"
                                }
                            }
                        ],
                        "label":"Title"
                    }
                ],
                theme={
                    "background": "#FFFFFF",
                    "textColor": "#31333F",
                    "tooltip": {
                        "container": {
                            "background": "#FFFFFF",
                            "color": "#31333F",
                        }
                    }
                }
            )
        with mui.Card(key="second_element"):
            nivo.Bar(
                data=BDATA,
                groupMode="grouped",
                keys=['UNITS', 'AMOUNT'],
                indexBy="STORE",
                valueFormat=">-.2f",
                margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
                borderColor={"from": "color"},
                gridLabelOffset=36,
                maxValue=40,
                dotSize=10,
                dotColor={"theme": "background"},
                dotBorderWidth=2,
                motionConfig="wobbly",
                legends=[
                    {
                        "anchor": "top-left",
                        "direction": "column",
                        "translateX": -50,
                        "translateY": -40,
                        "itemWidth": 80,
                        "itemHeight": 20,
                        "itemTextColor": "#999",
                        "symbolSize": 12,
                        "symbolShape": "circle",
                        "effects": [
                            {
                                "on": "hover",
                                "style": {
                                    "itemTextColor": "#000"
                                }
                            }
                        ]
                    }
                ],
                theme={
                    "background": "#FFFFFF",
                    "textColor": "#31333F",
                    "tooltip": {
                        "container": {
                            "background": "#FFFFFF",
                            "color": "#31333F",
                        }
                    }
                }
            )
        with mui.Card():
            nivo.Line(
                data=LDATA,
                margin={"top": 70, "right": 80, "bottom": 40, "left": 80},
                borderColor={"from": "color"},
                gridLabelOffset=36,
                dotSize=10,
                dotColor={"theme": "background"},
                dotBorderWidth=2,
                motionConfig="wobbly",
                legends=[
                    {
                        "anchor": "top-left",
                        "direction": "column",
                        "translateX": -50,
                        "translateY": -40,
                        "itemWidth": 80,
                        "itemHeight": 20,
                        "itemTextColor": "#999",
                        "symbolSize": 12,
                        "symbolShape": "circle",
                        "effects": [
                            {
                                "on": "hover",
                                "style": {
                                    "itemTextColor": "#000"
                                }
                            }
                        ],
                        "label":"Title"
                    }
                ],
                theme={
                    "background": "#FFFFFF",
                    "textColor": "#31333F",
                    "tooltip": {
                        "container": {
                            "background": "#FFFFFF",
                            "color": "#31333F",
                        }
                    }
                }
            )