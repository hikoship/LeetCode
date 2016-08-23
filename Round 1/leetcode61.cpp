// Rotate List

// find the length, then select the new head.

// Given a list, rotate the list to the right by k places, where k is non-negative.
//
// For example:
// Given 1->2->3->4->5->NULL and k = 2,
// return 4->5->1->2->3->NULL.

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
    ListNode* rotateRight(ListNode* head, int k) {
        int length = 0;
        ListNode* p = head;
        ListNode* new_head;

        // calculate length
        while (p) {
            length++;
            p = p->next;
        }
        if (length < 2) return head;
        k %= length;
        if (k == 0) return head;

        // look for the new head
        p = head;
        for (int i = 1; i < length - k; i++) p = p->next;
        new_head = p->next;
        p->next = NULL;
        p = new_head;
        while (p->next) p = p->next;
        p->next = head;
        return new_head;
    }
};
