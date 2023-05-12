import xmlschema
from pprint import pprint
from readFiles import ReadFiles, TryMakeIO
from writeXML import WriteXMLTree
from conversions import fixValueNames, renameCols
from objects.objects import ParticipantFormObject

TryMakeIO()
df = ReadFiles(headerSize = 20)
if df is None:
    print("No input files detected in IO folder")
    print("'IO' aplanke failų nerasta")
    exit()
renameCols(df)
df = fixValueNames(df)

obj = ParticipantFormObject("10.1.5-ESFA-V-924-01-0004", "2022-02-07")
obj.FrameToRecords(df)

xmlObj = obj.toXMLElement()

print("XML----------------")
print(xmlObj[:200])

xmlFileName = "output.xml"
xmlPath = WriteXMLTree(xmlFileName, xmlObj)
print("path saved: "+xmlPath)

p_schema = xmlschema.XMLSchema('schemas/xmlschema.xsd')

print("----------------is_valid: "+str(p_schema.is_valid(xmlPath)))
pprint(str(p_schema.to_dict(xmlPath))[:300])