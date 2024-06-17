from classes import Car
from tqdm import tqdm

def helloWorld(inputtedText: str):
    """This is a docstring
    """
    # Block Comment
    print(inputtedText) # Print Hellow World

    thisIsADict: dict[str, Car] = {}
    thisIsADict["owner1"] = Car(brand = "mazda")
    thisIsADict["owner2"] = Car(brand = "tesla")
    
    print(thisIsADict)
    for key in tqdm(thisIsADict):
        print(thisIsADict[key].carBrand)