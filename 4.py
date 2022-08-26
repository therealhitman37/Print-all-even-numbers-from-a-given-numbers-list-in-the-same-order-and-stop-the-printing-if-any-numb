#Print all even numbers from a given numbers list 
#in the same order and stop the printing if any numbers that come after 237 in the sequence

#Input the list
list = list(map(int, input('Enter a list of number: ').split(',')))


def l():
    numbers = []
    for i in list:
        if i %2 == 0 and i < 237:
            numbers.append(i)
        elif i >237:
            break
        
    return numbers        

print(l())

        

        

