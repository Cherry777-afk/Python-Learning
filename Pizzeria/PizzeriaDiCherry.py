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
and i will be serving you today

"""
print(accomodate)

#table diplay UI
table = """

___________________       _______________________
                                                
1 ⛩ ┬─┬ ⛩         2   𓊯𓀻          3 ⛩ ┬─┬ ⛩ 
                                                
4    𓊯𓀻           5 ⛩ ┬─┬ ⛩       6   𓊯𓀻

7 ⛩ ┬─┬ ⛩         8   𓊯𓀻          9 ⛩ ┬─┬ ⛩ 
_________________________________________________

"""
print(table)


#user will input table n^ 
#if conditions for occupied tables
occupied_tables =  [2, 4, 6, 8]
while True:
    try: 
        picktable = int(input("Which table would you like to pick? "))

        #table does not exist
        if picktable < 1 or picktable > 8:
            print("Table does not exist... try again")
            continue
        
        #table is occupied by another customer 
        if picktable in occupied_tables:
            print("This table is busy, pick again")
            continue
        
        #correct table selection 
        print(f"I will assign you to table n^ {picktable}")
        break

    except ValueError:
        print("Please enter a valid number")





