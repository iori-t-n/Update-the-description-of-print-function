"""
Week 4 practice project for Python Data Representation
Update syntax for print in a HTML file
from "print ..." syntax in Python 2 to "print(...)" syntax for Python 3
"""
# In HTML, "print ..." syntax is written as <pre class='cm'>print 12</pre></td><td><pre>12</pre> for Python 2 in HTML files

# HTML tags that bounds example code
PREFIX = "<pre class='cm'>"
POSTFIX = "</pre>"
PRINT = "print"


def update_line(line):
    """
    Takes a string line representing a single line of code
    and returns a string with print updated
    """

    # Strip left white space using built-in string method lstrip()
    stripped_line = line.lstrip()

    # If line is print statement,  use the format() method to add insert parentheses
    if stripped_line[: len(PRINT)] == "print":
        contents = stripped_line[len(PRINT) + 1 :]
        spaces = " " * line.find(PRINT)
        return "{}print({})".format(spaces, contents)
    return line

# # Some simple tests
# print(update_line(""))
# print(update_line("foobar()"))  
# print(update_line("print 1 + 1"))      
# print(update_line("    print 2, 3, 4"))

# Expect output
##
##foobar()
##print(1 + 1)
##    print(2, 3, 4)


def update_pre_block(pre_block):
    """
    Take a string that correspond to a <pre> block in html and parses it into lines.  
    Returns string corresponding to updated <pre> block with each line
    updated via update_line()
    """
    block_list = pre_block.split("\n")
    # print(block_list)
    updated_block = update_line(block_list[0])

    for item in block_list[1 :]:
        updated_block += "\n"
        updated_block += update_line(item)
           
    return updated_block

# # Some simple tests
# print(update_pre_block(""))
# print(update_pre_block("foobar()"))
# print(update_pre_block("if foo():\n    bar()"))
# print(update_pre_block("print\nprint 1+1\nprint 2, 3, 4"))
# print(update_pre_block("    print a + b\n    print 23 * 34\n        print 1234"))

# Expected output
##
##foobar()
##if foo():
##    bar()
##print()
##print(1+1)
##print(2, 3, 4)
##    print(a + b)
##    print(23 * 34)
##        print(1234)


def update_file(input_file_name, output_file_name):
    """
    Open and read the file specified by the string input_file_name
    Process the <pre> blocks in the loaded text to update print syntax
    Write the update text to the file specified by the string output_file_name
    """
    
    # open file and read text in file as a string
    input_file= open(input_file_name, "rt")
    input_data = input_file.read()

    # split text in <pre> blocks and update using update_pre_block()
    split_data = input_data.split(PREFIX)
    updated_data = split_data[0]

    for item in split_data[1 :]:
        updated_data += PREFIX
        [pre_block, filler] = item.split(POSTFIX, 1)
        updated_data += update_pre_block(pre_block)
        updated_data += POSTFIX
        updated_data += filler

    # Write the answer in the specified output file
    output_file = open(output_file_name, "wt")
    output_file.write(updated_data)
    
    input_file.close()
    output_file.close()


# A couple of test files
update_file("table.html", "table_updated.html")
update_file("docs.html", "docs_updated.html")

# Import some code to check whether the computed files are correct
import examples3_file_diff as file_diff
file_diff.compare_files("table_updated.html", "table_updated_solution.html")
file_diff.compare_files("docs_updated.html", "docs_updated_solution.html")

# # Expected output
# ##table_updated.html and table_updated_solution.html are the same
# ##docs_updated.html and docs_updated_solution.html are the samed
