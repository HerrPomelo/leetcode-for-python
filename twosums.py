def twosums[nums,i,a,b,target]
    # 任意给出一个序列num
    int i=len(nums)
    int a=0, b=0
    while a<(i-1):
    	while num(a)+num(b)==target:
    	    if a==b:
    	    	jump;
    	    else:
    	         print(num(a),num(b));
    	else b=b+1;
    else b=b+1;





class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        # 定义一个字典
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i





class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i + 1
            else:
                return map[num[i]], i + 1

        return -1, -1