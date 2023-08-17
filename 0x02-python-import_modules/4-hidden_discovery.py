#!/usr/bin/python3

if __name__ == "__main__":

    import hidden_4

    dis = dir(hidden_4)

    for i in dis:
        if i[:2] != "__":
            print(i)
