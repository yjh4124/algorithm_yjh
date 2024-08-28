from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        words_num = len(words)
        substring_len = word_len * words_num
        s_len = len(s)
        
        # Count frequency of each word in words
        word_count = Counter(words)
        
        result_indices = []

        # Iterate through the string with a window equal to the length of a word
        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()
            while right + word_len <= s_len:
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    current_count[word] += 1

                    # Move the left pointer to maintain valid counts
                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        left += word_len

                    # If the window size equals the substring length, it's a valid start
                    if right - left == substring_len:
                        result_indices.append(left)
                else:
                    # Reset the window if word not in word_count
                    current_count.clear()
                    left = right

        return result_indices
