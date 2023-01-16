#LogArray is a 1D array containing 500 elements of type STRING.
#A procedure, LogEvents, is required to add data from the array to the end of the existing text file
#LoginFile.txt
#Unused array elements are assigned the value "Empty". These can occur anywhere in the array
#and should not be added to the file.
#Write pseudocode for the procedure LogEvents.
#Refer to the Insert for the list of pseudocode functions and operators.

# add the path of an existing file at line 14 within ""

def LogEvents():
    LogArray = ["glide", "Empty", "clear", "Empty", "rumor"]
    # opening file in append mode, replace the path of your file within "" 
    fhandle = open(r"", "a")
    # \n added just for formatting
    for i in LogArray:
        if i != "Empty":
            fhandle.write(LogArray[LogArray.index(i)])
            fhandle.write('\n')
    fhandle.close()
    return "strings appended successfully."
print(LogEvents())
