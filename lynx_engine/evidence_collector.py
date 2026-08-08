from pathlib import Path
from lynx_engine.data import IGNORE
import os
import pathspec
# import json

class Evidence:

    def __init__(self):
        self.file_extension = {}
        self.files = {}
        self.directories = {}
        self.dependencies = []
    
    def merge(self,data_of_child: Evidence):

        for key,value in data_of_child.file_extension.items():
            if key in self.file_extension:
                self.file_extension[key] += value
            else:
                self.file_extension[key] = value
        
        for key,value in data_of_child.files.items():
            if key in self.files:
                self.files[key] += value
            else:
                self.files[key] = value
        
        for key,value in data_of_child.directories.items():
            if key in self.directories:
                self.directories[key] += value
            else:
                self.directories[key] = value
        
        for data in data_of_child.dependencies:
            if data not in self.dependencies:
                self.dependencies.append(data)
    
    # def display_data(self):
    #     print("{")
    #     print("'Files Extensions' : {")
    #     for key,value in self.file_extension.items():
    #         print(key," : ",value)
    #     print("},")
        
    #     print("'Files' : {")
    #     for key,value in self.files.items():
    #         print(key," : ",value)
    #     print("},")

        
    #     print("'directories' : {")
    #     for key,value in self.directories.items():
    #         print(key," : ",value)
    #     print("},")

    #     print("'dependencies' : [")
    #     for data in self.dependencies:
    #         print(data,",")
    #     print("]")
    #     print("}")
    
    def export_evidence(self):
        evidence_data = self.file_extension
        return evidence_data

    def export_files(self):
        return self.files



def scan(path_dir: str) -> Evidence:
    root = Path(path_dir).expanduser()

    node = Evidence()
    for item in os.listdir(root):

        path = root / item

        if path.is_dir():
            
            node.directories[item]=node.directories.get(item,0)+1
            
            if item in IGNORE:
                continue

            child = scan(path)
            node.merge(child)

        else:
            node.files[item]=node.files.get(item,0)+1
            _, extension = os.path.splitext(item)
            if extension != '':
                node.file_extension[extension]=node.file_extension.get(extension,0)+1

    return node

# def display(path: Path):
#     node = scan(path)
#     print(node.export_evidence())