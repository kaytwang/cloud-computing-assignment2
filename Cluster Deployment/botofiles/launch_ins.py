# Created by Yuan Wang (yuanw8)
# Cloud and Cluster Computing Assignment 2
# Semester 1, 2018

import time

from botofiles import config, connection

conn = connection.establish()

my_instances = set()


def create_ins():
    user_data_script = """#!/bin/bash
    echo "Hello World" >> /tmp/data.txt"""

    new_reservation = conn.run_instances(
        config.default_image_id(),
        key_name=config.default_key_name(),
        instance_type=config.default_flavour(),
        security_groups=config.default_security_groups(),
        placement=config.default_availability_zone(),
        user_data=user_data_script)

    new_instance = new_reservation.instances[0]
    conn.create_tags([new_instance.id], {"Name": config.default_instance_name()})

    while new_instance.state == u'pending':
        print('Creation status: {}'.format(new_instance.state))
        time.sleep(10)
        new_instance.update()

    print('Done. Instance {} with IP {} in zone {} is {}.'
          .format(new_instance.id, new_instance.private_ip_address, new_instance.placement, new_instance.state))

    return new_instance


def show_reservations_and_instances():
    reservations = conn.get_all_reservations()
    if len(reservations) < 1:
        print('You have no instances provisioned.')
    else:
        for res in reservations:
            print('Reservation {} has {} instances.'.format(res.id, len(res.instances)))
            for inst in res.instances:
                print('\t{} {} {} {}'.format(inst.id, inst.private_ip_address, inst.placement, inst.state))
                my_instances.add(inst.id)


def show_instances():
    instances = conn.get_only_instances()
    return instances


def main():
    print('=' * 100)
    uin = input('Launch new instance (y or n): ')
    if uin == 'y':
        create_ins()
    elif uin == 'n':
        print('Alright!')
    else:
        print('Excuse me?')

    if len(my_instances) < 1:
        exit()


if __name__ == '__main__':
    main()
