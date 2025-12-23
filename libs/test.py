from sklearn.tree import DecisionTreeClassifier

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
        return None
    
    def check(self):
        coffee = int(input("Have coffee ? 0 or 1 -> "))
        coca = int(input("Have coca ? 0 or 1 -> "))
        milk = int(input("Have milk ? 0 or 1 -> "))
        water = int(input("Have water ? 0 or 1 -> "))

        return coffee, coca, milk, water
    
    def predict(self, c, co, mi, wa):
        this_model = DecisionTreeClassifier()
        this_model.fit(self.data_set, self.result)

        print(this_model.predict([[c, co, mi, wa]]))