## https://leetcode.com/problems/method-chaining/

import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.sort_values('weight', ascending=False)[animals['weight'] > 100][['name']]