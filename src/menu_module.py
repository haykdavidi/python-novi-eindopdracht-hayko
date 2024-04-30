# Dit is de menu module, het startpunt van de applicatie.

import calculating_emissions_module as emissions
import companies_module as companies
import file_reader_module as file_reader
import inspectors_module as insp
import unknown_company_measurements_module as measure
import reports_module as reports
import visit_reports_menu
import co2_visualization_module as co2_visualization

def upload_files():
    file_reader.read_all_files()

def list_company_reports():
    companies.upload_companies()
    companies.publish_companies()

def list_inspectors():
    insp.upload_inspectors()
    insp.publish_inspectors()

def view_co2_gas_data():
    co2_visualization.lees_gas_co2(measure.GAS_FILE)

def manage_visit_reports():
    reports.upload_reports()
    visit_reports_menu.manage_reports_choice()

def calculate_emissions_and_fines():
    emissions.emissions_calculation()
    emissions.calculate_fines()


def analyze_unknown_companies():
    try:
        extra_value = int(input("Enter a value between 1 and 10: "))
        if 1 <= extra_value <= 10:
            measure.calculate_analysis_report(extra_value)
        else:
            print("Invalid value. The value must be between 1 and 10.")
    except ValueError:
        print("Invalid input. Please try again.")

def main():
    while True:
        print('Main Menu')
        print('==============================================================')
        print("1. Upload files")
        print("2. List company reports")
        print("3. List inspectors")
        print("4. View CO2 gas data")
        print("5. Visit reports")
        print("6. Calculation of emissions and fines")
        print("7. Analyzing unknown companies")
        print("9. Quit\n")

        try:
            choice = int(input("Your choice: "))
        except ValueError:
            choice = -1

        if choice == 1:
            upload_files()
        elif choice == 2:
            list_company_reports()
        elif choice == 3:
            list_inspectors()
        elif choice == 4:
            view_co2_gas_data()
        elif choice == 5:
            manage_visit_reports()
        elif choice == 6:
            calculate_emissions_and_fines()
        elif choice == 7:
            analyze_unknown_companies()
        elif choice == 9:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
