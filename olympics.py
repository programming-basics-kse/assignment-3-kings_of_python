import argparse
import csv
import sys

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("file", type=str, help = "Address of the file")
    parser.add_argument("-medals", action = "store_true", help = "Write -medals")
    parser.add_argument("country",type=str, help = "The country, team or code ")
    parser.add_argument("year", type=str, help = "The year of the event")
    parser.add_argument("-output", type=str, help = "File for output")

    args = sys.argv[1:]

    if len(args)>1 and args[1] == "-medals":
        args.pop(1)
    else:
        print("Please enter -medals as a second argument")
        sys.exit(1)

    args = parser.parse_args(args)
    args.medals = True
    return args

def load_data():
    data = []
    try:
        with open ("athlete_events.tsv", "rt") as file:
            reader = csv.DictReader(file, delimiter = "\t")
            for row in reader:
                data.append(row)
        return data
    except FileNotFoundError:
        print("File doesn't found")
        sys.exit(1)

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

def main():
    args = parse_args()
    data = load_data()
    have_medals = find_medals(data, args.country, args.year)
    count = count_medals(have_medals)
    results = result(have_medals, count)

    if not have_medals:
        print("No medalists found")
        sys.exit(1)

    if args.output:
        with open(args.output, "wt") as file:
            file.write(results)
    else:
        print(results)


main()

