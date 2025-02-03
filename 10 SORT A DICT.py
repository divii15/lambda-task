# 10. Sort a list of dictionaries by age  
   - **Input:** `[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 22}]`  
   - **Output:** `[{"name": "Bob", "age": 22}, {"name": "Alice", "age": 25}]`  






      sort= sorted([{"name": "Alice", "age": 25}, {"name": "Bob", "age": 22}], key=lambda x: x["age"])
      print(sort)