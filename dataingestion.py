
# coding: utf-8

# In[1]:

import pandas as pd
import json
import datetime, time
import boto
import boto.s3
import sys
from boto.s3.key import Key
import glob
import boto3
import botocore


# In[20]:

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%d%m%y%M%S')
st1 = datetime.datetime.fromtimestamp(ts).strftime('%d%m%y')


# In[13]:

# Create logfile.
logfile = open(st+".txt", "a")
def log_entry(s):
    #print('Date now: %s' % datetime.datetime.now())

    timestamp = '[%s] : ' % datetime.datetime.now()
    log_line = timestamp + s + '\n'
    logfile.write(log_line)
    logfile.flush()
  


# In[14]:

with open('config.json') as data_file:    
    configdata = json.load(data_file)
log_entry("Link from config file: "+configdata["link"])
print(configdata["link"])


# In[15]:

datadf=pd.read_csv(configdata["link"], sep=',', error_bad_lines=False, index_col=False, dtype='unicode')


# In[16]:

filename=configdata["state"]+"_"+st1+"_"+"12832"
datadf.to_csv(filename+".csv")
log_entry(filename+".csv has been created.")


# In[19]:

AWS_ACCESS_KEY_ID = configdata["AWSAccess"]
print(AWS_ACCESS_KEY_ID)
AWS_SECRET_ACCESS_KEY = configdata["AWSSecret"]
print(AWS_SECRET_ACCESS_KEY)
TeamNumber=configdata["team"]

bucket_name = str(TeamNumber) + configdata["state"].lower() + 'assignment1'
log_entry("S3 bucket has been successfully created.")
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.create_bucket(bucket_name, location=boto.s3.connection.Location.DEFAULT)

s3 = boto3.resource('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
file = filename+".csv"
exists = False

try:
    s3.Object(bucket_name, file).load()
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        exists = False
    else:
        raise
else:
    exists = True

if exists==False:
    print ('Uploading %s to Amazon S3 bucket %s' % (file, bucket_name))
    def percent_cb(complete, total):
        sys.stdout.write('.')
        sys.stdout.flush()
    k = Key(bucket)
    k.key = file
    k.set_contents_from_filename(file, cb=percent_cb, num_cb=10)
    log_entry(file+" has been uploaded to "+bucket_name)
    print("File uploaded.")
    
elif exists==True:
    print("File already exists.")
    log_entry("File already exists.")


# In[ ]:




# In[18]:

datadf[:5]


# In[ ]:



