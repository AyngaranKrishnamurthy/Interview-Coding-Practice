class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)       #Convert time string to list
        
        # Seperate Hour and handle
        if time[0] == '?':
            if time[1] == '?' or time[1] <= '3':  
                time[0] = '2'  
            else:
                time[0] = '1'
        if time[1] == '?':
            if time[0] == '2':
                time[1] = '3'
            else:
                time[1] = '9'
        
        # Handle the minute part
        if time[3] == '?':
            time[3] = '5'  
        if time[4] == '?':
            time[4] = '9'
        
        return ''.join(time)

solution = Solution()
print(solution.maximumTime("?5:?9"))