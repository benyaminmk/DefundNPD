""" Author: Benyamin Meschede-Krasa 
test cleaning scripts """
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from eer_cleaner import clean_pdf

######################
######  PARAMS  ######
######################
FP_EER16_PDF = os.path.join('data','eer16.pdf')
FP_EER16_TARGET = os.path.join('data','eer16.csv')

#############################
######  PRECONDITIONS  ######
#############################
assert os.path.exists(FP_EER16_PDF)

if __name__ == "__main__":
    pass 
