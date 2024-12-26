s1 = []
s2 = []
with open('24/input1p1', 'r', encoding='utf-8') as raw:
    file = raw.readlines()
    for line in file:
        a, s = line.split('   ')
        s1.append(a.strip())
        s2.append(s.strip())
    s1.sort()
    s2.sort()

# with open('24/s1','a') as f:
#     for each in s1:
#         f.write(f'{each}\n')
# with open('24/s2','a') as f:
#     for each in s2:
#         f.write(f'{each}\n')

with open('24/s1', 'r') as f:
    s1 = f.read()
with open('24/s2', 'r') as f:
    s2 = f.read()

# s1 = s1.rstrip(']')
# s1 = s1.lstrip('[')
s1s = s1.split('\n')

# s2 = s2.rstrip(']')
# s2 = s2.lstrip('[')
s2s = s2.split('\n')

s5 = 0
for i in range(0, 1000):
    s3 =  int(s1s[i])
    s4 =  int(s2s[i])

    if (s3 > s4):
        s5 += s3 - s4
    else:
        s5 += s4 - s3

print(s5) # 1341714