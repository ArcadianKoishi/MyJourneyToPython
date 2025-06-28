"""
给定一个整数数组nums和一个整数目标值target
请你在该数组中找出和为目标值target的那两个整数,并返回它们的数组下标。
你可以假设每种输入只会对应一个答案
并且你不能使用两次相同的元素(如nums=[3,2,4],target=6,不可选择3+3)

示例 1:
输入:nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

示例 2:
输入:nums = [3,2,4], target = 6
输出：[1,2]

示例 3:
输入:nums = [3,3], target = 6
输出：[0,1]

提示：
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案"""

def func(nums,target):
    l1={}
    for i in range(len(nums)):
        if (target-nums[i] in l1):
            return [l1[target-nums[i]],i]
        l1[nums[i]]=i

def test():
    testnums=[[3,3],[2,7,11,5],[3,2,4]]
    targetl=[6,9,6]
    ans=[[0,1],[0,1],[1,2]]
    for test in range(3):
        a=testnums[test]
        b=targetl[test]
        c=ans[test]
        print(func(a,b)==c)

test()