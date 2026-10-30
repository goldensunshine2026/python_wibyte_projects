import csv


# ============================================================
# FUNCTION 1: READ DATA FROM A CSV FILE
# ============================================================

def read_csv_data(filename):

    if not filename.lower().endswith(".csv"):
        filename += ".csv"

    with open(filename, "r", newline="", encoding="utf-8-sig") as csv_file:

        reader = csv.DictReader(csv_file)

        if not reader.fieldnames:
            raise ValueError(filename + " has no column headings.")

        data = []

        for row in reader:
            if any(value and value.strip() for value in row.values()):
                data.append(row)

    if not data:
        raise ValueError(filename + " contains no data.")

    return data


# ============================================================
# FUNCTION 2: DISPLAY EVERY ROW IN A TABLE
# ============================================================

def print_table(table):

    if not table:
        print("No data available.")
        return

    headings = list(table[0].keys())

    # Calculate column widths using every row.
    widths = {}

    for heading in headings:

        longest_value = max(
            len(str(row.get(heading, "")))
            for row in table
        )

        widths[heading] = max(len(heading), longest_value)

    # Display column headings.
    heading_line = " | ".join(
        heading.ljust(widths[heading])
        for heading in headings
    )

    print(heading_line)
    print("-" * len(heading_line))

    # Display EVERY player or tournament entry.
    for row in table:

        row_line = " | ".join(
            str(row.get(heading, "")).ljust(widths[heading])
            for heading in headings
        )

        print(row_line)

    print("-" * len(heading_line))
    print("Total records displayed:", len(table))


# ============================================================
# FUNCTION 3: ANALYSE PLAYER RANKINGS
# ============================================================

def analyze(title, data):

    print("\n")
    print("=" * 80)
    print(title)
    print("=" * 80)

    # Display every player, not just a few.
    print_table(data)

    countries = {
        row.get("Country", "").strip()
        for row in data
        if row.get("Country", "").strip()
    }

    ratings = []

    for row in data:

        try:
            ratings.append(float(row.get("Rating", "")))

        except (ValueError, TypeError):
            pass

    print("\nANALYSIS RESULTS")
    print("-" * 80)

    print("Total players:", len(data))
    print("Number of countries:", len(countries))

    if countries:
        print("Countries:", ", ".join(sorted(countries)))

    if ratings:
        print("Highest rating:", max(ratings))
        print("Lowest rating:", min(ratings))
        print("Average rating:", round(sum(ratings) / len(ratings), 2))

    print("=" * 80)


# ============================================================
# FUNCTION 4: COMPARE ALL THREE FORMATS
# ============================================================

def compare_all_formats():

    odi_data = read_csv_data("CricketODI")
    test_data = read_csv_data("CricketTest")
    t20_data = read_csv_data("CricketT20")

    # Display every player in each format.
    analyze("ODI INTERNATIONAL RANKINGS", odi_data)
    analyze("TEST INTERNATIONAL RANKINGS", test_data)
    analyze("T20 INTERNATIONAL RANKINGS", t20_data)

    # Create sets of player names.
    odi_players = {
        row.get("Player", "").strip()
        for row in odi_data
        if row.get("Player", "").strip()
    }

    test_players = {
        row.get("Player", "").strip()
        for row in test_data
        if row.get("Player", "").strip()
    }

    t20_players = {
        row.get("Player", "").strip()
        for row in t20_data
        if row.get("Player", "").strip()
    }

    # Players appearing in all three formats.
    common_players = odi_players & test_players & t20_players

    print("\nPLAYERS IN ALL THREE FORMATS")
    print("-" * 80)

    if common_players:
        for player in sorted(common_players):
            print(player)
    else:
        print("None")

    # Players appearing in any format.
    all_players = odi_players | test_players | t20_players

    print("\nTotal different players across all formats:", len(all_players))

    # Players appearing only in ODI.
    only_odi = odi_players - (test_players | t20_players)

    print("\nPLAYERS ONLY IN ODI")

    if only_odi:
        for player in sorted(only_odi):
            print(player)
    else:
        print("None")

    # Players appearing only in Test.
    only_test = test_players - (odi_players | t20_players)

    print("\nPLAYERS ONLY IN TEST")

    if only_test:
        for player in sorted(only_test):
            print(player)
    else:
        print("None")

    # Players appearing only in T20.
    only_t20 = t20_players - (odi_players | test_players)

    print("\nPLAYERS ONLY IN T20")

    if only_t20:
        for player in sorted(only_t20):
            print(player)
    else:
        print("None")


