from os import path 
import __main__ as main
from xml.etree.ElementTree import Element,tostring, ElementTree

def WriteFile(fileName,xml):
    curr_path = path.dirname(path.abspath(main.__file__))
    xml_abs_path = path.join(curr_path, "IO", fileName)

    f = open(xml_abs_path, "w", encoding="utf-8")
    f.write(xml)
    return xml_abs_path
    print('File saved!')


def WriteXMLTree(fileName,xmlTree):
    curr_path = path.dirname(path.abspath(main.__file__))
    xml_abs_path = path.join(curr_path, "IO", fileName)
    tree = ElementTree()
    tree._setroot(xmlTree)
    tree.write(xml_abs_path, encoding='utf-8', xml_declaration = True)
    print('XML saved!')
    return xml_abs_path


def WriteXML(fileName,xml):
    curr_path = path.dirname(path.abspath(main.__file__))
    xml_abs_path = path.join(curr_path, "IO", fileName)
    with open(xml_abs_path, "w", encoding="utf-8") as f:
        f.write(tostring(xml, encoding='utf8', method='xml').decode())
    print('XML saved!')