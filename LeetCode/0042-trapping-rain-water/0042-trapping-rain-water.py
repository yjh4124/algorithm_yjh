class Solution:
    def trap(self, height: List[int]) -> int:
        
        def get_trapped_water():
            nonlocal height
            stack=[]
            last_max_height=0
            trapped_water=0
            
            for h in height:
                if h<last_max_height:
                    stack.append(h)
                else:
                    while stack:
                        trapped_water+=last_max_height-stack.pop()

                    stack.append(h)
                    last_max_height=h
            
            height=stack[::-1]
            return trapped_water
            
        trapped_water = get_trapped_water()
        trapped_water += get_trapped_water()
            
        return trapped_water
        