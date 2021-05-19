import pandas as pd
from pyexcel import Reader
import csv

# cleaning of the confirmed us
df_confirmed_us = pd.read_csv('raw_files/time_series_covid19_confirmed_US.csv')
df_confirmed_us=df_confirmed_us.drop(df_confirmed_us.columns[4:len(df_confirmed_us.columns)-1], axis='columns')
df_confirmed_us.columns = [*df_confirmed_us.columns[:-1],'confirmed_us']
# cleaning of the confirmed death us
df_death_us = pd.read_csv('raw_files/time_series_covid19_deaths_US.csv')
df_death_us=df_death_us.drop(df_death_us.columns[4:len(df_death_us.columns)-1], axis='columns')
df_death_us.columns = [*df_death_us.columns[:-1],'confirmed_death_us']
# cleaning of the confirmed global 
df_confirmed_global = pd.read_csv('raw_files/time_series_covid19_confirmed_global.csv')
df_confirmed_global=df_confirmed_global.drop(df_confirmed_global.columns[4:len(df_confirmed_global.columns)-1], axis='columns')
df_confirmed_global.columns = [*df_confirmed_global.columns[:-1],'confirmed_general']
# cleaning of the death global
df_death_global = pd.read_csv('raw_files/time_series_covid19_deaths_global.csv')
df_death_global=df_death_global.drop(df_death_global.columns[4:len(df_death_global.columns)-1], axis='columns')
df_death_global.columns = [*df_death_global.columns[:-1],'confirmed_death']
# cleaning of the recovered global
df_recovered_global = pd.read_csv('raw_files/time_series_covid19_recovered_global.csv')
df_recovered_global=df_recovered_global.drop(df_recovered_global.columns[4:len(df_recovered_global.columns)-1], axis='columns')
df_recovered_global.columns = [*df_recovered_global.columns[:-1],'confirmed_recovered']


# constructing the complete flatfile based on the clean data (US)
#reading in the cleaned confirmed cases in the us
reader_confirmed_us = Reader('cleaned_files/cleaned_confirmed_us.csv', delimiter=',')
#reading in the cleaned confirmed death in the us
reader_death_us = Reader('cleaned_files/cleaned_death_us.csv', delimiter=',')
#creating the flatfile with combined us data
csv_flatfile_us = pd.read_csv('cleaned_files/flat_file_us.csv')
csv_flatfile_us['UID'] = reader_confirmed_us.column_at(0)[1:]
csv_flatfile_us['iso2'] = reader_confirmed_us.column_at(1)[1:]
csv_flatfile_us['iso3'] =  reader_confirmed_us.column_at(2)[1:]
csv_flatfile_us['code3'] = reader_confirmed_us.column_at(3)[1:]
csv_flatfile_us['confirmed_us'] = reader_confirmed_us.column_at(4)[1:]
csv_flatfile_us['confirmed_death_us'] = reader_death_us.column_at(4)[1:]
print(csv_flatfile_us) 



#constructing the complete flatfile based on the clean data (global, except US)
#reading in the cleaned confirmed  global
reader_confirmed_global = Reader('cleaned_files/cleaned_confirmed_global.csv', delimiter=',')
#reading in the cleaned confirmed death global
reader_death_global = Reader('cleaned_files/cleaned_death_global.csv', delimiter=',')

#creating the flatfile with the combined global data
csv_flatfile_global_no_us = pd.read_csv('cleaned_files/flat_file_global_no_us.csv')
csv_flatfile_global_no_us['Province_State'] = reader_confirmed_global.column_at(0)[1:]
csv_flatfile_global_no_us['Country_Region'] = reader_confirmed_global.column_at(1)[1:]
csv_flatfile_global_no_us['Lat'] = reader_confirmed_global.column_at(2)[1:]
csv_flatfile_global_no_us['Long'] = reader_confirmed_global.column_at(3)[1:]
csv_flatfile_global_no_us['confirmed_general'] = reader_confirmed_global.column_at(4)[1:]
csv_flatfile_global_no_us['confirmed_death'] = reader_death_global.column_at(4)[1:]
print(csv_flatfile_global_no_us)



#constructing the recovered info flatfile based on the cleaned data (global, except us)
#reading in the cleanec recovered global
reader_recovered_global = Reader('cleaned_files/cleaned_recovered_global.csv', delimiter=',')

csv_flatfile_recovered_global_no_us = pd.read_csv('cleaned_files/flat_file_recovered_global.csv')
csv_flatfile_recovered_global_no_us['Country_Region'] = reader_recovered_global.column_at(1)[1:]
csv_flatfile_recovered_global_no_us['recovered_global'] = reader_recovered_global.column_at(4)[1:]
csv_flatfile_recovered_global_no_us['Province_State'] = reader_recovered_global.column_at(0)[1:]
print(csv_flatfile_recovered_global_no_us)


csv_flatfile_recovered_global_no_us.to_csv('flatfile_recovered_globally_no_us.csv',index = False)
csv_flatfile_us.to_csv('flat_file_us.csv',index = False)
csv_flatfile_global_no_us.to_csv('flat_file_globally_no_us.csv',index = False)