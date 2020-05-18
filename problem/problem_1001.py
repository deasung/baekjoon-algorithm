
# 두 정수 A와 B를 입력받은 다음, A-B를 출력하는 프로그램을 작성하시오. (0 < A, B < 10)

while True:
    try:
        a, b = map(int, input().split())

        if (0 < a and b < 10):
            print(a - b)
            break

    except ValueError:
        print("Not a number")

