class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        pos = 1

        first = -1
        prev_critical = -1
        min_dist = float('inf')
        max_dist = -1

        while curr.next:
            next_node = curr.next

            if (curr.val > prev.val and curr.val > next_node.val) or \
               (curr.val < prev.val and curr.val < next_node.val):

                if first == -1:
                    first = pos
                else:
                    min_dist = min(min_dist, pos - prev_critical)
                    max_dist = pos - first

                prev_critical = pos

            prev = curr
            curr = next_node
            pos += 1

        if first == prev_critical:
            return [-1, -1]

        return [min_dist, max_dist]
