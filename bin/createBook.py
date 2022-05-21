#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
from bs4 import BeautifulSoup
from jinja2 import Template,FileSystemLoader,Environment

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

OSHLDIR=sys.argv[1]
outputDir=sys.argv[2]

xmlDic="%s/BrownDriverBriggs.xml"%OSHLDIR
#xmlDic="/home/melmoth/dev/html/index.html"
#xmlDic="./test.xml"
#xmlDic="/home/melmoth/dev/LXX/xml1/01-Gen.xml"
print(xmlDic)

with open(xmlDic) as fp:
  soup=BeautifulSoup(fp, 'lxml')

for node in soup.find_all("part"):
  print("##################################")
  print(node["id"],node["title"])
  for entry in node.find_all("entry"):
    cnt=0
    word=entry.find("w")
    print("cnt=%s"%word)
    if(len(entry.find_all("w"))!=1):
      print("LEN=",len(entry.find_all("w")))
    else:
      print(entry)


