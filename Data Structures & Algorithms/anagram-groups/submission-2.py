class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            sort_s = ''.join((sorted(s)))
            new_list = anagrams.get(sort_s, [])
            new_list.append(s)
            anagrams.update({sort_s: new_list})
        return list(anagrams.values())


