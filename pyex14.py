marks = {}
print("Hey there! Can you give me the name and marks of 10 students please? Thanks!")

i1 = str(input())
print("Now the marks of " + i1 + " please?")
i1_1 = str(input())
marks[i1] = i1_1

i2 = str(input())
print("Now the marks of " + i2 + " please?")
i2_2 = str(input())
marks[i2] = i2_2

i3 = str(input())
print("Now the marks of " + i3 + " please?")
i3_3 = str(input())
marks[i3] = i3_3

i4 = str(input())
print("Now the marks of " + i4 + " please?")
i4_4 = str(input())
marks[i4] = i4_4

i5 = str(input())
print("Now the marks of " + i5 + " please?")
i5_5 = str(input())
marks[i5] = i5_5

i6 = str(input())
print("Now the marks of " + i6 + " please?")
i6_6 = str(input())
marks[i6] = i6_6

i7 = str(input())
print("Now the marks of " + i7 + " please?")
i7_7 = str(input())
marks[i7] = i7_7

i8 = str(input())
print("Now the marks of " + i8 + " please?")
i8_8 = str(input())
marks[i8] = i8_8

i9 = str(input())
print("Now the marks of " + i9 + " please?")
i9_9 = str(input())
marks[i9] = i9_9

i10 = str(input())
print("Now the marks of " + i10 + " please?")
i10_10 = str(input())
marks[i10] = i10_10

for key, value in marks.items():
    print(key.title() + " got " + value + " marks.")