#Bubble sort 
 # takes adjacent items in the list and compares them then exchanges them if the property is fulfilled

bubbleArray = [8, 2 , 5 ,2 ,3 ,4, 5, 3 ,2 , 1, 9 , 0, 7 ]

for j in range(len(bubbleArray) - 1):

    for i in range(len(bubbleArray)):
        
        if i < len(bubbleArray) -1:

            if bubbleArray[i] > bubbleArray[i + 1]:

                check = bubbleArray[i]
                bubbleArray[i] = bubbleArray[i + 1]
                bubbleArray[i + 1] = check

print(bubbleArray)