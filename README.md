# azure-tools
## Prerequisites
* Azure keyvault
* add a secret to keyvault: helloworld: kAGNihurXfZEPXVBRTXR037Ls9z8fg5tcMqmHjiqJWg=
* Ubuntu / Linux - 18.04LTS or 20.04
* bash
* python 3.6.9
* ansible 2.9.x
* az cli 
  * python3 install azure-cli
* perl 
  * cpanm install JSON
  * cpanm install Text::CSV
  * cpanm install Text::ANSITable
* jq
  * sudo apt install jq
* update the keyvault name in the utility conf class. 
  * edit utils/u.py

## Install
* copy directories bin, azure to system
  * cp -rf azure ~/. (optional)
  * cp -rf bin ~/. (optional)
* export PATH to the directories 
  * export PATH="$PATH:~/bin" (optional)
  * export PATH="$PATH:~/azure" (optional)

## Run
* update the name of Azure key vault in the u.py conf callse
  * kvn = "name of keyvault" # the existing key vault name in azure
* get key vault secret as a Json array
  * ./kv.py  [ secret 2 ]  [ secret 2 ] ...
  * ./kv.py  [ '*' | all ]
* assign screts to ansible playbook
  * ansible-playbook secret-playbook.yml
