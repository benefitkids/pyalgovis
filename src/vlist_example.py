from pyalgovis.vlist import VList, wait_quit

x = [1, 2, 3]
x = VList(x)
# x = list([1, 2, 3])

y1 = x[1]
y2 = x[2]

x[1] = y2
x[2] = y1

wait_quit()
