log_file = open("um-server-01.txt") # Opens the file containing the sales report data.


def sales_reports(log_file): # This defines a function that takes a log_file as an parameter.
    for line in log_file: # Goes through each line in the log_file paramter. (Just a foor loop)
        line = line.rstrip() # Removes the line ending at the end of the stirng.
        day = line[0:3] # Grabs the first 3 chars of the line, which in this case are a day.
        if day == "Mon": # Checks the first 3 chars set above and if they're equal to a value
            print(line) # prints the value to the console. Similar to console.log in JavaScript

        melon = line.split()
        if int(melon[2]) > 10:
            print(f'Larger order: {line}')


sales_reports(log_file) # Calls the function defined above passing through the log_file var set on line 1.
