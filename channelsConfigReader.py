import sys
import re


class ConfigChannel():
    def __init__(self, update, site, site_id, xmltv_id):
        self.update = update
        self.site = site
        self.site_id = site_id
        self.xmltv_id = xmltv_id


class ConfigChanReader():
    def __init__(self, filename):
        self.filename = filename
        self.pattern = '<channel update="(.*)" site="(.*)" site_id="(.*)" xmltv_id="(.*)">(.*)<\/channel>'

    def getChannels(self):
        result = {}
        f = open(self.filename, 'r')
        for line in f:
            res = re.search(self.pattern,line)
            if res is not None:
                #line has a channel. get the info
                update = res.groups()[0]
                site = res.groups()[1]
                site_id = res.groups()[2]
                xmltv_id = res.groups()[3]
                name = res.groups()[4]

                curChan = ConfigChannel(update, site, site_id, xmltv_id)
                result[name] = curChan
        return result


if __name__ == "__main__":
    ccr = ConfigChanReader('/home/kons/tvtoday.de.channels.xml')
    data = ccr.getChannels()
    print(data)
