#!/bin/bash

ansible-playbook roselian.yml  -K -u deployer -i hosts --become
