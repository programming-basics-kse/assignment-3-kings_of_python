with open("Olympic Athletes - athlete_events.tsv", "rt") as file:
    next_line = file.readline()
    while next_line:
        next_line = file.readline()
        print(next_line)