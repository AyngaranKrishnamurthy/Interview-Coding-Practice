keyboard = "abcdefghijklmnopqrstuvwxy"
text = "leetcode" 

class Solution:
    def TimeToTypeString(self, keyboard:str, text: str) -> int:
        time = 0
        current = 0
        listk = list(keyboard)
        listt = list(text)

        for i in range(len(text)):
            for j in range(len(listk)):
                if listt[i] == listk[j]:            
                    time += abs(j - current)
                    current = j 
                    break
        return time
                
solution=Solution()
print(solution.TimeToTypeString(keyboard,text)) 
