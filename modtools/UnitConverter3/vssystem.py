#!python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------------
# @version: 2020-05-07 | v0.53
# @created: 2008-08-05
# @author : pyramid
# @contact: pyramid@sapo.pt
# @brief  : Provides various methods to read, write, and update .system files
#---------------------------------------------------------------------------------
#
# Vega Strike star system editor
# Copyright (C) 2008 Vega Strike team
# Contact: hellcatv@users.sourceforge.net
# Internet: http://vegastrike.sourceforge.net/
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
#---------------------------------------------------------------------------------
# Features:
# reads and writes .system files
# updates node attributes
#---------------------------------------------------------------------------------

from xml.dom.minidom import *

class VsSystem:

  def __init__(self, vsSystemFile):
    # load system file
    self.fileAddress = vsSystemFile
    print("Reading ", vsSystemFile)
    file = open(vsSystemFile)
    self.system = parse(file)   # parse an open file
    file.close()
    #print self.system.toxml() # testing

  def updateNodeAttribute(self, nodeName, attributeName, newValue):
  # updates attribute of all nodes with a given name
    nodeList = self.system.getElementsByTagName(nodeName)
    for node in nodeList:
      nodeList = node.attributes[attributeName]
      nodeList.value = newValue

  def saveSystemFile(self):
  # writes the file
    file = open(self.fileAddress, 'w')
    file.write(self.system.toxml())
    file.close()
