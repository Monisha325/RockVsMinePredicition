# -*- coding: utf-8 -*-
"""
Created on Fri Jul 25 21:16:55 2025

@author: patna
"""

import numpy as np
import pickle 
import streamlit

#load the saved model
loaded_model = pickle.load(open('C:/Users/patna/OneDrive/Desktop/RockVsMinePredicition/trained_model.sav','rb'))
