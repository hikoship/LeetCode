// Reverse String

// C++ 可以在原位修改字符串，Python 不可以。注意 s[::-1] 的实现

// Write a function that takes a string as input and returns the string reversed.
//
// Example:
// Given s = "hello", return "olleh".

class Solution {
public:
    string reverseString(string s) {
        string res = "";
        for (int i = s.length() - 1; i >= 0; i--) {
            res += s[i];
        }
        return res;
    }
};
