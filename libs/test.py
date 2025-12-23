from sklearn.tree import DecisionTreeClassifier

import sklearn.tree as sk_tree
import matplotlib.pyplot as pyplt

class drink_maker:
    def __init__(self):
        # coffee - milk - coca - water
        self.data_set = [
            [1, 0, 0, 1],
            [2, 0, 0, 2],
            [0, 1, 1, 0],  
            [0, 2, 2, 0],  
            [1, 1, 1, 0],  
            [2, 2, 1, 0],  
            [0, 0, 0, 0],  
            [0, 0, 0, 1],
        ]
        self.result = ["Coffee", "Coffee", "Hot Chocolate", "Hot Chocolate", "Mocha", "Mocha", "None", "None"]

        self.this_model = DecisionTreeClassifier(max_depth=6, random_state=0)
        self.this_model.fit(self.data_set, self.result)

        return None
    
    def check(self):
        coffee = int(input("Enter coffee amount -> "))
        milk = int(input("Enter milk amount -> "))
        coca = int(input("Enter coca amount -> "))
        water = int(input("Enter water amount -> "))

        return coffee, milk, coca, water
    
    def predict(self, c, mi, co, wa):
        print(self.this_model.predict([[c, mi, co, wa]])[0])

    def decision_tree_display(self):
        pyplt.figure(figsize=(7, 7))
        sk_tree.plot_tree(self.this_model, feature_names=["coffee", "milk", "coca", "water"],
                          class_names=["Coffee", "Hot Chocolate", "Mocha", "None"],
                          filled=True, rounded=True)
        pyplt.show()
        