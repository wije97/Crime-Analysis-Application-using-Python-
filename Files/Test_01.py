import pandas as pd
import matplotlib.pyplot as plt
import os
os.environ['USE_PYGEOS'] = '0'
import geopandas as gpd

gdf = gpd.read_file('D:\Ongoing\Melani\LSOA_(Dec_2021)_Boundaries_Generalised_Clipped_EW_(BGC)\LSOA_(Dec_2021)_Boundaries_Generalised_Clipped_EW_(BGC).shp')

sp_rows_array=[]
lsoa_arr=[]
lsoa_count_arr=[]
shp_data_arr=[]

type_c = "Violence and sexual offences"
df_southwales_2020 = pd.read_csv('D:\Ongoing\Melani\CSV\Southwales_2020.csv')
specific_rows_by_crime = df_southwales_2020.loc[df_southwales_2020['Crime type'] == type_c]
grouped_places = specific_rows_by_crime.groupby('LSOA code')
#print(grouped_places.groups)

for x,group in grouped_places:
    #print(x)
    specific_rows_by_place = specific_rows_by_crime.loc[specific_rows_by_crime['LSOA code'] == x]
    #print(specific_rows_by_place)
    sp_rows_array.append(specific_rows_by_place)

for row in sp_rows_array:
    value_counts_by_crime = row['LSOA code'].value_counts()
    #print(value_counts_by_crime)
    lsoa_arr.append(value_counts_by_crime.keys())
    lsoa_count_arr.append(value_counts_by_crime.values)
"""
for x,group in grouped_places:
    rows_by_place = con_df.loc[con_df['LSOA21CD'] == x]
    shp_data_arr.append(rows_by_place.values)
print(shp_data_arr)
"""

dtframe_from_with_LSOA = pd.DataFrame(data=lsoa_arr, columns=['LSOA21CD'])
dtframe_from_with_LSOA_count = pd.DataFrame(data=lsoa_count_arr, columns=['LSOA_count'])
#dtframe_LSOA = pd.DataFrame(shp_data_arr, columns=['OBJECTID', 'LSOA21CD', 'LSOA21NM', 'GlobalID', 'Shape__Are', 'Shape__Len', 'geometry'])
#print(dtframe_LSOA)
dtframe_coupled = pd.concat([dtframe_from_with_LSOA,dtframe_from_with_LSOA_count], axis=1)
#print(dtframe_coupled.head())
merged = dtframe_coupled.set_index('LSOA21CD').join(gdf.set_index('LSOA21CD'))
gdf_x = gpd.GeoDataFrame(merged, geometry="geometry")
#print(merged)


# create figure and axes for Matplotlib and set the title

fig, ax = plt.subplots(1, figsize=(10, 6))
ax.axis('off')
ax.set_title('Crime Analysis', fontdict={'fontsize': '15', 'fontweight' : '3'})
gdf_x.plot(column='LSOA_count',
            cmap='viridis',
            linewidth=0.9,
            ax=ax,
            legend=True)

plt.show()
