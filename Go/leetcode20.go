// Valid Parentheses

// stack

// Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
// 
// The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
func isValid(s string) bool {
	var stack []byte
	for i := 0; i < len(s); i++ {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
			stack = append(stack, s[i])
		} else {
			if (len(stack) == 0) {
				return false
			}
            if (s[i] == ')' && stack[len(stack) - 1] != '(' ||
				    s[i] == ']' && stack[len(stack) - 1] != '[' ||
                    s[i] == '}' && stack[len(stack) - 1] != '{') {
				return false
			}
			stack = stack[:len(stack) - 1]
		}
	}
    if (len(stack) == 0) {
        return true
    }
    return false
}


