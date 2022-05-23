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

# Zone = namedtuple("Zone", {[[]]})


def zoneJsonDecod(zoneDict):
    return dict({zoneDict.keys(): zoneDict.values()})


zoneJSON = """
{
  "1": [
    {
      "mac": "00:a3:8e:c7:a4:fc",
      "RSSI": -68.0
    },
    {
      "mac": "00:a3:8e:e2:3c:13",
      "RSSI": -68.0
    },
    {
      "mac": "00:27:e3:07:b3:53",
      "RSSI": -66.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fb",
      "RSSI": -68.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f4",
      "RSSI": -63.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f1",
      "RSSI": -64.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fc",
      "RSSI": -64.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fd",
      "RSSI": -64.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f3",
      "RSSI": -64.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f5",
      "RSSI": -63.0
    },
    {
      "mac": "00:27:e3:07:b3:5d",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:54",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:51",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:55",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:5c",
      "RSSI": -65.0
    },
    {
      "mac": "00:a3:8e:e2:3c:11",
      "RSSI": -67.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1c",
      "RSSI": -68.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1d",
      "RSSI": -68.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fe",
      "RSSI": -67.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f3",
      "RSSI": -68.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f2",
      "RSSI": -68.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fa",
      "RSSI": -68.0
    },
    {
      "mac": "00:a3:8e:e2:3c:14",
      "RSSI": -69.0
    },
    {
      "mac": "00:a3:8e:e2:3c:15",
      "RSSI": -67.0
    },
    {
      "mac": "00:27:e3:07:b3:57",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:56",
      "RSSI": -64.0
    },
    {
      "mac": "00:27:e3:07:b3:52",
      "RSSI": -65.0
    },
    {
      "mac": "00:a3:8e:e2:3c:16",
      "RSSI": -68.0
    },
    {
      "mac": "00:27:e3:07:b3:5b",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:5e",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:53",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:5c",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:5a",
      "RSSI": -65.0
    },
    {
      "mac": "00:a3:8e:e2:3c:12",
      "RSSI": -68.0
    },
    {
      "mac": "00:27:e3:07:b3:52",
      "RSSI": -67.0
    },
    {
      "mac": "00:27:e3:07:b3:5d",
      "RSSI": -61.0
    },
    {
      "mac": "70:db:98:ee:25:34",
      "RSSI": -83.0
    },
    {
      "mac": "00:27:e3:07:b3:59",
      "RSSI": -61.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1c",
      "RSSI": -79.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1a",
      "RSSI": -79.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f7",
      "RSSI": -70.0
    },
    {
      "mac": "3e:dc:bc:0a:62:ee",
      "RSSI": -83.0
    },
    {
      "mac": "12:e0:aa:22:15:81",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:19",
      "RSSI": -79.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:85",
      "RSSI": -83.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:87",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:17",
      "RSSI": -68.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:8d",
      "RSSI": -83.0
    },
    {
      "mac": "5c:5a:c7:29:c5:41",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:31",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:3c",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:37",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:3d",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1d",
      "RSSI": -79.0
    }
  ],
  "2": [
    {
      "mac": "00:a3:8e:c7:a4:fc",
      "RSSI": -75.0
    },
    {
      "mac": "00:a3:8e:e2:3c:13",
      "RSSI": -72.0
    },
    {
      "mac": "00:27:e3:07:b3:53",
      "RSSI": -65.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fb",
      "RSSI": -74.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f4",
      "RSSI": -69.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f1",
      "RSSI": -70.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fc",
      "RSSI": -68.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fd",
      "RSSI": -70.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f3",
      "RSSI": -69.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f5",
      "RSSI": -68.0
    },
    {
      "mac": "00:27:e3:07:b3:5d",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:54",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:51",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:55",
      "RSSI": -64.0
    },
    {
      "mac": "00:27:e3:07:b3:5c",
      "RSSI": -65.0
    },
    {
      "mac": "00:a3:8e:e2:3c:11",
      "RSSI": -69.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1c",
      "RSSI": -70.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1d",
      "RSSI": -71.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fe",
      "RSSI": -75.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f3",
      "RSSI": -75.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f2",
      "RSSI": -75.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fa",
      "RSSI": -75.0
    },
    {
      "mac": "00:a3:8e:e2:3c:14",
      "RSSI": -69.0
    },
    {
      "mac": "00:a3:8e:e2:3c:15",
      "RSSI": -71.0
    },
    {
      "mac": "00:27:e3:07:b3:57",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:56",
      "RSSI": -67.0
    },
    {
      "mac": "00:27:e3:07:b3:52",
      "RSSI": -65.0
    },
    {
      "mac": "00:a3:8e:e2:3c:16",
      "RSSI": -69.0
    },
    {
      "mac": "00:27:e3:07:b3:5b",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:5e",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:53",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:5c",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:5a",
      "RSSI": -66.0
    },
    {
      "mac": "00:a3:8e:e2:3c:12",
      "RSSI": -68.0
    },
    {
      "mac": "00:27:e3:07:b3:52",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:5d",
      "RSSI": -61.0
    },
    {
      "mac": "70:db:98:ee:25:34",
      "RSSI": -83.0
    },
    {
      "mac": "00:27:e3:07:b3:59",
      "RSSI": -61.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1c",
      "RSSI": -79.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1a",
      "RSSI": -79.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f7",
      "RSSI": -70.0
    },
    {
      "mac": "3e:dc:bc:0a:62:ee",
      "RSSI": -83.0
    },
    {
      "mac": "12:e0:aa:22:15:81",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:19",
      "RSSI": -79.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:85",
      "RSSI": -83.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:87",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:17",
      "RSSI": -68.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:8d",
      "RSSI": -83.0
    },
    {
      "mac": "5c:5a:c7:29:c5:41",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:31",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:3c",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:37",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:3d",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1d",
      "RSSI": -79.0
    },
    {
      "mac": "2a:80:cf:be:25:dd",
      "RSSI": -83.0
    },
    {
      "mac": "88:11:96:e6:fd:ff",
      "RSSI": -83.0
    }
  ],
  "3": [
    {
      "mac": "00:a3:8e:c7:a4:fc",
      "RSSI": -71.0
    },
    {
      "mac": "00:a3:8e:e2:3c:13",
      "RSSI": -71.0
    },
    {
      "mac": "00:27:e3:07:b3:53",
      "RSSI": -64.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fb",
      "RSSI": -70.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f4",
      "RSSI": -64.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f1",
      "RSSI": -65.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fc",
      "RSSI": -65.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fd",
      "RSSI": -65.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f3",
      "RSSI": -65.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f5",
      "RSSI": -63.0
    },
    {
      "mac": "00:27:e3:07:b3:5d",
      "RSSI": -64.0
    },
    {
      "mac": "00:27:e3:07:b3:54",
      "RSSI": -64.0
    },
    {
      "mac": "00:27:e3:07:b3:51",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:55",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:5c",
      "RSSI": -65.0
    },
    {
      "mac": "00:a3:8e:e2:3c:11",
      "RSSI": -71.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1c",
      "RSSI": -72.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1d",
      "RSSI": -72.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fe",
      "RSSI": -71.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f3",
      "RSSI": -70.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f2",
      "RSSI": -71.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fa",
      "RSSI": -71.0
    },
    {
      "mac": "00:a3:8e:e2:3c:14",
      "RSSI": -72.0
    },
    {
      "mac": "00:a3:8e:e2:3c:15",
      "RSSI": -70.0
    },
    {
      "mac": "00:27:e3:07:b3:57",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:56",
      "RSSI": -64.0
    },
    {
      "mac": "00:27:e3:07:b3:52",
      "RSSI": -67.0
    },
    {
      "mac": "00:a3:8e:e2:3c:16",
      "RSSI": -72.0
    },
    {
      "mac": "00:27:e3:07:b3:5b",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:5e",
      "RSSI": -67.0
    },
    {
      "mac": "00:27:e3:07:b3:53",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:5c",
      "RSSI": -67.0
    },
    {
      "mac": "00:27:e3:07:b3:5a",
      "RSSI": -67.0
    },
    {
      "mac": "00:a3:8e:e2:3c:12",
      "RSSI": -72.0
    },
    {
      "mac": "00:27:e3:07:b3:52",
      "RSSI": -67.0
    },
    {
      "mac": "00:27:e3:07:b3:5d",
      "RSSI": -61.0
    },
    {
      "mac": "70:db:98:ee:25:34",
      "RSSI": -83.0
    },
    {
      "mac": "00:27:e3:07:b3:59",
      "RSSI": -61.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1c",
      "RSSI": -79.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1a",
      "RSSI": -79.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f7",
      "RSSI": -70.0
    },
    {
      "mac": "3e:dc:bc:0a:62:ee",
      "RSSI": -83.0
    },
    {
      "mac": "12:e0:aa:22:15:81",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:19",
      "RSSI": -79.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:85",
      "RSSI": -83.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:87",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:17",
      "RSSI": -71.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:8d",
      "RSSI": -83.0
    },
    {
      "mac": "5c:5a:c7:29:c5:41",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:31",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:3c",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:37",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:3d",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1d",
      "RSSI": -79.0
    },
    {
      "mac": "2a:80:cf:be:25:dd",
      "RSSI": -83.0
    },
    {
      "mac": "88:11:96:e6:fd:ff",
      "RSSI": -83.0
    }
  ],
  "4": [
    {
      "mac": "00:a3:8e:c7:a4:fc",
      "RSSI": -76.0
    },
    {
      "mac": "00:a3:8e:e2:3c:13",
      "RSSI": -76.0
    },
    {
      "mac": "00:27:e3:07:b3:53",
      "RSSI": -64.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fb",
      "RSSI": -75.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f4",
      "RSSI": -72.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f1",
      "RSSI": -72.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fc",
      "RSSI": -72.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fd",
      "RSSI": -72.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f3",
      "RSSI": -71.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f5",
      "RSSI": -71.0
    },
    {
      "mac": "00:27:e3:07:b3:5d",
      "RSSI": -64.0
    },
    {
      "mac": "00:27:e3:07:b3:54",
      "RSSI": -64.0
    },
    {
      "mac": "00:27:e3:07:b3:51",
      "RSSI": -62.0
    },
    {
      "mac": "00:27:e3:07:b3:55",
      "RSSI": -63.0
    },
    {
      "mac": "00:27:e3:07:b3:5c",
      "RSSI": -64.0
    },
    {
      "mac": "00:a3:8e:e2:3c:11",
      "RSSI": -75.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1c",
      "RSSI": -75.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1d",
      "RSSI": -75.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fe",
      "RSSI": -76.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f3",
      "RSSI": -75.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f2",
      "RSSI": -76.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fa",
      "RSSI": -76.0
    },
    {
      "mac": "00:a3:8e:e2:3c:14",
      "RSSI": -75.0
    },
    {
      "mac": "00:a3:8e:e2:3c:15",
      "RSSI": -75.0
    },
    {
      "mac": "00:27:e3:07:b3:57",
      "RSSI": -62.0
    },
    {
      "mac": "00:27:e3:07:b3:56",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:52",
      "RSSI": -67.0
    },
    {
      "mac": "00:a3:8e:e2:3c:16",
      "RSSI": -72.0
    },
    {
      "mac": "00:27:e3:07:b3:5b",
      "RSSI": -67.0
    },
    {
      "mac": "00:27:e3:07:b3:5e",
      "RSSI": -67.0
    },
    {
      "mac": "00:27:e3:07:b3:53",
      "RSSI": -67.0
    },
    {
      "mac": "00:27:e3:07:b3:5c",
      "RSSI": -67.0
    },
    {
      "mac": "00:27:e3:07:b3:5a",
      "RSSI": -68.0
    },
    {
      "mac": "00:a3:8e:e2:3c:12",
      "RSSI": -72.0
    },
    {
      "mac": "00:27:e3:07:b3:52",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:5d",
      "RSSI": -61.0
    },
    {
      "mac": "00:27:e3:07:b3:59",
      "RSSI": -61.0
    },
    {
      "mac": "3e:dc:bc:0a:62:ee",
      "RSSI": -83.0
    },
    {
      "mac": "12:e0:aa:22:15:81",
      "RSSI": -83.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:85",
      "RSSI": -83.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:87",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:17",
      "RSSI": -71.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:8d",
      "RSSI": -83.0
    },
    {
      "mac": "5c:5a:c7:29:c5:41",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:31",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:3c",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:37",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:3d",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1d",
      "RSSI": -79.0
    },
    {
      "mac": "2a:80:cf:be:25:dd",
      "RSSI": -83.0
    },
    {
      "mac": "88:11:96:e6:fd:ff",
      "RSSI": -83.0
    },
    {
      "mac": "b8:c3:85:5e:e1:dd",
      "RSSI": -83.0
    }
  ],
  "5": [
    {
      "mac": "00:a3:8e:c7:a4:fc",
      "RSSI": -70.0
    },
    {
      "mac": "00:a3:8e:e2:3c:13",
      "RSSI": -71.0
    },
    {
      "mac": "00:27:e3:07:b3:53",
      "RSSI": -67.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fb",
      "RSSI": -71.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f4",
      "RSSI": -66.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f1",
      "RSSI": -67.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fc",
      "RSSI": -67.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fd",
      "RSSI": -67.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f3",
      "RSSI": -66.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f5",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:5d",
      "RSSI": -68.0
    },
    {
      "mac": "00:27:e3:07:b3:54",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:51",
      "RSSI": -67.0
    },
    {
      "mac": "00:27:e3:07:b3:55",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:5c",
      "RSSI": -67.0
    },
    {
      "mac": "00:a3:8e:e2:3c:11",
      "RSSI": -70.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1c",
      "RSSI": -70.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1d",
      "RSSI": -71.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fe",
      "RSSI": -70.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f3",
      "RSSI": -70.0
    },
    {
      "mac": "00:a3:8e:c7:a4:f2",
      "RSSI": -71.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fa",
      "RSSI": -71.0
    },
    {
      "mac": "00:a3:8e:e2:3c:14",
      "RSSI": -70.0
    },
    {
      "mac": "00:a3:8e:e2:3c:15",
      "RSSI": -69.0
    },
    {
      "mac": "00:27:e3:07:b3:57",
      "RSSI": -62.0
    },
    {
      "mac": "00:27:e3:07:b3:56",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:52",
      "RSSI": -66.0
    },
    {
      "mac": "00:a3:8e:e2:3c:16",
      "RSSI": -70.0
    },
    {
      "mac": "00:27:e3:07:b3:5b",
      "RSSI": -65.0
    },
    {
      "mac": "00:27:e3:07:b3:5e",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:53",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:5c",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:5a",
      "RSSI": -66.0
    },
    {
      "mac": "00:a3:8e:e2:3c:12",
      "RSSI": -72.0
    },
    {
      "mac": "00:27:e3:07:b3:52",
      "RSSI": -66.0
    },
    {
      "mac": "00:27:e3:07:b3:5d",
      "RSSI": -61.0
    },
    {
      "mac": "00:27:e3:07:b3:59",
      "RSSI": -61.0
    },
    {
      "mac": "3e:dc:bc:0a:62:ee",
      "RSSI": -83.0
    },
    {
      "mac": "12:e0:aa:22:15:81",
      "RSSI": -83.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:85",
      "RSSI": -83.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:87",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:17",
      "RSSI": -71.0
    },
    {
      "mac": "5c:5a:c7:3e:e8:8d",
      "RSSI": -83.0
    },
    {
      "mac": "5c:5a:c7:29:c5:41",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:31",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:3c",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:37",
      "RSSI": -83.0
    },
    {
      "mac": "70:db:98:ee:25:3d",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:e2:3c:1d",
      "RSSI": -79.0
    },
    {
      "mac": "2a:80:cf:be:25:dd",
      "RSSI": -83.0
    },
    {
      "mac": "88:11:96:e6:fd:ff",
      "RSSI": -83.0
    },
    {
      "mac": "b8:c3:85:5e:e1:dd",
      "RSSI": -83.0
    },
    {
      "mac": "00:a3:8e:c7:a4:fd",
      "RSSI": -71.0
    },
    {
      "mac": "00:a3:8e:e2:3c:19",
      "RSSI": -79.0
    }
  ]
}
"""
zoneObj = json.loads(zoneJSON, object_hook=zoneJsonDecod)
print("After Converting JSON into Movie Object")
print(zoneObj)

# plus tard pour récupérer toutes les données de tous les fichiers
#
# for name in os.listdir("./data/"):
#     for zone in os.listdir("./data/" + name + "/zones"):
#         for position in os.listdir("./data/" + name + "/zones/" + zone):
#             with open("./data/" + name
#                       + "/zones"
#                       + "/" + zone
#                       + "/" + position, "r") as file:
#                 print(json.load(file))
