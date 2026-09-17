class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []

        for word in strs:
            key = sorted(word)
            found = False

            for group in result:
                if key == sorted(group[0]):
                    group.append(word)
                    found = True
                    break

            if not found:
                result.append([word])

        return result