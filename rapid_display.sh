#!/bin/bash
for i in `seq 1 10`;
do
	echo $RANDOM >~/rapidbalance.txt
	python ~/adafruitdisplay.py <~/rapidbalance.txt
	sleep 1
done
