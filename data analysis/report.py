def report_generate(total_revenal,total_average,summary,chart,report="Report_file.txt"):
    print("Simple Sale Report")
    print(f"Total Revenal : {total_revenal:.2f}")
    print(f"Total Average : {total_average:.2f}")
    print(f"Category Foe Sales : {summary.to_string(index=False)}")
    print(f"Chart is saved as : {chart}")

    with open(report, "w") as file:
        file.write(report)

        print(report)