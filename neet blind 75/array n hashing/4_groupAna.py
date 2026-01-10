# brute 
""" 
in this brute force, we create a list as Because for each “anagram group,” we want to store multiple words 
that share the same sorted signature.

so we first sort the s like eat,tea,etc will be "aet" as key in res so the same series of words will be listed or something
 """
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res= defaultdict(list)

        for s in strs:

            sortedS= ''.join(sorted(s))
            res[sortedS].append(s)
        return list (res.values())


#optimal- hash table, using tuple

""" 
pretty much similar to above solution but the catch is, in
above solution we were making the sorted words the key
but here we're taking "tuple of count" as key 
 """
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())


