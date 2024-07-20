# variable length arguments *args (Non Keyword Arguments) Here name(arg) doesn't matter, * matters


def order_food(min_order, *args):      # *args will be stored in the form of tuple.
    print(f"You have ordered, first item: {min_order}")
 #   print(args)
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 min")
    print("Enjoy the party")

order_food("Salad", "Pizza", "Biryani", "Soup")     # Salad is stored in min_order and other items are stored in *args