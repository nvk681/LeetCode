from black import schedule_formatting


def minDifficulty(jobDifficulty, d) -> int:
        jobs = len(jobDifficulty)
        if jobs < d : return -1
        schedule = [[float('inf')]*jobs for _ in range(d)]
        hard = 0
        for job in range(0, jobs-d+1, 1):
            hard = max(hard, jobDifficulty[job])
            schedule[0][job] = hard
        for day in range(1, d, 1):
            for job in range(day-1, jobs-(d-day)+1):
                hard = 0
                for i in range(job, jobs-(d-day)+1):
                    hard = max(hard, jobDifficulty[i])
                schedule[day][job] = schedule[day-1][job-1]+hard#min(schedule[day-1][job-1]+hard, schedule[day-1][job])
        return min(schedule[d-1][d-1:])

def aminDifficulty(jobDifficulty, d) -> int:
        n = len(jobDifficulty)
        # If we cannot schedule at least one job per day, 
        # it is impossible to create a schedule
        if n < d:
            return -1
        
        dp = [[float("inf")] * (d + 1) for _ in range(n)]
        
        # Set base cases
        dp[-1][d] = jobDifficulty[-1]

        # On the last day, we must schedule all remaining jobs, so dp[i][d]
        # is the maximum difficulty job remaining
        for i in range(n - 2, -1, -1):
            dp[i][d] = max(dp[i + 1][d], jobDifficulty[i])

        for day in range(d - 1, 0, -1):
            for i in range(day - 1, n - (d - day)):
                hardest = 0
                # Iterate through the options and choose the best
                for j in range(i, n - (d - day)):
                    hardest = max(hardest, jobDifficulty[j])
                    # Recurrence relation
                    dp[i][day] = min(dp[i][day], hardest + dp[j + 1][day + 1])

        return dp[0][1]

# print(minDifficulty([6,5,10,3,2,1], 3))
# print(minDifficulty([9,9,9], 4))
# print(minDifficulty([9,9,9], 3))
# print(minDifficulty([1, 1, 1], 3))
print(minDifficulty([11,111,22,222,33,333,44,444], 6))
print(aminDifficulty([11,111,22,222,33,333,44,444], 6))
# print(minDifficulty())
# print(minDifficulty())
