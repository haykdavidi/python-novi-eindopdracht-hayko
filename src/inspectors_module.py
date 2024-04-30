"""Inspecteurs module"""
import os

# Inlezen van het tekstbestand met de inspecteur-gegevens
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
INSPECTORS_FILE = os.path.join(CURRENT_DIRECTORY, "assignment-files", "inspectors.txt")
FILES_READ = set()

# lijst met alle inspecteur objecten
inspector_list = []

class Inspector:
    def __init__(self, code, name="", location=""):
        self.__code = code
        self.__name = name
        self.__location = location
        self.__visit_reports = []

    def get_code(self):
        return self.__code

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def add_visit_report(self, visit_report):
        self.__visit_reports.append(visit_report)

    def show_data(self):
        print(f"\tInspector Code: {self.__code}")
        print(f"\tName: {self.__name}")
        print(f"\tLocation: {self.__location}")

    def show_code_and_name(self):
        print(f"\tInspector Code: {self.__code}")
        print(f"\tName: {self.__name}")

def upload_inspectors(file_name=INSPECTORS_FILE):
    if file_name in FILES_READ:
        print(f"File {file_name} has already been uploaded.")
        return 0

    try:
        with open(file_name, mode="r") as inspectors_file:
            for record in inspectors_file:
                code, name, location = record[:3], record[4:24], record[24:44]
                inspector = Inspector(code.strip(), name.strip(), location.strip())
                inspector_list.append(inspector)
        print(f"File {file_name} uploaded.")
        FILES_READ.add(file_name)
        return 0
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return 1

def is_inspectors_list_complete():
    if not inspector_list:
        print("No inspectors found.")
        return False
    return True

def publish_inspectors():
    if not is_inspectors_list_complete():
        return
    print("Inspectors List")
    print("===================================\n")
    for inspector in inspector_list:
        inspector.show_data()
        print("-" * 55)

def show_inspectors_code_and_name():
    if not is_inspectors_list_complete():
        return
    print("Inspector List (code/name)")
    print("=====================================\n")
    for inspector in inspector_list:
        inspector.show_code_and_name()
        print("-" * 55)

def inspector_exists(code):
    if not is_inspectors_list_complete():
        return False
    for inspector in inspector_list:
        if inspector.get_code() == code:
            return True
    return False
