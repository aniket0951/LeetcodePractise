
def TestFunc(ans):
    for _ in range(int(input())):
        a,b,c = input().split()

        res = int(a) + int(b) + int(c)
        if res >= 2:ans += 1 
    return ans

if __name__ == "__main__":
    ans = TestFunc(0) 
    print(ans)   


