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
    print(soupEntry["id"])
    rawsoup=copy.copy(soupEntry)
