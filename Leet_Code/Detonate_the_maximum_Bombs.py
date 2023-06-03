import math
from typing import List

class Solution:
    @staticmethod
    def maximumDetonation(bombs: List[List[int]]) -> int:
        maxDetonations = 0

        for i in range(len(bombs)):
            x1, y1, r1 = bombs[i]
            detonations = 0

            for j in range(len(bombs)):
                if i != j:
                    x2, y2, r2 = bombs[j]
                    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

                    if distance <= r1 + r2:
                        detonations += 1

            maxDetonations = max(maxDetonations, detonations)

        return maxDetonations



bombs = [[54,95,4],[99,46,3],[29,21,3],[96,72,8],[49,43,3],[11,20,3],[2,57,1],[69,51,7],[97,1,10],[85,45,2],[38,47,1],[83,75,3],[65,59,3],[33,4,1],[32,10,2],[20,97,8],[35,37,3]]
solution = Solution()
print(solution.maximumDetonation(bombs))  # Output: 2
