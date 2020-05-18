
# 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

while True:
    try:
        a, b = map(int, input().split())

        if (0 < a and b < 10):
            print(a + b)
            break

    except ValueError:
        print("Not a number")

