def dragon(heat, damage):
    """
    Creates a mean dragon
    :param heat: potency of dragon fire (1-100)
    :param damage: how hard the dragon bites )1-50)
    :return: the sum of heat and damage
    """
    try:
        heat = int(heat)
        damage = int(damage)
    except ValueError:
        print("You must use numbers for the dragon attributes")
        return
    #here comes the body of the function
    print(f"You are creating a dragon with fire power of {heat} and bite power of {damage}")
    return heat+damage
    #that's it
#print(help(dragon))
dragon1 = dragon(17, 10)
dragon2 = dragon(17,45)
if dragon1 > dragon2:
    print("dragon1 is stronger")
else:
    print("dragon2 is stronger")
#dragon("Bogdan",999)