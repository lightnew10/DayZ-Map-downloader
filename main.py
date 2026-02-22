import os
import requests

#If u want more maps, go to https://www.izurvive.com/chernarusplus/ and access the network (F12). Copy the WebP image URL when you zoom in to load them :)
#example map url : https://maps.izurvive.com/maps/ChernarusPlus-Sat/1.26.0/tiles/2/0/2.webp
MAP = "ChernarusPlus-Sat"  # "ChernarusPlus-Top", "Livonia-Sat", "Banov-Sat", "DeerIsle-Sat", "Namalsk-Sat", "Sakhal-sat"
VERSION = "1.26.0"
ZOOM = 7  # 7 = 128 tiles | 8 = 256 tiles

# u need to change the url if izurvive change his url :)
BASE_URL = f"https://maps.izurvive.com/maps/{MAP}/{VERSION}/tiles/{ZOOM}/"
SAVE_DIR = f"tiles_{MAP}_{ZOOM}"
os.makedirs(SAVE_DIR, exist_ok=True)


def download():
    max_coord = 2 ** ZOOM
    print(f"Download started : {MAP} Zoom {ZOOM}")
    print(f"Folder destination : {SAVE_DIR}")

    for x in range(max_coord):
        os.makedirs(os.path.join(SAVE_DIR, str(x)), exist_ok=True)

        for y in range(max_coord):
            file_path = f"{x}/{y}.webp"
            url = f"{BASE_URL}{file_path}"
            target_path = os.path.join(SAVE_DIR, file_path)

            if not os.path.exists(target_path):
                r = requests.get(url, timeout=10)
                if r.status_code == 200:
                    with open(target_path, 'wb') as f:
                        f.write(r.content)
                elif r.status_code == 404:
                    continue

        print(f"Progression : {x}/{max_coord - 1} finished.")


if __name__ == "__main__":
    download()