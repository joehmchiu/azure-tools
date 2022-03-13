# azure-tools
## Prerequisites
* Ubuntu / Linux - 18.04LTS or 20.04
* bash
* python 3.6.9
* az cli 
  * python3 install azure-cli
* perl 
  * cpanm install JSON
  * cpanm install Text::CSV
  * cpanm install Text::ANSITable
* jq
  * sudo apt install jq

## Install
* copy directories bin, azure, utils to system
* export PATH to the directories 

## Run
* get key vault secret as a Json array
  * ./kv.py  [ secret 2 ]  [ secret 2 ] ...
  * ./kv.py  [ '*' | all ]
* assign screts to ansible playbook
  * ansible-playbook secret-playbook.yml
