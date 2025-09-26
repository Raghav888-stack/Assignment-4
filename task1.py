

print("Reading file content:")
try:
    with open("sample.txt", "r") as file1:
        for i, line in enumerate(file1, 1): 
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")


