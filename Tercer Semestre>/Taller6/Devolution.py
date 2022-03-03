def devolution(bills:list, value:int):
  bills.sort(reverse = True) #O(n log n)
  for i in bills:
    number_of_bills = value //i
    value = value % i
    if value == 0:
      print(str(number_of_bills) + " de " + str(i))
      break
    print(str(number_of_bills) + " de " + str(i))


devolution([500, 200, 100, 50] , 1900)
