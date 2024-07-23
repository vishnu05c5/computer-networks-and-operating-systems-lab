def main():
    
    n = int(input("Enter the number of processes -- "))
    
    bt = [0] * n  
    wt = [0] * n  
    tat = [0] * n  
    
    
    for i in range(n):
        bt[i] = int(input(f"Enter Burst Time for Process {i} -- "))
    
    
    wt[0] = 0
    tat[0] = bt[0]
    wtavg = 0
    tatavg = bt[0]
    
    
    for i in range(1, n):
        wt[i] = wt[i - 1] + bt[i - 1]
        tat[i] = tat[i - 1] + bt[i]
        wtavg += wt[i]
        tatavg += tat[i]
    
    
    print("\t PROCESS \tBURST TIME \t WAITING TIME\t TURNAROUND TIME")
    for i in range(n):
        print(f"\n\t P{i} \t\t {bt[i]} \t\t {wt[i]} \t\t {tat[i]}")
    
    print(f"\nAverage Waiting Time -- {wtavg / n:.2f}")
    print(f"Average Turnaround Time -- {tatavg / n:.2f}")


if __name__ == "__main__":
    main()
