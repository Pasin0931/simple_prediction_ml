from libs.test import drink_maker

baresta = drink_maker()

coffee, milk, coca, water = baresta.check()
baresta.predict(coffee, milk, coca, water)

baresta.decision_tree_display()

# Train / Test not yet (not done)
# detect overfitting (not done)