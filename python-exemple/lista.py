def list_manipulation(list_, command, location, value=0):
    if command == "remove":
        if location == "end":
            return list_.pop()
        if location == "beginning":
            return list_.pop(0)
    elif command == "add":
        if location == "beginning":
            list_.insert(0, value)
            return list_
        if location == "end":
            list_.append(value)
            return list_
    else:
        return "Something is WRONG!"
    
list_manip = list_manipulation([2, 5, 7, 1, 9], "add", "end", 1)
print(list_manip)