class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if not people:
            return 0
        people.sort()
        lidx,ridx=0,len(people)-1
        cnt=0
        while lidx<=ridx:
            if lidx == ridx:
                cnt+=1
                break
            elif people[ridx] == limit:
                cnt+=1
                ridx-=1
            else:
                if people[ridx]+people[lidx]<= limit:
                    cnt+=1
                    lidx+=1
                    ridx-=1
                else:
                    cnt+=1
                    ridx-=1
        return cnt

