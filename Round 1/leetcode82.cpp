// Remove Duplicates from Sorted List II

// recursive / iterative

// Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
//
// For example,
// Given 1->2->3->3->4->4->5, return 1->2->5.
// Given 1->1->1->2->3, return 2->3.

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// recursive
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        if (head->val != head->next->val) {
            head->next = deleteDuplicates(head->next);
            return head;
        }
        do {
            head->next = head->next->next;
        } while (head->next && head->val == head->next->val);

        return deleteDuplicates(head->next);
    }
};

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head || !head->next) {
            return head;
        }
        if (head->val != head->next->val) {
            head->next = deleteDuplicates(head->next);
            return head;
        }
        int v = head->val;
        do {
            head = head->next;
        } while (head && head->val == v);

        return deleteDuplicates(head);
    }
};

// shorter iterative
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* fakeHead = new ListNode(0);
        fakeHead->next = head;
        ListNode* pre = fakeHead;
        ListNode* cur = head;
        while (cur) {
            while (cur->next && cur->val == cur->next->val) {
                cur = cur->next;
            }
            if (pre->next == cur) {
                pre = pre->next;
            }
            else {
                pre->next = cur->next;
            }
            cur = cur->next;
        }
    }
    return fakeHead->next;
};


// iterative
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        while (head && head->next && head->val == head->next->val) {
            do {
                head = head->next;
            } while (head->next && head->val == head->next->val);
            head = head->next;
        }
        if (!head) {
            return NULL;
        }

        ListNode* start = head;
        ListNode* end = head->next;
        while (end) {
            if (end->next && end->val == end->next->val) {
                do {
                    end = end->next;
                } while(end->next && end->val == end->next->val);
                start->next = end->next;
                if (!start->next) {
                    break;
                }
                else {
                    end = start->next;
                }
            }
            else {
                start = end;
                end = end->next;
            }
        }
        return head;
    }
};
