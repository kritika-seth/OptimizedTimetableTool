import pandas as pd
from itertools import combinations

file_path = 'C:/Users/kriti/Desktop/starsdb.csv'

starsdb = pd.read_csv(file_path)

def find_combinations(db, target_au):
    starsdb_no_duplicates = db.drop_duplicates(subset=['Course Code'])
    courses = starsdb_no_duplicates['Course Code'].tolist()
    au_values = starsdb_no_duplicates['AU'].tolist()
    combined_list = list(zip(courses, au_values))
    print(combined_list)
    possible_combinations = []
    unique_combinations = []

    for r in range(1, len(combined_list) + 1):
        for combo in combinations(combined_list, r):
            total_au = sum(au for course, au in combo)
            if total_au == target_au:
                courses_only = [course for course, _ in combo]
                possible_combinations.append(courses_only)

    for sublist in possible_combinations:
        unique_sublist = list(set(sublist))
        unique_sublist.sort()
        if unique_sublist not in unique_combinations:
            unique_combinations.append(unique_sublist)

    return unique_combinations

total_au = int(input("Total AU"))
print(find_combinations(starsdb, total_au))
