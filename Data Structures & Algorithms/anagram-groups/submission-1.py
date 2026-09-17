class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        for i in range(len(strs)):
            group = []

            for j in range(len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])

            if group not in result:
                result.append(group)

        return result