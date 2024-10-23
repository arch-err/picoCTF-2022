#!/usr/bin/env bash
#!CMD: ./solve.sh
HOST="http://saturn.picoctf.net:55521/"

curl ${HOST} -ks | grep -Po "picoCTF{.*}"
