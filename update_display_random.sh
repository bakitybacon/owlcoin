#!/bin/bash
echo $RANDOM >~/balance.txt
python ~/adafruitdisplay.py <~/balance.txt
