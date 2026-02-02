# 1 থেকে 10 পর্যন্ত সব সংখ্যার list বানাও

list=[x for x in range(10)]
# print(list)

# 1 থেকে 10 পর্যন্ত সব even number এর list বানাও

list2=[]

for i in range(10):
    if i%2==0:
        list2.append(i)
# print(list2)

list3=[x for x in range(10) if x%2==0]
# print(list3)

# "python" string থেকে প্রতিটা character এর list বানাও
list4=[x for x in "Python"]
print(list4)

# 1 থেকে 5 পর্যন্ত সংখ্যার square বের করো
squre=[x*x for x in range(5)]
print(squre)

# 1 থেকে 10 পর্যন্ত শুধু odd number রাখো
odd=[x for x in range(1,10) if x%2!=0]
print(odd)

# 1 থেকে 20 পর্যন্ত যেসব সংখ্যা 3 দিয়ে ভাগ যায়
thrDev=[x for x in range(1,20) if x%3==0]
print(thrDev)

# "HelloWorld" থেকে শুধু vowel গুলো বের করো
vowel=[x for x in "HelloWorld" if x in "aAeEiIoOuU" ]
print("".join(vowel))

# 1 থেকে 10 পর্যন্ত সংখ্যা
# even হলে square, odd হলে 그대로 রাখো

result = [x*x if x%2 == 0 else x for x in range(1, 11)]
print(result)

# 1 থেকে 10 পর্যন্ত সংখ্যাকে string বানাও
string1 ="".join(str(i) for i in range(10))
print(string1)

# "a1b2c3" থেকে শুধু digit বের করো

digit=" ".join(i for i in "a1b2c3" if i.isdigit() == True)
print(digit)


# 1-3 এবং 1-3 দিয়ে সব possible pair বানাও
# Output: [(1,1),(1,2)...]

pair=[(i, j) for i in range(1, 4) for j in range(1, 4)]
print(pair)

# 2D list flatten করো
# matrix = [[1,2],[3,4],[5,6]]

matrix = [[i, i+1] for i in range(1, 7, 2)]

print(matrix)

multiplication=[[i*j for j in range(1,4)] for i in range(1,4)]
print(multiplication)

multiplication2=[]

for i in range(1,4):
    row=[]
    for j in range(1, 4):
        row.append(i*j)
    multiplication2.append(row)

print(multiplication2)


multiplication3=[ [i*j for j in range(1, 4)] for i in range(1, 4)]

# Level-2: 2D array

array1=[]

for i in range(1, 4):
    arr=[]
    for j in range(1, 4):
        arr.append(j*i)
    array1.append(arr)

print(array1)

array2 = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(array2)

array3 = [[i*j for j in range(1, 5)] for i in range(1, 5)]
print(array3)

array4 = [[i*j for j in range(1, 5)] for i in range(1, 4)]
print(array4)

table = []

for i in range(1, 6):        # row
    row = []
    for j in range(1, 6):    # column
        if (i * j) % 2 == 0:
            row.append(i * j)
    table.append(row)

print(table)

# 1*1 1*2 1*3 1*4 1*5
# 2*1 2*2 2*3 2*4 2*5
# 3*1 3*2 3*3 

def multipicationTable():
    table1=[]

    for i in range(1,6):
        arr=[]
        for j in range(1,6):
            if  j*i % 2 == 0:
                arr.append(j*i)
        table1.append(arr)
    return table1

print(multipicationTable())

multipicationTable2=[[i*j for j in range(1, 6) if i*j % 2==0] for i in range(1,6)]

print(multipicationTable2)


def oddEven():
    arr=[]

    for i in range(1, 6):
        row=[]
        for j in range(1, 6):
            product = i*j
            if i % 2 == 0:
                if product % 2 == 0:
                    row.append(i*j)
            else:
                if product % 2==1:
                    row.append(i*j)
        arr.append(row)
    
    return arr

print(oddEven())



oddEven1 = lambda: [[i*j for j in range(1, 6) if (i*j) % 2 == i % 2] for i in range(1, 6)]
print(oddEven1())

print("\n\n")

oddEven2 = [[i*j for j in range(1, 6) if (i*j) % 2 == i % 2] for i in range(1, 6)]
print(oddEven2)


# Lower triangular matrix

def LowerTriangleMatrix():
    arr=[]

    for i in range(1, 5):
        row=[]
        for j in range(1, i+1):
            row.append(j)
        arr.append(row)
    
    return arr

print(LowerTriangleMatrix())

print("\n\n")

cl=[[j for j in range(1, i+1)] for i in range(1, 5)]
print(cl)

# MultipleTableAsString

def MultipleTableAsString():
    arr=[]
    print("\n\n\n")
    for i in range(1, 4):
        row=[]
        for j in range(1, 4):
            # print(f"{i}x{j}={i*j}")
            row.append(f"{i}x{j}={i*j}")
        arr.append(row)
    return arr

print(MultipleTableAsString())

v=[[f"{i}X{j}={i*j}" for j in range(1, 4)] for i in range(1, 4)]
print(v)