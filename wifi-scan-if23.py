import subprocess
import time
import json
import re
import os


# Regexes
p = re.compile("^BSS ")
wlan_regex = re.compile("^w.*$")

# Constants
NB_OF_ACQUISITIONS = 5
WAITING_TIME = 3


def get_interface_name():
    """Gets the system's interface name on a GNU/Linux OS """

    for interface_name in os.listdir("/sys/class/net"):
        if wlan_regex.match(interface_name) is not None:
            return interface_name


def get_acquisitions():
    """Returns array of dictionary entries, each one corresponding
     to an AP
     """

    result = subprocess.run(["iw", "dev", get_interface_name(),
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


def retrieve_data(dict, iter):
    """Aggregate data into the dict"""

    print(f"_Wi-Fi networks scan n°{iter} (requires admin privileges)_")
    for i in range(1, NB_OF_ACQUISITIONS+1):
        dict[str(i)] = get_acquisitions()
        # time to wait before starting a new acquisition
        # we try to take into account Wi-Fi signal waves variance
        time.sleep(WAITING_TIME)


def write_to_file(dict, iter):
    """Writing as json the retrieved data"""

    if os.path.exists("./data") is True:
        with open("./data/output" + str(iter) + ".json", "w") as dump:
            json.dump(dict, dump, indent=2)
    print("### Dumped results in ./data/output" + str(iter) + ".json")


iteration = 1
output = {}
while True:
    retrieve_data(output, iteration)
    write_to_file(output, iteration)

    test = input("""If the acquisition failed, enter 'retry' at the prompt.
    Change zone now ? Or end the experience by typing 'end' : """)
    if test == "end":
        break
    elif test == "retry":
        pass
    else:
        # We are not quitting
        iteration += 1
