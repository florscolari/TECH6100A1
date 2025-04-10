# TECH6100 Assessment 1 Florencia Scolari ID 1847863 Apr 2025
def calculate_statistics(*numbers):
    if len(numbers) > 0:
        """To get the MEAN"""
        mean = sum(numbers) / len(numbers)  # average value

        """To get the MEDIAN"""
        median = sorted(numbers)
        """Calculate Median for 2 cases: list is odd or list is even"""
        m = len(numbers) // 2  # m is the middle point. '//' is floor division, rounded to min closest digit
        if len(numbers) % 2 != 0:  # reminder not equal to 0 = ODD
            median = numbers[m]
        elif len(numbers) % 2 == 0:  # reminder equals to 0 = EVEN
            median = (numbers[m - 1] + numbers[m]) / 2  # Calculating median for even numbers

        """To get the POPULATION STANDARD DEVIATION"""
        temp = []
        for item in numbers:
            item = (item - mean)  # 2. Subtract the mean from each data point.
            item = item * item  # 3. Square each deviation to make it positive.
            temp.append(item)  # Hold all squared deviations together (list)
        total = 0
        for num in temp:
            total += num  # 4. Sum of all squared deviations together
        variance = total / len(numbers)  # 5. Divide the sum by the number of data points (called Variance)
        deviation = variance ** 0.5  # 6. Get the square root of the variance (called population std deviation)

        return {
            'mean': float(mean),
            'median': float(median),
            'std_dev': round(deviation, 3)
        }
    else:
        message = "No numbers were given."
        return message


test3 = calculate_statistics(1, 2, 3, 4, 5)
test4 = calculate_statistics(10, 15, 20, 25, 30, 35)

print('Test 3', test3)
print('Test 4', test4)
