
def squarePool(n, t, trees):
    w, h = (n, n)
    arr = [["0" for x in range(w)] for y in range(h)]

    print(trees[0][0])

    for index, i in enumerate(trees):
        arr[trees[index][0]][trees[index][1]] = "1"

    for index, i in enumerate(arr):
        print(arr[index])


print(squarePool(5, 3, [[2, 4],[1,3],[2, 0]]))