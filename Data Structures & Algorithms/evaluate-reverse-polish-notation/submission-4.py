class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                val2, val1 = stack.pop(), stack.pop()
                match token:
                    case "+": res = val1 + val2
                    case "-": res = val1 - val2
                    case "*": res = val1 * val2
                    case "/": res = val1 / val2
                stack.append(int(res))

        return (stack[-1])