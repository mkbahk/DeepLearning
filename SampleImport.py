# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as tm
# tm.price(4)
# tm.price_morning(3)
# tm.price_soldier(4)

# from theater_module import *
# price(3)
# price_morning(3)
# price_soldier(4)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(4)

# from theater_module import price_soldier as price
# price(5)

import theater_module as tm 
import inspect 
import random

tm.price_soldier(4)
print(inspect.getabsfile(random))
print(inspect.getabsfile(tm))