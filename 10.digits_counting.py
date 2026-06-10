num = int(input("Enter any number:"))
count = 0
while num>0:
    count+=1
    num//10
print(f"Total digits :{count}")