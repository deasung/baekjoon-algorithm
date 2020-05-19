'''
A×B
두 정수 A와 B를 입력받은 다음, A×B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
첫째 줄에 A×B를 출력한다.

'''

while True:
    try:
        a, b = map(int, input().split())

        if (0 < a and b < 10):
            print(a * b)
            break

    except ValueError:
        print("Not a number")