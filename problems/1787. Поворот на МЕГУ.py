thr, minutes = raw_input().split(' ')
s = 0

for car in raw_input().split(' '):
    s += (int(car) - int(thr))
    s = 0 if s < 0 else s
print s