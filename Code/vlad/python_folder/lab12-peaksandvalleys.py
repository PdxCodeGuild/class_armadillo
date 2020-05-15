#Lab 12: Peaks and Valleys!

"""
#       0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
​
​
# iterating over the elements
# for element in data:
#   print(element)
​
# iterating over a range
# for i in range(10) # 0, 1, 2, ... 9
# for i in range(20) # 0, 1, 2, ... 19
# for i in range(0, 10) # 0, 1, 2, ... 9
# for llama in range(5, 10) # 5, 6, 7, 8, 9
​
# iterating over the indices
# for i in range(len(data)):
#   print(data[i])
​
# example - adding of numbers
def sum_pairs(nums):
  output = []
  # crashes because i+1 will be one past the end
  # for i in range(0, len(nums)):
  for i in range(0, len(nums)-1):
    print(i, nums[i])
    total = nums[i] + nums[i+1]
    output.append(total)
  return output
​
print(sum_pairs([1, 2, 3, 4])) # [3, 5, 7]
print(sum_pairs([6, 1, 4])) # [7, 5]
"""

#Define the following functions:

#peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.

#valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.

#peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of appearance in the original data.



data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# if a value at either side of the index are equal and the middle  
# then the value is greater than the two indexes then there is a peak
def peaks(data):
    output_peaks = []
#    for i, value in enumerate(data):
#       #if data[5] == data[7] and data[6]:
#       print(i,value)
    i = 1 # we start the counter at 1 is to void going to negative numbers
    while i < len(data) -1:
        current = data[i]
        previous = data[i-1]
        following = data[i+1]
        if current > previous and current > following:
            output_peaks.append(i)
            print(f'Current peak value of {current} at index {i} is equal to previous value of {previous}')
            
        # data[i]
        # print(f'index:{i} value: {data[i]} ')
        #print(f'{}')
    
    
        i += 1
   # print(output_peaks)
    return output_peaks
            
peaks(data)

def valleys(data):
    output_valley = []
    i = 1
    while i < len(data) -1:
        current1 = data[i]
        previous1 = data[i+1]
        following1 = data[i-1]
        if current1 < previous1 and current1 < following1:
            output_valley.append(i)
            
            print(f'Current1 valley value of {current1} at index {i} is less to previous value of {previous1}')
        # data[i]
        # print(f'index:{i} value: {data[i]} ')
        #print(f'{}')
        i += 1
       
   # print(output_valley)
    return output_valley


valleys(data)

def s_and_valleyspeak(data):
    peaks_list = peaks(data) 
    valleys_list = valleys(data)
    peaks_and_valleys = peaks_list + valleys_list
    peaks_and_valleys.sort()
    print(peaks_and_valleys)
    
s_and_valleyspeak(data) #[6, 9, 14, 17]