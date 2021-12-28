import os
current_folder = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(current_folder, "list.md")

file = open(input_path, "r")
file_str = file.read()
lines = file_str.split("\n")

def no_empty_lines(string):
    print(string)
    if(string == ""):
        return False
    return True
new_lines = list(filter(no_empty_lines, lines))

for i in range(0, len(new_lines)):
    new_lines[i] = "#{}: {}".format(i+1, new_lines[i]) 
new_string = '\n'.join(new_lines)
file = open(input_path, "w")
file.write(new_string)