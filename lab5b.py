#!/usr/bin/env python3
# Author ID: [seneca_id]

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    readfile = f.read()
    f.close
    return readfile

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    f = open(file_name, 'r')
    listlines_nl = list(f)
    listlines = []
    
    for line in listlines_nl:
        listlines.append(line.strip())
    f.close
    return listlines

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    file = open(file_name, 'a')
    file.write(string_of_lines)
    file.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    file = open(file_name, 'w')

    for line in list_of_lines:
        file.write(line + '\n')

    file.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    
    original_list = read_file_list(file_name_read)
    file_to_write = open(file_name_write, 'w')

    line_number = 1
    for line in original_list:
        line_with_number = str(line_number) + ':' + line + '\n'
        file_to_write.write(line_with_number)
        line_number = line_number + 1
        


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))