from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        unsatisfied = []
        for customer, grump in zip(customers, grumpy):
            if grump == 0:
                satisfied += customer
                unsatisfied.append(0)
            else:
                unsatisfied.append(customer)

        max_sum = sum(unsatisfied[:minutes])
        rolling_sum = max_sum
        start_index = 0

        for i in range(minutes,len(unsatisfied)):
            rolling_sum = rolling_sum - unsatisfied[start_index] + unsatisfied[i]
            if rolling_sum > max_sum:
                max_sum = rolling_sum
            start_index += 1
            
        return satisfied + max_sum
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSatisfied(customers=[1,0,1,2,1,1,7,5], grumpy=[0,1,0,1,0,1,0,1], minutes=3))