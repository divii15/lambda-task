# 6. Sort a list of tuples based on the second value  
   - **Input:** `[(1, 3), (2, 2), (4, 1)]`  
   - **Output:** `[(4, 1), (2, 2), (1, 3)]`  




      sort= sorted([(1, 3), (2, 2), (4, 1)], key=lambda x: x[1])
      print(sort)