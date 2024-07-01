class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count = 0
        index = 0
        length_of_list = len(arr)
        for number in arr:
            if number % 2 != 0:
                odd_count += 1
            else:
                odd_count = 0
            
            if odd_count == 3:
                return True
            
            if (length_of_list - index) + odd_count < 3:
                return False

            index += 1
        return False