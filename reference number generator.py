import time
title = "Automatic learner reference number generator for high\nschools(G10-12) only.\n"
print(title.upper())
print("NB:The learner reference number is only produced for candidates intending to register for grade 10.\n")
school_name = input("Enter the school name: ")
capacity = int(input("Enter a caring capacity of "+school_name+": "))
time = list(time.localtime(time.time()))
capacity_1 = list(range(1, capacity+1 ))
r_numbers = capacity_1
r_numbers.append(0)
year = time[0]
all_ref_nums = []
for number in range(0, capacity):
    if number > 0:
        answer = input("Is another candidate intending to register(y/n)?: ")
    else:
        answer = input("Is a candidate intending to register(y/n)?: ")
        
    if answer == "y":
        year = str(year)
        r_year = year[2:4]
        
        if r_numbers[0] != 0:
            if r_numbers[0]<10:
                ref_num = r_year +"00"+ str(r_numbers[0])
                print("The learner reference number is ", ref_num)
                r_numbers.remove(r_numbers[0])
            elif r_numbers[0] <100:
                ref_num = r_year +"0"+ str(r_numbers[0])
                print( "The learner reference number is ",ref_num)
                r_numbers.remove(r_numbers[0])
     
            else:
                ref_num = r_year + str(r_numbers[0])
                print("The learner reference number is ",ref_num)
                r_numbers.remove(r_numbers[0])     
        
    else:
        print("\nAnother reference number was not generated!,this is due to your choice.\n")
        break
        
    print("\n")
    all_ref_nums.append(ref_num)
allRefNumbers = []
for num in all_ref_nums:
    if num!=0:
        num = int(num)
        allRefNumbers.append(num)
print("\nBelow is a list of all generated reference numbers for "+school_name+" 'newcomers':\n")
print(allRefNumbers)






