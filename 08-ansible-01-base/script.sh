#!/bin/bash

sudo docker start fedora37 ubuntu centos7
sudo ansible-playbook --ask-vault-pass -i ./playbook/inventory/prod.yml ./playbook/site.yml
sudo docker stop fedora37 ubuntu centos7
