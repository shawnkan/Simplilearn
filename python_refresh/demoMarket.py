class demoMarket():

  #private date members
  __admin = {
      "a1":"p1",
      "a2":"p2"
      }
  __user = {
      "u1":"pa",
      "u2":"pb"
      }
  #used to track sessions and generate sessionID that is not in carts
  session = 2

  _carts = {
      1: {1001:1,1002:2},
      2: {1001:3,1002:4}
  }
  productCatalog = [
      {"productID": 1001, "name": "Boots",   "categoryID":1, "price": 80},
      {"productID": 1002, "name": "Shoes",   "categoryID":1, "price": 30},
      {"productID": 1003, "name": "Coats",   "categoryID":2, "price": 200},
      {"productID": 1004, "name": "Jackets", "categoryID":2, "price": 150},
      {"productID": 1005, "name": "Caps",    "categoryID":2, "price": 20},
      {"productID": 1006, "name": "Monitor", "categoryID":3, "price": 180},
      {"productID": 1007, "name": "Mouse",   "categoryID":3, "price": 10}

  ]

  def __init__(self):
    print("Welcome to the Demo Marketplace.")

  #check for unique sessionID
  def genSessionID(self):
    while self.session in self._carts:
      self.session+=1
    return self.session

  #check for admin login
  def adminLogin(self, userName, pWord):
    #check if admin exists
    if userName not in self.__admin or self.__admin[userName] != pWord:
      return False
    else:
        return True
  ################################## User Menus #########################################
  #check for user login
  def userLogin(self, userName, pWord):
    #check if user exists
    if userName not in self.__user or self.__user[userName] != pWord:
      return False
    else:
      return True

  #prints the catalog
  def viewCatalog(self):
    print("ProductID\tName\t\tCategory\tPrice")
    for item in self.productCatalog:
      print(f"{item['productID']}\t\t{item['name']}\t\t{item['categoryID']}\t\t{item['price']}")


  #allows users to select a previous session and view the contents of the cart
  def viewCart(self):
    print("Sessions Available: ")
    print(list(self._carts.keys()))
    sid = input("Enter Session ID: ")
    if sid.isdigit():
      sid = int(sid)
      if sid in self._carts:
        carts = self._carts[sid]
        print("ProductID\tName\t\tQty")
        for k,v in carts.items():
          for product in self.productCatalog:
            if product["productID"] == k:
              print(f"{product['productID']}\t\t{product['name']}\t\t{v}")
              break

      else:
        print("Invalid SessionID")
    else:
      print("Invalid Integer Input")


  #allows users to select a session and add items to the session's cart
  #allows users to create a new session and add items to the session's cart
  #error messages if session does not exist
  def addCart(self):
    print("Sessions Available: ")
    print(list(self._carts.keys()))

    sid = input("Key in SessionID to add to or enter 'N' for new: ")
    mydict = {}
    #create empty cart
    if sid == 'N' or sid == 'n':
      sessionID = self.genSessionID()

      self._carts[sessionID]={}
      sid = sessionID
    #retrieve existing cart
    elif sid.isdigit():
      sid = int(sid)
      if sid in self._carts:
        mydict = self._carts[sid]
      else:
        print("Invalid Session ID")
        return None
    else:
      print("Invalid Integer SessionID")
      return None

    inLoop = True
    while(inLoop):
      print("Current Items in Cart: ")
      print(mydict)
      pid = input("Enter product ID to add or press 'q' to exit: ")
      #check if quit
      if pid == "q" or pid =="Q":
        break

      qty = int(input("Enter quantity: " ))

      #add item to list
      pid = int(pid)
      if pid in mydict:
        total = mydict[pid]+qty
        mydict[pid] = total
      else:
        mydict[pid] = qty

      self._carts[sid] = mydict

  #allows the user to delete items from cart
  def deleteCart(self):
    print("Sessions Available: ")
    print(list(self._carts.keys()))

    sid = input("Key in SessionID/Cart to delete or press 'q' to exit: ")

    if int(sid) in self._carts:
      sid = int(sid)
      mydict = self._carts[sid]
      print("Items in cart:")
      print(mydict)
      delItem = input("Enter pid of item to delete: ")
      if int(delItem) in mydict:
        mydict.pop(int(delItem))
        print("Item " + delItem + " has been deleted")
      else:
        print("Item not in cart")

      self._carts[sid]=mydict
    else:
      print("Cart does not exist")

  def checkOut(self):
    payOption = {
      1: "Net banking",
      2: "Pay Pal",
      3: "Credit Card"
    }
    print("Sessions Available: ")
    print(list(self._carts.keys()))

    sid = input("Key in SessionID/Cart to CheckOut or press 'q' to exit: ")

    if int(sid) in self._carts:
      sid=int(sid)
      mydict = self._carts[sid]
      total = 0


      print("Payment options:")
      for k,v in payOption.items():
        #print(item)
        print(str(k) + " : " + str(v))
      payChoice = input("Enter payment option: ")

      print("Your Order is successfully placed.")

      for pid,qty in mydict.items():
        for product in self.productCatalog:
          if(product["productID"] == pid):
            print(str(pid) + " " + product['name'] + " " + str(qty) + " " + str(product["price"]))
            total = total + (qty*product["price"])
            break

      print("You will shortly be redirected to the portal for "+ payOption[int(payChoice)] + " to make a payment of $" + str(total))

    else:
      print("Cart does not exist")
      return None

  def userSession(self):
    inLoop = True
    while (inLoop):
      print ("User Menu:")
      print("1.View Catalog")
      print("2.View Cart Contents")
      print("3.Add Item to Cart")
      print("4.Delete Item from Cart")
      print("5.Checkout")
      print("6.Exit")
      userChoice = int(input("Please Enter User Choice: "))
      print("================================================")
      if userChoice == 1:
        self.viewCatalog()
      elif userChoice == 2:
        self.viewCart()
      elif userChoice == 3:
        self.addCart()
      elif userChoice == 4:
        self.deleteCart()
      elif userChoice == 5:
        self.checkOut()
      elif userChoice == 6:
        inLoop = False
      print("================================================")

  ################################## Admin Session ##############################
  def addCatalog(self):
    print("Items in Catalog")
    self.viewCatalog()
    itemID = int(input("Enter product ID (Integer): "))
    itemName = input("Enter product name: ")
    categoryID = int(input("Enter Category ID (Integer): "))
    price = int(input ("Enter price (Integer):"))

    mydict ={'productID':itemID, 'name':itemName, 'categoryID':categoryID, 'price':price}
    print(mydict)
    self.productCatalog.append(mydict)

  def modCatalog(self):
    print("Items in Catalog")
    self.viewCatalog()
    itemID = input("Enter product ID(Integer) to modify or 'q' to exit to previous: ")
    if itemID == 'q' or itemID =='Q' or itemID.isdigit()==False:
      return
    else:
      itemID = int(itemID)

    itemName = input("Enter product name: ")
    categoryID = int(input("Enter Category ID (Integer): "))
    price = int(input ("Enter price (Integer):"))
    mydict ={'productID':itemID, 'name':itemName, 'categoryID':categoryID, 'price':price}

    count = 0
    for item in self.productCatalog:
      if item['productID'] == itemID:
        break
      else:
        count+=1

    if count >= len(self.productCatalog):
      print("Item not in list")
    else:
      self.productCatalog[count] = mydict

  def deleteItem(self):
    print("Items in Catalog")
    self.viewCatalog()
    itemID = input("Enter product ID to delete(Integer) or 'q' to exit to previous: ")
    if itemID == 'q' or itemID =='Q' or itemID.isdigit()==False:
      return
    else:
      itemID = int(itemID)

    count = 0
    for item in self.productCatalog:
      if item['productID'] == itemID:
        break
      else:
        count+=1
    self.productCatalog.pop(count)

  def deleteCategory(self):
    print("Items in Catalog")
    self.viewCatalog()
    catID = input("Enter Category ID to delete(Integer) or 'q' to exit to previous: ")
    if catID == 'q' or catID =='Q' or catID.isdigit()==False:
      return
    else:
      catID = int(catID)

    toRemove = []
    for item in self.productCatalog:

      if item['categoryID'] == catID:
        toRemove.append(item)

    for item in toRemove:
      self.productCatalog.remove(item)


  def adminSession(self):
    inLoop = True
    while (inLoop):
      print("================================================")
      print ("Admin Menu:")
      print("1.View Catalog")
      print("2.Add Items to Catalog")
      print("3.Modify Item in Catalog")
      print("4.Delete Item from Catalog")
      print("5.Delete Category from Catalog")
      print("6.Exit")
      userChoice = int(input("Please Enter User Choice: "))
      print("================================================")
      if userChoice == 1:
        self.viewCatalog()
      elif userChoice == 2:
        self.addCatalog()
      elif userChoice == 3:
        self.modCatalog()
      elif userChoice == 4:
        self.deleteItem()
      elif userChoice == 5:
        self.deleteCategory()
      elif userChoice == 6:
        inLoop = False
      print("================================================")


  #check if admin or user, key in username and password
  #attempt to login
  def login(self):

    inLoop = True
    while(inLoop):
        option = input("Type 'A' for Admin, 'U' for user, 'Q' to quit: ")
        if option=='q' or option =='Q':
          break
        userName = input("Key in UserName: ")
        pWord = input("Key in Password: ")
        if (option=='A' or option=='a'):
            checkAdmin = self.adminLogin(userName,pWord)
            if checkAdmin:
                self.adminSession()
            else:
                print("Incorrect Credentials or Admin does not exist")
        elif (option=='U' or option =='u'):
            checkUser = self.userLogin(userName,pWord)
            if checkUser:
                self.userSession()
            else:
                print("User does not exist")
        else:
            print("Invalid Login")

test = demoMarket()
test.login()
