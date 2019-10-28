import os
import os.path
from os.path import isdir, isfile
import sys
import argparse
from scripts.getxmlRoot import GetxmlRoot
from scripts.xml2graph import Xml2Graph

def main():
    parser = argparse.ArgumentParser(description='XML to Graph')
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filename', action='store', metavar='', type=str, required=True, help='Choose the input XML file')
    parser.add_argument('-H', '--host', action='store', metavar='', type=str, help='Ip address of neo4j server instance')
    parser.add_argument('-P', '--port', action='store', metavar='', type=str, help='Port number of neo4j server instance')
    parser.add_argument('-u', '--username', action='store', metavar='', type=str, help='Username of neo4j server instance')
    parser.add_argument('-p', '--password', action='store', metavar='', type=str, help='Password of neo4j server instance')
    args = parser.parse_args()

    #Get root, namespace from input xml
    xml = GetxmlRoot(args.filename)
    root, namespace = xml.filterXml()

    #Write XML details to XML like structure in neo4j
    xml_graph = Xml2Graph(root, namespace, args.host, args.port, args.username, args.password)
    xml_graph.dumpXml()

if __name__ == '__main__':
    sys.exit(not main())
