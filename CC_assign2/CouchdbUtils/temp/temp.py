# Created by Yuan Wang (yuanw8)
# Cloud and Cluster Computing Assignment 2
# Semester 1, 2018

from Connector import Connector
from DataProcessor import DataProcessor

dp = DataProcessor()

with open('twitterdocs504.json', 'r') as tw:
    with open('504target.json', 'w') as w:
        for line in tw:
            target_info = dp.get_geo_twi_target_info(line)
            if target_info is not None:
                w.write(target_info)
                w.write('\n')
                print(target_info)
