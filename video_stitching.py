class Solution:
    def videoStitching(self, clips, stop) -> int:
        clips.sort()
        count, current, start = 0, 0, 0
        while start < len(clips) and current < stop:
            if clips[start][0] > current: return -1
            while start < len(clips) and clips[start][0] <= current:
                if clips[start][1] >= stop: return count+1
                start += 1
                if start == len(clips) and clips[-1][1] < stop:
                    return -1
            if clips[start-1][1] >= stop:
                return count+1
            else:
                count += 1
                current = clips[start-1][1]
        if current < stop:
            return count
        else:
            return -2
        
s = Solution()
print(s.videoStitching([[16,18],[16,20],[3,13],[1,18],[0,8],[5,6],[13,17],[3,17],[5,6]], 15))
print(s.videoStitching([[0,2],[4,8]],5))
print(s.videoStitching([[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], 10))
print(s.videoStitching([[0,1],[1,2]], 5))
print(s.videoStitching([[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], 9))
print(s.videoStitching([[0,4],[2,8]], 5))