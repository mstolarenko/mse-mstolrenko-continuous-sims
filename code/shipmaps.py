import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


def draw_Map(c1, c2, c3, c4):
    """initialize a basemap centered on the continental USA"""
    plt.figure(figsize=(14, 10))
    return Basemap(projection='lcc', resolution='l',
                   llcrnrlon=c1, urcrnrlon=c2,
                   llcrnrlat=c3, urcrnrlat=c4,
                   lat_1=33, lat_2=45, lon_0=-95,
                   area_thresh=10000)


m = draw_Map(-90, -74.5, 23.3, 31)  # Florida
# m = draw_Map(-78.0, -71.0, 36.4, 39.6) # Chesapeake Bay
# m = draw_Map(-68.1, -64.2, 17.4, 19.5)  # Puerto Rico
# m = draw_Map(-132.0, -54.0, 15.3, 51)  # USA

# Draw map background
m.fillcontinents(color='white', lake_color='#eeeeee')
m.drawstates(color='lightgrey')
m.drawcoastlines(color='gray')
m.drawcountries(color='black')
# m.drawcounties(color='black')         # Uncomment this line when calling Puerto Rico
m.drawmapboundary(fill_color='#eeeeee')

df=pd.read_csv("C:/Users/maxwe/Documents/Grad/Classes/Fall 2022/SimTech/assignment2-data/data/"
               "AIS_2020_02/AIS_2020_02_05_PATUXENT.csv")        # cd to appropriate csv file

style = dict(s=20, marker='o', alpha=0.5, zorder=2)
m.scatter( df.iloc[:,3], df.iloc[:,2], latlon=True, color='#E52BDF', **style)



plt.show()