import pandas as pd
import os
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
current_path = os.path.dirname(__file__)
csv_path = os.path.join(current_path, "ir.csv")
df = pd.read_csv(csv_path)
# df = pd.read_csv(os.path.join(os.getcwd(), "ir.csv"))
# print(df)
# print(df.columns)
cities = ["Tehran", "Mashhad", "Esfahan", "Rasht", "Shiraz",
          "Tabriz", "Sanandaj", "Ahvaz", "Kermanshah", "Zahedan"]
selected_cities = df[df["city"].isin(cities)][["city", "lat", "lng", "population"]].reset_index(drop=True)
# print(selected_cities)
plt.figure(figsize=(10, 10))
# m = Basemap(llcrnrlon=44, llcrnrlat=25, urcrnrlon=64, urcrnrlat=40, projection="lcc", lat_1=33,
#             lat_2=45, lon_0=53)
m = Basemap(projection="aea", llcrnrlon=44, llcrnrlat=25, urcrnrlon=64, urcrnrlat=40,
            lat_1=27, lat_2=39, lon_0=53, resolution="l")
m.drawcoastlines(color="green", linewidth=2)
m.drawcountries(color="red", linewidth=2)
m.drawmapboundary()
m.drawparallels(range(25, 41, 5), labels=[1, 0, 0, 0])
m.drawmeridians(range(44, 65, 5), labels=[0, 0, 0, 1])
x, y = m(selected_cities["lng"].values, selected_cities["lat"].values)
m.scatter(x, y, s=selected_cities["population"] / 15_000, color="green", alpha=0.6,
          edgecolors="black", linewidth=0.5, zorder=5)
for name, xc, yc in zip(selected_cities["city"], x, y):
    plt.text(xc, yc - 55000, name, fontsize=9, ha="center", color="red", weight="bold")
plt.title("population of 10 cities in Iran", fontsize=14, weight="bold")
plt.savefig("iran_map.png", dpi=300, bbox_inches="tight")
plt.show()
