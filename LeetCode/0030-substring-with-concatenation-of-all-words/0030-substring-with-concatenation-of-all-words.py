from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        # Count frequency of each word in words
        word_counter=Counter(words)
        
        # Length of each word and the number of words
        word_len=len(words[0])
        words_num=len(words)
        
        # Length of the concatenated substring and string s
        substring_len=word_len*words_num
        s_len=len(s)
    
        # Memoization for substring checks
        substring_memo=[-1]*s_len
        
        # List to store starting indices of valid substrings
        result_indices=[]
        
        def check_substring(start):
            temp_words=[]
            
            for i in range(start, start+substring_len-word_len+1, word_len):
                temp_word=substring_memo[i] \
                    if substring_memo[i]!=-1 else s[i:i+word_len]
                
                if temp_word in words:
                    substring_memo[i]=temp_word
                    temp_words.append(temp_word)
                else:
                    substring_memo[i]=False
                    return False
            
            return Counter(temp_words)==word_counter
        
        # Iterate through possible starting indices
        for i in range(s_len-substring_len+1):
            if substring_memo[i] is not False:
                if check_substring(i):
                    result_indices.append(i)
            
        return result_indices