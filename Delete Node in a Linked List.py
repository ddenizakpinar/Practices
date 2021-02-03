# https://leetcode.com/problems/delete-node-in-a-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteNode(node):
    node.next, node.val = node.next.next, node.next.val
