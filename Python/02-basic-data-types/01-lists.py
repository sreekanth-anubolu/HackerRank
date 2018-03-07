if __name__ == '__main__':
    N = int(input())

    a = []
    for i in range(N):
        data = input().split(" ")
        action = data[0]
        if action == "insert":
            a.insert(int(data[1]), int(data[2]))
        elif action == "append":
            a.append(int(data[1]))
        elif action == "remove":
            a.remove(int(data[1]))
        elif action == "pop":
            a.pop()
        elif action == "sort":
            a.sort()
        elif action == "reverse":
            a.reverse()
        else:
            # action == "print"
            print(a)


