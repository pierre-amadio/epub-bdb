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
print(xmlDic)

with open(xmlDic) as fp:
  soup=BeautifulSoup(fp, 'lxml')


todo={}

for curpart in soup.find_all("part"):
  print("part",curpart['id'])
  for cursect in curpart.find_all("section",recursive=False):
    print("  sect",cursect["id"])
    for curentry in cursect.find_all("entry",recursive=False):
      a=entry(curentry)
      """pdb.run('mymodule.test()')"""
      print(a.mylabel)
      print(a.mydef)
