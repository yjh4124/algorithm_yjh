class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        # 0. sort words
        words.sort()
        
        # 1. check length of each word.
        word_length=len(words[0])
        
        # 2. check length of words.
        words_length=len(words)
        
        # 2-1. check length of string s.
        s_length=len(s)
        
        # 2-2. check length of substring.
        substring_length=word_length*words_length
    
        # 2-3. memo substring starting indexs are available or not.
        substring_starting_indexs_memo=[-1]*s_length
        
        # 2-4. save substring indexs.
        substring_starting_indexs_result=[]
        
        def is_substring_from_starting_index(starting_index):
            # global s
            # global words
            # global word_length
            # global words_length
            # global substring_length
            
            substring_index=starting_index
            substring_index_limit=starting_index+substring_length-word_length+1
            
            temp_words=[]
            
            while substring_index<substring_index_limit:
                temp_word=substring_starting_indexs_memo[substring_index]
                if temp_word==-1:
                    temp_word=s[substring_index:substring_index+word_length]
                
                if temp_word in words:
                    substring_starting_indexs_memo[substring_index]=temp_word
                    temp_words.append(temp_word)
                else:
                    substring_starting_indexs_memo[substring_index]=False
                    return False
                substring_index+=word_length
            
            return True if sorted(temp_words)==words else False
        
        # 3. search string s starting from index zero.
        s_index=0
        s_index_limit=s_length-substring_length+1
            
        while s_index<s_index_limit:
            if substring_starting_indexs_memo[s_index] is not False:
                # 4. check substrings
                if is_substring_from_starting_index(s_index):
                    substring_starting_indexs_result.append(s_index)
            
            # 5. go to next index
            s_index+=1
            
        return substring_starting_indexs_result