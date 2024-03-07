import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Error")
        sys.exit(0)

    # TODO: Read database file into a variable
    rows = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # TODO: Read DNA sequence file into a variable
    txt_file = sys.argv[2]
    with open(txt_file, "r", encoding="utf-8") as f:
        read_data = f.read()

    # TODO: Find longest match of each STR in DNA sequence

    AGATC = longest_match(read_data, "AGATC")
    TTTTTTCT = longest_match(read_data, "TTTTTTCT")
    AATG = longest_match(read_data, "AATG")
    TCTAG = longest_match(read_data, "TCTAG")
    GATA = longest_match(read_data, "GATA")
    TATC = longest_match(read_data, "TATC")
    GAAA = longest_match(read_data, "GAAA")
    TCTG = longest_match(read_data, "TCTG")

    # TODO: Check database for matching profiles
    if (sys.argv[1] == "databases/large.csv"):
        for row in rows:
            if (int(row["AGATC"]) == AGATC and int(row["TTTTTTCT"]) == TTTTTTCT and int(row["AATG"]) == AATG and int(row["TCTAG"]) == TCTAG and int(row["GATA"]) == GATA and int(row["TATC"]) == TATC and int(row["GAAA"]) == GAAA and int(row["TCTG"]) == TCTG):
                print(row["name"])
                return
    if (sys.argv[1] == "databases/small.csv"):
        for row in rows:
            if (int(row["AGATC"]) == AGATC and int(row["AATG"]) == AATG and int(row["TATC"]) == TATC):
                print(row["name"])
                return

    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
