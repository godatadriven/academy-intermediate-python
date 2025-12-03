# with for-loop
counter=0
for item in shopping_list:
    if item.lower()[0] in 'aeiou':
        counter +=1
print(counter)

# with list-comprehension
len([1 for item in shopping_list if item.lower()[0] in 'aeiou'])