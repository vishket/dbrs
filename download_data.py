"""
A Python script to download datasets using REST API's
"""
import urllib2

# Configure download URI
url = "https://data.cityofnewyork.us/api/views"
file_name = "6b8n-sx7y"
download_url = "{}/{}/rows.csv".format(url, file_name)
save_as = "2017_sr_dataset.csv"

try:
    print "[INFO] Downloading file {}...".format(file_name)
    resp = urllib2.urlopen(download_url)
    data = resp.read()
    print "[INFO] Download complete!"


    # Write response to csv file
    print "[INFO] Saving file as {}".format(save_as)
    with open(save_as, "wb") as f:
        f.write(data)
    print "[INFO] File saved!"

except urllib2.HTTPError as e:
    print "[Error] Downloading file failed with error: {}".format(e)


