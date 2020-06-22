def find(arr):
    n = len(arr)
    i = 0
    j = n - 1
    res = -1
    while i < n and j >= 0:
        if arr[i][j] == 0:
            while j >= 0 and (arr[i][j] == 0 or i == j):
                j -= 1
                if j == -1:
                    res = i
                    break
                else: i += 1
        else:
            while i < n and (arr[i][j] == 1 or i == j):
                i +=1
                if i == n:
                    res = j
                    break
                else:
                    j -= 1
            if res == -1:
                return res
	    
    for i in range(0, n):
        if res != i and arr[i][res] != 1:
            return -1
    for j in range(0, j):
        if res != j and arr[res][j] != 0:
            return -1;
    return res;

def main():
    arr = [[1,0,0,0],
           [1,1,1,0],
           [1,1,0,0],
           [1,1,1,0]]
    print(find(arr) )

main()
