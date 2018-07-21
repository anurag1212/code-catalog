def permute(nums, i=0, ans=[], used=[]):
    if not nums:
        print(ans)
        return
    for n in nums:
        if n not in used:
            ans.append(n)
            used.append(n)
        permute(nums, i+1, ans, used)
        ans.pop()
        used.pop()

def permutes(s, ans):
    if not s:
        print ans
    for c in s:
        ans+=c
        permute(s, ans)

def permuterec(nums,l,r):
    if l==len(nums):
        print(nums)
        return
    for r in range(l,len(nums)):
        nums[l], nums[r] = nums[r], nums[l]
        permuterec(nums,l+1,r)
        nums[r], nums[l] = nums[l], nums[r]

permuterec("1234",0,3)

#TODO LATER
