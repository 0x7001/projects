#!/usr/bin/env bash

if [ "$1" = "-a" ];
then
	clear && mpg123 --utf8 -o pulse -C --cpu AVX /mnt/backup/Yedek/MP3/*
	exit 0
fi

if [ "$1" = "" ];
then
	echo "-a = ALL"
	exit 1
fi
