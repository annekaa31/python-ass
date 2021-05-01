# python-ass

Exercise Task #1:

Given the list nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the list in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:

Input: nums = [2,5,1,3,4,7]

Output: [2,3,5,4,1,7] 

Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:

Input: nums = [1,2,3,4,4,3,2,1]

Output: [1,4,2,3,3,2,4,1]

Example 3:

Input: nums = [1,1,2,2]

Output: [1,2,1,2]

Constraints:

nums.length == 2n
1 <= nums[i] <= 10^3
 

Exercise Task #2:

Given two files inputA and inputB that contain one word each of them. Write an algorithm to determine if the word in the inputA file is an anagram of the word in the inputB file.

Example 1:

Input: 

inputA.txt: anagram

inputB.txt: nagaram

Output: true

Example 2:

Input:

inputA.txt: rat

inputB.txt: car

Output: false

Note:

You may assume the string contains only lowercase alphabets.

Explanation:

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, the word anagram can be rearranged into nag a ram, or the word binary into brainy or the word adobe into abode.

 

Exercise Task #3:

Given a non-empty list of integers, every element appears twice except for one. Find that single one.

Example 1:

Input: [2,2,1]

Output: 1

Example 2:

Input: [4,1,2,1,2]

Output: 4

 

Exercise Task #4:

Given a list nums. We define a running sum of a list as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]

Output: [1,3,6,10]

Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:

Input: nums = [1,1,1,1,1]

Output: [1,2,3,4,5]

Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:

Input: nums = [3,1,2,10,1]

Output: [3,4,6,16,17]

 Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
 

Exercise Task #5:

Given an encrypted text t and value s. Write an algorithm that will decrypt the text by moving each letter by s numbers in an alphabet. For example if the input is a and s is equal to 3, the algorithm must return d. (a,b,c,d)

Link: https://en.wikipedia.org/wiki/Caesar_cipher (Links to an external site.)

Example:

t = ”Tkh txlfn eurzq ira mxpsv ryhu wkh odcb grj”

s = 3

Output: 

Encrypted text: “Tkh txlfn eurzq ira mxpsv ryhu wkh odcb grj”

Shift: 3

Decrypted text: “The quick brown fox jumps over the lazy dog”

Note:

You must shift only small case letters
