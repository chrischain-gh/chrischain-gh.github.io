import pandas as pd
import xml.etree.ElementTree as ET
from urllib.parse import unquote
from pyscript import display, document
from js import window

pd.set_option('display.max_rows', None)


def find_tracks_with_bitrate_from_text(xml_text, target_bitrate=128):
    root = ET.fromstring(xml_text)

    matching_tracks = []

    for track in root.iter("TRACK"):
        bitrate = track.attrib.get("BitRate")

        if bitrate is not None and int(bitrate) == target_bitrate:
            attrib = track.attrib.copy()

            location = attrib.get("Location", "")
            if location.startswith("file://"):
                attrib["Location"] = unquote(
                    location.replace("file://localhost", "")
                )

            attrib["BitRate"] = int(attrib["BitRate"])

            matching_tracks.append(attrib)

    return matching_tracks


def run_func(e=None):
    file_input = document.getElementById("fileInput")

    if not file_input.files.length:
        display("No file selected")
        return

    file = file_input.files.item(0)

    reader = window.FileReader.new()

    def onload(evt):
        xml_text = evt.target.result

        tracks_128 = find_tracks_with_bitrate_from_text(xml_text, 128)

        display(f"Found {len(tracks_128)} tracks with BitRate = 128")

        df = pd.DataFrame(tracks_128)

        df = df.rename(columns={
            "Name": "Name",
            "Artist": "Artist",
            "Album": "album",
            "BitRate": "Bitrate (kbps)",
            "Location": "File Path"
        })

        df = df[[
            "Name", "Artist", "album",
            "Bitrate (kbps)", "File Path"
        ]]

        display(df)

        display(
            df.groupby(["Artist", "album"])
              .count()["Name"]
              .sort_values(ascending=False)
              .to_frame()
        )

    reader.onload = onload
    reader.readAsText(file)


document.getElementById("runButton").onclick = run_func