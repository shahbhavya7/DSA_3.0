class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        
        result = {} 
        
        for word in strs:
            sort_word = ''.join(sorted(word))
            if sort_word not in result:
                result[sort_word] = []
            result[sort_word].append(word)
        
        return list(result.values()) 
    
    ["tanishka", "eat", "tea", "tan", "ate", "nat", "bat"]