# 9. Filter numbers greater than 3 from a list  
   - **Input:** `[1, 2, 3, 4, 5, 6]`  
   - **Output:** `[4, 5, 6]` 




     greater_num= list(filter((lambda x: x > 3), [1, 2, 3, 4, 5, 6]))
     print(greater_num)