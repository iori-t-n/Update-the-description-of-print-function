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
    if stripped_line[0:5] == "print":
        pre_index = stripped_line.index(POSTFIX)
        contents = stripped_line[6 : pre_index]
        rest_line = stripped_line[pre_index :]
        spaces = " " * (len(line) - len(stripped_line))
        new_line = "{0}print({1}){2}".format(spaces, contents, rest_line)
        return new_line
    else:
        return line

# # Some simple tests
# print(update_line(""))
# print(update_line("foobar()"))  
# print(update_line("print 1 + 1</pre></td><td>"))      
# print(update_line("    print 2, 3, 4</pre></td><td>"))

# Expected output
##
##foobar()
##print(1 + 1)</pre></td><td>
##    print(2, 3, 4)</pre></td><td>


def update_pre_block(pre_block):
    """
    Take a string that correspond to a <pre> block in html and parses it into lines.  
    Returns string corresponding to updated <pre> block with each line
    updated via process_line()
    """
    block_list = pre_block.split(PREFIX)
    # print(block_list)
    updated_list = []

    for item in block_list:
        new_item = update_line(item)
        # print(new_item)
        updated_list.append(new_item)
    
    updated_block = PREFIX.join(updated_list)
    return updated_block

# # Some simple tests
# print(update_pre_block(""))
# print(update_pre_block("foobar()"))
# print(update_pre_block("if foo():<pre class='cm'>    bar()"))
# print(update_pre_block("<pre class='cm'>print</pre></td><td><pre class='cm'>print 1+1</pre></td><td><pre class='cm'>print 2, 3, 4</pre></td><td>"))
# print(update_pre_block("<pre class='cm'>    print a + b</pre></td><td><pre class='cm'>    print 23 * 34</pre></td><td><pre class='cm'>        print 1234</pre></td><td>"))

# Expected output
##
##foobar()
##if foo():<pre class='cm'>    bar()
##<pre class='cm'>print()</pre></td><td><pre class='cm'>print(1+1)</pre></td><td><pre class='cm'>print(2, 3, 4)</pre></td><td>
##<pre class='cm'>    print(a + b)</pre></td><td><pre class='cm'>    print(23 * 34)</pre></td><td><pre class='cm'>        print(1234)</pre></td><td>

def update_file(input_file_name, output_file_name):
    """
    Open and read the file specified by the string input_file_name
    Process the <pre> blocks in the loaded text to update print syntax
    Write the update text to the file specified by the string output_file_name
    """
    
    # open file and read text in file as a string
    # openfile = open(input_file_name, "rt")

    # split text in <pre> blocks and update using update_pre_block()

    # Write the answer in the specified output file
    

# A couple of test files
# update_file("table.html", "table_updated.html")
# update_file("docs.html", "docs_updated.html")

# Import some code to check whether the computed files are correct
##import examples3_file_diff as file_diff
##file_diff.compare_files("table_updated.html", "table_updated_solution.html")
##file_diff.compare_files("docs_updated.html", "docs_updated_solution.html")

# Expected output
##table_updated.html and table_updated_solution.html are the same
##docs_updated.html and docs_updated_solution.html are the same
