# Read the original file and store its content
original_file_path = 'original_file.txt'
with open(original_file_path, 'r') as original_file:
    original_content = original_file.readlines()

# Determine how many times the content needs to be written to reach 10 million records
total_records = 10_000_000
times_to_write = total_records // len(original_content)

# Write the content multiple times to create the new file
new_file_path = 'cloned_file.txt'
with open(new_file_path, 'w') as cloned_file:
    for _ in range(times_to_write):
        cloned_file.writelines(original_content)

print(f'{total_records} records have been written to {new_file_path}')

