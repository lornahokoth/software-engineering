def twoSum(num, target):
    for num1 in range(len(num)):
        for num2 in range(num1+1, len(num)):
            if num[num1] + num[num2] == target:
                print("[" + str(num1) + "," + str(num2) + "]")


twoSum([2, 7, 11, 15], 9)
twoSum([3, 2, 4], 6)
twoSum([3, 3], 6)
