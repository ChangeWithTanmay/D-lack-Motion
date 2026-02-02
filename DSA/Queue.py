queue=[]

choose = int(input("1. Enqueue\n2. Dqueue\n3. Peek\n4.Is Full\n IsEmpty"))

if choose == 1:
    push=int(input("\nEnter Element: "))
    queue.append(push)