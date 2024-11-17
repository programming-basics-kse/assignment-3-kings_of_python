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

    parsed_args = parser.parse_args(args)
    parsed_args.medals = True
    return parsed_args

def load_data():
    data = []
    try:
        with open ("Olympic Athletes - athlete_events.tsv", "rt") as file:
            reader = csv.DictReader(file, delimiter = "\t")
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)
    return data

