# Module waarbij de bezoekrapporten worden weergegeven van de inspecteurs en bedrijven

import os
from inspectors_module import inspector_list
from companies_module import companies_l
from datetime import datetime, date, MINYEAR, MAXYEAR

# Dit zal automatisch de juiste padseparator gebruiken om meer OS'en te ondersteunen
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
VISITREPORT_FILE = os.path.join(CURRENT_DIRECTORY, "assignment-files", "visit_reports.txt")

# Lijst van alle bezoekrapporten
report_list = []
FILES_READ = set()

class Visit:
    def __init__(
            self,
            inspector_code,
            company_code,
            visit_date,
            report_date,
            state,
            comment,
    ):
        self.__inspector_code = inspector_code
        self.__company_code = company_code
        self.__visit_date = visit_date
        self.__report_date = report_date
        self.__state = state
        self.__comment = comment
        report_list.append(self)

    # Haal inspecteur op met specifieke inspecteurscode
    def get_inspector_by_code(self, inspector_code):
        return next((inspector for inspector in inspector_list if inspector.get_code() == inspector_code), None)

    # Haal bedrijf op met specifieke bedrijfscode
    def get_company_by_code(self, company_code):
        return next((company for company in companies_l if company.get_code() == company_code), None)

    def get_inspector_code(self):
        return self.__inspector_code

    def get_company_code(self):
        return self.__company_code

    def get_visit_date(self):
        return self.__visit_date

    # Toon details van het bezoekrapport
    def show_details(self):
        print(f"\tVisit Date: {self.__visit_date}")
        print(f"\tReport Date: {self.__report_date}")
        print(f"\tState: {self.__state}")
        print(f"\tComment: {self.__comment}")

# Uploadt de bezoekrapporten vanuit het tekstbestand
def upload_reports(file_name=VISITREPORT_FILE):
    if file_name in FILES_READ:
        print(f"File {file_name} has already been uploaded.")
        return

    try:
        with open(file_name, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) >= 6:
                    inspector_code, company_code, visit_date, report_date, state = parts[:5]
                    comment = " ".join(parts[5:]) if len(parts) > 5 else None

                    Visit(inspector_code, company_code, visit_date if visit_date != "." else None,
                          report_date if report_date != "." else None, state if state != "." else None, comment)

            print(f"Visit reports from {file_name} uploaded.")
            FILES_READ.add(file_name)

    except FileNotFoundError:
        print(f"File {file_name} not found.")

# Toon een overzicht van alle bezoekrapporten
def show_reports():
    print("Length of report list: ", len(report_list))
    for report in report_list:
        inspector = report.get_inspector_by_code(report._Visit__inspector_code)
        if inspector:
            print("Inspector info:")
            inspector.show_data()
        else:
            print("Inspector Code:", report._Visit__inspector_code)

        company = report.get_company_by_code(report._Visit__company_code)
        if company:
            print("Company info:")
            company.show_details()
        else:
            print("Company Code:", report._Visit__company_code)

        print("Visit Date:", report._Visit__visit_date)
        print("Report Date:", report._Visit__report_date)
        print("State:", report._Visit__state)
        print("Comment:", report._Visit__comment)
        print("=" * 50 + "\n")

# Toon een overzicht van alle bezoekrapporten van een bedrijf mogelijk met een start- en einddatum, gesorteerd op datum aflopend
def show_report_company(
        company_code, start_date=date(MINYEAR, 1, 1), end_date=date(MAXYEAR, 1, 1)
):
    visits_per_company_list = [visit for visit in report_list if visit.get_company_code() == company_code
                               and start_date <= datetime.strptime(visit.get_visit_date(),
                                                                   "%d-%m-%Y").date() <= end_date]

    visits_per_company_list.sort(key=lambda x: datetime.strptime(x.get_visit_date(), "%d-%m-%Y"), reverse=True)

    if not visits_per_company_list:
        print("There are no visit reports available of this company:", company_code)
        print("In the period from", start_date, "|", end_date)
        return

    for visit_from_company in visits_per_company_list:
        print()
        print("\tCompany info:", visit_from_company.get_company_code())
        inspector = visit_from_company.get_inspector_by_code(
            visit_from_company._Visit__inspector_code
        )
        if inspector:
            print("\tInspector name:", inspector.get_name())
        else:
            print("\tInspector Code:", visit_from_company._Visit__inspector_code)
        visit_from_company.show_details()

 # Toon een overzicht van alle bezoekrapporten van een inspecteur mogelijk met een start- en einddatum, gesorteerd op datum aflopend
def show_report_by_inspector(
        inspector_code, start_date=date(MINYEAR, 1, 1), end_date=date(MAXYEAR, 1, 1)
):
    visits_per_inspector_list = [visit for visit in report_list if visit.get_inspector_code() == inspector_code
                                 and start_date <= datetime.strptime(visit.get_visit_date(),
                                                                     "%d-%m-%Y").date() <= end_date]

    visits_per_inspector_list.sort(key=lambda x: datetime.strptime(x.get_visit_date(), "%d-%m-%Y"), reverse=True)

    if not visits_per_inspector_list:
        print(
            "No visit reports found from the inspector:", inspector_code
        )
        print("In the period from", start_date, "|", end_date)
        return

    for visit_from_inspector in visits_per_inspector_list:
        print()
        print("\tInspector info:", visit_from_inspector.get_inspector_code())
        company = visit_from_inspector.get_company_by_code(
            visit_from_inspector._Visit__company_code
        )
        if company:
            print("\tCompany name:", company.get_name())
        else:
            print("\tCompany Code:", visit_from_inspector._Visit__company_code)
        visit_from_inspector.show_details()
