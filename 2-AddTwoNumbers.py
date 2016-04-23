class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        ptr = head
        carry = 0
        while True:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            ptr.val = carry % 10
            carry /= 10
            if l1 != None or l2 != None or carry != 0:
                ptr.next = ListNode(0)
                ptr = ptr.next
            else:
                break
        return head

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(6)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(6)
sol = Solution()
result = sol.addTwoNumbers(l1,l2)
while result:
    print('%d' %result.val)
    result = result.next

