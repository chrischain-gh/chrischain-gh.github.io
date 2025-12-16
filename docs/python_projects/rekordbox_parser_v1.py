import pandas as pd
#import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
from urllib.parse import unquote
from pyscript import display

pd.set_option('display.max_rows', None)

def find_tracks_with_bitrate(xml_path, target_bitrate=128):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    matching_tracks = []

    # Iterate over all TRACK elements
    for track in root.iter("TRACK"):
        bitrate = track.attrib.get("BitRate")

        # BitRate is stored as a string
        if bitrate is not None and int(bitrate) == target_bitrate:
            name = track.attrib.get("Name", "")
            artist = track.attrib.get("Artist", "")
            album = track.attrib.get("Album", "")
            location = track.attrib.get("Location", "")

            # Decode file URL for readability
            if location.startswith("file://"):
                location = unquote(location.replace("file://localhost", ""))

            matching_tracks.append({
                "name": name,
                "artist": artist,
                "bitrate": bitrate,
                "album": album,
                "location": location
            })

    return matching_tracks



xml_file = "2025-12-13_backup.xml"  # <-- path to your XML export


tracks_128 = find_tracks_with_bitrate(xml_file, 128)



print(f"Found {len(tracks_128)} tracks with BitRate = 128:\n")

for t in tracks_128:
    #display(f"- {t['name']} | {t['artist']} | {t['bitrate']} kbps")
    #display(f"  {t['location']}\n")
    pass
    
df = pd.DataFrame(tracks_128)

# Optional: nicer column order + names
df = df.rename(columns={
    "name": "Name",
    "artist": "Artist",
    "bitrate": "Bitrate (kbps)",
    "location": "File Path"
})

df = df[["Name", "Artist", "album", "Bitrate (kbps)", "File Path"]]

display(df)

display(df.groupby(['Artist', 'album']).count()['Name'].sort_values(ascending=False).to_frame())
