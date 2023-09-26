
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.val, end=" ")
        current = current.next

n = int(input())
values = list(map(int, input().split()))


head = None
current = None
for val in values:
    new_node = ListNode(val)
    if head is None:
        head = new_node
        current = head
    else:
        current.next = new_node
        current = new_node


new_head = reverseLinkedList(head)

printLinkedList(new_head)
