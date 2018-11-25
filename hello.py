# hello.py was created in the same folder
print("VS Code to run Python file")

print("########################")
print(" ")
print(" ")

l=[1,2,3,4]
counter=0
for item in l:

    l[counter]=(item*2)
    counter=counter+1
print (l)  


print("########################")
print(" ")
print(" ")


l=[1,2,3,4]
for item in enumerate(l):
    print(item)

print("########################")
print(" ")
print(" ")



l=[1,2,3,4]
print(list(map(lambda x: x*2, l)))

print("########################")
print(" ")
print(" ")




# util.py was created in the same folder and contains my_sum func
import util

print (util.my_sum(5,3))

