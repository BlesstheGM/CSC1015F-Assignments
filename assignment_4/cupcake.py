# program to determine whether you should eat a dropped cupcake or not
# Blessing Hlongwane
# HLNBLE002
# 07 March 2023

print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")
anyone_see = input("""Did anyone see you? (yes/no)
""")
if anyone_see == "yes":
    person_saw = input("""Was it a boss/lover/parent? (yes/no)
""")
    if person_saw == "yes":
        expensive = input("""Was it expensive? (yes/no)
""")
        if expensive == "yes":
            touch_floor = input("""Can you cut off the part that touched the floor? (yes/no)
""")
            if touch_floor == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Your call.")
        else:
            chocolate = input("""Is it chocolate? (yes/no)
""")
            if chocolate == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
    else:
        print("Decision: Eat it.")
else:
    sticky = input("""Was it sticky? (yes/no)
""")
    if sticky == "yes":
        raw_steak = input("""Is it a raw steak? (yes/no)
""")
        if raw_steak == "yes":
            puma = input("""Are you a puma? (yes/no)
""")
            if puma == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat_lick = input("""Did the cat lick it? (yes/no)
""")
            if cat_lick == "yes":
                cat_healthy = input("""Is your cat healthy? (yes/no)
""")
                if cat_healthy == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
    else:
        emausaurus = input("""Is it an Emausaurus? (yes/no)
""")
        if emausaurus == "yes":
            megalosaurus = input("""Are you a Megalosaurus? (yes/no)
""")
            if megalosaurus == "yes":
                print("Decision: Eat it.")
            else:
                print("Decision: Don't eat it.")
        else:
            cat_like = input("""Did the cat lick it? (yes/no)
""")
            if cat_like == "yes":
                cat_healthy = input("""Is your cat healthy? (yes/no)
""")
                if cat_healthy == "yes":
                    print("Decision: Eat it.")
                else:
                    print("Decision: Your call.")
            else:
                print("Decision: Eat it.")
        