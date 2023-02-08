t = int(input())

for i in range(t):
    n = int(input())
    
    quarter = n
    dime = quarter % 25
    nickel = dime % 10
    penny = nickel % 5

    print(quarter // 25, dime // 10, nickel // 5, penny // 1)
