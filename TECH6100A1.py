# TECH6100 Assessment 1 Florencia Scolari ID 1847863 Apr 2025



def calculate_statistics(*numbers):
    """To calculate the mean, median, and standard deviation of the given values"""
    if len(numbers) > 0:
        mean = sum(numbers) / len(numbers) #average value
        median = sorted(numbers)
        """2 cases for when: list is odd or list is even"""
        m = len(numbers)//2 # m is the middle point. '//' is floor division, rounded to min closest digit
        if len(numbers)%2!=0: #reminder not equal to 0 = ODD
            median = numbers[m]
        elif len(numbers)%2==0: #reminder equals to 0 = EVEN
            median = (numbers[m-1]+numbers[m])/2 #Calculating median for even numbers
        #todo: to be continue on deviation

        #deviation = stdev(numbers,mean)
        return float(mean), float(median)
    else:
        return None

test1 = calculate_statistics(20, 30, 40)
test2 = calculate_statistics(3.5, 2.56, 12, 34, 90)
test3 = calculate_statistics(1, 2, 3, 4, 5)
test4 = calculate_statistics(10, 15, 20, 25, 30, 35)
print(test1)
print(test2)
print(test3)
print(test4)