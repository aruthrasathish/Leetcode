class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Step 1: Find the kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # Step 2: Save the next group's starting node
            group_next = kth.next

            # Step 3: Reverse the current group
            prev = group_next
            current = group_prev.next

            while current != group_next:
                temp = current.next
                current.next = prev
                prev = current
                current = temp

            # Step 4: Connect the reversed group
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
