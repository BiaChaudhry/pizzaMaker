# -*- coding: utf-8 -*- 
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print("")
print("\t\t\t\t\t\tWELCOME TO FREE PIZZA MAKER >>> NO MONEY PIZZA")
print("\t\t\t\t\t\t\tWE BAKE, YOU TAKE")
print(" ")
print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

orderCount = 0
def pizzaTypesAndSize(orderCount, counterListForPizzaType, counterListForPizzaSize, typeList, sizeList):
	listComb = []
	
	while(orderCount < 5):
	    #for pizza type
		print("Please Select the Pizza Type:")
		countT = 0
		for i in (typeList):
			countT +=1
			print(i)
		print("--------------------------------------------------------------------")

		pizzaTypeNo = input("Please Enter Pizza Type Number: ")

		for pizzaType in typeList:
			if pizzaTypeNo == int(pizzaType[0]):
				counterListForPizzaType[pizzaTypeNo-1] += 1
				
				listComb.append(pizzaType[2:])
		print("--------------------------------------------------------------------")	
		#for pizza size
		print("Please Select the Pizza Size:")
		countS = 0
		for i in (sizeList):
			countS +=1

			print(i)
		print("--------------------------------------------------------------------")
		pizzaSizeNo = input("Please Enter Pizza Size Number: ")

		for pizzaSize in sizeList:
			if pizzaSizeNo == int(pizzaSize[0]):		
				counterListForPizzaSize[pizzaSizeNo-1] += 1
				
				listComb.append(pizzaSize[2:])

		print("--------------------------------------------------------------------")
		

		orderCount += 1
		

	print("|||||||||||||||||||||||||||||||||||||||||R E P O R T||||||||||||||||||||||||||||||||||||||||")
	print("")

	orderNo = 1
	for i in range(0,len(listComb)-1,2):
		print("Order No: "+str(orderNo) + " is "+ listComb[i] + ", " + listComb[i+1]  )
		orderNo += 1

	print("--------------------------------------------------------------------")

 	print("There are Total " + str(orderCount) +" Orders,"+ "\n")
 	print("")
 	print("--------------------------------------------------------------------")
	counter(orderCount)

	print("--------------------------------------------------------------------")


def order(orderCount, counterListForPizzaType, counterListForPizzaSize, typeList, sizeList):
	
	
	counterT = 1
	counterL = 0
	
	print("|||||||||||||||||||||||||||||||||||||PIZZA TYPE REPORT|||||||||||||||||||||||||||||||||||||")
	for typeNo in counterListForPizzaType:
		
		if typeNo != 0:
			
			print("\tOrder For: "+ str((typeList[counterT-1])[2:]))
			print("\tQuantity: " + str(typeNo))
			counterL += 1
		counterT += 1
	print("|||||||||||||||||||||||||||||||||||||PIZZA TYPE REPORT ENDS||||||||||||||||||||||||||||||||")
	print("")
	print("|||||||||||||||||||||||||||||||||||||PIZZA SIZE REPORT|||||||||||||||||||||||||||||||||||||")
	counterS = 1
	for sizeNo in counterListForPizzaSize:
		
		if sizeNo != 0:
			print("\tSize: "+ str((sizeList[counterS-1])[2:])) 
			print("\tQuantity: " + str(sizeNo))
		counterS += 1

	counterComb = 1

	print("||||||||||||||||||||||||||||||||||||||PIZZA SIZE REPORT ENDS|||||||||||||||||||||||||||||||||||||")

def counter(orderCount):
	while orderCount > 0:
		if orderCount <= 2:
			orderCount -= 1
			print("")
			print("There is " + str(orderCount) + " order remaining")
			print("")
			print("|||||||||||||||||||||||||||||||||||||PIZZA IN PROCESS|||||||||||||||||||||||||||||||||||||")
			print("")
			complete()
			print("")
			
		
		else:
			orderCount -= 1
			print("")
			print("There are " + str(orderCount) + " orders remaining")
			print("")
			print("|||||||||||||||||||||||||||||||||||||PIZZA IN PROCESS|||||||||||||||||||||||||||||||||||||")
			print("")
			complete()
	print("\t\t\t\t\t\tAll ORDERS OF TODAY ARE DONE, GO HOME WITH SATISFACTION !")


def complete():
	print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>PIZZA DELIVERED>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def main():

	
	
	counterListForPizzaType = [0,0,0,0,0,0,0]
	counterListForPizzaSize = [0,0,0,0,0]	
	typeList = ["1-chicken cheese","2-cheesy Veg","3-bar b que","4-fahita","5-spicy lahori pizza","6-mutton pizza","7-beef pizza"]
	sizeList = ["1-small","2-medium","3-large","4-extra large","5-customize"]
	
	pizzaTypesAndSize(orderCount, counterListForPizzaType, counterListForPizzaSize, typeList, sizeList)
	order(orderCount, counterListForPizzaType, counterListForPizzaSize, typeList, sizeList)
	
	

main()
