# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	def mergeTwoLists(list1, list2):
		i = 0
		i2 = 0
		newlist = []
		while(i < len(list1)):
			while i2 < len(list2):
				if list1[i] < list2[i2]:
					newlist.append(list1[i])
					i += 1
				elif list1[i] == list1[i2]:
					newlist.append(list1[i])
					newlist.append(list2[i2])
					i += 1
					i2 += 1
				elif list2[i2] < list1[i]:
					newlist.append(list2[i2])
					i2 += 1
				else:
					continue
		print(newlist)




def main():
    list1 = [1,2,4]
    list2 = [1,3,4]
    list3 = []
    list3 = Solution.mergeTwoLists(list1, list2)


main()