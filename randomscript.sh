#!/bin/bash

if [[ -s /tmp/xx_x__x.log  ]]
then 
        printf "\n\n%s\n\n\n" true > /tmp/sizelog.log
else 
        printf "\n\n%s\n\n\n" false > /tmp/sizelog.log
fi
