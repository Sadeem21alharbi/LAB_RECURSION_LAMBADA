## 2) Given a list of numbers : `[40,35, 10, 15, 20]`

#### create a new list containing each number from the previous list mutliplied by itself.
#### print the new list.
#### Note: use `map()` with a `lambda funciton`


numbers = [40 ,35, 10, 15, 20]

new_list = list(map(lambda x : x*x , numbers))

print (new_list)
