
import csv

def generate_report(data):

    with open(
        "monthly_budget_report.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            [
                "Department",
                "Allocated",
                "Spent"
            ]
        )

        for item in data:

            writer.writerow(
                [
                    item["department"],
                    item["allocated"],
                    item["spent"]
                ]
            )

    return "Report Generated"