keyboard = "abcdefghijklmnopqrstuvwxy"
text = "cba" 

class Solution:
    def TimeToTypeString(self, keyboard:str, text: str) -> int:
        time = 0
        current = 0
        listk = list(keyboard)
        listt = list(text)

        for i in range(len(text)):
            for j in range(len(listk)):
                if listt[i] == listk[j]:            
                    if current < j:
                        current = j - current
                    else:
                        current = current - j
                    time+=current
        return time
                
solution=Solution()
print(solution.TimeToTypeString(keyboard,text))
