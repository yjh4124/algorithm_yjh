class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s, p = ' ' + s, ' ' + p
        lenS, lenP = len(s), len(p)
        dp = [[0] * (lenP) for i in range(lenS)]
        dp[0][0] = 1
 
        for j in range(1, lenP):
            if p[j] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, lenS):
            for j in range(1, lenP):
                if p[j] in {s[i], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j] == "*":
                    dp[i][j] = dp[i][j - 2] or int(dp[i - 1][j] and p[j - 1] in {s[i], '.'})
        
        return bool(dp[-1][-1])
    
#         def get_next_pattern(idx):
#             try:
#                 return p[idx]
#             except:
#                 return False
         
#         def is_same_p_s(char_p, char_s):
#             return char_p==char_s
        
#         def count_char_p_in_pattern_slice(char, slice_p):
#             count=0
#             for char_p in slice_p:
#                 if char==char_p: count+=1
#             return count
        
#         def count_last_char_in_pattern_slice(slice_p):
#             return len(slice_p.replace("*", ""))
            
            
#         len_s=len(s)
#         len_p=len(p)
#         idx_s=0
        
#         for idx_p, pattern in enumerate(p):
#             current_s=s[idx_s]
#             current_p=p[idx_p]
#             next_idx_p=idx_p+1
            
#             if idx_s==len_s-1: break
#             if current_p=="*":continue            
#             elif current_p==".":
#                 if get_next_pattern(next_idx_p)=="*":
#                     count_last_char=count_last_char_in_pattern_slice(p[next_idx_p:])
#                     idx_s=len_s-count_last_char-1
#                 else:
#                     if idx_s<len_s-1: idx_s+=1
            
#             else:
#                 if get_next_pattern(next_idx_p)=="*": 
#                     count_char_p=count_char_p_in_pattern_slice(current_p, p[next_idx_p:])
#                     while is_same_p_s(current_p, current_s) and idx_s<len_s-count_char_p-1:
#                         if idx_s<len_s-1: 
#                             idx_s+=1
#                             current_s=s[idx_s]
#                         else: break
#                 else:
#                     if is_same_p_s(current_p, current_s):
#                         if idx_s<len_s-1: idx_s+=1
#                         # try: current_s=s[idx_s]
#                         # except: continue
#                     else:
#                         continue
        
#         print(idx_s, len(s), current_s, idx_p, len(p), current_p)
        
#         if len_p==1:
#             if is_same_p_s(current_s, current_p) and len_p==len_s: return True
#             else: return False
#         if len_p>=2:
#             previous_p=p[idx_p-1]
#             if current_p!="*" and (is_same_p_s(current_s, current_p) or previous_p=="."):
#                 if idx_s<=idx_p and idx_p==len_p-1: 
#                     print(1)
#                     return True
#                 else:
#                     if idx_p+1<=len_p-1:
#                         last_slice_p=p[idx_p+1:]
#                         count_star=0
#                         for elem in last_slice_p:
#                             if elem=="*": count_star+=1

#                         if count_star*2==len_p-idx_p-1:
#                             return True
#                         else: return False
#                     else: return False
#             else: 
#                 if is_same_p_s(current_s, previous_p) or previous_p==".":
#                     if idx_p==len_p-1: return True
#                     else:
#                         if idx_p+1<=len_p-1:
#                             last_slice_p=p[idx_p+1:]
#                             count_star=0
#                             for elem in last_slice_p:
#                                 if elem=="*": count_star+=1

#                             if count_star*2==len_p-idx_p-1: return True
#                             else: return False
#                         else: return False
#                 else: 
#                     if idx_p+1<=len_p-1:
#                         next_p=p[idx_p+1]
#                         if is_same_p_s(current_s, next_p) or next_p==".":
#                             if idx_p+1==len_p-1: return True
#                             else:
#                                 last_slice_p=p[idx_p+1:]
#                                 count_star=0
#                                 for elem in last_slice_p:
#                                     if elem=="*": count_star+=1

#                                 if count_star*2==len_p-idx_p-1: return True
#                                 else: return False
#                         else: return False
#                     else:
#                         return False
#         # return idx_s>=len(s) and idx_p>=len(p)-1