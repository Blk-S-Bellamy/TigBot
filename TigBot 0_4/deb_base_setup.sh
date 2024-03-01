#!/bin/bash

# TESTED ON DEBIAN 12

NOTES=()

# exit codes for coloring text during installation
# colors 
NC='\033[0m' # No Color
CYAN='\033[0;36m'
RED='\033[0;31m'
LPUR='\033[1;35m'
# colors, prompts
NO='\033[1;31m'
YES='\033[1;32m'
HAS='\033[1;32m'

# headers for different log outputs
check="${HAS}|░░CHECKING░░${NC}>"  
installing="${CYAN}|░░INSTALLING░░${NC}>"
skipping="${CYAN}|░░SKIPPING░░>${NC}"
satisfied="${HAS}|░░DEPENDENCY-SATISFIED░░>${NC}"
updating="${RED}|░░UPDATING...░░>${NC}"
creating="${LPUR}|░░CREATING...░░>${NC}"
loaded="${LPUR}|░░LOADED...░░>${NC}"
extracting="${LPUR}|░░EXTRACTING...░░>${NC}"

dep="python-dotenv\npy-cord\nopenai==0.28\nbs4\nrequests\nasycio"

echo "" >> setup.log
LOG="setup.log"

echo -e "${RED}Tigbot needs permission to install the following packages in a venv:\n${CYAN}${dep}${NC}"
sudo ls > /dev/null 2>&1
echo -e "${updating} ${CYAN}apt-get repositories${NC}" && sudo apt-get update >> $LOG 2>&1
echo -e "${check} ${CYAN}python3.11 (not changing PATH variables)${NC}" && DC=$(sudo apt-get install python3.11 -y) >> $LOG 2>&1
echo -e "${check} ${CYAN}python3 virt-env${NC}" && DC=$(sudo apt-get install virtualenv -y) >> $LOG 2>&1

# determine if the virt env exists already
FR=$(ls -a | grep "tigbot_pev")
if [ ${#FR} -eq 0 ]
then 
    echo -e "${creating} ${CYAN}virtual environment${NC}" && DC=$(virtualenv tigbot_pev)
else
    echo -e "${satisfied} ${CYAN}virt env \'tigbot_pev\' exists${NC}"
fi

echo -e "${loaded} ${CYAN}tigbot_pev${NC}" && source tigbot_pev/bin/activate

echo -e ${LPUR}
pip install openai==0.28
pip install bs4
pip install requests
python3 -m pip install python-dotenv
pip install asyncio
pip install py-cord
echo -e ${NC}

FR=$(ls -a | grep "jokes.db.7z")
if [ ${#FR} -gt 0 ]
then
    echo -e "${installing} ${CYAN}7zip${NC}" && sudo apt-get install p7zip >> $LOG 2>&1
    echo -e "${extracting} ${CYAN}jokes.db.7z database${NC}" && 7za x jokes.db.7z >> $LOG 2>&1
else
    echo -e "${skipping} ${CYAN} extraction of jokes.db.7z in directory, missing${NC}"
    
    FRR=$(ls -a | grep "jokes.db")
    if [ ${#FRR} -eq 0 ]
    then
        echo -e "${skipping} ${CYAN} cannot find jokes.db in directory!${NC}"
        NOTES+=("${RED}please add jokes.db in the main directory and extract it before running the bot!!${NC}\n") 
    else
        echo -e "${satisfied} ${CYAN} found jokes.db in directory${NC}"
    fi
fi

if [ ${#NOTES} -gt 1 ]
then
    echo -e "${RED}${NOTES}${NC}"
    exit
else
    echo -e "${RED} Setup complete, you can now configure the program and launch with \"python3 TigBot_run.py\"${NC}"
    exit
fi