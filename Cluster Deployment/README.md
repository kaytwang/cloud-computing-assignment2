Cluster Deployment with Boto and Ansible



The CC_assign2 is the project which is used to show the one click deployment
of a new cluster node.

The project also includes:

  - Boto file for instance creation
  - Ansible file for cluster deployment
  - CouchDB API
  - Part of the Data Harvester
  - Part of the Data processor
  - Part of the Web Server document updater

Main files Description

- ansible # contains all the yaml files for deployment
  - couchdb # installation, configuration and join cluster files
  - essentials # install all the essentials that the new vm needs
  - python # the harvester and data processing that file needed by the new node
  - main.yaml # call all the yaml files above

- botofiles # includes all that needed files to create a new instance in nectar

- CouchdbUtils # CouchDB API and some temperate files to process data
  - Connector.py # CouchDB API
  - Updater.py # Applications to update the JSON file which is needed by the WebServer

- data # all the file needed for the one click deployment demo

- host.ini # created by main.py automatically if a new instance is launched

- main.py # the entry for one click deployment, which calls both boto and ansible playbooks
