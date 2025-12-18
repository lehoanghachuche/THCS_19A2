t = tuple(map(int, input("Nhập các phần tử của tuple: ").split()))
chan = []
le = []
for x in t:
    if x % 2 == 0:
        chan.append(x)
    else:
        le.append(x)
tuple_chan = tuple(chan)
tuple_le = tuple(le)
print("Tuple chẵn:", tuple_chan)
print("Tổng các số chẵn:", sum(tuple_chan))
print("Tuple lẻ:", tuple_le)
print("Tổng các số lẻ:", sum(tuple_le))