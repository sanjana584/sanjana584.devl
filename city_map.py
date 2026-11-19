import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point

data = {
    "city": ["Berlin", "Paris", "Munich"],
    "latitude": [52.518611111111, 48.856666666667, 48.137222222222],
    "longitude": [13.408333333333, 2.3516666666667, 11.575555555556],
}

df = pd.DataFrame(data)

geometry = [
    Point(longitude, latitude)
    for longitude, latitude in zip(df["longitude"], df["latitude"])
]

gdf = gpd.GeoDataFrame(
    df[["city"]],
    geometry=geometry,
    crs="EPSG:4326",
)

print(gdf)

world = gpd.read_file(
    "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
)

base = world.plot(color="white", edgecolor="black")
gdf.plot(ax=base, marker="o", color="red", markersize=20)

plt.show()
