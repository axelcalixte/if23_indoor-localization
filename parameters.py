path = "output/romain/" #do not for the / at the end of the path
rssi_csv_output = "rssi.csv"
mac_csv_output = "mac.csv"
zones_csv_output = "zones.csv"

# preparing datas :
# for removing access points :
ap_ignoring_threshold = 0.1 # 0 - 1 ; minimum occurence average that an access point need to have in zones
#if more then the value -95 will be used, if less, the access point will be removed
#threshold (0 - 1) to average when missing RSSI :
acquisition_average_threshold = 0.8 # in an acquisition within a certain position
zone_average_threshold = 0.7 # in a zone between the positions

# Machine learning :
learningRate = 5e-5 # between 0 and 1
epochs = 5000
dropout = 0.2

plot_saving_location = "plots/"
