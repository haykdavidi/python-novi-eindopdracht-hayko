import os
import companies_module as companies
import inspectors_module as inspectors
import reports_module as reports
import unknown_company_measurements_module as measure


def read_all_files():
    """Reads all necessary files"""
    CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    file_paths = [
        os.path.join(CURRENT_DIRECTORY, "assignment-files", "companies.txt"),
        os.path.join(CURRENT_DIRECTORY, "assignment-files", "inspectors.txt"),
        os.path.join(CURRENT_DIRECTORY, "assignment-files", "visit_reports.txt"),
        os.path.join(CURRENT_DIRECTORY, "assignment-files", "gases.csv")
    ]
    upload_functions = [
        companies.upload_companies,
        inspectors.upload_inspectors,
        reports.upload_reports,
        measure.calculate_analysis_report
    ]

    for file_path, upload_func in zip(file_paths, upload_functions):
        upload_func(file_path)

    print("Files have been uploaded.")
