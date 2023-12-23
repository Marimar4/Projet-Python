# Importation des bases des packages
import io 
from io import BytesIO 
import pycodestyle as pep8
import zipfile
import requests
import openpyxl as xl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pycountry
import seaborn as sns
import missingno as msno
from statistics import *

np.random.seed(123)

class MonProjet:
    def __init__(self) -> None:
        self.f_gmd = 'GMD'
        self.f_countrycode = 'countrycode'
        self.f_countryname = 'countryname'
        self.f_year = 'year'
        self.f_region = 'region'
        self.f_regionname = 'regionname'
        self.f_incomelevelname = 'incomelevelname'
        self.f_lendingtypename = 'lendingtypename'
        self.f_index = 'index'
        self.f_between = 'between'
        self.f_within = 'within'
        self.f_noregion = 'noregion'
        self.f_nobs = 'nobs'
        self.f_minwelfare_median = 'minwelfare_median'
        self.f_maxwelfare_median = 'maxwelfare_median'
        self.f_minwelfare_mean = 'minwelfare_mean'
        self.f_maxwelfare_mean = 'maxwelfare_mean'
        self.f_minwelfare_b1 = 'minwelfare_b1'
        self.f_maxwelfare_b1 = 'maxwelfare_b1'
        self.f_minwelfare_t1 = 'minwelfare_t1'
        self.f_maxwelfare_t1 = 'maxwelfare_t1'
        self.f_ineq = 'ineq'
        self.f_withinreg = 'withinreg'
        self.f_ny_gdp_pcap_pp_kd = 'ny_gdp_pcap_pp_kd'
        self.f_sp_urb_totl_in_zs = 'sp_urb_totl_in_zs'
        self.f_sp_pop_totl = 'sp_pop_totl'
        self.f_en_urb_lcty_ur_zs = 'en_urb_lcty_ur_zs'
        self.f_si_pov_lmic = 'si_pov_lmic'
        self.f_loggdp = 'loggdp'
        self.f_logpop = 'logpop'
        self.f_pib = 'pib'
        self.f_unemployment_rate = 'unemployment_rate'
        
        """Rajouter les méthodes"""
        pass


