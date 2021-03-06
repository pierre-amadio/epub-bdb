#!/usr/bin/env python3
import copy
import re

class entry:
  def __init__(self, soupEntry):
    self.myid=None
    self.mylabel=None
    self.mytype=None
    self.mydef=[]
    self.mysense=[]
    self.mysoup=None
    self.mypos=None
    self.myasp=None
    self.rawsoup=None
    self.myoutput=None

    self.mysoup=copy.copy(soupEntry)
    self.myid=self.mysoup["id"]
    #print("--",myid)
    #print("my def=",mydef)
    #print(rawsoup.contents)
    #print("@@@@")
    #print(str(rawsoup))
    
    if "type" in self.mysoup.attrs:
      self.mytype=self.mysoup["type"]
    
    for adef in self.mysoup.find_all("def",recursive=False):
      self.mydef.append(adef.string)

    cnt=0
    for curword in self.mysoup.find_all("w",recursive=False):
      if(cnt==0):
        self.mylabel=curword.string
      cnt+=1

    if(cnt==0):
        print("Why is there no W for", myid)
        sys.exit()
    
    if len(self.mydef):
      """
        there are some def nodes, just using thoses.
      """
      self.myoutput=""
      for d in self.mydef:
        self.myoutput+="%s, "%d
      return 

    """
      no def nodes, so, what to put ?
    """
    """ may be there is a reference to another word"""
    for curword in self.mysoup.find_all("w",recursive=False):
      if curword.has_attr("src"):
        if not self.myoutput:
          self.myoutput="see "

        m=re.match("^(\w+)\.",curword["src"])
        if not m:
            print("Cannot parse",curword["src"])
            sys.exit()

        self.myoutput+="<a href=\"%s.xhtml#%s\">%s</a>"%(m.group(1),curword["src"],curword.string)

    """ still nothing...."""
    if not self.myoutput:
      self.myoutput=""
      for c in self.mysoup.stripped_strings:
        self.myoutput+=c


