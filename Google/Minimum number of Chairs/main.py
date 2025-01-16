class Solution:
    def maxChairs(self, S, E):
        self.S = S
        self.E = E
        max_guests= counter = 0
        n = len(S)
        
        i = j = 0
        list.sort(S)
        list.sort(E)

        while i<n and j<n:
            if S[i] < E[j]:
                counter +=1
                max_guests = max(max_guests, counter)
                i+=1
            else:
                counter -=1
                j+=1
        return max_guests

solution = Solution()
testcase1 = solution.maxChairs(S = [1, 2, 6, 5, 3], E = [5, 5, 7, 6, 8])
print("Test Case 1: ",testcase1)

testcase2 = solution.maxChairs(S = [1], E = [10])
print("Test Case 2: ",testcase2)