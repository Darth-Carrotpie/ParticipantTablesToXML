from datetime import datetime
from CONSTANTS import particVulnGroup
from typing import List
from xml.etree.ElementTree import Element

class Participant(object):
    def __init__(self, row = None):
        self.ParticipantMarkList = []
        self.ParticipantCriterionList = []
        self.VulnGroupList = []
        if row is not None:
            self.dateFilled = row.dateFilled #date
            self.surname = row.surname[:30] if len(row.surname) else row.surname
            self.forename = row.forename[:30] if len(row.forename) else row.forename
            self.dateOfBirth = row.dateOfBirth #date
            self.email = row.email[:100] if len(row.email) else row.email
            self.phoneNo = row.phoneNo[:30] if len(row.phoneNo) else row.phoneNo
            self.employerName = row.employerName[:140] if len(row.employerName) else row.employerName
            self.employerCode = row.employerCode[:15] if len(row.employerCode) else row.employerCode
            self.gender = row.gender
            self.education = row.education
            self.occupation = row.occupation
            self.educProgram = row.educProgram

            #LISTS
            self.ParticipantMarkList.append(ParticipantMark(1, row.Kp1))
            self.ParticipantMarkList.append(ParticipantMark(2, row.Kp2))
            self.ParticipantMarkList.append(ParticipantMark(3, row.Kp3))

            self.ParticipantCriterionList.append(ParticipantCriterion(1, row.K1))
            self.ParticipantCriterionList.append(ParticipantCriterion(2, row.K2))
            self.ParticipantCriterionList.append(ParticipantCriterion(3, row.K3))
            self.ParticipantCriterionList.append(ParticipantCriterion(4, row.K4))
            self.ParticipantCriterionList.append(ParticipantCriterion(5, row.K5))
            self.ParticipantCriterionList.append(ParticipantCriterion(6, row.K6))
            self.ParticipantCriterionList.append(ParticipantCriterion(7, row.K7))
            self.ParticipantCriterionList.append(ParticipantCriterion(8, row.K8))
            self.ParticipantCriterionList.append(ParticipantCriterion(9, row.K9))
            self.ParticipantCriterionList.append(ParticipantCriterion(10, row.K10))

            if(row.G1 > 0):
                self.VulnGroupList.append("PVG_G1")
            if(row.G2 > 0):
                self.VulnGroupList.append("PVG_G2")
            if(row.G3 > 0):
                self.VulnGroupList.append("PVG_G3")
            if(row.G4 > 0):
                self.VulnGroupList.append("PVG_G4")
            if(row.G5 > 0):
                self.VulnGroupList.append("PVG_G5")
            if(row.G6 > 0):
                self.VulnGroupList.append("PVG_G6")
            if(row.G7 > 0):
                self.VulnGroupList.append("PVG_G7")
            if(row.G8 > 0):
                self.VulnGroupList.append("PVG_G8")
            if(row.G9 > 0):
                self.VulnGroupList.append("PVG_G9")
        else:
            self.dateFilled = ""
            self.surname = ""
            self.forename = ""
            self.dateOfBirth = ""
            self.email = ""
            self.phoneNo = ""
            self.employerName = ""
            self.employerCode = ""
            self.ParticipantMarkList = []
            self.ParticipantCriterionList = []
            self.gender = ""
            self.education = ""
            self.occupation = ""
            self.educProgram = ""
            self.VulnGroupList = []

    def toXMLElement(self):
        root = Element("Participant")
        root.append(AttrToElement("dateFilled", datetime.fromisoformat(self.dateFilled).strftime("%Y-%m-%d")))
        root.append(AttrToElement("surname", str(self.surname)))
        root.append(AttrToElement("forename", str(self.forename)))
        root.append(AttrToElement("dateOfBirth", datetime.fromisoformat(self.dateOfBirth).strftime("%Y-%m-%d")))
        root.append(AttrToElement("email", str(self.email)))
        root.append(AttrToElement("phoneNo", str(self.phoneNo)))
        root.append(AttrToElement("employerName", str(self.employerName)))
        root.append(AttrToElement("employerCode", str(self.employerCode)))
        root.append(AddListXML("ParticipantMarkList", self.ParticipantMarkList))
        root.append(AddListXML("ParticipantCriterionList", self.ParticipantCriterionList))
        root.append(AttrToElement("gender", str(self.gender)))
        root.append(AttrToElement("education", str(self.education)))
        root.append(AttrToElement("occupation", str(self.occupation)))
        root.append(AttrToElement("educProgram", str(self.educProgram)))
        root.append(AddListXMLRaw("VulnGroup","VulnGroupList", self.VulnGroupList))
        return root

class ParticipantMark(object):
    markNumbering = 1
    response = ''
    def __init__(self, num = None, resp = None):
        self.markNumbering = num
        self.response = resp

    def toXMLElement(self):
        root = Element("ParticipantMark")
        child = Element("markNumbering")
        child.text = str(self.markNumbering)
        child2 = Element("response")
        child2.text = str(self.response)
        root.append(child)
        root.append(child2)
        return root

class ParticipantCriterion(object):
    criterionNumbering = 1
    fitCriteria = False
    def __init__(self, num = None, criteria = None):
        self.criterionNumbering = num
        self.fitCriteria = criteria

    def toXMLElement(self):
        root = Element("ParticipantCriterion")
        child = Element("criterionNumbering")
        child.text = str(self.criterionNumbering)
        child2 = Element("fitCriteria")
        child2.text = str(self.fitCriteria)
        root.append(child)
        root.append(child2)
        return root

class ParticipantFormObject(object):
    def __init__(self, pcode = None, formDate = None, ParticipantList: List[Participant]=None):
        self.projectCode = pcode
        self.formDate = formDate
        self.ParticipantList = [] if ParticipantList is None else ParticipantList

    def FrameToRecords(self,df):
        partRows = df.to_records()
        for partRow in partRows:
            self.ParticipantList.append(Participant(partRow))

    def toXMLElement(self):
        root = Element("ParticipantFormObject")
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
        addPart = Element("VulnGroup")
        addPart.text = item
        root.append(addPart)
    return root

def AttrToElement(attrName, val):
   child = Element(attrName)
   child.text = val
   return child