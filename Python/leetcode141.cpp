// Linked List Cycle

// change value or use two pointers (the "two pointers" tag reminds me of a faster pointer and a slower one.)

// Given a linked list, determine if it has a cycle in it.
//
// Follow up:
// Can you solve it without using extra space?

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
    bool hasCycle(ListNode *head) {
        while (head != NULL) {
            if (head->val == -99999) return true;
            head->val = -99999;
            head = head->next;
        }
        return false;
    }
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *p1 = head;
        ListNode *p2 = head;
        while (p1 != NULL && p1->next != NULL) {
            p1 = p1->next->next;
            p2 = p2->next;
            if (p1 == p2) return true;
        }
        return false;
    }
};
