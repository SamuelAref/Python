#Binary Search 
import math

array = [4,1,6,2,9,200,49,28,13,44,2,3,7]
find = False
start = 0
end = len(array) - 1
checkCounter = -1 #how many times it searches

searchingFor = int(input('which number do you want to search? '))

while checkCounter!= math.floor(len(array)/2):

    middle = math.floor((start + end) / 2)
    # print(middle) //checks how many times it searches
    checkCounter+=1

    if searchingFor < sorted(array)[middle]:

        end = middle - 1

    elif searchingFor > sorted(array)[middle]:

        start = middle + 1

    elif searchingFor == sorted(array)[middle] :
        find = True
        checkCounter = math.floor(len(array)/2)

print(find)