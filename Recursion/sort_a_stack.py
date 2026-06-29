class Solution:
    def insert(self,st, temp):
        if not st or st[-1] <= temp: # if temp is gt than top or stack empty
            st.append(temp)
            return
        
        # if the top is greater than top then pop the value then again recursive call insert untill
        # we find a value less than top, then insert the temp variable and then append the remaining values back which were 
        # popped earlier and were greater than temp variable
        val = st.pop() 
        self.insert(st,temp)
        st.append(val)

    def sortStack(self,st):
        if st:
            temp = st.pop()
            self.sortStack(st) # this only empties the stack storing variables in recursion call stack
            self.insert(st,temp) # this will insert the value in sorted manner


st = []
st.append(5)
st.append(2)
st.append(3)
st.append(4)
st.append(1)
solution = Solution()
solution.sortStack(st)
print(st)