import prettytable

itemArray = prettytable.PrettyTable()
itemName = []
itemCode = []
itemCount = []
matches = 0

while True:
    matches = 0

    barcode = input("Scan an Item or Say 'Done': ")
    
    if (barcode.lower() == "done"):
        itemArray.add_column("Barcode", itemCode)
        itemArray.add_column("Name", itemName)
        itemArray.add_column("Count", itemCount)

        print(itemArray)

        break
    
    for i in range (len(itemCode)):
        if barcode == itemCode[i]:
            itemCount[i] += 1
            matches = 1

            break
    
    if matches == 0:
        itemName.append(input("Item Name: "))
        itemCode.append(barcode)
        itemCount.append(1)