import argparse

def fibonacci(contador):
    x = 0
    y = 1
    for i in range(0,contador):
        if i % 2 == 0:
            yield x
            x = x + y
        else:
            yield y
            y = y + x

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fibonacci')
    parser.add_argument('--num', type=int, required=True, help='Cuantos numeros de la serie Fibonacci queremos mostrar.')

    args = parser.parse_args()

    for num in fibonacci(args.num):
        print(num, end=" ")
