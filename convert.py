import xmlschema
from pprint import pprint
from readFiles import ReadFiles
import pandas
from writeXML import WriteXMLTree, dict_to_xml
from conversions import fixValueNames, renameCols
from objects import ParticipantFormObject, Participant

df = ReadFiles()
renameCols(df)
df = fixValueNames(df)

obj = ParticipantFormObject("10.1.5-ESFA-V-924-01-0004", "2022-02-07", [Participant(df.to_records()[0])])
obj.FrameToRecords(df)

xmlObj = obj.toXMLElement()

print("XML----------------")
print(xmlObj[:200])

xmlFileName = "output.xml"
xmlPath = WriteXMLTree(xmlFileName, xmlObj)
print("path saved: "+xmlPath)

p_schema = xmlschema.XMLSchema('xmlschema.xsd')

print("----------------is_valid: "+str(p_schema.is_valid(xmlPath)))
pprint(str(p_schema.to_dict(xmlPath))[:300])