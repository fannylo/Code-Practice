#!/bin/bash

#grep '<Name>' sh3-getDevice.20201203.txt > test.csv #擷取有<Name>的那一行
#sed 's/^[ \t]*//g' test.csv > test2.txt #去除<Name>前面的空格
#cut -b 7- test2.txt > test3.txt #擷取<Name>之後的字串
#sed 's/........$//' test3.txt > test4.csv #去除</Name>

#grep '<Name>' sh3-getDevice.20201203.txt | sed 's/^[ \t]*//g' | cut -b 7- | sed 's/........$//' > final.csv

grep '<Name>' sh3-getDevice.20201203.txt | sed 's/<Name>//g' | sed 's/<\/Name>//g' | sed 's/[[:space:]]//g' > final.csv

#sed s/[[:space:]]//g #去除全部空格
#sed 's/(.*)//' #去除()以及()中的字串
#sed 's/\[.*\]//' #去除[]以及[]中的字串

sed s/[[:space:]]//g check_item.csv | sed 's/(.*)//' | sed 's/\[.*\]//' > check_item2.csv

python check.py check_item2.csv final.csv out.csv
