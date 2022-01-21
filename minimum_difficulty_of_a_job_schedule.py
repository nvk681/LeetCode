from functools import lru_cache

def minDifficulty(jobDifficulty, d: int) -> int:
    if d>len(jobDifficulty):
        return -1
    if d == len(jobDifficulty):
        return sum(jobDifficulty)
    hardest_job_left = [0]*len(jobDifficulty)
    hard = 0
    for index in range(len(jobDifficulty)-1,-1,-1):
        hard = max(hard, jobDifficulty[index])
        hardest_job_left[index] = hard
    @lru_cache(None)
    def find_min(i, day):
        if day == d:
            return hardest_job_left[i]
        hardest = 0
        best = float("inf")
        for j in range(i, len(jobDifficulty) - (d - day)):
                hardest = max(hardest, jobDifficulty[j])
                best = min(best, hardest + find_min(j + 1, day + 1))
        return best
    return find_min(0, 1)

print(minDifficulty([6,5,4,3,2,1], 2))