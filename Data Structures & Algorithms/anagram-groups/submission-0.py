class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        groups = {}
        index = 0

        for word in strs:
            if "".join(sorted(word)) not in groups:
                groups["".join(sorted(word))] = index
                index += 1
                result.append([word])
            elif "".join(sorted(word)) in groups:
                result[groups["".join(sorted(word))]].append(word)
        
        return result


        