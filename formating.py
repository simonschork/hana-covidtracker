import pandas

df_confirmed_us = pandas.read_csv('time_series_covid19_confirmed_US.csv')

df_death_us = pandas.read_csv('time_series_covid19_deaths_US.csv')


df_confirmed_global = pandas.read_csv('time_series_covid19_confirmed_global.csv')
print(df_confirmed_global.head)
df_confirmed_global=df_confirmed_global.drop(df_confirmed_global.columns[4:len(df_confirmed_global.columns)-1], axis='columns')
df_confirmed_global.columns = [*df_confirmed_global.columns[:-1],'confirmed general']
print(df_confirmed_global)

df_death_global = pandas.read_csv('time_series_covid19_deaths_global.csv')

df_death_global=df_death_global.drop(df_death_global.columns[4:len(df_death_global.columns)-1], axis='columns')
df_death_global.columns = [*df_death_global.columns[:-1],'confirmed death']
print(df_death_global)

df_recovered_global = pandas.read_csv('time_series_covid19_recovered_global.csv')

df_recovered_global=df_recovered_global.drop(df_recovered_global.columns[4:len(df_recovered_global.columns)-1], axis='columns')
df_recovered_global.columns = [*df_recovered_global.columns[:-1],'confirmed recovered']
print(df_recovered_global)