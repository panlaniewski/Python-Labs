user_str = input("Введите любую строку: ")

if user_str == "":
    print(0)
else:  
    result_str = ""
    counter = 1
    for i in range(1, len(user_str)):
        if user_str[i] == user_str[i-1]:
            counter += 1
        else:
            result_str += user_str[i-1] + str(counter)
            counter = 1
    result_str += user_str[-1] + str(counter)
        
    print(result_str)