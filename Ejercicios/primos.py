
def primo():
    for num in range(1,101):
        if num>1:
            for index in range(2,num):
                if num % index == 0:
                    break
            else:
                print(num) 
primo()



