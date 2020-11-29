import pandas as pd

def lambda_handler(event, context):
    data = [1,2,3,4,5]
    df = pd.DataFrame(data)
    print(df)