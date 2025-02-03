# 13. Find the shortest word in a list  
   - **Input:** `["apple", "banana", "cherry", "blue"]`  
   - **Output:** `"blue"`




    short_word = min(["apple", "banana", "cherry", "blue"], key=lambda a:len(a))
    print(short_word)