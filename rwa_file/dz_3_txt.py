

def united_files(file1, file2, file3, file4):
    files_info = []
    for file_name in (file1, file2, file3):
        with open(file_name, 'r') as f:
            lines = f.readlines()
            files_info.append({
                'name': file_name,
                'line_count': len(lines),
                'lines': lines
            })
    
    sorted_files = sorted(files_info, key = lambda x: x['line_count'])
    with open(file4, 'w') as f:
        for file in sorted_files:
            f.write(f'{file['name']}\n')
            f.write(f'{file['line_count']}\n')
            f.writelines(file['lines'])
            f.write('\n')

united_files("file1.txt", "file2.txt", "file3.txt", "file4.txt")