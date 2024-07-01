from typing import List


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        letters_to_find: List[str] = list(s)
        current_letter_index: int = 0
        letters_needed: int = len(letters_to_find)
        for letter in t:
            letter_to_find = letters_to_find[current_letter_index]
            if letter == letter_to_find:
                current_letter_index += 1
                if current_letter_index == letters_needed:
                    return True
            if current_letter_index == letters_needed:
                return False

        
        return False