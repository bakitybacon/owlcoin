#!/bin/bash
/usr/local/bin/comradecoind getbalance >~/balance.txt 2>~/error.txt
if [[ -s ~/error.txt ]] #checks if there are any contents in the file
then
  read msg <~/error.txt
  if [[ "$msg" = "error: couldn't connect to server" ]]
  then
    /usr/local/bin/comradecoind
    printf "starting up..." | python ~/adafruitdisplay.py
    python ~/advancedleds.py 60 noblink
  else
    python ~/adafruitdisplay.py <~/error.txt
    python ~/advancedleds.py 60 blink
  fi
else
  python ~/adafruitdisplay.py <~/balance.txt
fi
