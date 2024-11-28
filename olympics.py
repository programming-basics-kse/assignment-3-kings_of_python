import argparse
import csv
import sys

parser = argparse.ArgumentParser()

parser.add_argument("file", type=str, help="Address of the file")
parser.add_argument("-medals", nargs="+", help="Write -medals")
parser.add_argument("-output", type=str, help="File for output")
parser.add_argument("-total", type=str, help="Write -total")
parser.add_argument("-overall", nargs="+", type=str, help="Write -overall and countries you want")
parser.add_argument("-interective", action='store_true', help="Write -interective to turn on interective mode" )
args = parser.parse_args()

medals = args.medals
output = args.output
total = args.total
overall = args.overall
interective = args.interective


def load_data():
    data = []
    try:
        with open ("athlete_events.tsv", "rt") as file:
            reader = csv.DictReader(file, delimiter = "\t")
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("File doesn't found")
        sys.exit(1)
    return data

def find_medals(data, country, year):
    have_medals = [row for row in data if
        row["Team"] == country or row["NOC"] == country and row["Year"] == year
    ]
    return have_medals

def count_medals(have_medals):
    medals = {"Gold":0, "Silver":0, "Bronze":0}
    for row in have_medals:
        if row["Medal"] in medals:
            medals[row["Medal"]] += 1
    return medals

def result(have_medals, medals):
    result = []
    result.append("First 10 medalists: ")
    for row in have_medals[:10]:
        result.append(f"{row["Name"]} - {row["Sport"]} - {row["Medal"]}")
    result.append("\n")
    result.append("Total number of medals by type: ")
    for medal,number in medals.items():
        result.append(f"{medal} - {number}")
    return "\n".join(result)

def total(data, year):
    countries_medals = {}
    for row in data:
        if row["Year"] == year and row["Medal"] in ["Gold","Silver","Bronze"]:
            country = row["Team"]
            if country not in countries_medals:
                countries_medals[country] = {"Gold":0,"Silver":0,"Bronze":0}
            countries_medals[country][row["Medal"]] += 1

    if not countries_medals:
        return "No medalists found"

    total_result = []
    total_result.append("All the countries medalists: ")
    for country,medals in countries_medals.items():
        total_result.append(f"{country} - {medals["Gold"]} - {medals['Silver']} - {medals['Bronze']}")
    return "\n".join(total_result)

def overall(data, countries):
    country_max = {}
    for country in countries:
        yearmedals = {}
        country_fromdata = [row for row in data if row["Team"] == country or row["NOC"] == country ]
        for row in country_fromdata:
            if row["Medal"] in ["Gold", "Silver", "Bronze"]:
               year = row["Year"]
               if year not in yearmedals:
                   yearmedals[year] = 0
               yearmedals[year] += 1

        if yearmedals:
            max_year = None
            max_amount = 0
            for year in yearmedals:
                if yearmedals[year] > max_amount:
                    max_year = year
                    max_amount = yearmedals[year]
            country_max[country] = (max_year, max_amount)
        else:
            country_max[country] = ("No medals", 0)

    return country_max

def interective(data):
    name_country = input("Write a country: ")
    country_data1 = [row for row in data if row["Team"] == name_country or row["NOC"] == name_country ]
    for row in country_data1:
        if row[""]

def main():
    data = load_data()

    if medals != None:
        if len(medals) == 2:
            if medals[1].isdigit():
                m_year= medals[1]
                m_team = medals[0]

    if args.interective:


    if args.overall:
       max_result = overall(data, args.overall)
       for country, (year, amount) in max_result.items():
           print(f"{country}: Year with most medals - {year}, overall medals - {amount}")
       return

    if args.total:
        total_data = total(data, args.total)
        print(total_data)
        return

    have_medals = find_medals(data, m_team, m_year)
    if not have_medals:
        print("No medalists found")
        sys.exit(1)

    count = count_medals(have_medals)
    results = result(have_medals, count)

    if args.output:
        with open(args.output, "wt") as file:
            file.write(results)
    else:
        print(results)

main()