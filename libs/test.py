from sklearn.tree import DecisionTreeClassifier

import sklearn.tree as sk_tree

class drink_maker:
    def __init__(self):
        # coffee - milk - coca - water
        self.data_set = [
            [1, 0, 0, 1],
            [0, 1, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0]
        ]
        self.result = ["Coffee", "Hot Chocolate", "Mocha", "None"]

        self.this_model = DecisionTreeClassifier()
        self.this_model.fit(self.data_set, self.result)

        return None
    
    def check(self):
        coffee = int(input("Have coffee ? 0 or 1 -> "))
        milk = int(input("Have milk ? 0 or 1 -> "))
        coca = int(input("Have coca ? 0 or 1 -> "))
        water = int(input("Have water ? 0 or 1 -> "))

        return coffee, milk, coca, water
    
    def predict(self, c, mi, co, wa):
        print(self.this_model.predict([[c, mi, co, wa]]))

    def decision_tree_display(self):
        sk_tree.plot_tree(self.this_model)
        