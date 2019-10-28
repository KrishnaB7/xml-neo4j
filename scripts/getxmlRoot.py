from xml.etree import ElementTree as ET

class GetxmlRoot:
    def __init__(self, filename):
        self.filename = filename

    #Pre-process XML and return root, namespace
    def filterXml(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        namespace = self.getNamespace(root)
        self.removeNamespace(root, namespace)
        return root, namespace

    #Get namespace of XML file
    def getNamespace(self, root):
        if len(root.tag.split('}')) > 1:
            namespace = root.tag.split('}')[0].strip('{')
        else:
            namespace = ''
        return namespace

    #Remove namespace from all elements in XML
    def removeNamespace(self, root, namespace):
        ns = u'{%s}' % namespace
        nsl = len(ns)
        for elem in root.getiterator():
            if elem.tag.startswith(ns):
                elem.tag = elem.tag[nsl:]

