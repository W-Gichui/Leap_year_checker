num = input("Input number...")
y = int(num)
def fibrinolysis(n):
    global sequence
    sequence = [0, 1]
    a = 0
    b = 1
    global c
    for i in range (2, n) :
        c = a + b
        a = b
        b = c   
        sequence.append(c)
fibrinolysis(9999)
if y in sequence :
            print("Present")
else:
            print("Absent")
 