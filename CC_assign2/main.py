# team 20
# Created by Yuan Wang (yuanw8)
# Cloud and Cluster Computing Assignment 2
# Semester 1, 2018

import configparser
import os
import shlex
import subprocess
import time

from botofiles import config, launch_ins
import boto

conn = launch_ins.conn
instances = conn.get_only_instances()
parser = configparser.ConfigParser(allow_no_value=True, delimiters=' ')


def main():
    try:
        instance = launch_ins.create_ins()
        time.sleep(5)
        print('')
    except boto.exception.EC2ResponseError:
        print('Instance existed! \n')

    for idx, inst in enumerate(instances):
        print('{}:\t{}\t{}\t{}\t{}'.format(idx, inst.id, inst.private_ip_address, inst.state, inst.placement))

    parser['targetIns'] = {instance.private_ip_address: ''}

    with open('hosts.ini', 'w') as host_file:
        parser.write(host_file)

    key_file_path = config.parser['local']['key_file_path']
    key_file = config.parser['local']['key_file']

    command_line = ' ansible-playbook'
    command_line += ' -i hosts.ini'
    command_line += ' -u ubuntu'
    command_line += ' -b --become-method=sudo'
    command_line += ' --key-file=' + os.path.join(key_file_path, key_file)
    command_line += ' ansible/main.yaml '

    print(command_line)

    args = shlex.split(command_line)
    print(args)

    time.sleep(60)

    process = subprocess.Popen(args, shell=False)
    process.communicate()


if __name__ == '__main__':
    main()
