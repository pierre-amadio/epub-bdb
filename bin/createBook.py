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
toc=[]

for curpart in soup.find_all("part"):
  part={}
  tocpart={}
  
  part["id"]=curpart['id']
  part["title"]=curpart["title"]
  part["entries"]=[]

  tocpart["mylabel"]=curpart["title"]
  tocpart["file"]="Files/%s.xhtml"%curpart["id"]
  tocpart["myitems"]=[]
  tocitemcnt=0
  toccuritem={}

  for cursect in curpart.find_all("section",recursive=False):
    """ print("  sect",cursect["id"]) """
    for tmpent in cursect.find_all("entry",recursive=False):
      newentry=entry(tmpent)
      part["entries"].append(newentry)
      if tocitemcnt==0:
        toccuritem={}
        toccuritem["startid"]=newentry.myid
        toccuritem["startlabel"]=newentry.mylabel
      if tocitemcnt==50:
        toccuritem["endlabel"]=newentry.mylabel
        tocpart["myitems"].append(toccuritem)
        tocitemcnt=-1
      tocitemcnt+=1
        
  data.append(part)
  if not tocpart["myitems"]:
      """
      vav vav vav...
      emptyitem={}
      emptyitem["startid"]=""
      emptyitem["startlabel"]=""
      emptyitem["endlabel"]=""
      tocpart["myitems"].append(emptyitem)
      """
      tocpart["myitems"]=[]
  else:
      toc.append(tocpart)

for p in data:
  for ent in p["entries"]:
    if(not ent.myoutput):
      print(ent.mysoup)

  partTemplate=env.get_template("part.xhtml")
  partOutput=partTemplate.render(part=p)
  fileOutput="%s/%s.xhtml"%(outputDir,p["id"])
  with open(fileOutput,"w") as f:
    f.write(partOutput)

tocTemplate=env.get_template("TOC.xhtml")
tocOutput=tocTemplate.render(book=toc)
fileOutput="%s/TOC.xhtml"%outputDir
with open(fileOutput,"w") as f:
    f.write(tocOutput)

navTemplate=env.get_template("nav.xhtml")
navOutput=navTemplate.render(toc=toc)
fileOutput="nav.txt"
with open(fileOutput,"w") as f:
    f.write(navOutput)
