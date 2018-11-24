#!/bin/bash
f1 = open("/home/quynh/OutputOfCommand/test","r")
f2 = open("/home/quynh/OutputOfCommand/test.txt","r")
for line2 in f2
for line1 in f1
if [ $line1 == $line2 ]
then
echo "Success"
else
echo "False"
fi
