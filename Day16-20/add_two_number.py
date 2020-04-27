def twoSum(nums,target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i ,num in enumerate(nums):
        j=hashmap.get(target-num)
        if j is not None:
            return [i,j]
        continue

def main():
    nums=[2,3,6,9,11,17,19,15]
    target=17
    print(twoSum(nums,target))

if __name__ == "__main__":
    main()