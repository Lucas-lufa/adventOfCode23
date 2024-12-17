s1 = []
s2 = []
# with open('24/input1p1', 'r', encoding='utf-8') as raw:
#     file = raw.readlines()
#     for line in file:
#         a, s = line.split('   ')
#         s1.append(a.strip())
#         s2.append(s.strip())
#     s1.sort()
#     s2.sort()

# with open('s1','w') as f:
#     f.write(str(s1))
# with open('s2', 'w') as f:
#     f.write(str(s2))

with open('s1', 'r') as f:
    s1 = f.read()
with open('s2', 'r') as f:
    s2 = f.read()

s3 = 0
for i in range(0, 999):
    s3 +=  int(s2[i]) - int(s1[i])

print(s3)