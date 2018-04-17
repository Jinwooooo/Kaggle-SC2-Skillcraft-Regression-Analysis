import numpy as np
import pandas as pd
import urllib.request as urllib
import matplotlib.pyplot as plt
import statsmodels.api as sm

# getting data
url = 'https://raw.githubusercontent.com/Jinwooooo/Kaggle-SC2-Skillcraft-Regression-Analysis/master/data/skillcraft.csv'
response = urllib.urlopen(url)
df_main = pd.read_csv(response)
response.close()

# EDA
# checking if data looks like a normal distribution
# df_league_index_distr = (df_main['LeagueIndex'].value_counts()).to_frame()
# df_league_index_distr.sort_index(inplace=True)
# df_league_index_distr.plot(kind='bar',y='LeagueIndex',colormap='Paired')
# plt.show()
# checking if there are lots of outliers in the data
# note that GameID has been exlcuded since it presents no purpose in the analysis
fig, ax = plt.subplots(nrows=6, ncols=3, sharey=False)
ax[0,0] = df_main.boxplot(column='Age',by='LeagueIndex')
ax[0,1] = df_main.boxplot(column='HoursPerWeek',by='LeagueIndex')
# df_main.boxplot(['LeagueIndex','Age'])
# # df_main[['LeagueIndex','HoursPerWeek']].boxplot()
plt.show()

# # Dependent Variable
# y = df_main[['LeagueIndex']]
#
# # 1st Model : Full Model
# x_1 = df_main.drop(['GameID','LeagueIndex'], axis=1)
# model_1 = sm.OLS(y,x_1).fit()
# print(model_1.summary())
#
# # 2nd Model : Excluding Independent Variable w/ p-values lower than 0.05
# x_2 = df_main.drop(['GameID','LeagueIndex','TotalHours','MinimapRightClicks','UniqueUnitsMade',
#                    'ComplexUnitsMade','ComplexAbilitiesUsed'], axis=1)
# model_2 = sm.OLS(y,x_2).fit()
# print(model_2.summary())
