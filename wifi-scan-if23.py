import subprocess
import time
import json
import re


p = re.compile("^BSS ")


def get_acquisitions():
    """Returns array of dictionary entries, each one corresponding
     to an AP """

    result = subprocess.run(["sudo", "iw", "dev", "wlan0",
                            "scan"], stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8").split("\n")

    signals = []
    addr = []
    for line in output:
        if line.find("signal: ") != -1:
            signals.append(float(line.split(" ")[1]))
        if p.match(line) is not None:
            # could be optimized by a better regex
            addr.append(line.split(" ")[1].split("(")[0])

    acquisitions = []
    for line in zip(addr, signals):
        dict = {"mac": line[0], "RSSI": line[1]}
        acquisitions.append(dict)

    return acquisitions


print("### Scanning for Wi-Fi networks requires admin privileges")
dict = {}
# number of acquisitions to get inside the range call
for i in range(5):
    dict[str(i)] = get_acquisitions()
    # time to wait before starting a new acquisition
    # we try to take into account Wi-Fi signal waves variance
    time.sleep(3)

print("### Dumping results in a file")
with open("if23-feature.json", "w") as file:
    json.dump(dict, file, indent=2)
