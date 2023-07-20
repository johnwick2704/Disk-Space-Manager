import time

fin = []

start = time.time()
for i in range(1, 66666666):
    fin.append(i)
end = time.time()
print(end - start)


# 2.6699910163879395
# 8.571256875991821