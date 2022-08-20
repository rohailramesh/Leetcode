# Pseudocode solution

# initialise a ListNode() using a variable called dummy
# Assign that dummy to a variable called the tail
# while list1 and list2 are not empty
# check if the current value of list1 is smaller than current value of list2
# if it is, then add that to the tail
# update the pointer of list1
# else if the value of list2 is smaller than the current value of list1
# add that current valuue of list2 to the tail
# increase the counter of list2
# outside of those conditions change the pointer of the tail
# outside the loop if list1 still has values (list2 is empty)
# add the remaining list1 to the tail 
# else if list2 still has values (list1 is empty)
# add the remaining list2 to the tail
# return the dummy

def merge_two_list(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    tail = dummy
    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    return dummy.next


list_1 = [2,4,6,8,10]
list_2 = [1,3,5,7,9]
result = merge_two_list(list_1, list_2)
print(result)