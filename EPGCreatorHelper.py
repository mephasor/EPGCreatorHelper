# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design3.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os.path

import ChanReader
from ChanReader import Channel

import EPGReader
import channelsConfigReader as ccr
from channelsConfigReader import ConfigChannel

def log(msg):
    print('LOG: '+msg)


class Ui_Form(object):
    def __init__(self):
        super().__init__()
        self.fileList = []
        self.channelData = {}
        self.epgData = {}
        self.groups = []
        self.channelConfigData = {}
        self.configsToExport = []
        self.hiddenGroups = []


    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 600)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setObjectName("mainLayout")
        self.listLayout = QtWidgets.QVBoxLayout()
        self.listLayout.setObjectName("listLayout")
        self.channelListLabel = QtWidgets.QLabel(Form)
        self.channelListLabel.setObjectName("channelListLabel")
        self.listLayout.addWidget(self.channelListLabel)
        self.chanListLayout = QtWidgets.QHBoxLayout()
        self.chanListLayout.setObjectName("chanListLayout")
        self.chListList = QtWidgets.QListWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chListList.sizePolicy().hasHeightForWidth())
        self.chListList.setSizePolicy(sizePolicy)
        self.chListList.setMinimumSize(QtCore.QSize(800, 5))
        self.chListList.setObjectName("chListList")
        self.chanListLayout.addWidget(self.chListList)
        self.chanLIstButtonLayout = QtWidgets.QVBoxLayout()
        self.chanLIstButtonLayout.setObjectName("chanLIstButtonLayout")
        self.addCHButton = QtWidgets.QPushButton(Form)
        self.addCHButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.addCHButton.setObjectName("addCHButton")
        self.chanLIstButtonLayout.addWidget(self.addCHButton)
        self.removeCHButton = QtWidgets.QPushButton(Form)
        self.removeCHButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.removeCHButton.setObjectName("removeCHButton")
        self.chanLIstButtonLayout.addWidget(self.removeCHButton)
        self.chanListLayout.addLayout(self.chanLIstButtonLayout)
        self.listLayout.addLayout(self.chanListLayout)
        self.epgListLabel = QtWidgets.QLabel(Form)
        self.epgListLabel.setObjectName("epgListLabel")
        self.listLayout.addWidget(self.epgListLabel)
        self.epgListLayout = QtWidgets.QHBoxLayout()
        self.epgListLayout.setObjectName("epgListLayout")
        self.epgLine = QtWidgets.QLineEdit(Form)
        self.epgLine.setObjectName("epgLine")
        self.epgListLayout.addWidget(self.epgLine)
        self.epgButton = QtWidgets.QPushButton(Form)
        self.epgButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.epgButton.setObjectName("epgButton")
        self.epgListLayout.addWidget(self.epgButton)
        self.listLayout.addLayout(self.epgListLayout)
        self.mainLayout.addLayout(self.listLayout)
        self.configListLayout = QtWidgets.QHBoxLayout()
        self.configListLayout.setObjectName("configListLayout")
        self.configInPathEdit = QtWidgets.QLineEdit(Form)
        self.configInPathEdit.setReadOnly(True)
        self.configInPathEdit.setObjectName("configInPathEdit")
        self.configListLayout.addWidget(self.configInPathEdit)
        self.configOpenButton = QtWidgets.QPushButton(Form)
        self.configOpenButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.configOpenButton.setObjectName("configOpenButton")
        self.configListLayout.addWidget(self.configOpenButton)
        self.mainLayout.addLayout(self.configListLayout)
        self.separatorLine = QtWidgets.QFrame(Form)
        self.separatorLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.separatorLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separatorLine.setObjectName("separatorLine")
        self.mainLayout.addWidget(self.separatorLine)
        self.columnsLayout = QtWidgets.QVBoxLayout()
        self.columnsLayout.setObjectName("columnsLayout")
        self.columnHeadersLayout = QtWidgets.QHBoxLayout()
        self.columnHeadersLayout.setObjectName("columnHeadersLayout")
        self.groupLayout = QtWidgets.QHBoxLayout()
        self.groupLayout.setObjectName("groupLayout")
        self.groupHeader = QtWidgets.QLabel(Form)
        self.groupHeader.setObjectName("groupHeader")
        self.groupLayout.addWidget(self.groupHeader)
        self.grHideButton = QtWidgets.QPushButton(Form)
        self.grHideButton.setObjectName("grHideButton")
        self.groupLayout.addWidget(self.grHideButton)
        self.columnHeadersLayout.addLayout(self.groupLayout)
        self.channelColumnLayout = QtWidgets.QHBoxLayout()
        self.channelColumnLayout.setObjectName("channelColumnLayout")
        self.channelHeader = QtWidgets.QLabel(Form)
        self.channelHeader.setObjectName("channelHeader")
        self.channelColumnLayout.addWidget(self.channelHeader)
        self.columnHeadersLayout.addLayout(self.channelColumnLayout)
        self.epgHeaderLayout = QtWidgets.QHBoxLayout()
        self.epgHeaderLayout.setObjectName("epgHeaderLayout")
        self.epgHeader = QtWidgets.QLabel(Form)
        self.epgHeader.setObjectName("epgHeader")
        self.epgHeaderLayout.addWidget(self.epgHeader)
        self.columnHeadersLayout.addLayout(self.epgHeaderLayout)
        self.configHeaderLayout = QtWidgets.QHBoxLayout()
        self.configHeaderLayout.setObjectName("configHeaderLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.configHeaderLayout.addWidget(self.label)
        self.columnHeadersLayout.addLayout(self.configHeaderLayout)
        self.columnsLayout.addLayout(self.columnHeadersLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupView = QtWidgets.QListWidget(Form)
        self.groupView.setObjectName("groupView")
        self.horizontalLayout.addWidget(self.groupView)
        self.channelView = QtWidgets.QListWidget(Form)
        self.channelView.setObjectName("channelView")
        self.horizontalLayout.addWidget(self.channelView)
        self.epgView = QtWidgets.QListWidget(Form)
        self.epgView.setObjectName("epgView")
        self.horizontalLayout.addWidget(self.epgView)
        self.configView = QtWidgets.QListWidget(Form)
        self.configView.setEnabled(True)
        self.configView.setObjectName("configView")
        self.horizontalLayout.addWidget(self.configView)
        self.columnsLayout.addLayout(self.horizontalLayout)
        self.mainLayout.addLayout(self.columnsLayout)
        self.verticalLayout_2.addLayout(self.mainLayout)
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.exportLayout = QtWidgets.QVBoxLayout()
        self.exportLayout.setObjectName("exportLayout")
        self.exportPathsLayout = QtWidgets.QFormLayout()
        self.exportPathsLayout.setObjectName("exportPathsLayout")
        self.cfgExportLabel = QtWidgets.QLabel(Form)
        self.cfgExportLabel.setObjectName("cfgExportLabel")
        self.exportPathsLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.cfgExportLabel)
        self.m3uExportLabel = QtWidgets.QLabel(Form)
        self.m3uExportLabel.setObjectName("m3uExportLabel")
        self.exportPathsLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.m3uExportLabel)
        self.m3uExportEdit = QtWidgets.QLineEdit(Form)
        self.m3uExportEdit.setReadOnly(True)
        self.m3uExportEdit.setObjectName("m3uExportEdit")
        self.exportPathsLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.m3uExportEdit)
        self.configPathEdit = QtWidgets.QLineEdit(Form)
        self.configPathEdit.setReadOnly(True)
        self.configPathEdit.setObjectName("configPathEdit")
        self.exportPathsLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.configPathEdit)
        self.exportLayout.addLayout(self.exportPathsLayout)
        self.exportButtonLayout = QtWidgets.QHBoxLayout()
        self.exportButtonLayout.setObjectName("exportButtonLayout")
        self.chListExportButton = QtWidgets.QPushButton(Form)
        self.chListExportButton.setObjectName("chListExportButton")
        self.exportButtonLayout.addWidget(self.chListExportButton)
        self.configExPathButton = QtWidgets.QPushButton(Form)
        self.configExPathButton.setObjectName("configExPathButton")
        self.exportButtonLayout.addWidget(self.configExPathButton)
        self.saveButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.exportButtonLayout.addWidget(self.saveButton)
        self.exportLayout.addLayout(self.exportButtonLayout)
        self.verticalLayout_2.addLayout(self.exportLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.channelListLabel.setText(_translate("Form", "Channel Lists"))
        self.addCHButton.setText(_translate("Form", "+"))
        self.removeCHButton.setText(_translate("Form", "-"))
        self.epgListLabel.setText(_translate("Form", "EPG"))
        self.epgButton.setText(_translate("Form", "FILE"))
        self.configOpenButton.setText(_translate("Form", "CFG"))
        self.groupHeader.setText(_translate("Form", "Group"))
        self.grHideButton.setText(_translate("Form", "(Un)Hide"))
        self.channelHeader.setText(_translate("Form", "Channel"))
        self.epgHeader.setText(_translate("Form", "EPG"))
        self.label.setText(_translate("Form", "Config"))
        self.cfgExportLabel.setText(_translate("Form", "Config Export path:"))
        self.m3uExportLabel.setText(_translate("Form", "M3U Export path:"))
        self.chListExportButton.setText(_translate("Form", "M3U Export Location"))
        self.configExPathButton.setText(_translate("Form", "Config Export Location"))
        self.saveButton.setText(_translate("Form", "Export NOW!"))

## KONS
        self.addCHButton.clicked.connect(self.addCHButtonClicked)
        self.removeCHButton.clicked.connect(self.removeCHButtonClicked)
        self.epgButton.clicked.connect(self.openEPGFile)
        self.configOpenButton.clicked.connect(self.configOpenButtonClicked)
        self.groupView.itemSelectionChanged.connect(self.groupItemClicked)
        self.channelView.itemSelectionChanged.connect(self.channelSelectionHandler)
        self.epgView.itemSelectionChanged.connect(self.epgSelectHandler)
        self.configView.itemSelectionChanged.connect(self.configViewHandler)
        self.saveButton.clicked.connect(self.saveChangesToFile)
        self.configExPathButton.clicked.connect(self.configExPathButtonClicked)
        self.grHideButton.clicked.connect(self.grHideButtonClicked)

        if self.m3uExportEdit.text() == '':
            self.m3uExportEdit.setText('channelExport.m3u')

        if self.configPathEdit.text() == '':
            self.configPathEdit.setText('my.channels.xml')

    def grHideButtonClicked(self):
        #What group if any
        items = self.groupView.selectedIndexes()
        if len(items) < 1:
            return
        grName = items[0].data()
        # assume that hiding everything is an accident
        # TODO: change it to actually unhide/hide everything
        if grName == '(all)':
            if len(self.hiddenGroups) != self.groupView.count():
                log('hide all')
                for row in range(self.groupView.count()):
                    current = self.groupView.item(row).text()
                    if current not in self.hiddenGroups:
                        self.hiddenGroups.append(current)
                        self.groupView.item(row).setForeground(QColor(210,210,210))
            else:
                for row in range(self.groupView.count()):
                    current = self.groupView.item(row).text()
                    self.hiddenGroups.remove(current)
                    self.groupView.item(row).setForeground(QColor(0,0,0))

        else:
            row = items[0].row()
            if grName not in self.hiddenGroups:
                self.hiddenGroups.append(grName)
                self.groupView.item(row).setForeground(QColor(210,210,210))
            else:
                self.hiddenGroups.remove(grName)
                self.groupView.item(row).setForeground(QColor(0,0,0))
        self.scanAllVisibleForEPG()


    def configViewHandler(self):
        curChannel = self.channelView.selectedItems()
        if len(curChannel) == 0:
            return

        curChannel = curChannel[0].text()
        #remember config
        curCItem = self.configView.selectedItems()
        if len(curCItem) > 0:
            conf = curCItem[0].text()
            if conf not in self.configsToExport:
                log('Adding to remember: '+conf)
                self.configsToExport.append(conf)

        #change tvgid and name of channel
            self.channelData[curChannel].ID = self.channelConfigData[conf].xmltv_id
            log('changing tvid from '+self.channelData[curChannel].ID+' to '+
                self.channelConfigData[conf].xmltv_id)

        #should an existing epg have been selected, unselect it
            curEPG = self.epgView.selectedItems()
            if len(curEPG) > 0:
                self.epgView.clearSelection()

            self.scanAllVisibleForEPG()


    def refreshConfigChannels(self):
        self.configView.clear()
        for name in sorted(self.channelConfigData):
            self.configView.addItem(name)

    def configOpenButtonClicked(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None,'open stuff', '/home/kons', 'ChannelsFile (*.channels.xml)')[0]
        myCCR = ccr.ConfigChanReader(fileName)
        self.channelConfigData = myCCR.getChannels()
        self.refreshConfigChannels()


    def configExPathButtonClicked(self):
        log('Change of config file export path')
        fileName = QtWidgets.QFileDialog.getOpenFileName(None,'open stuff', '/home/kons', 'bla (*.m3u)')[0]
        if fileName != '':
            print('Selected channel file: '+fileName)
            self.chListList.addItem(fileName)
            self.readChannelLists()
            self.scanAllVisibleForEPG()




    def epgSelectHandler(self):
        epgSelected = ''
        einx = self.epgView.selectedIndexes()
        if len(einx) > 0:
            epgSelected = einx[0].data()
        else:
            return

        curChannel = ''
        inx = self.channelView.selectedIndexes()
        if len(inx) > 0:
            curChannel = inx[0].data()
        else:
            #channel not selected
            return
        if self.channelData[curChannel].ID != epgSelected:
            self.channelData[curChannel].ID = epgSelected



    def getConfigRow(self, curSelection):
        if self.channelData[curSelection].ID != '':
            curSelection = self.channelData[curSelection].ID
        else:
            curSelection = self.channelData[curSelection].name

        for row in range(self.configView.count()):
            text = self.configView.item(row).text()
            config_id = self.channelConfigData[text].xmltv_id

            if curSelection == config_id:
                return row


        return -1

    def channelSelectionHandler(self):
        self.epgView.clearSelection()
        self.configView.clearSelection()
        curSelection = ''
        selection = self.channelView.selectedIndexes()
        if len(selection) > 0:
            curSelection = selection[0].data()
        else:
            return
        print('you clicked channel: '+ curSelection)
        row = self.findEPG(curSelection)
        if row > 0:
            self.epgView.setCurrentRow(row)
            return

        if self.isInConfigRememberList(curSelection):
            row = self.getConfigRow(curSelection)
            self.configView.setCurrentRow(row)


    def findEPG(self, curSelection):
        # check if tvg-id is present
        if self.channelData[curSelection].ID != '':
            curSelection = self.channelData[curSelection].ID
        else:
            curSelection = self.channelData[curSelection].name

        for row in range(self.epgView.count()):
            chName = self.epgView.item(row).text()
            chID = None
            for key in self.epgData:
                if self.epgData[key] == chName:
                    chID = key
                    myRow = row
                    break

            if chID == curSelection:
                return myRow
        return -1


    def isInConfigRememberList(self,curSelection):
        if self.channelData[curSelection].ID != '':
            curSelection = self.channelData[curSelection].ID
        else:
            curSelection = self.channelData[curSelection].name

        for entry in self.configsToExport:
            idName = self.channelConfigData[entry].xmltv_id
            if idName == curSelection:
                return True

        return False


    def scanAllVisibleForEPG(self):
        for row in range(self.channelView.count()):
            name = self.channelView.item(row).text()
            #do nothing if hidden group
            if self.channelData[name].group in self.hiddenGroups:
                self.channelView.item(row).setForeground(QColor(210,210,210))
                continue

            num = self.findEPG(name)
            if num < 0:
                if self.isInConfigRememberList(name):
                    self.channelView.item(row).setForeground(QColor(0,255,0))
                else:
                    self.channelView.item(row).setForeground(QColor(255,0,0))
            else:
                self.channelView.item(row).setForeground(QColor(0,0,0))


    def openEPGFile(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(None,'open stuff', '/home/kons', 'bla (*.xml.gz)')[0]
        er = EPGReader.EPGReader(fileName)
        self.epgData = er.getChannelNames()
        self.epgLine.setText(fileName)
        self.epgView.clear()
        for chID in self.epgData:
            self.epgView.addItem(self.epgData[chID])
        self.scanAllVisibleForEPG()


    def groupItemClicked(self):
        for index in self.groupView.selectedIndexes():
            print("you selected " + index.data())
            self.channelView.clear()
            if(index.data() == '(all)'):
                for key in sorted(self.channelData):
                    self.channelView.addItem(key)
            else:
                for key in sorted(self.channelData):
                    if self.channelData[key].group == index.data():
                        self.channelView.addItem(key)
        self.scanAllVisibleForEPG()


    def addCHButtonClicked(self):
        print('Add Channel list')
        fileName = QtWidgets.QFileDialog.getOpenFileName(None,'open stuff', '/home/kons', 'bla (*.m3u)')[0]
        if fileName != '':
            print('Selected channel file: '+fileName)
            self.chListList.addItem(fileName)
            self.readChannelLists()
            self.scanAllVisibleForEPG()


    def removeCHButtonClicked(self):
        print('Remove Channel list')
        for index in self.chListList.selectedIndexes():
            print('Removing file: '+index.data())
            self.chListList.takeItem(index.row())
        #Reread the remaining channel lists
        self.channelData = {}
        self.readChannelLists()
        self.refreshAll()


    def refreshAllChannelNames(self):
        #delete all
        self.channelView.clear()

        for key in sorted(self.channelData):
            self.channelView.addItem(key)


    def getAllGroupsFromChannelLists(self):
        groups = ['(all)']
        self.groups = []
        for key in self.channelData:
            group = self.channelData[key].group
            if group not in groups:
                groups.append(group)
                self.groups.append(group)
        return groups


    def refreshAllGroupNames(self):
        self.groupView.clear()
        groups = self.getAllGroupsFromChannelLists();
        for group in groups:
            self.groupView.addItem(group)

    def importDataFromExportFile(self):
        filename = self.m3uExportEdit.text()
        if os.path.isfile(filename):
            log('Importing from old file')
            cr = ChanReader.ChannelReader(filename)
            cr.readFile()
            self.channelData = cr.getData()
        else:
            log('Nothing to import.')


    def readChannelLists(self):
        newChannels = 0
        self.epgView.clearSelection()
        self.channelData = {}
        self.importDataFromExportFile()
        for index in range(self.chListList.count()):
            fName = self.chListList.item(index).text()
            print(fName)
            cr = ChanReader.ChannelReader(fName)
            cr.readFile()
            newData = cr.getData()
            for key in newData:
                if key not in self.channelData:
                    self.channelData[key+'('+str(index)+')'] = newData[key]
                    newChannels = newChannels + 1
            log(str(newChannels)+' were added.')

        #load the channels into the tables.
        self.refreshAll()


    def refreshAll(self):
        self.refreshAllGroupNames()
        self.refreshAllChannelNames()

    def saveChangesToFile(self):
        # save channels
        outFile = self.m3uExportEdit.text()
        f = open(outFile, 'w+')
        f.write('#EXTM3U\n')
        for group in sorted(self.groups):
            for key in sorted(self.channelData):
                channel = self.channelData[key]
                # skip hidden channels
                if channel.group in self.hiddenGroups:
                    continue

                if channel.group == group:
                   f.write('#EXTINF:-1 tvg-id="%s" tvg-name="%s" tvg-logo="%s" group-title="%s",%s\n' %
                           (
                               channel.ID,
                               channel.ID,
                               channel.logo,
                               channel.group,
                               channel.name
                           ))
                   f.write(channel.url)
        f.close()
        #save configs
        outFile = self.configPathEdit.text()
        f = open(outFile, 'w+')
        for entry in self.configsToExport:
            cfgItem = self.channelConfigData[entry]
            f.write('<channel update="%s" site="%s" site_id="%s" xmltv_id="%s">%s</channel>\n'%
            (
                cfgItem.update,
                cfgItem.site,
                cfgItem.site_id,
                cfgItem.xmltv_id,
                entry
            ))
        f.close()

## KONS END

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

