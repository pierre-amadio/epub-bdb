#!/usr/bin/env python3
import copy

class entry:
  myid=None
  mytype=None
  mydef=[]
  mysense=[]
  mysoup=None
  mypos=None
  myasp=None
  rawsoup=None

  def __init__(self, soupEntry):
    rawsoup=copy.copy(soupEntry)
    myid=rawsoup["id"]
    print("my id",myid)
    print("--")
    print(rawsoup.contents)
    print("@@@@")
    print(str(rawsoup))
    
    if "type" in rawsoup.attrs:
      mytype=rawsoup["type"]
    
    for adef in rawsoup.find_all("def",recursive=False):
      print(adef)

    for curword in rawsoup.find_all("w",recursive=False):
      print(curword)
