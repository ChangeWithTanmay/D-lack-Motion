def squre():
    # 1 - 10 create a squre dict
    sq={x: x**2 for x in range(1, 10)}
    return sq

# print(squre())

def dubleList():
    # {2: 4, 4: 8, 6: 12, 8: 16}
    nums = [2, 4, 6, 8]
    dictList={x: x*2 for x in nums}
    return dictList

# print(dubleList())

def stringLength():
    names = ["rahim", "karim", "tamim", "Tanmay"]
    dictList={x: len(x) for x in names}
    return dictList

# print(stringLength())

def asciiValueOfAString():
    s="Python"
    dictString={x: ord(x) for x in s}
    return dictString
# print(asciiValueOfAString())

def ListIncrement():
    nums=[5, 10, 15]
    d={x: x+5 for x in nums}
    return d
# print(ListIncrement())

def lastCharFind():
    words = ["apple", "banana", "cherry"]
    d = {x: x[len(x)-1] for x in words}
    return d
# print(lastCharFind())

def positionFind():
    s = "apple"
    d = {x: s.find(x)+1 for x in s}
    return d
# print(positionFind())

def divideThree():
    nums = [3, 6, 9]
    d = {x: x/3 for x in nums}
    return d
# print(divideThree())

def squreTwo():
    d = {x: x**2 for x in range(1,6)}
    return d
# print(squreTwo())

def evenNumSqure():
    nums = [1, 2, 3, 4, 5, 6]
    d = {x: x**2 for x in nums if x%2==0}
    return d
# print(evenNumSqure())

def onlyPassedFifty1():
    marks = {"rahim": 80, "karim": 45, "tamim": 90}
    passed={}
    for x in marks:
        if x in marks and marks.get(x)>=50:
            passed[x]=marks[x]
            print(f"{x} : {marks[x]}")
    return passed


# print(onlyPassedFifty1())

def onlyPassedFifty():
    marks = {"rahim": 80, "karim": 45, "tamim": 90}
    passed={x: marks[x] for x in marks if x in marks and marks.get(x)>=50}
    
    return passed

# print(onlyPassedFifty())

def listAds():
    nums = [-5, -3, 0, 2, 4]
    ab={x:abs(x) for x in nums}
    return ab

# print(listAds())

def noDuplicate1():
    s="banana"
    
    du={}
    for x in s:
        count=0
        if x in du:
            du[x] = du[x] + 1
        else:
            du[x]=1
    return du

def noDuplicate2():
    s="banana"
    du={}
    for x in s:
        if x not in du:
            du[x]=s.count(x)
    
    return du

def noDuplicate():
    s="banana"
    du={x: s.count(x) for x in s}
    return du

# print(noDuplicate2())

def Listlength():
    words = ["hi", "hello", "hey", "good"]
    dic={x: len(x) for x in words if len(x)>3}
    
    return dic

# print(Listlength())

def ListEvenOdd1():
    nums = [10, 15, 20, 25]
    dic={}
    for x in nums:
        if x % 2 ==0:
            dic[x]="Even"
        else:
            dic[x]="Odd"
    return dic

def ListEvenOdd():
    nums = [10, 15, 20, 25]
    return {x: "Even" if x % 2 == 0 else "Odd" for x in nums}


# print(ListEvenOdd())

def negetivePositive():
    nums = [-10, 15, -20, 25]
    return {x: "Positive" if x>=0 else "Negetive" for x in nums}

# print(negetivePositive())

def priceSort():
    prices = {"apple": 120, "banana": 40, "mango": 150}
    return {x: prices[x] for x in prices if prices[x] >= 100}

# print(priceSort())

def evenOdd():
    nums = [1, 2, 3, 4]
    return {x: "Even" if x%2==0 else "Odd" for x in nums}

# print(evenOdd())

def repTwice():
    s = "abcd"
    return {x: f"{x}{x}" for x in s}
# print(repTwice())

def listOrderValues():
    list2=["i","a","b","c", "d", "e", "f", "g"]
    return {x: ord(x)-97+1 for x in list2}

# print(listOrderValues())

def isPrime1():
    nums = [1, 2, 3, 4, 5]
    di={}
    for x in nums:
        if x < 2:
            di[x]="Not prime"
            continue

        isPrime=True
        for y in range(2, x):
            if x % y == 0:
                isPrime = False
                break

        if isPrime:
            di[x]="Prime"
        else:
            di[x]="Not Prime"
    return di

def isPrime():
    nums = [1, 2, 3, 4, 5]

    return {
        # The all() function returns True if all items in an iterable are true, otherwise it returns False.
        x: "Prime" if x > 1 and all(x % y != 0 for y in range(2, x))
        else "Not Prime"
        for x in nums
    }

# print(isPrime())

def isPrime2():
    nums = [1, 2, 3, 4, 5]
    return {x: "prime" if x > 1 and all(x%y != 0 for y in range(2, x))
        else "Not prime"  
        for x in nums 
            }

# print(isPrime2())

def splitWord():
    s = "this is python"
    return {x: len(x) for x in s.split()}

# print(splitWord())

def passAndFail():
    students = {"rahim": 80, "karim": 45, "tamim": 90}
    return {x: "pass" if students[x]>=55 else "fail" for x in students}
# print(passAndFail())

def divTotal1():
    nums = [2, 4, 6, 8]
    du={}
    avg=0
    for x in nums:
        avg += x
    for x in nums:
        du[x]=x/avg
    return du

def divTotal():
    nums = [2, 4, 6, 8]
    return {x: x/sum(nums) for x in nums}
    
# print(divTotal())

def wordLower():
    # print("Apple".lower())
    words = ["Apple", "banana", "Cherry"]
    return {x.lower(): x for x in words}
# print(wordLower())

def frequencyString():
    s = "mississippi"
    return {x: s.count(x) for x in s}

# print(frequencyString())

def ListFactorial1():
    nums = [1, 2, 3, 4]
    du={}
    for x in nums:
        fact=0
        for y in range(0, x+1):
            if y==0:
                fact=1
            else:
                fact *= y
        du[x]=fact
    return du


import math

def ListFactorial():
    nums = [1, 2, 3, 4]
    return {x: math.factorial(x) for x in nums}

print(ListFactorial())

