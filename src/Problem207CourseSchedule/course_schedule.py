from typing import List


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # just realized i dont need time since i dont check it for anything
        # global time

        # You can structure as a directed graph, and detect if there is a cycle or not
        # With the cycle you need to
        # if there is a cycle return False return True
        # THEOREM CHAPTER 22 CLRS: "a DAG G is acyclic iff dfs of G yields no back edges"
        # detect back edges!
        G = {}  # {int : int}

        # construct G
        for u in range(numCourses):
            G[u] = []
            # G keys contains all the courses need to take
        for u, v in prerequisites:
            # print(f"go from {u} to {v}")

            if u in G:
                G[u] = [*G[u], v]  # arr destructure works
            else:  # u not in G
                G[u] = [v]
        # print(G)

        # set gray and black, discovered and finished
        # each course i, 0 1 3 ..., has a color, "gray" or "black"
        color = ["white" for i in range(numCourses)]
        # print(color)
        # time = 0
        # each course i, 0 1 3 ..., has a d_time
        # d_time = [0 for i in range(numCourses)]
        # each course i, 0 1 3 ..., has a f_time
        # f_time = [0 for i in range(numCourses)]

        def dfs_visit(u):
            # global time
            # time = time + 1
            # d_time[u] = time
            color[u] = "gray"
            # print(f"discovered with {u}")

            for v in G[u]:
                # print(f"v {v}, color {color}")
                if color[v] == "white":
                    dfs_visit(v)
                elif color[v] == "gray":
                    '''''''''CYCLE DETECTED ABORT !!!!!!!!!!!!'''''''''
                    return

            color[u] = "black"
            # print(f"finished with {u}")
            # time = time + 1
            # f_time[u] = time

        def dfs():
            for u in G:
                if color[u] == "white":
                    dfs_visit(u)

        # v not black and not white, v == gray

        dfs()
        # print(f"color {color}")
        # only no cycle if all nodes is finished (all node color is BLACK)
        return all(c == "black" for c in color)


if __name__ == "__main__":
    solution = Solution()

    numCourses = 2
    prerequisites = [[1, 0]]
    print(solution.canFinish(numCourses, prerequisites))

    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    print(solution.canFinish(numCourses, prerequisites))

    numCourses = 3
    prerequisites = [[1, 0], [1, 2]]
    print(solution.canFinish(numCourses, prerequisites))

    numCourses = 6
    prerequisites = [[1, 0], [1, 2], [1, 5], [5, 1]]
    print(solution.canFinish(numCourses, prerequisites))
