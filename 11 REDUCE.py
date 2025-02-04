# 11. Find the product of numbers in a list using `reduce()`  
   - **Input:** `[1, 2, 3, 4]`  
   - **Output:** `24`  




     from functools import reduce
     product=reduce(lambda x,y:x*y,[1,2,3,4])
     print(product)