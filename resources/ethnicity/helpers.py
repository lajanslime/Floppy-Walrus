import pandas as pd

lacounty_zip_df = pd.read_csv('ZIP_Codes_and_Postal_Cities.csv')

lacounty_zips=list(lacounty_zip_df['ZIP Code'])

def is_lacounty(zipcode):
    return int(zipcode) in lacounty_zips 

assert is_lacounty(90713) == True, "Function is not capturing a LA County Zip Code"
assert is_lacounty(91306) == True, "Function is not capturing a LA County Zip Code"
assert is_lacounty(94101) == False, "Function is misclassified as LA County Zip Code"
assert is_lacounty('90713') == True, "Function is not capturing a LA County Zip Code"
assert is_lacounty('91306') == True, "Function is not capturing a LA County Zip Code"
assert is_lacounty('94101') == False, "Function is misclassified as LA County Zip Code"

def extract_zip(code: str) -> str:
    return code[-5:]
