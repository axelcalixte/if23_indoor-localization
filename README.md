# Indoor localization

Python application trained to localize a computer in several rooms in the UTT.

## Scan the RSSI :

1. wifi-scan-if23.py : scan the wifi networks and save them in json
2. format-bdd-if23.py : combine the datas in one json file from wifi-scan-if23.py

## Data imports and pre-processing :

An example is available in a Jupyter Notebook `processDatas.ipynb`

- `prepareRSSI.py` is a lib needed to import and prepare the RSSI values in an array
- `paramters.py` contains the file names for imports and exports, as well as the parameters for processing the RSSI values
- `rssi.csv` processed RSSI values
- `mac.csv` processed mac adresses associated to `rssi.csv`
- `zones.csv` processed zone ids associated to `rssi.csv`
- `rawRSSI.csv` non-processed RSSI values, exported in the Jupyter Notebook

Authors : Axel CALIXTE, Romain STEVENS, Romain THOMAS

2022