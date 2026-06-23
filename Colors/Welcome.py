# F-format string Welcome brief
#insert name with format string (f)
name = input(str("Enter your name --> "))
print("")
print("***********************************")
print(f"Welcome my fellow soldier {name}!!")
print("***********************************")
print("")

#insert color lower case
color = input(str("Insert your favourite color --> ")).lower()
print("")

#color red output
if color == "red" or color == "dark red" or color == "bordeaux":
    red =""" YOU COMMUNIST !!!! 

    Spiritually...
    the color red symbolizes life force, raw energy, and passion. 

    It connects directly to our most primal instincts:
    courage, survival, and physical action. 
    Because of its intensity, 

    red bridges the gap between material manifestation 
    and the deepest desires of the heart.

     ㅤ♡ ㅤ♡ ㅤ♡ ㅤ♡ ㅤ♡ ㅤ♡ ㅤ♡ ㅤ♡ ㅤ♡ ㅤ♡ 
    
          """
    print(red)

#color orange output  ㅤ
elif color == "orange":
    orange = """                     
                       " ॐ "
    
    In Buddhism and Hinduism, shades of orange (saffron) 
    represent sacred devotion, illumination
    and the relinquishing of material desires.


    It is also linked to the fall season, it represents
    seasonal transition and abundance
    """
    print(orange)

#color yellow output
elif color == "yellow":
    yellow = """ Morning sunshine...

    Yellow color symbolism represents 
    both the brightest joy 
    and the darkest warnings.

    Yellow is simultaneously the color of sunshine,
    creativity and cowardice, 
    enlightenment and anxiety.
              
              𖤓

    """
    print(yellow)

#color green output
elif color == "green" or color == "dark green":
    green = """ Ohhh...What a Wise choice soldier...

          🌿
    Green for nature
    Green for growth
    Green for health
    of the mind 
    and the body

     𖡼.𖤣𖥧𖡼.𖤣𖥧

    """
    print(green)

#color sky-blue output
elif color == "sky blue" or color == "sky-blue" or color == "light blue":
    skyBlue = """ The color of the sky and the sea 
but most importantly, the color of... FREEDOM !


Beyond the wall...
there's a sea. 
On the other side of the sea... 
is freedom. 
That's what I always believed... 
But I was wrong. 
On the other side of the ocean... 
are our enemies.
Every day... spent over there. 
Minds and bodies ruined. Dreams of freedom erased. 
If we kill all our enemies over there... 
will we finally be free?

    ⊹ ࣪ ﹏𓊝﹏𓂁﹏⊹ ࣪ ˖

                    -Eren Yeager
"""
    print(skyBlue)

#color blue output
elif color == "blue" or color == "dark blue" or color == "dark-blue":
    blue = """  the color of - AUTHORITY -

    Represents Depth and Order
            ⚖️🗝️📜
         but also...
    Loneliness or Detachment 
               𐀪 
the blues...

"""
    print(blue)

#color purple output
elif color == "purple":
    purple = """ Purple... what a rare and mysterious color...
    
    FUN FACT: purple is considered to be 
    one of the most difficult colors
    to find in nature !!

    and...

    It actually does not exist in the light spectrum of a rainbow 
    it is a "non-spectral" color. 
    Your brain hallucinates purple 
    when your eyes take in blue and red light 
    at the exact same time !!
                                           
                                            - ⋒
    

"""
    print(purple)


#color brown output 
elif color == "brown" or color == "light-brown" or color == "light brown":
    brown = """ Nice choice !!
                often people misread this as a boring color but they don't know...

                That you are a great counselor and friend full of wisdom.
                it is also a symbol of stability security and protection,


                                                        -𖣂
"""
    print(brown)

#color black output
elif color == "black":
    black = """ You emo...

    Black...
    is tied to the unknown, 
    the night sky, and hidden cosmic truths. 
    It represents sacred wisdom 
    that has not yet been revealed
    to the conscious mind ˚꩜｡

"""
    print(black)

#color white output
elif color == "white":
    white = """ You might be an angel...

            White represents purity and innocence
            it is often used in religious ceremonies
            such as weddings and baptism 

            some considere it peaceful and calming 
            others think that it looks empty and bland 
            
            it's a matter of perspective 𝓐𝓷𝓰𝓮𝓵 ་࿐

            
"""
    print(white)

#color pink output 
elif color == "pink" or color == "baby-pink" or color == "baby pink":
    pink = """ Sakura...

         Associated with the blooming of 
         cherry blossoms, 
         symbolizing: renewal, beauty
         and the transience of life. 
          
               𐫱  ✿  ❀  ❁  ✽
            
               
"""
    print(pink)


else:
    print("COLOR NOT FOUND!!")

