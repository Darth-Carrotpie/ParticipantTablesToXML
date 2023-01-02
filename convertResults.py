import xmlschema
from pprint import pprint
from readFiles import ReadFiles, ReadResultFiles, TryMakeIO
from writeXML import WriteXMLTree
from conversions import fixValueNames, renameCols
from objects.participantResult import EndedParticipantFormObject
from datetime import datetime

TryMakeIO()
df = ReadResultFiles()
if df is None:
    print("No input files detected in IO folder")
    print("'IO' aplanke failų nerasta")
    exit()
print(df.head())
obj = EndedParticipantFormObject("10.1.5-ESFA-V-924-01-0004", datetime.today().strftime('%Y-%m-%d')) #pakeisti į šios dienos
obj.FrameToRecords(df)

xmlObj = obj.toXMLElement()

print("XML----------------")
print(xmlObj[:50])

xmlFileName = "output.xml"
xmlPath = WriteXMLTree(xmlFileName, xmlObj)
print("path saved: "+xmlPath)

p_schema = xmlschema.XMLSchema('schemas/xmlschema_result.xsd')

print("----------------is_valid: "+str(p_schema.is_valid(xmlPath)))
#pprint(str(p_schema.to_dict(xmlPath))[:50])