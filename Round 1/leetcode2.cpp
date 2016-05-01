// Add Two Numbers

// 顺序地相加即可。位数不同时在前面补0。最后的结果有进位，新建一个为0的节点。

// You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
//
// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        short digit = l1->val + l2->val;
        ListNode* res = new ListNode(digit % 10);
        ListNode* cur = res;
        short carry = short(digit / 10);

        while (l1->next || l2->next) {
            if (!l1->next) l1->next = new ListNode(0);
            if (!l2->next) l2->next = new ListNode(0);
            l1 = l1->next;
            l2 = l2->next;
            digit = l1->val + l2->val + carry;
            cur->next = new ListNode(digit % 10);
            carry = short(digit / 10);
            cur = cur->next;
        }
        if (carry == 1) cur->next = new ListNode(1);
        return res;

    }
};
