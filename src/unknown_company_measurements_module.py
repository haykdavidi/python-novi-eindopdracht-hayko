# Module waarmee de verschillende emissie-metingen geanalyseerd worden

import os
import numpy as np
import companies_module as companies

# Uploaden van het gas bestand
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
GAS_FILE = os.path.join(CURRENT_DIRECTORY, "assignment-files", "gases.csv")

# Inlezen van gassen data vanuit het csv-gassenbestand
gassen_data = np.loadtxt(GAS_FILE, delimiter=",", skiprows=1, usecols=(2, 3, 4, 5))


# Extraheren van CO2, CH4, NO2 en NH3 data en hervormen naar 100x100 matrix
co2_data, ch4_data, no2_data, nh3_data = [
    data.reshape(100, 100) for data in gassen_data.T
]

# Constanten voor bekende bedrijfslocaties
known_company_locations = np.zeros([100, 100])


# Haal de CO2-emissie op van de opgegeven locatie.
def get_emission_gas_CO2(latitude, longitude):
    global known_company_locations
    known_company_locations[latitude, longitude] = 1
    return co2_data[int(latitude), int(longitude)]


# Functies voor het ophalen van emissiegegevens van verschillende gassen op een opgegeven locatie
def get_emission_gas_CH4(latitude, longitude):
    global known_company_locations
    known_company_locations[latitude, longitude] = 1
    return ch4_data[int(latitude), int(longitude)]


def get_emission_gas_NO2(latitude, longitude):
    global known_company_locations
    known_company_locations[latitude, longitude] = 1
    return no2_data[int(latitude), int(longitude)]


def get_emission_gas_NH3(latitude, longitude):
    global known_company_locations
    known_company_locations[latitude, longitude] = 1
    return nh3_data[int(latitude), int(longitude)]


# Identificeer vervuilde locaties waar onbekende bedrijven zich bevinden.
def calculate_analysis_report(number_of_locations):
    global known_company_locations
    if not np.any(known_company_locations):
        print(
            "Please first calculate the emission and fine per company before choosing this option"
        )
        return
    # Bereken de totale gassen per locatie op basis van emissiefactoren en gegevens van bekende bedrijven
    total_gases = (
        companies.CO2_EMISSION_FACTOR * co2_data
        + companies.CH4_EMISSION_FACTOR * ch4_data
        + companies.NO2_EMISSION_FACTOR * no2_data
        + companies.NH3_EMISSION_FACTOR * nh3_data
    )

    # Bepaal de meest vervuilde locaties
    polluted_locations_list = get_list_of_most_polluted_locations(
        total_gases, number_of_locations
    )
    print_analysis_report_with_gas_values(polluted_locations_list)


def get_list_of_most_polluted_locations(array_to_check, number_of_locations):
    # Vind de indices van de N hoogste waarden zonder volledige sortering
    highest_indices = np.argpartition(array_to_check.ravel(), -number_of_locations)[-number_of_locations:]
    # Converteer de platte indices naar 2D-indices
    highest_location_2_d_indices = np.unravel_index(highest_indices, array_to_check.shape)
    # Maak een lijst van locaties en hun waarden
    locations = [(i, j, array_to_check[i, j]) for i, j in zip(highest_location_2_d_indices[0], highest_location_2_d_indices[1])]
    # Sorteer de lijst op basis van de gaswaarden van hoog naar laag
    locations.sort(key=lambda x: x[2], reverse=True)
    return locations


# Print het analyseverslag samen met gaswaarden.
def print_analysis_report_with_gas_values(locations):
    print("=" * 70)
    print(" " * 20 + "Analysis Report & Gas Values")
    print("=" * 70)
    print("\nDescription of the Analysis Functionalities")
    print("=" * 70)
    print(
        "This program collects data of several gas types around company locations which could be potential polluters."
    )
    print(
        "It focuses on areas where there are less known companies to find unknown polluters in order to investigate these place."
    )
    print(
        "On the list above you can see the locations and the highest gas values which are present there."
    )
    print("=" * 70)

    if not locations:
        print("\nNo locations found with high measured gas values.")
        return
    else:
        print(
            f"\n{len(locations)} locations found with the highest measured gas values:"
        )

    print("\nLocation (x, y)  |  Total Gas Value")
    print("-" * 70)

    for location in locations:
        print(
            f"  ({location[0]:>2}, {location[1]:<2})     |       {location[2]:.2f}"
        )
