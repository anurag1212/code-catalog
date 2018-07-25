def permuteiter(nums):
    s=[("".join(nums),0)]
    while s:
        nums, l = s.pop()
        if l == len(nums):
            print(nums)
        else:
            nums = list(nums)
            for r in range(l, len(nums)):
                nums[l], nums[r] = nums[r], nums[l]
                s.append(("".join(nums), l+1))
                nums[r], nums[l] = nums[l], nums[r]

def permuterec(nums,l=0):
    if l==len(nums):
        print(nums)
        return
    for r in range(l,len(nums)):
        nums[l], nums[r] = nums[r], nums[l]
        permuterec(nums,l+1)
        nums[r], nums[l] = nums[l], nums[r]

permuteiter(list("ABCD"))
permuterec(list("ABCD"))
# I basically just converted recursive to iterative.
# And recursive I looked up.
