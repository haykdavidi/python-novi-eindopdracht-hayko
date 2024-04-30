import companies_module as companies
import inspectors_module as insp
import reports_module as reports
from datetime import datetime


def print_menu():
    print("=" * 70)
    print("Visit Report Menu")
    print("-" * 70)
    print("1. Overview visit reports")
    print("2. Overview of visit report inspectors")
    print("3. Overview of visit report companies")
    print("0. Quit\n")


def manage_reports_choice():
    while True:
        print_menu()
        try:
            report_choice = int(input("Your choice: "))
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        if report_choice == 1:
            reports.show_reports()
        elif report_choice == 2:
            manage_inspector_reports()
        elif report_choice == 3:
            manage_company_reports()
        elif report_choice == 0:
            return False
        else:
            print("Invalid choice")


def manage_inspector_reports():
    while True:
        try:
            if not insp.is_inspectors_list_complete():
                return False  # Terug naar het vorige menu
            insp.show_inspectors_code_and_name()
            inspector_choice = input("Choose the inspector code: ")
            if not insp.inspector_exists(inspector_choice):
                print("The inspector code was not found")
                return False  # Terug naar het vorige menu
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        try:
            start_or_end_date = ask_for_start_or_end_date()
            if start_or_end_date == "n":
                reports.show_report_by_inspector(inspector_choice)
            else:
                chosen_start_date = user_input_date(
                    "Choose a start date (YYYY-MM-DD): "
                )
                chosen_end_date = user_input_date(
                    "Choose an end date (YYYY-MM-DD): "
                )
                reports.show_report_by_inspector(
                    inspector_choice, chosen_start_date, chosen_end_date
                )
            break
        except ValueError:
            print("Invalid input. Please try again.")


def manage_company_reports():
    while True:
        try:
            if not companies.is_company_list_complete():
                return False  # Terug naar het vorige menu
            companies.show_company_code_and_name()
            company_code_choice = input("Choose the company code: ")
            if not companies.company_exists(company_code_choice):
                print("This company code does not exist")
                return False  # Terug naar het vorige menu
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        try:
            start_or_end_date = ask_for_start_or_end_date()
            if start_or_end_date == "n":
                reports.show_report_company(company_code_choice)
            else:
                chosen_start_date = user_input_date(
                    "Choose start-date (YYYY-MM-DD): "
                )
                chosen_end_date = user_input_date(
                    "Choose end-date (YYYY-MM-DD): "
                )
                reports.show_report_company(
                    company_code_choice, chosen_start_date, chosen_end_date
                )
            break
        except ValueError:
            print("Invalid input. Please try again.")


def ask_for_start_or_end_date():
    while True:
        choice_date = input(
            "Do you want to search with a start and an end date? (yes - 'y')/(no - 'n'): "
        )
        choice_date = choice_date.lower()
        if choice_date not in {"y", "n"}:
            print("Choose 'y' or 'n'")
        else:
            return choice_date


def user_input_date(prompt):
    while True:
        input_user = input(prompt)
        try:
            correct_date = datetime.strptime(input_user, "%Y-%m-%d").date()
            return correct_date
        except ValueError:
            print("Use format YYYY-MM-DD please")
