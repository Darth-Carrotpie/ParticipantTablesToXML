from datetime import datetime
from CONSTANTS import particVulnGroup
from typing import List
from xml.etree.ElementTree import Element

class ParticipantResult(object):
    def __init__(self, row = None):
        self.ResultList = []
        if row is not None:
            self.surname = row.surname[:30] if len(row.surname) else row.surname
            self.forename = row.forename[:30] if len(row.forename) else row.forename
            self.dateOfBirth = row.dateOfBirth #date
            self.particTill = row.particTill #date

            #LISTS
            try:
                if(row.PR1 > 0):
                    self.ResultList.append("PR_1")
                if(row.PR2 > 0):
                    self.ResultList.append("PR_2")
                if(row.PR3 > 0):
                    self.ResultList.append("PR_3")
                if(row.PR4 > 0):
                    self.ResultList.append("PR_4")
                if(row.PR5 > 0):
                    self.ResultList.append("PR_5")
                if(row.PR6 > 0):
                    self.ResultList.append("PR_6")
                if(row.PR7 > 0):
                    self.ResultList.append("PR_7")

                if(len(self.ResultList)<=0):
                    self.ResultList.append("PR_8")

            except:
                if(len(self.ResultList)<=0):
                    self.ResultList.append("PR_8")
        else:
            self.surname = ""
            self.forename = ""
            self.dateOfBirth = ""
            self.particTill = ""
            self.ResultList = []

    def toXMLElement(self):
        root = Element("Participant")
        root.append(AttrToElement("surname", str(self.surname)))
        root.append(AttrToElement("forename", str(self.forename)))
        root.append(AttrToElement("dateOfBirth", datetime.fromisoformat(self.dateOfBirth).strftime("%Y-%m-%d")))
        root.append(AttrToElement("particTill", datetime.fromisoformat(self.particTill).strftime("%Y-%m-%d")))
        root.append(AddListXMLRaw("Result","ResultList", self.ResultList))
        return root


class EndedParticipantFormObject(object):
    def __init__(self, pcode = None, formDate = None, ParticipantList: List[ParticipantResult]=None):
        self.projectCode = pcode
        self.formDate = formDate
        self.ParticipantList = [] if ParticipantList is None else ParticipantList

    def FrameToRecords(self,df):
        partRows = df.to_records()
        for partRow in partRows:
            self.ParticipantList.append(ParticipantResult(partRow))

    def toXMLElement(self):
        root = Element("EndedParticipantFormObject")
        child = Element("projectCode")
        child.text = str(self.projectCode)
        child2 = Element("formDate")
        child2.text = datetime.fromisoformat(self.formDate).strftime("%Y-%m-%d")
        root.append(child)
        root.append(child2)
        root.append(AddListXML("ParticipantList", self.ParticipantList))
        return root

def AddListXML(elListName, elList):
    root = Element(elListName)
    for item in elList:
        root.append(item.toXMLElement())
    return root

def AddListXMLRaw(elName, elListName, elList):
    root = Element(elListName)
    for item in elList:
        addPart = Element("Result")
        addPart.text = item
        root.append(addPart)
    return root

def AttrToElement(attrName, val):
   child = Element(attrName)
   child.text = val
   return child