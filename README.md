# xml-neo4j
Stores XML files into XML like structure in Neo4j graph database


## Folder Structure
```.
├── LICENSE
├── README.md
├── scripts
│   ├── __init__.py
│   ├── getxmlRoot.py
│   └── xml2graph.py
└── xml-neo4j.py
```
- ```xml-neo4j.py``` - Main script that takes multiple arguments from user
- ```scripts/getxmlRoot.py``` - Module to parse input XML and return root and namespace
- ```scripts/xml2graph.py``` - Module to parse and create XML like graph in neo4j


## Installation
```Python 2.7```, ```pip``` should be installed before this step

```
git clone https://github.com/KrishnaB7/xml-neo4j.git
cd xml-neo4j
pip install -r requirements.txt
```

## Usage

- Check the various arguments allowed-
```python xml-neo4j.py -h```
```
usage: xml-neo4j.py [-h] -f  [-H] [-P] [-u] [-p]

optional arguments:
  -h, --help        show this help message and exit
  -f , --filename   Choose the input XML file
  -H , --host       Ip address of neo4j server instance
  -P , --port       Port number of neo4j server instance
  -u , --username   Username of neo4j server instance
  -p , --password   Password of neo4j server instance
```
-f (filename) is required

-H (host) defaults to "localhost"

-P (port) defaults to "7687"

-u (username) defaults to "neo4j"

-p (password) defaults to "neo4j"

### Run Script
- Running remote neo4j server on machine with ip - ```54.116.62.222```, port - ```7687```, username - ```mydb```, password - ```test```

  ```python xml-neo4j.py -f examples/employees.xml -H 54.116.62.222 -P 7687 -u mydb -p test```
- Running neo4j instance in local system with user - ```neo4j```, password - ```test```

  ```python xml-neo4j.py -f examples/employees.xml -u neo4j -p test```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
