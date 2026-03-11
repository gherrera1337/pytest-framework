import csv

def test_csv_ops():
    with open("basic-data.csv", mode="r") as file:
        csv_file = csv.reader(file)
        for line in csv_file:
            print(line)


