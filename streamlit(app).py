# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 22:51:29 2023

@author: VManickam2
"""

import streamlit as st
import pandas as pd
st.title("Welcome to my app")
st.header("TDS Assignment8")
st.info("This app to find greatest among given 3 numbers")
def user_input_features():
    Number1 = st.number_input("Number1",min_value=0,max_value=10000000)
    Number2 = st.number_input("Number2",min_value=0,max_value=10000000)
    Number3 = st.number_input("Number3",min_value=0,max_value=10000000)
    st.write('greatest number is',  max(Number1,Number2,Number3))
    
    data = {'Number1': Number1,
            'Number2': Number2,
            'Number3': Number3}
    features = pd.DataFrame(data, index=[0])
    return features
            
df = user_input_features()