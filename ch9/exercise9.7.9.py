def count_reversed():
    solution_dictionary = {}
    for age_difference in range(16, 35):
        ages = []
        for child in range(0, 82):
            parent = child + age_difference
            if str(child).zfill(2) == str(parent)[::-1]: ages.append((child, parent))
        
        solution_dictionary[age_difference] = ages

    return solution_dictionary

# It's interesting how the only age differnces that produce these palendromic ages at all are 18 and 27
print(count_reversed())
