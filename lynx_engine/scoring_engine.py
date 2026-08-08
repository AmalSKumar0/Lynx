from lynx_engine.evidence_collector import Evidence,scan
from lynx_engine.data import EXTENSION_TO_LANGUAGE,FILES_TO_TECHNOLOGY

import sys


class Score:
    def __init__(self):
        self.language = {
            "primary":[],
            "secondary":[],
            "supporting":[]
        }
        self.frameworks = {}
        self.libraries = {}
        self.runtimes = {}
        self.tools = {}
        self.package_managers = {}
        self.configuration = {}
    

    def load_languages(self,language_raw_data: dict):

        for key,value in language_raw_data.items():
            if value >= 50:
                self.language["primary"].append(key)
            elif value >= 10:
                self.language["secondary"].append(key)
            else:
                self.language["supporting"].append(key)

    def display(self):

        print(self.__dict__)

    def putting_data(self,category,technology,count):
            target = getattr(self, category)
            target[technology] = target.get(technology, 0) + count
            
# Helper function to clean languages less tahn 1% presence in the folder
def filter_languages(languages):
    return {
        key:value
        for key,value in languages.items()
        if value >= 1.0 
    }


def language_scoring_engine(Language_raw_data: dict,score: Score):
    lang = {}
    total = 0
    
    for key,value in Language_raw_data.items():
        language = EXTENSION_TO_LANGUAGE.get(key)
        if language == None:
            continue
        
        total += value
        if language in lang:
            lang[language] += value
        else:
            lang[language] = value
    
    for key,value in lang.items():
        percentage = (value/total)*100
        lang[key] = percentage

    lang = filter_languages(lang)
    score.load_languages(lang)

def framework_scoring_engine(files_raw_data, score):
    categories = [
        "frameworks",
        "libraries",
        "runtimes",
        "tools",
        "package_managers",
        "configuration",
    ]

    for filename, count in files_raw_data.items():

        for category in categories:
            technology = FILES_TO_TECHNOLOGY[category].get(filename)

            if technology is not None:
                score.putting_data(
                    category,
                    technology,
                    count
                )


def main():
    path = "~/College Projects/noir"
    score = Score()
    evidence = scan(path)
    data = evidence.export_evidence()
    language_scoring_engine(data,score)

    data = evidence.export_files()
    framework_scoring_engine(data,score)
    score.display()

if __name__ == "__main__":
    main()