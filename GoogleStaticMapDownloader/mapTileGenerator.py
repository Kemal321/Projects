import folium
# lat = 41.0984920
# lon = 29.3186839
# defaultZoom = 12

# mapObj = folium.Map(lat,lon,zoom_start=defaultZoom)

# mytoken = "AIzaSyCDy9v5vQycRps0CcmpoO31IWXOVTHFLNM"    >>> My google's API key 
m = folium.Map(location=[45.523, -122.675], width=750, height=500)
m = folium.Map(location=[45.523, -122.675], tiles="cartodb positron")
m = folium.Map(
    location=[45.523, -122.675],    
    zoom_start=2,
    tiles="Stamen",
    attr="Mapbox attribution",
)
