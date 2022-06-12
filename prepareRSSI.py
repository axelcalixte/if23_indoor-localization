import json
import numpy as np
import pandas as pd
import os
import parameters as param

class RssiDatas:
    """Class for importing, formating, store and export RSSI values measured
    with relative access points (MAC) and zones"""

    def __init__(self):
        #super(RssiDatas, self).__init__()
        self.rssi = []
        self.mac = []
        self.position_changes = []

        self.file_path = "output/romain/h106.json" #temporary for test


    # list the mac in all zones to create a consistent index in all rssi array
    def listMac(self):
        self.mac = []
        for zone_file in os.listdir(param.path):
            # Opening JSON file
            f = open(param.path + zone_file)

            # returns JSON object as a dictionary
            data = json.load(f)
            for position in data:
                i_acquisition = -1
                for acquisition in data[position]:
                    i_acquisition += 1
                    n_access_points = len(data[position][i_acquisition])
                    for i_access_point in range(n_access_points):
                        i_mac = data[position][i_acquisition][i_access_point]['mac']
                        #check if mac address is already known :
                        if not i_mac in self.mac:
                            self.mac.append(i_mac) #if not, add it in the mac array



    def importRssiValues(self, zone_file_path):
        self.position_changes = [0] # acquisition numbers corresponding to a change of position

        # Opening JSON file
        f = open(zone_file_path)

        # returns JSON object as a dictionary
        data = json.load(f)

        #print("number of positions : ",len(data))
        #print("number of acquisitions (first acquisition) : ",len(data['output4']))
        #print("number of RSSI detected (first acquisition) : ",len(data['output4'][0]))
        #print("mac and RSSI (first acquisition) : ",len(data['output4'][0][0]))

        #compute the number of acquisitions (and saving the position changes) :
        n_acquisition = 0
        i_position = -1
        for position in data:
            i_position += 1
            n_acquisition += len(data[position])
            self.position_changes.append(n_acquisition)

        #print(self.position_changes)
        n_mac = len(self.mac)
        #print("number of acquisition : ", n_acquisition)
        #print("number of access points (mac) detected : ", n_mac)

        #initialize the array with all the rssi values :
        self.rssi = np.zeros([n_acquisition, n_mac])

        #print(data['output4'][1])

        acquisition_index_for_rssi_array = -1
        i_position = -1
        for position in data:
            i_acquisition = -1
            i_position += 1
            #print("\n",i_position)
            for acquisition in data[position]:
                i_acquisition += 1
                acquisition_index_for_rssi_array += 1
                n_access_points = len(data[position][i_acquisition])
                #print("\n",i_acquisition)
                #print(n_access_points)
                #print(len(data[position][i_acquisition]))
                for i_access_point in range(n_access_points):
                    #print("\n",i_access_point)
                    i_mac = data[position][i_acquisition][i_access_point]['mac']
                    #print("mac : ",self.mac)
                    i_rssi = data[position][i_acquisition][i_access_point]['RSSI']
                    #print("RSSI : ",m_rssi)
                    #print(data[position][i_acquisition][i_access_point])
                    #add the RSSI value in the rssi array :
                    #print(self.mac.index(i_mac))
                    self.rssi[acquisition_index_for_rssi_array, self.mac.index(i_mac)] = i_rssi

    def correctDataWithinPosition(self):
        # average within a position :
        # for each access point
        for access_point in range(len(self.mac)):
            #for each position :
            for position in range(len(self.position_changes) - 1) :
                number_of_zeros = 0
                number_of_acquisitions = self.position_changes[position + 1] - self.position_changes[position]
                #print(self.position_changes[position])
                # computing the number of 0 for the position
                for acquisition in range(number_of_acquisitions):
                    #print(self.position_changes[position] + acquisition)
                    if self.rssi[self.position_changes[position] + acquisition, access_point] == 0: #if rssi = 0 aka not detected
                        #print(self.position_changes[position] + acquisition, access_point) # print the indexs of the RSSI
                        number_of_zeros += 1
                #print(number_of_zeros)
                #print(number_of_acquisitions)
                if number_of_zeros/number_of_acquisitions <= 1.000000000000001 - param.acquisition_average_threshold:
                    #the number of zeros is low enough to fill the value of rssi with the average
                    #computing the average :
                    rssi_acquisition_values = self.rssi[self.position_changes[position]:self.position_changes[position + 1], access_point]
                    rssi_acquisition_values = rssi_acquisition_values[rssi_acquisition_values != 0]
                    average_value = np.average(rssi_acquisition_values)
                    #print(rssi_acquisition_values)
                    for acquisition in range(number_of_acquisitions):
                        if self.rssi[self.position_changes[position] + acquisition, access_point] == 0: #if rssi = 0 aka not detected
                            self.rssi[self.position_changes[position] + acquisition, access_point] = average_value


    # average within zone :
    def correctDataWithinZone(self):
        # for each access point
        number_of_acquisitions = self.position_changes[-1] # self.position_changes[-1] correspond to the number of acquisitions
        for access_point in range(len(self.mac)):
            number_of_zeros = 0
            for acquisition in range(number_of_acquisitions):
                if self.rssi[acquisition, access_point] == 0: #if rssi = 0 aka not detected
                    number_of_zeros += 1
            if number_of_zeros == 0:
                pass # nothing to do as each rssi value in the array is filled
            elif number_of_zeros/number_of_acquisitions <= 1.000000000000001 - param.zone_average_threshold:
                #the average will be used to complete
                #computing the average :
                rssi_acquisition_values = self.rssi[:, access_point]
                rssi_acquisition_values = rssi_acquisition_values[rssi_acquisition_values != 0]
                average_value = np.average(rssi_acquisition_values)
                for acquisition in range(number_of_acquisitions):
                    if self.rssi[acquisition, access_point] == 0: #if rssi = 0 aka not detected
                        self.rssi[acquisition, access_point] = average_value

    def correctDataByDeletingMac(self):
        access_point_to_delete = []
        number_of_acquisitions = self.position_changes[-1] # self.position_changes[-1] correspond to the number of acquisitions
        # for each access point
        for access_point in range(len(self.mac)):
            number_of_zeros = 0
            for acquisition in range(number_of_acquisitions):
                if self.rssi[acquisition, access_point] == 0: #if rssi = 0 aka not detected
                    number_of_zeros += 1
            if number_of_zeros == 0:
                pass # nothing to do as each rssi value in the array is filled
            elif number_of_zeros/number_of_acquisitions <= 1.000000000000001 - param.ap_ignoring_threshold: # a deplacer pour toutes les zones
                #filling the RSSI value with -95 as it's not detected and we suppose the access point is too far
                for acquisition in range(number_of_acquisitions):
                    if self.rssi[acquisition, access_point] == 0: #if rssi = 0 aka not detected
                        self.rssi[acquisition, access_point] = -95
            else:
                #delete the access point with not enough measures
                #print("this access point will be deleted : ", rssi[:, access_point])
                access_point_to_delete.append(access_point)
                #self.rssi = np.delete(self.rssi, access_point, 1)
        print(len(access_point_to_delete), "access point will be deleted")
        print(np.shape(self.rssi))
        self.rssi = np.delete(self.rssi, access_point_to_delete, 1)
        print(np.shape(self.rssi))
