def find_duplicates(numbers):
    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return duplicates

data = [10, 20, 30, 10, 40, 20, 50]

result = find_duplicates(data)

print("Duplicate values:", result)