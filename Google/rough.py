load = [1, 2, 3, 4, 5]

class Solution(object):
    def loadDifference(self, load: list[int]) -> int:
        res1 = 0  # Sum of list1
        res2 = 0  # Sum of list2
        list1 = []
        list2 = []
        
        # Sort the load to balance the distribution better
        load.sort()

        for i in load:
            # Distribute the values between list1 and list2
            if res1 <= res2:
                list1.append(i)
                res1 += i  # Add to sum of list1
            else:
                list2.append(i)
                res2 += i  # Add to sum of list2
        
        # Calculate the result as the difference between the sums of the two lists
        res = res2 - res1
        
        # Output the lists and result
        print(f"list1: {list1}")
        print(f"list2: {list2}")
        print(f"Sum of list1: {res1}, Sum of list2: {res2}")
        print(f"Difference: {res}")
        
        return res

# Create an instance of Solution and call the method
solution = Solution()
print("Final Difference:", solution.loadDifference(load))

