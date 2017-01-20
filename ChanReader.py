import sys
import re

from PyQt5 import *

class Channel():
    def __init__(self,name):
        self.name = name
        self.tvgname = ''
        self.url = ''
        self.logo = ''
        self.group = ''
        self.ID = ''


class ChannelReader():
    def __init__(self, filename):
        self.filename = filename
        self.channelList ={} 

    reg_logo = re.compile('tvg-logo="(.*?)"')
    reg_group = re.compile('group-title="(.*?)"')
    reg_id = re.compile('tvg-id="(.*?)"')
    reg_name = re.compile('tvg-name="(.*?)"')
    reg_channel =re.compile(',(.*)\n' )

    def readFile(self):
        readInEXT = False
        prevCHName = ''
        myFile = open(self.filename, 'r')
        for line in myFile:
            if 'EXTINF' in line:
                readInEXT = True
                res = re.search(ChannelReader.reg_channel, line)
                if res == None:
                    continue
                else:
                    print('found channel: '+ res.groups()[0]) 
                    chLogo = ''
                    chGroup = ''
                    chID = ''
                    chTvName = ''
                    chName = res.groups()[0]
                    self.channelList[chName] = Channel(chName)
                    prevCHName = chName

                    res = re.search(ChannelReader.reg_logo, line)
                    if res is not None:
                        self.channelList[chName].logo = res.groups()[0]
                        print('\t logo: ' + self.channelList[chName].logo)

                    res = re.search(ChannelReader.reg_group, line)
                    if res is not None:
                        self.channelList[chName].group = res.groups()[0]
                        print('\t group: ' + self.channelList[chName].group)

                    res = re.search(ChannelReader.reg_id, line)
                    if res is not None:
                        self.channelList[chName].ID = res.groups()[0]
                        print('\t id: ' + self.channelList[chName].ID)

                    res = re.search(ChannelReader.reg_name, line)
                    if res is not None:
                        self.channelList[chName].tvgname = res.groups()[0]
                        print('\t tvgname: ' + self.channelList[chName].tvgname)

            else:
                if readInEXT:
                    print('\t url: '+line)
                    self.channelList[prevCHName].url = line
                    prevCHName = ''

                readInEXT = False


    def getData(self):
        return self.channelList

    def printFile(self):
        for line in self.myFile:
            print(line)



