import time
i = 0
num = 0
start = time.time()
for i in range(100000000):
    num += 1
    i += 1

end = time.time()

print(end - start)
print("验证是否代码冲突")

