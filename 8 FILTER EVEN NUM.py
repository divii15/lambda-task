# 8. Filter even numbers from a list using `filter()`  
   - **Input:** `[1, 2, 3, 4, 5, 6]`  
   - **Output:** `[2, 4, 6]`



     
     even_num= list(filter((lambda x: x % 2 == 0),[1, 2, 3, 4, 5, 6]))
     print(even_num) 