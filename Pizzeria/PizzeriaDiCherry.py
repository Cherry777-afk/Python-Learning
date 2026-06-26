menu = """ 

       - CHERRY'S PIZZERIA -


Pizza's:                     Prices:

. MARGHERITA                |   5.00 £
. FRIES & WURSTEL           |   6.00 £    
. DIAVOLA                   |   6.50 £   
. CACIO PEPE                |   6.00 £
. PARMIGIANA                |   7.00 £   
. BRESAOLA E RUCOLA         |   7.50 £
. FRUTTI DI MARE            |   8.00 £


Side's:
. FRENCH FRIES              |   2.50 £
. CURLY FRIES               |   3.00 £
. 4 FILLED JALAPENO         |   3.50 £
. 4 PRAWN SPIEDINI          |   4.50 £
. FRITTO MISTO              |   7.00 £
. SALMON TARTARE            |   8.00 £


Deserts:
. PIZZA NUTELLA             |   4.00 £ 
. TIRAMISU'                 |   4.00 £
. PARADISO CAKE             |   4.00 £
. BUENO CAKE                |   4.50 £
. CREAM & STRAWBERRIES      |   2.50 £      
. BANANA SPLIT              |   3.50 £

************************
  HOUSE SPECIALS:   
. CHERRY CAKE               |   5.00 £   
*************************


Drinks: 
. REFIL WATER                |   FREE
. COKE                       |   2.00 £ 
. SPRITE                     |   2.00 £
. FANTA                      |   2.00 £
. ESTATHE'                   |   1.50 £
. NON-ALCOHOLIC MOJITO       |   4.00 £
. NON-ALCOHOLIC SPRITZ       |   4.50 £

"""

# -Welcome brief-  
welcome ="""

********************************
Welcome to - CHERRY'S PIZZERIA -

      つ ◕_◕ ༽つ🍅🧀🍕

********************************

"""
print(welcome)

#-user starting point- insert INPUT name + accomodation message
name = str(input("Customer name: "))

accomodate = f"""
Good evening, {name}
my name is Lilly :3
and i will be serving you today !!
"""
print(accomodate)

#table diplay UI
table = """
_______________________       _________________________
                                                
1|  ⛩ ┬─┬ ⛩        2|  𓊯𓀻             3|  ⛩ ┬─┬ ⛩ 
                                                
4|   𓊯𓀻             5| ⛩ ┬─┬ ⛩        6|   𓊯𓀻

7|  ⛩ ┬─┬ ⛩        8|   𓊯𓀻            9|  ⛩ ┬─┬ ⛩ 
_______________________________________________________

"""

#asking in the user wants to take table seat show table
while True:
    try:
      viewtable = str(input("- Would do like to take a seat? ")).lower()
      if viewtable in ["yes", "yeah", "sure"]:
        print("")
        print("********************************************************")
        print(table)
        eat_inside = True
        break

      #if user says no to table seat and wants to take-away, show the menu
      elif viewtable in ["no", "nah", "nope"]:
        takeAway = input(str("- Would you like to view menu and take-away? ")).lower()

        if takeAway in ["yes", "yeah", "sure"]:
          print("")
          print("**************************************************")
          print(menu)
          eat_inside = False
          break

        else:
           print("Ok, no menu' shown")
           eat_inside = False
           break
        
      else:
        print("Please answer yes or no.\n")

    except ValueError:
        print("Enter a valid option.\n")



#table selection if viewtable == yes
#user will input table n^ 
#if conditions for already occupied tables
occupied_tables =  [2, 4, 6, 8]

while eat_inside ==  True:
  try: 
      pickTable = int(input("Which table Number would you like to pick? "))
      print("")

      #table does not exist
      if pickTable < 1 or pickTable > 9:
        print("Table does not exist... try again")
        continue
        

        #table is occupied by another customer 
      if pickTable in occupied_tables:
        print("This table is busy, pick again")
        continue 

      print(f"I will walk you through to table N'{pickTable}")
      break

  except ValueError:
    print("Please enter a valid number")


#the user will now be assigned to his table (UI)
if eat_inside == True:
    chosenTable = f"""

______________      __________________

{pickTable}|  ⛩ ┬─┬ ⛩  <-- {name}'s table

   -This will be your table for today
______________________________________

"""
    print(chosenTable)

closing = """
**YOU HAVE BEEN ESCORTED OUT OF THE PIZZERIA**

                  |
            _____ V ______
           |   pizzeria   | 
           |    CLOSED    |
           |______________| 

           """         

while eat_inside == True:
  try:
      tableMenu = str(input("Would you like to see the menu? ")).lower()

      #if customers says YES show menu
      if tableMenu in ["yes", "yeah", "sure"]:
        print (menu)
        break

      #if customer says no 
      elif tableMenu in ["no", "nah", "nope"]:
          company = str(input("Are you waiting for someone? ")).lower()

          #if they said no and are waiting for company
          if company in ["yes", "yeah", "sure"]:
            print("")
            print("No problem! i will come back later")
        
            #the company arrives
            companyArrives = """

    *15 minutes later*
............................
    *Company has arrived*
            𐦂𖨆𐀪𖠋
            """       
            print(companyArrives)

            print("***************************************")
            print("Menu has now been brought to your table")
            print("***************************************")
            print("")


            openMenu = str(input("**Would you like to open menu' (yes / no)** : ")).lower()

            if openMenu in ["yes", "yeah", "sure"]:
              print(menu)
              break

            elif openMenu in ["no", "nah", "nope"]:                 
              print(closing)
              break

            else:
              print("answer yes/no")

          else:
            print(closing)
            break

  except ValueError:
    print("Insert correct Value !")