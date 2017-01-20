import sys
import gzip
import xml.etree.ElementTree as ET

class EPGReader():
    def __init__(self, filename):
        self.filename = filename

    def getChannelNames(self):
        result = {}
        file_content = ''
        with gzip.open(self.filename, 'r') as f:
            file_content = f.read()

        root = ET.fromstring(file_content)
        channels = root.findall('channel')
        for channel in channels:
            chID = channel.attrib['id']
            chName = channel.find('display-name').text
            result[chID] = chName

        return result


if __name__ == "__main__":
    er = EPGReader('/home/kons/guideGer.xml.gz')
    er.getChannelNames()
