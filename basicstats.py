def basicStats():
    print("-------------------------------------------------------------------")    
    print("Basic Statistics (Mean, Median, Mode, Standard Deviation, Variance )")
    print("-------------------------------------------------------------------")
    while True:
        try:
            frequncies = list(map(float, input("Enter frequencies seperated by space: ").split()))
            print(frequncies)
            print()
            print("1. Mean")
            print("2. Median")
            print("3. Mode")
            print("4. Variance ")
            print("5. Standard Deviation")
            print("99. Exit")
            print()

            operation = int(input("Select an operation: "))
            mean = sum(frequncies)/len(frequncies)
            variance = sum((x - mean)**2 for x in frequncies)/len(frequncies)
            std_dev = variance**0.5

            print()

            #mean
            if operation == 1:
                print(f"Answer > {mean}")
                print()
                break
            #median
            if operation == 2:
                frequncies.sort()
                if len(frequncies) % 2 == 0:
                    median = (frequncies[len(frequncies)//2] + frequncies[len(frequncies)//2 - 1])/2
                    print(f"Answer > {median}")
                    print()
                    break
                else:
                    median = frequncies[len(frequncies)//2]
                    print(f"Answer > {median}")
                    print()
                    break
            #mode
            if operation == 3:
                count = {}
                for i in frequncies:
                    if i in count:
                        count[i] += 1
                    else:
                        count[i] = 1
                max_count = max(count.values())
                mode = [k for k, v in count.items() if v == max_count]
                print(f"Answer > {mode}")
                print()
                break
            #variance
            if operation == 4:
                print(f"Answer > {variance}")
                print()
                break
            #standard deviation
            if operation == 5:
                print(f"Answer > {std_dev}")
                print()
                break 
            
            if operation == 99:
                break



                

        except ValueError:
            print("Enter a valid numbers")   

basicStats()



    