# Deze module analyseert de bedrijven en gebruikt hiervoor de emissie-berekenformulen

import os
import unknown_company_measurements_module as measurements

# Deze code zorgt ervoor dat het juiste pad automatisch wordt gebruikt om besturingssystemen te ondersteunen
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
COMPANY_FILE = os.path.join(CURRENT_DIRECTORY, "assignment-files", "companies.txt")

# Lijst alle bedrijven
companies_l = []
FILES_READ = set()

# Definieer constanten voor de emissiewaarden van verschillende gassen en een fijnheidsfactor.
CO2_EMISSION_FACTOR = 1  # CO2
CH4_EMISSION_FACTOR = 25  # CH4
NO2_EMISSION_FACTOR = 5  # NO2
NH3_EMISSION_FACTOR = 1000  # NH3
FACTOR_FINE = 2


# Klasse om bedrijfsgegevens te definiëren en te manipuleren.
class Company:
    def __init__(
            self,
            code=None,
            name=None,
            street=None,
            house_number=None,
            postal_code=None,
            city=None,
            latitude=None,
            longitude=None,
            max_allowed_emission=None,
            emission_calculated=None,
            fine=None,
            control=None,
            inspection_frequency=None,
            contact_inspector=None,
    ):
        self.__code = code
        self.__name = name
        self.__street = street
        self.__house_number = house_number
        self.__postal_code = postal_code
        self.__city = city
        self.__latitude = latitude
        self.__longitude = longitude
        self.__max_allowed_emission = max_allowed_emission
        self.__emission_calculated = emission_calculated
        self.__fine = fine
        self.__control = control
        self.__inspection_frequency = inspection_frequency
        self.__contact_inspector = contact_inspector

    #  Methode om alle details van het bedrijf weer te geven.
    def show_details(self):
        print(f"\tCompany Code: {self.__code}")
        print(f"\tName: {self.__name}")
        print(f"\tStreet: {self.__street}")
        print(f"\tHouse Number: {self.__house_number}")
        print(f"\tPostal Code: {self.__postal_code}")
        print(f"\tCity: {self.__city}")
        print(f"\tLatitude: {self.__latitude}")
        print(f"\tLongitude: {self.__longitude}")
        print(f"\tMax Allowed Emission: {self.__max_allowed_emission}")
        print(f"\tEmission Calculated: {self.__emission_calculated}")
        print(f"\tFine: {self.__fine}")
        print(f"\tControl: {self.__control}")
        print(f"\tInspection Frequency: {self.__inspection_frequency}")
        print(f"\tContact Inspector: {self.__contact_inspector}")

    # Methode om de bedrijfscode op te halen.
    def get_code(self):
        return self.__code

    # Methode om de bedrijfscode op te halen.
    def get_name(self):
        return self.__name

    # Methode om de breedtegraad op te halen.
    def get_latitude(self):
        return self.__latitude

    # Methode om de lengtegraad op te halen.
    def get_longitude(self):
        return self.__longitude

    # Methode om de emissie van gas 1 op een specifieke locatie op te halen.
    def get_emission1(self, latitude, longitude):
        return measurements.get_emission_gas_CO2(latitude, longitude)

    # Methode om de emissie van gas 2 op een specifieke locatie op te halen.
    def get_emission2(self, latitude, longitude):
        return measurements.get_emission_gas_CH4(latitude, longitude)

    # Methode om de emissie van gas 3 op een specifieke locatie op te halen.
    def get_emission3(self, latitude, longitude):
        return measurements.get_emission_gas_NO2(latitude, longitude)

    # Methode om de emissie van gas 4 op een specifieke locatie op te halen.
    def get_emission4(self, latitude, longitude):
        return measurements.get_emission_gas_NH3(latitude, longitude)

    # Methode om de berekende emissie in te stellen.
    def set_calculated_emission(self, emission_calculated):
        self.__emission_calculated = emission_calculated

    #  Methode om de maximale toegestane uitstoot op te halen
    def get_max_allowed_emission(self):
        return self.__max_allowed_emission

    # Methode om de boete te berekenen op basis van de berekende uitstoot en de maximale toegestane uitstoot.
    def calculate_fine(self):
        if float(self.__emission_calculated) > float(self.__max_allowed_emission):
            fine = (float(self.__emission_calculated) - float(self.__max_allowed_emission)) * 2
            self.__fine = format(fine, ".2f")
            print(
                f"\t{self.__name} will receive a fine of: {self.__fine}\n\tbased on the calculated emission of approximately: {self.__emission_calculated}\n"
            )
        else:
            self.__fine = 0

    #  Methode om alleen de bedrijfscode en -naam weer te geven.
    def show_code_and_name(self):
        print(f"\tCompany Code: {self.__code}")
        print(f"\tName: {self.__name}")


#  Functie om bedrijfsgegevens uit een bestand te uploaden naar de applicatie.
def upload_companies(file_name=COMPANY_FILE):
    if file_name in FILES_READ:
        print(f"companies file {file_name} has been uploaded.")
        return

    try:
        with open(file_name, "r") as file:
            for line_num, line in enumerate(file, 1):
                try:
                    indices = [0, 5, 25, 55, 59, 67, 87, 90, 93, 108, 123, 135, 139, 142, 162]
                    values = [line[i:j].strip() for i, j in zip(indices[:-1], indices[1:])]
                    company = Company(*values)
                    companies_l.append(company)

                except ValueError as e:
                    print(f"Error found in line {line_num}: {e}")

            print("companies file", file_name, "uploaded.")
            FILES_READ.add(file_name)

    except FileNotFoundError:
        print("companies file", file_name, "not found")
        return 1


# Functie om een scheidingslijn af te drukken.
def print_separator():
    print("-" * 55)


# Functie om alle bedrijfsgegevens af te drukken.
def publish_companies():
    if not companies_l:
        print("companies not found")
        return

    print("Publish Company List")
    print("==================================\n")
    for company in companies_l:
        company.show_details()
        print_separator()


# Functie om te controleren of de lijst met bedrijven volledig is.
def is_company_list_complete():
    if not companies_l:
        print("companies not found")
        return False
    return True


#  Functie om alleen de bedrijfscode en -naam weer te geven.
def show_company_code_and_name():
    if not companies_l:
        print("companies not found")
        return

    print("Company List (code/name)")
    print("==================================\n")
    for company in companies_l:
        company.show_code_and_name()
        print_separator()


#  Functie om te controleren of een bedrijf bestaat op basis van de bedrijfscode.
def company_exists(code):
    if not companies_l:
        print("companies not found")
        return False

    for company in companies_l:
        if company.get_code() == code:
            return True
    return False
