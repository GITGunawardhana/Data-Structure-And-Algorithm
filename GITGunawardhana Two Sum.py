nums1, target1 = input().strip().split(", ")
n = nums1.split("=")[1].strip()
d = len(n)
nums = list(map(int, n[1:d-1].split(",")))
target = int(target1.split("=")[1].strip())


def twoSum(nums, target):
        result = []
        index_map = {}
        for i, n in enumerate(nums):
            difference = target - n
            if difference in index_map:
                result.append(i)
                result.append(index_map[difference])
                break
            else:
                index_map[n] = i
        return result

print(twoSum(nums, target))
