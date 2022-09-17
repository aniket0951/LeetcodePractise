from collections import defaultdict
def MakingaMeal():
    ans = 0 
    for _ in range(int(input())):
        n = int(input())
        data = defaultdict(int)
        for j in range(n):
            # s = input()
            for char in input():
                data[char] += 1
        
        while True:
            meal = "codechef"
            i = 0
            tag = False
            while i < len(meal):
                if meal[i] not in data:
                    tag = True
                    break
                else:
                    data[meal[i]] -= 1
                    if data[meal[i]] <= 0:
                        del data[meal[i]]
                i += 1

            if tag:
                break
            ans += 1    
        return ans            


def ASubtaskProblem():
    ans = 0
    for _ in range(int(input())):
        n,m,k = input().split()
        score = list(map(int, input().split(' ')))

        pass_test = 0 

        for i in range(len(score)):
            if score[i] == 1:
                pass_test += 1
            else:
                m = int(m)
                if pass_test >= m:
                    ans = int(k)
                    break
                else:return ans    
        if ans == 0:
            return 100
        else:
            return ans            


if __name__ == "__main__":
    # ans = MakingaMeal()    
    ans = ASubtaskProblem()           
    print(ans)