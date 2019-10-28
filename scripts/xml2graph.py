from xml.etree import ElementTree as ET
from neo4j import GraphDatabase
import os
import sys

class Xml2Graph():
    def __init__(self, root, namespace, host_ip, port, username, password):
        self.root = root
        self.namespace = namespace
        if not host_ip:
            self.host_ip = "localhost"
        else:
            self.host_ip = host_ip
        if not port:
            self.port = "7687"
        else:
            self.port = port
        if not username:
            self.username = "neo4j"
        else:
            self.username = username
        if not password:
            self.password = "neo4j"
        else:
            self.password = password
        self.rootNode = 'root'
        self.tx = ''

    #Load XML elements into neo4j
    def dumpXml(self):
        driver = self.graphInitialization(self.host_ip, self.port, self.username, self.password)
        session = driver.session()
        self.tx = session.begin_transaction()
        root_id = self.executeQuery(('MERGE(n:`{}`) return id(n)').format(self.rootNode)).single()[0]
        if self.namespace:
            query = 'MATCH (n) WHERE id(n)=%d CREATE(a:`%s` {namespace:"%s"}) MERGE(n)-[:`%s`]->(a) RETURN id(a)' % (root_id, self.root.tag, self.namespace, self.root.tag)
        else:
            query = 'MATCH (n) WHERE id(n)=%d CREATE(a:`%s`) MERGE(n)-[:`%s`]->(a) RETURN id(a)' % (root_id, self.root.tag, self.root.tag)
        node_id = self.executeQuery(query).single()[0]
        self.writeToGraph(self.root, node_id)
        self.tx.commit()

    #Initialize neo4j server instance
    def graphInitialization(self, host_ip, port, username, password):
        uri = "bolt://" + host_ip + ":" + str(port)
        print uri
        driver = GraphDatabase.driver(uri, auth=(username, password))
        return driver

    #Execute a given query
    def executeQuery(self, query):
        result = self.tx.run(query)
        return result

    #Handle meta-characters
    def encodeText(self, text):
        text = text.replace('\\', '\\\\')
        text = text.replace('"', '\\"')
        return text

    #Get attributes of an element
    def getAttributes(self, element):
        propsList = []
        for key, value in element.attrib.iteritems():
            propsList.append('`{}`:"{}"'.format(self.encodeText(key), self.encodeText(value)))
        return  ",".join(propsList)

    #Parse through entire XML and query to neo4j
    def writeToGraph(self, root, node_id):
        if not root.getchildren():
            return
        for child in root:
            if child.text.strip() == '':
                props =  self.getAttributes(child)
                query = 'MATCH (n) WHERE id(n)=%d CREATE(a:`%s` {%s}) MERGE(n)-[:`%s`]->(a) RETURN id(a)' % (node_id, child.tag, props, child.tag)
                print query
                _id = self.executeQuery(query).single()[0]
                self.writeToGraph(child, _id)
            else:
                #print "<{}>{}</{}>".format(child.tag, child.text, child.tag)
                props = self.getAttributes(child)
                if props:
                    props += ', `_text`:"{}"'.format(self.encodeText(child.text))
                else:
                    props = '`_text`:"{}"'.format(self.encodeText(child.text))
                query = 'MATCH (n) WHERE id(n)=%d CREATE(a:`%s` {%s}) MERGE(n)-[:`%s`]->(a) RETURN id(a)' % (node_id, child.tag, props, child.tag)
                print query
                self.executeQuery(query)




