############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []

    
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        
        self.code = new_code


def make_melon_types(melon_types):
    """Returns a list of current melon types."""

    all_melon_types = [] # musk, cas, cren, yw 

    # code, first_harvest, color, is_seedless, is_bestseller, name

    musk = MelonType("musk", 1998, "green", True, True, "Muskmelon")
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType("cas", 2003, "orange", True, False, "Casaba" )
    cas.add_pairing("strawberries", "mint")
    all_melon_types.append(cas)


    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('prosciutto')
    all_melon_types.append(cren)
    
    
    yw = MelonType("yw", 2013, "yellow", True, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)
    
    return all_melon_types


def print_pairing_info(all_melon_types_list):
    """Prints information about each melon type's pairings."""

    for melon in all_melon_types_list:
        print(f"{melon.name} pairs with")
        for pairing in melon.pairings:
            print(f"- {pairing}")

    


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""


    melon_dict = {}
    for melon in melon_types:
        melon_dict[melon.code] = melon

    return melon_dict

# dict = {code: "musk", color: 'green}

############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods


def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest


musk = MelonType("musk",
    "Muskmelon",
    1998,
    "green",
    True,
    True)

print_pairing_info(musk)