# ============================================================
# FUNCTION 5: DISPLAY TOURNAMENT-WINNING CAPTAINS
# ============================================================

def show_tournament_captains(filename, tournament_name):

    data = read_csv_data(filename)

    print("\n")
    print("=" * 80)
    print(tournament_name.upper())
    print("=" * 80)

    # Display every tournament entry and captain.
    print_table(data)

    captains = {
        row.get("Captain", "").strip()
        for row in data
        if row.get("Captain", "").strip()
    }

    print("\nCAPTAIN ANALYSIS")
    print("-" * 80)

    print("Number of different captains:", len(captains))

    if captains:

        print("\nList of captains:")

        for captain in sorted(captains):
            print(captain)

    # Count appearances in the file.
    captain_counts = {}

    for row in data:

        captain = row.get("Captain", "").strip()

        if captain:
            captain_counts[captain] = captain_counts.get(captain, 0) + 1

    print("\nCaptains appearing more than once:")

    repeated = False

    for captain, count in sorted(captain_counts.items()):

        if count > 1:
            print(captain, "-", count, "entries")
            repeated = True

    if not repeated:
        print("None")


# ============================================================
# FUNCTION 6: DISPLAY THE MAIN MENU
# ============================================================

def display_menu():

    print("\n")
    print("=" * 60)
    print("             CRICKET ANALYSIS PROJECT")
    print("=" * 60)

    print("1. ODI International Rankings")
    print("2. Test International Rankings")
    print("3. T20 International Rankings")
    print("4. Compare All Three Formats")

    print("-" * 60)

    print("5. World Cup Winning Captains")
    print("6. T20 World Cup Winning Captains")
    print("7. Asia Cup Winning Captains")
    print("8. Champions Trophy Winning Captains")
    print("9. World Test Championship Winning Captains")

    print("-" * 60)
    print("0. Exit")
    print("=" * 60)


# ============================================================
# FUNCTION 7: PROCESS MENU CHOICES
# ============================================================

def run_choice(choice):

    if choice == "1":

        data = read_csv_data("CricketODI")
        analyze("ODI INTERNATIONAL RANKINGS", data)

    elif choice == "2":

        data = read_csv_data("CricketTest")
        analyze("TEST INTERNATIONAL RANKINGS", data)

    elif choice == "3":

        data = read_csv_data("CricketT20")
        analyze("T20 INTERNATIONAL RANKINGS", data)

    elif choice == "4":

        compare_all_formats()

    elif choice == "5":

        show_tournament_captains(
            "WorldCupCaptains",
            "World Cup Winning Captains"
        )

    elif choice == "6":

        show_tournament_captains(
            "T20WorldCupCaptains",
            "T20 World Cup Winning Captains"
        )

    elif choice == "7":

        show_tournament_captains(
            "AsiaCupCaptains",
            "Asia Cup Winning Captains"
        )

    elif choice == "8":

        show_tournament_captains(
            "ChampionsTrophyCaptains",
            "Champions Trophy Winning Captains"
        )

    elif choice == "9":

        show_tournament_captains(
            "WorldTestChampionshipCaptains",
            "World Test Championship Winning Captains"
        )

    elif choice == "0":

        print("\nThank you for using the Cricket Analysis Project!")
        return False

    else:

        print("\nInvalid choice. Enter a number from 0 to 9.")

    return True


# ============================================================
# FUNCTION 8: MAIN PROGRAM
# ============================================================

def main():

    print("\nWelcome to the Cricket Analysis Project!")
    print("All results will be displayed on the screen.")

    while True:

        display_menu()

        choice = input("Enter your choice (0-9): ").strip()

        try:

            if not run_choice(choice):
                break

        except FileNotFoundError as error:

            print("\nERROR: A required CSV file was not found.")
            print("Make sure the file is in your project folder.")
            print("Details:", error)

        except (ValueError, KeyError) as error:

            print("\nERROR while processing the data:", error)

        except PermissionError:

            print("\nERROR: Permission denied while reading a file.")

        except OSError as error:

            print("\nFILE ERROR:", error)


# ============================================================
# START THE PROGRAM
# ============================================================

if __name__ == "__main__":
    main()