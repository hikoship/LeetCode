// Linked List Cycle II

// needs mathematical proof.

// Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
//
// Note: Do not modify the linked list.
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
    ListNode *detectCycle(ListNode *head) {
        ListNode *p1 = head;
        ListNode *p2 = head;
        while (p1 != NULL && p1->next != NULL) {
            p1 = p1->next->next;
            p2 = p2->next;
            if (p1 == p2) {
                while (p1 != head) {
                    p1 = p1->next;
                    head = head->next;
                }
                return head;
            }
        }
        return NULL;
    }
};
