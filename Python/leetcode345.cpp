// Reverse Vowels of a String
//
// 同 344，Python 暂未找到不超时的方法
//
// Write a function that takes a string as input and reverse only the vowels of a string.
//
// Example 1:
// Given s = "hello", return "holle".
//
// Example 2:
// Given s = "leetcode", return "leotcede".

class Solution {
public:
    string reverseVowels(string s) {
        int i = 0, j = s.length() - 1;
        bool vowel_i, vowel_j;
        while (i < j) {
            if (
                s[i] == 'a' ||
                s[i] == 'e' ||
                s[i] == 'i' ||
                s[i] == 'o' ||
                s[i] == 'u' ||
                s[i] == 'A' ||
                s[i] == 'E' ||
                s[i] == 'I' ||
                s[i] == 'O' ||
                s[i] == 'U'
            ) vowel_i = true;

            else vowel_i = false;
            if (
                s[j] == 'a' ||
                s[j] == 'e' ||
                s[j] == 'i' ||
                s[j] == 'o' ||
                s[j] == 'u' ||
                s[j] == 'A' ||
                s[j] == 'E' ||
                s[j] == 'I' ||
                s[j] == 'O' ||
                s[j] == 'U'
            ) vowel_j = true;
            else vowel_j = false;

            if (vowel_i && vowel_j) {
                char tmp = s[i];
                s[i] = s[j];
                s[j] = tmp;
                i++;
                j--;
            }
            if (!vowel_i) i++;
            if (!vowel_j) j--;

        }
        return s;
    }
};
