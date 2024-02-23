def add_new_item(inventory):
    name=input("Enter the name for new item:--")
    quantity=int(input("Enter Quantity:"))
    price=float(input("Enter Price: "))
    category=input("Enter category: ")
    inventory[name]={"quantity":quantity,"price":price,"category":category}
    print("Item Added successfully!")

def update_items(inventory):
    n1=input("Enter the name of item whcih you want to update")
    new_quantity=int(input("enter the new quantity for selected otem"))
    new_price=int(input("enter the new price for selected item"))
    new_category=input("enter the new category for selected item")

    if n1 in inventory:
        inventory[n1]['category']=new_category
        inventory[n1]['quantity']=new_quantity
        inventory[n1]['price']=new_price

    for i,item in enumerate(inventory):
        if(item[name]==n1):
            item['quantity']=new_quantity
            item['price']=new_price
            item['category']=new_category
            print("Item updated successfully!")
            return
    print("Item not found")

def remove_item(inventory):
    view_items(inventory)
    index=int(input("Enter the index which you want to remove:---"))

    if(0<=index<len(inventory)):
        r_item=inventory.pop(index)
        print("item is removed!")
    else:
        print("invalid Item index")

def view_items(inventory):
    print("\n Inventory List")

    for name, details in inventory.items():
        print(f"{name}---category: {details['category']}, quautity---{details['quantity']}, price--{details['price']}")

def search_item(inventory):
    n1=input("Enter the name of the item which you want to search")

    if n1 in inventory:
        print(f"\n contact Details for {n1}:- ")
        print(f"category: {inventory[n1]['category']}")
        print(f"quantity: {inventory[n1]['quantity']}")
        print(f"price: {inventory[n1]['price']}")
    else:
        print(f"Contact '{n1}' not found")

def display():
    print("Inventory Management System")
    print("1.--add new item into inventory")
    print("2.---update exiting items into the inventory")
    print("3.---remove the item from the inventory")
    print("4.--- View the items present in inventory")
    print("5.---serach item by name in inventory")
    print("6.--- exit")

inventory={}

while True:
    display()
    choice=int(input("Enter your choice:- "))

    if(choice==1):
        add_new_item(inventory)
    elif(choice==2):
        update_items(inventory)
    elif(choice==3):
        remove_item(inventory)
    elif(choice==4):
        view_items(inventory)
    elif(choice==5):
        search_item(inventory)
    elif(choice==6):
        print("Exiting")
        break