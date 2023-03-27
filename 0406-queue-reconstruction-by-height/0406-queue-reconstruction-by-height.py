class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        people.sort(key = lambda x : (x[0], -x[1]))
        people_len = len(people)
        for p in range(people_len):
            temp = people.pop()          
            idx = 0
            while queue and temp[1] > idx:
                idx += 1
            queue.insert(idx, temp)
        return queue