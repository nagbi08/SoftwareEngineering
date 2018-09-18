#############################
# Created by Nebi Kirmali
# Date: 18-09-18
# Saxion Enschede
# Exercise: Find the sum of all the multiples of 3 or 5 below 1000
#############################
sum = 0;

for x in range(1, 1000):
    if(x%3)== 0 or ((x%5)== 0):
       sum = sum + x;
print(sum)






