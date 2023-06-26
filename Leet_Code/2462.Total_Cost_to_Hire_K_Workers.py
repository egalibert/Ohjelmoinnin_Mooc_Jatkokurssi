import heapq

class Solution:
    def totalCost(self, costs, k, candidates):
        i = 0
        j = len(costs) - 1
        list1= []
        list2= []

        ans = 0
        while k > 0:
            while len(list1) < candidates and i <= j:
                heapq.heappush(list1, costs[i])
                i += 1
            while len(list2) < candidates and i <= j:
                heapq.heappush(list2, costs[j])
                j -= 1

            t1 = list1[0] if list1 else float('inf')
            t2 = list2[0] if list2 else float('inf')

            if t1 <= t2:
                ans += t1
                heapq.heappop(list1)
            else:
                ans += t2
                heapq.heappop(list2)

            k -= 1
        return ans


        

def main():
    # costs = [17,12,10,2,7,2,11,20,8]
    # k = 3
    # candidates = 4
    # costs = [31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58]
    # k = 11
    # candidates = 2
    costs = [96,697,801,892,752,948,176,92,469,595,642,686,729,872,547,443,50,746,13,102,548,158,155,73,114,77,204,544,956,484,565,190,310,210,726,347,2,665,800,749,751,600,580,942,966,198,886,15,607,439,725,279,345,183,104,696,699,631,562,654,79,518,77,469,806,525,487,84,707,880,21,463,696,212,877,697,538,207,832,793,906,965,666]
    k = 47
    candidates = 82
    result = 0
    result = Solution.totalCost(costs, k, candidates)
    print (result)

main()




# class Solution:
#     def totalCost(costs :list, k: int, candidates: int) -> int:
#         t_cost = 0
#         print(len(costs))
#         while (k > 0):
#             smallest = 100000
#             i = 0
#             smallest_i = 0
#             if (candidates > len(costs)):
#                 while (i < len(costs)):
#                     if costs[i] < smallest:
#                         smallest = costs[i]
#                         smallest_i = i
#                     i += 1 
#             else:
#                 while (i < candidates ):
#                     if costs[i] < smallest:
#                         smallest = costs[i]
#                         smallest_i = i
#                     i += 1
#                 x = (len(costs)) - candidates
#                 print (x)
#                 while (x < len(costs)):
#                     if costs[x] < smallest:
#                         smallest = costs[x]
#                         smallest_i = x
#                     x += 1
#             print((costs))
#             print (costs[smallest_i], smallest_i)
#             print(sorted(costs))
#             k -= 1
#             t_cost += costs[smallest_i]
#             costs.pop(smallest_i)
#         # print (t_cost)
#         return (t_cost)