# //Google Question
# //Given an array = [2,5,1,2,3,5,1,2,4]:
# //It should return 2

# //Given an array = [2,1,1,2,3,5,1,2,4]:
# //It should return 1

# //Given an array = [2,3,4,5]:
# //It should return undefined

# //Bonus... What if we had this:
# // [2,5,5,2,3,5,1,2,4]
# // return 5 because the pairs are before 2,2

def FRC(arr):
    d={}
    for item in arr:
        if item in d:
            return item
        else:
            d[item]=1
    return "Undefined"

arr=list(map(int,input().split()))
print(FRC(arr))