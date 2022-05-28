import json
import os

# JSON for bdd
# The object represented is a complete zone which is composed of multiple
# positions where we got multiples features per acquisition in the same zone
#
# on veut
# {  # début du fichier .json de la zone
#     "pos1":    # première position
#         [      # tableau d'acquisitions, il y en a 5
#             [  #
#                 {"mac": "aa:11:22:33:bb:cc", "rssi": -67},
#                 {"mac": "aa:11:ab:33:bb:cc", "rssi": -87},
#                 { ... },
#                 {"mac": "aa:11:cd:33:bb:cc", "rssi": -99}
#             ],
#             [  # seconde acquisition
#             ...
#             ],
#         ],
#     "pos2":
#         [
#         ...
#         ],
#     "..."
# }

# actuellement nous avons
# {  # début du fichier représentant une position
#     "tableau_d'acquisition_N": [
#          {"mac": "aa:11:22:33:bb:cc", "rssi": -67},
#          {"mac": "aa:11:ab:33:bb:cc", "rssi": -87},
#          { ... },
#          {"mac": "aa:11:cd:33:bb:cc", "rssi": -99}
#     ],
#     "tableau_d'acquisition_N+1": [
#         ...
#     ],
#     ...
# }

for name in os.listdir("./data/"):
    for z in os.listdir("./data/" + name + "/zones"):
        zone = {}
        for position in os.listdir("./data/" + name + "/zones/" + z):
            with open("./data/" + name
                      + "/zones"
                      + "/" + z
                      + "/" + position, "r") as file:
                ap_list = []
                for acquisition_nb, ap_arr in json.load(file).items():
                    ap_list.append(ap_arr)
                zone[os.path.splitext(position)[0]] = ap_list

        with open("./output/" + name + "/" + z + ".json", "w") as out:
            json.dump(zone, out)
