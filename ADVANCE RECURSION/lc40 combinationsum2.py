class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(index: int, total: int, subset: List[int]) -> None:
            if total == target:
                result.append(subset.copy())
                return

            if total > target:
                return

            if index >= len(candidates):
                return    

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue

                if total + candidates[i] > target:
                    break

                subset.append(candidates[i])
                backtrack(i + 1, total + candidates[i], subset)
                subset.pop()

        backtrack(0, 0, [])
        return result