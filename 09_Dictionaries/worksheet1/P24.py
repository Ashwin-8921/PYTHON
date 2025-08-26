'''
Print only the subjects with marks above 60 from scores = {'math': 75, 'science': 55, 'english': 82}.
Sample Output:
math
english
'''
import ast

inp=input("enter dict:")

scores=ast.literal_eval(inp)
#print(*[key for key in scores if scores[key] > 60 ])
for key in scores:
    if scores[key] > 60:
        print(key)


