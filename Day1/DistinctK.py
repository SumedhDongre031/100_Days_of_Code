def find_kth_unique_string(strings, k):
    string_counts = {}
    for string in strings:
        if string in string_counts:
            string_counts[string] += 1
        else:
            string_counts[string] = 1

    unique_strings = [string for string, count in string_counts.items() if count == 1]

    if k > len(unique_strings):
        return ""

    return unique_strings[k - 1]

# Read input
n = int(input())
strings = [input().strip() for _ in range(n)]
k = int(input())

# Find and print the kth distinct string
result = find_kth_unique_string(strings, k)
print(result)
