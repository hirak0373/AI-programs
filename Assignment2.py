arr = []
import random
for i in range(1000):
        arr.append(random.randint(1,1000))
temp=arr[0]
print(arr)
index=0
for j in range(len(arr)):
   if temp > arr[j]:
    #   print(arr[j])
       temp=arr[j]
       index=j
print ("Minimum value: ",temp,"    at index nbr: ",index)

for j in range(len(arr)):
   if temp < arr[j]:
  
       temp=arr[j]
       index=j
print ("Maximum value: ",temp,"    at index nbr: ",index)
sum=0
for k in range(len(arr)):
    sum=sum+arr[k]

mean=sum/len(arr)
print("Mean: ",mean)