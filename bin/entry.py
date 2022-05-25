#!/usr/bin/env python3
import copy

class entry:
  def __init__(self, soupEntry):
    myid=None
    mylabel=None
    mytype=None
    mydef=[]
    mysense=[]
    mysoup=None
    mypos=None
    myasp=None
    rawsoup=None

    rawsoup=copy.copy(soupEntry)
    myid=rawsoup["id"]
    #print("--",myid)
    #print("my def=",mydef)
    #print(rawsoup.contents)
    #print("@@@@")
    #print(str(rawsoup))
    
    if "type" in rawsoup.attrs:
      self.mytype=rawsoup["type"]
    
    for adef in rawsoup.find_all("def",recursive=False):
      mydef.append(adef.contents)

    cnt=0
    for curword in rawsoup.find_all("w",recursive=False):
      if(cnt==0):
        mylabel=curword.contents
      cnt+=1

    if(cnt==0):
        print("Why is there no W for", myid)
        sys.exit()
    
