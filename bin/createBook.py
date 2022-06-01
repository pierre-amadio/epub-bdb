#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
import pdb
from bs4 import BeautifulSoup
from jinja2 import Template,FileSystemLoader,Environment
from entry import *

def escapeall(s):
  import htmlentitydefs
  for k, v in htmlentitydefs.items():
    s = string.replace(s, v, '&' + k)
  return s

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
    print("  sect",cursect["id"]) 
    for tmpent in cursect.find_all("entry",recursive=False):
      part["entries"].append(entry(tmpent))
  data.append(part)

for p in data:
  print("#####PART %s #####"%p["title"])
  for ent in p["entries"]:
    print("__")
    print(ent.mylabel)
    print(ent.mydef)
    """
    if(len(ent.mydef)==0):
      print(ent.mysoup)
    """

  partTemplate=env.get_template("part.xhtml")
  partOutput=partTemplate.render(part=p)
  fileOutput="%s/%s.xhtml"%(outputDir,p["id"])
  with open(fileOutput,"w") as f:
    f.write(partOutput)


