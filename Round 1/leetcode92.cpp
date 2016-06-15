// Reverse Linked List II

/   /

// Reverse a linked list from position m to n. Do it in-place and in one-pass.
//
// For example:
// Given 1->2->3->4->5->NULL, m = 2 and n = 4,
//
// return 1->4->3->2->5->NULL.
//
// Note:
// Given m, n satisfy the following condition:
// 1 ≤ m ≤ n ≤ length of list.

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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
        if (m == n) return head;
        ListNode* seg1Tail = NULL;
        ListNode* seg2Tail = NULL;
        ListNode* p1 = NULL;
        ListNode* p2 = NULL;
        ListNode* p3 = NULL;

        if (m > 1) {
            seg1Tail = head;
            for (int i = 2; i < m; i++) seg1Tail = seg1Tail->next; // NOTE: wrote as seg1Tail = head->next by mistake
            seg2Tail = seg1Tail->next;
        }
        else {
            seg2Tail = head;
        }

        p1 = seg2Tail;
        p2 = p1->next;
        p3 = p2->next;

        for (int i = m; i < n; i++) {
            p2->next = p1;
            p1 = p2;
            p2 = p3;
            if (p3 != NULL) p3 = p3->next;
            else break;
        }

        seg2Tail->next = p2;

        if (m > 1) {
            seg1Tail->next = p1;
            return head;
        }
        else return p1;
    }
};
