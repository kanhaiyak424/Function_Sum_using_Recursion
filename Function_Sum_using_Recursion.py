#Program for summation of natural number using Recurrsion

n=int(input("Enter a number:"));
def sum(a):
 if a<=1:
  return 1;
 else:
  return a+sum(a-1); # recursion logic here
print("The summation of given series is:",sum(n));
