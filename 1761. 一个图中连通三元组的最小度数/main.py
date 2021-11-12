

class Solution:
    def minTrioDegree(self, n: int, edges: list[list[int]]) -> int:
        mindegree=-1
        isExist=False
        edgesmaps={}
        for u,v in edges:
            if u not in edgesmaps.keys():
                edgesmaps[u]=set([v])
            else:
                edgesmaps[u].add(v)
            if v not in edgesmaps.keys():
                edgesmaps[v]=set([u])
            else:
                edgesmaps[v].add(u)
        print(edgesmaps)
        for s,ends in edgesmaps.items():
            for e in ends:
                if e == s:
                    continue
                es = edgesmaps.get(e,set())
                for p in es:
                    if p in (e,s):
                        continue
                    ps=edgesmaps.get(p,set())
                    if s in ps:
                        isExist=True
                        thisd=len(ends)+len(es)+len(ps)-6
                        mindegree =thisd if mindegree==-1 else  min(mindegree,thisd)
        return mindegree if isExist else -1


if __name__ == '__main__':
    s=Solution()
    n=7
    d=[[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
    print(s.minTrioDegree(n,d))