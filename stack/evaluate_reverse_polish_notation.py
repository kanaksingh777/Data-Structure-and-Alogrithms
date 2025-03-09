
def evalRPN(tokens):
    num_list = []
    arthematic_list  = []

    for i in tokens:
        if i == '+' or i == '-' or i == '*' or i ==  '/':
            arthematic_list.append(i)
        else : num_list.append(i)

    ans = num_list[0] ,arthematic_list[0] ,num_list[1]
            




tokens = ["1","2","+","3","*","4","-"]

ans = evalRPN(tokens)
print(ans)