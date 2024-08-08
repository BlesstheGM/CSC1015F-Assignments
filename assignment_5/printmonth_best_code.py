skip = 0
start_day = input("Enter the start day: ") - 1
skip += start_day

print("Mo Tu We Th Fr Sa Su")
print("   "*start_day, end="")
for i in range(1, 32):
    if len(str(i)) < 2:
        print(f" {i}", end=" ", sep="")
    else:
        print(f"{i}", end=" ")
    if skip < 6:
        skip+= 1
    else:
        print()
        skip = 0