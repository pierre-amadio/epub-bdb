#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
import pdb
from bs4 import BeautifulSoup
from jinja2 import Template,FileSystemLoader,Environment
from entry import *

file_loader = FileSystemLoader("templates")
env = Environment(loader=file_loader)

OSHLDIR=sys.argv[1]
outputDir=sys.argv[2]

xmlDic="%s/BrownDriverBriggs.xml"%OSHLDIR
#xmlDic="/home/melmoth/dev/html/index.html"
#xmlDic="./test.xml"
#xmlDic="/home/melmoth/dev/LXX/xml1/01-Gen.xml"

with open(xmlDic) as fp:
  soup=BeautifulSoup(fp, 'lxml')


data=[]

for curpart in soup.find_all("part"):
  part={}
  part["id"]=curpart['id']
  part["title"]=curpart["title"]
  part["entries"]=[]
  for cursect in curpart.find_all("section",recursive=False):
    """ print("  sect",cursect["id"]) """
    for tmpent in cursect.find_all("entry",recursive=False):
      part["entries"].append(entry(tmpent))
  data.append(part)

for p in data:
  print("#####PART %s #####"%p["title"])
  for ent in p["entries"]:
    print("__")
    print(ent.mylabel)
    print(ent.mydef)
