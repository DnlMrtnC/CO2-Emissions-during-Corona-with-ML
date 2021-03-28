import os

cur_dir = os.getcwd()
os.chdir('../prediction/co2_covid/')

from power_industry import Power_Indicators

pl = Power_Indicators()
pl.clean_co2()
pl.clean_power_industry()
pl.select_indicator(False)
pl.plot_indicators('EU')
axes = pl.plot_sarima(country)
os.chdir(cur_dir)