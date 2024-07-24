import os
import requests

def download_map_tiles(api_key, lat, lng, zoom_levels, output_directory):
    base_url = "https://maps.googleapis.com/maps/api/staticmap"

    # Dizin yoksa oluştur
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for zoom in range(zoom_levels[0], zoom_levels[1] + 1):
        params = {
            "center": f"{lat},{lng}",
            "zoom": zoom,
            "size": "256x256",
            "maptype": "satellite",
            "key": api_key
        }

        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            file_path = os.path.join(output_directory, f"map_tile_{zoom}.png")
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"Zoom seviyesi {zoom} için harita döşemesi indirildi: {file_path}")
        else:
            print(f"Zoom seviyesi {zoom} için harita döşemesi indirilemedi. Hata kodu: {response.status_code}")

if __name__ == "__main__":
    # API anahtarınızı ve indirmek istediğiniz bölgenin koordinatlarını girin
    API_KEY = "YOUR_API_KEY"
    LATITUDE = YOUR_LATITUDE
    LONGITUDE = YOUR_LONGTITUDE
    # İndirmek istediğiniz zoom seviyelerini belirleyin (13-22 arasında)
    ZOOM_LEVELS = (17, 20)
    # Harita döşemelerini kaydetmek istediğiniz dizini belirtin
    OUTPUT_DIRECTORY = "GoogleStaticMapDownloader/DownloadedMaps"
    
    download_map_tiles(API_KEY, LATITUDE, LONGITUDE, ZOOM_LEVELS, OUTPUT_DIRECTORY)
