def main():
    
    n = int(input("Enter the number of processes -- "))
    
    p = list(range(n))  
    bt = [0] * n  
    wt = [0] * n  
    tat = [0] * n  
    
    
    for i in range(n):
        bt[i] = int(input(f"Enter Burst Time for Process {i} -- "))
    
    
    for i in range(n):
        for k in range(i + 1, n):
            if bt[i] > bt[k]:
                bt[i], bt[k] = bt[k], bt[i]
                p[i], p[k] = p[k], p[i]
    
    
    wt[0] = 0
    tat[0] = bt[0]
    wtavg = 0
    tatavg = bt[0]
    
    
    for i in range(1, n):
        wt[i] = wt[i - 1] + bt[i - 1]
        tat[i] = tat[i - 1] + bt[i]
        wtavg += wt[i]
        tatavg += tat[i]
    
    
    print("\n\t PROCESS \tBURST TIME \t WAITING TIME\t TURNAROUND TIME")
    for i in range(n):
        print(f"\n\t P{p[i]} \t\t {bt[i]} \t\t {wt[i]} \t\t {tat[i]}")
    
    print(f"\nAverage Waiting Time -- {wtavg / n:.2f}")
    print(f"Average Turnaround Time -- {tatavg / n:.2f}")


if __name__ == "__main__":
    main()
