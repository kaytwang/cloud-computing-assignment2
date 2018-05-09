# Created by Yuan Wang (yuanw8)
# Cloud and Cluster Computing Assignment 2
# Semester 1, 2018

import boto
from boto.ec2.regioninfo import RegionInfo

from botofiles import config


def establish():
    my_region = RegionInfo(name=config.region(), endpoint=config.endpoint())

    conn = boto.connect_ec2(
        aws_access_key_id=config.aws_access_key_id(),
        aws_secret_access_key=config.aws_secret_access_key(),
        is_secure=True,
        region=my_region,
        port=config.port(),
        path=config.endpoint_path(),
        validate_certs=False)

    return conn


def main():
    conn = establish()
    print(conn)
    print(conn.region)



if __name__ == '__main__':
    main()
