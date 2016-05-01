// Insertion Sort List

//

// Sort a linked list using insertion sort.

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
    ListNode* insertionSortList(ListNode* head) {
        if (!head || !head->next) return head;
        ListNode* prev = head;
        ListNode* loc;
        ListNode* cur = prev->next;
        ListNode* preHead = new ListNode(0);
        preHead->next = head;
        bool flag = true; // false if insertion happens

        while (cur) {
            loc = preHead;
            flag = true;
            while (loc != prev) {
                if (cur->val < loc->next->val) {
                    prev->next = cur->next ;
                    cur->next = loc->next;
                    loc->next = cur;
                    flag = false;
                    break;
                }
                loc = loc->next;
            }
            if (flag) prev = prev->next;
            cur = prev->next;
        }

        return preHead->next;

    }
};
