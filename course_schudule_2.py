def has_dependency(prerequisites):
    has_dep = []
    for items in prerequisites:
        if items[0] not in has_dep:
            has_dep.append(items[0])
    return has_dep

def process_dep(prerequisites, item):
    list_of_all = []
    for index in range(len(prerequisites)):
        if prerequisites[index][1] != item:
           list_of_all.append(prerequisites[index])
    return list_of_all

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        list_of_all = list(range(numCourses))
        if len(prerequisites) == 0:
            return list_of_all
        # list_of_all = #list_of_courses(prerequisites)
        has_dep = has_dependency(prerequisites)
        has_no_dependency = set(list_of_all) - set(has_dep)
        # print(list_of_all);print(has_dep)
        processed = [x for x in list_of_all if x not in has_dep]
        while len(has_no_dependency) != 0 :#or len(has_no_dependency) != numCourses:
            item = has_no_dependency.pop()
            if item not in processed:
                processed.append(item)
            prerequisites = process_dep(prerequisites, item)
            has_no_dependency = set(list_of_all) - set(has_dependency(prerequisites)) - has_no_dependency.union(set(processed))
        return processed
            
        
s = Solution()
# print(s.findOrder(2,[[1,0]]))
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
        