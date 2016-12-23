// Partition List

//

// Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
//
// You should preserve the original relative order of the nodes in each of the two partitions.
//
// For example,
// Given 1->4->3->2->5->2 and x = 3,
// return 1->2->2->4->3->5.


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
    ListNode* partition(ListNode* head, int x) {
        ListNode* smallHead = NULL;
        ListNode* smallCur = NULL;
        ListNode* largeHead = NULL;
        ListNode* largeCur = NULL;
        ListNode* cur = head;
        while (cur) {
            if (cur->val < x) {
                if (!smallHead) {
                    smallHead = new ListNode(cur->val);
                    smallCur = smallHead;
                }
                else {
                    smallCur->next = new ListNode(cur->val);
                    smallCur = smallCur->next;
                }
            }
            else {
                if (!largeHead) {
                    largeHead = new ListNode(cur->val);
                    largeCur = largeHead;
                }
                else {
                    largeCur->next = new ListNode(cur->val);
                    largeCur = largeCur->next;
                }
            }
            cur = cur->next;
        }
        if (!smallHead) return largeHead;
        else smallCur->next = largeHead;
        return smallHead;

    }
};
