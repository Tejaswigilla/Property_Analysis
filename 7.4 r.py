loc = pd.Series(df['location'].unique())
loc_long = loc.apply(longitude)
loc_long.isnull().sum()
df1 = pd.DataFrame()
df1['Location'] = loc
df1['Longitude']=loc_long
df1.head()
loc_lat = loc.apply(latitude)
df1.to_csv('long_lat.csv')
def generateBaseMap(default_location=[17.4447, 78.4664], default_zoom_start=11):
    base_map = folium.Map(location=default_location, control_scale=True, zoom_start=default_zoom_start)
    return base_map

basemap = generateBaseMap()
basemap

df1.keys()

df1.columns = ['location','longitude','latitude']

df2 = df.merge(df1,on='location')

dff = df2.dropna(axis=0)

dff.to_csv('real_lat_long.csv')


