from loaddata import loaded_Data
from cleandata import cleaned_data
from analyzer import analysis_data
from report import report_generate

def main():
    raw_data = loaded_Data()
    clean_data = cleaned_data(raw_data)
    total_revenal, total_average, summary, chart = analysis_data(clean_data)
    generate_data = report_generate(total_revenal, total_average, summary, chart)

if __name__ == "__main__":
    main()