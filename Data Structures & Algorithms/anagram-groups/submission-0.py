class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # HashMap = {}

        # for s in strs:
        #     count = [0] * 26

        #     for char in s:
        #         count[ord(char) - ord('a')] += 1
        #     key = tuple(count)

        #     if key not in HashMap:
        #         HashMap[key] = []
        #     HashMap[key].append(s)

        # return list(HashMap.values())


        #2nd Logic
        HashMap = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            HashMap[key].append(s)

        return list(HashMap.values())



        