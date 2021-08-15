from os.path import getsize
from urllib.request import urlretrieve

# you will need to create the "large" folder if it does not exist
# you can also change this to change where you want the data to be downloaded
output_dir = "../Project 1/data"

# template for the type of taxi / year you wish to download
fname_template = "yellow_tripdata_2020"

# change range(x, y) to be the months you want
for m in range(1, 13):
    month = str(m).zfill(2)
    out = f'{fname_template}-{month}.csv'
    url = f"https://s3.amazonaws.com/nyc-tlc/trip+data/{out}"
    urlretrieve(url, f"{output_dir}/{out}")

    print(f"Done downloading {out} to {output_dir} with size {getsize(f'{output_dir}/{out}') / 1073741824:.2f}GB")
