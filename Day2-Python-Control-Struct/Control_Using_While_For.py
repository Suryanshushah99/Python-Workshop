#while loop
words=["hello","world","echo","dat"]

i=0
max=len(words)-1

while  i<=max:
	print(words[i]+"!")
	i+=1


#for loop
for word in words:
	print(word+"!")
i=[1,2,3,words]
for i in i:
	print(i)
#loops with range function
for i in range(7):
	print("hello")

#while loop continue break
i = 0
while True:
    i = i +1
    if i == 2:
        print("Skipping 2")
        continue
    if i == 5:
        print("Breaking")
        break
    print(i)

print("Finished")
