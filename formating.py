import hana_ml, pandas

#might be necessary to summarize and append us data to the global data

df_confirmed_us = pandas.read_csv('raw_files/time_series_covid19_confirmed_US.csv')
df_confirmed_us=df_confirmed_us.drop(df_confirmed_us.columns[4:len(df_confirmed_us.columns)-1], axis='columns')
df_confirmed_us.columns = [*df_confirmed_us.columns[:-1],'confirmed us']
print(df_confirmed_us)
df_confirmed_us.to_csv(r'./cleaned_files/cleaned_confirmed_us', sep='\t', index=False, header=True)

df_death_us = pandas.read_csv('raw_files/time_series_covid19_deaths_US.csv')
df_death_us=df_death_us.drop(df_death_us.columns[4:len(df_death_us.columns)-1], axis='columns')
df_death_us.columns = [*df_death_us.columns[:-1],'confirmed death us']
print(df_death_us)
df_death_us.to_csv(r'./cleaned_files/cleaned_death_us', sep='\t', index=False, header=True)

df_confirmed_global = pandas.read_csv('raw_files/time_series_covid19_confirmed_global.csv')
df_confirmed_global=df_confirmed_global.drop(df_confirmed_global.columns[4:len(df_confirmed_global.columns)-1], axis='columns')
df_confirmed_global.columns = [*df_confirmed_global.columns[:-1],'confirmed general']
print(df_confirmed_global)
df_confirmed_global.to_csv(r'./cleaned_files/cleaned_confirmed_global', sep='\t', index=False, header=True)


df_death_global = pandas.read_csv('raw_files/time_series_covid19_deaths_global.csv')
df_death_global=df_death_global.drop(df_death_global.columns[4:len(df_death_global.columns)-1], axis='columns')
df_death_global.columns = [*df_death_global.columns[:-1],'confirmed death']
print(df_death_global)
df_death_global.to_csv(r'./cleaned_files/cleaned_death_global', sep='\t', index=False, header=True)

df_recovered_global = pandas.read_csv('raw_files/time_series_covid19_recovered_global.csv')
df_recovered_global=df_recovered_global.drop(df_recovered_global.columns[4:len(df_recovered_global.columns)-1], axis='columns')
df_recovered_global.columns = [*df_recovered_global.columns[:-1],'confirmed recovered']
print(df_recovered_global)
df_recovered_global.to_csv(r'./cleaned_files/cleaned_recovered_global', sep='\t', index=False, header=True)