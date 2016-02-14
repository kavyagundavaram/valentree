import csv, pprint

def parse():
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            users[row['user_num']] = {
                "user_name": row['user_name'],
                "match": {
                    "match_name": row['match_name'],
                    "match_school": row['match_school'],
                    "interest": row['interest'],
                    "day": row['day'],
                    "time": row['time'],
                    "airport": row['airport'],
                    "matched_num": row["matched_num"]
                }
            }

parse()
