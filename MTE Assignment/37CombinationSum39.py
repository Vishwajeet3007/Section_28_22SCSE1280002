def combinationSum(candidates,target):
    def backtrack(start,target,curr_combination):
        if target == 0:
            result.append(list(curr_combination))
            return
        if target < 0:
            return
        for i in range(start,len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            curr_combination.append(candidates[i])
            backtrack(i ,target - candidates[i],curr_combination)
            curr_combination.pop()
    candidates.sort()
    result = []
    backtrack(0,target,[])
    return result
candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates,target))
candidates = [2,3,5]
target = 8
print(combinationSum(candidates,target))