# List of ec2_instnaces
List ec2 instances running in your account.

# Usage
```
$ python3 list_ec2_instances.py --help
usage: list_ec2_instances.py [-h] [-price]

List EC2 instances

optional arguments:
  -h, --help  show this help message and exit
  -price, -p  Pass this if you want the prices to be included
```

# Examples
```
$ python3 list_ec2_instances.py

| Type       | Launch Time   | Private IP Address   | Key Name   | Tag                | State   |
|------------+---------------+----------------------+------------+--------------------+---------|
| m1.small   | 2014-01-02    | xx.xxx.x.xxx         | key1       | webserver1         | running |
| m1.small   | 2014-01-02    | xx.xxx.x.xxx         | key1       | webserver2         | running |
| m1.large   | 2014-10-14    | xx.xxx.x.xxx         | key1       | webserver3         | running |
| m3.large   | 2015-06-11    | xx.xxx.x.xxx         | key3       | database1          | running |
| c3.2xlarge | 2016-02-09    | xx.xxx.x.xxx         | key2       | database2          | running |
| c3.2xlarge | 2016-02-11    | xx.xxx.x.xx          | key2       | database3          | running |
| c3.2xlarge | 2016-02-11    | xx.xxx.x.xx          | key3       | loadbalancer1      | running |
| m3.medium  | 2016-06-08    | xx.xxx.x.xx          | key3       | loadbalancer2      | running |
| m2.4xlarge | 2016-07-18    | xx.xxx.x.xxx         | key4       | backup-database    | running |
| m3.xlarge  | 2016-08-09    | xx.xxx.x.xxx         | key3       | backup-webserver   | running |
Time taken:  0:00:00.745601

```

```
$ python3 list_ec2_instances.py -p
----------------------------------------
Please wait, getting ec2-instances
----------------------------------------
| Type       | Launch Time   | Private IP Address   | Key Name   | Tag                | State   |   Price per hour |   Price per month |
|------------+---------------+----------------------+------------+--------------------+---------+------------------+-------------------|
| m1.small   | 2014-01-02    | xx.xxx.x.xxx         | key1       | webserver1         | running |            0.044 |             32.12 |
| m1.small   | 2014-01-02    | xx.xxx.x.xxx         | key1       | webserver2         | running |            0.044 |             32.12 |
| m1.large   | 2014-10-14    | xx.xxx.x.xxx         | key1       | webserver3         | running |            0.175 |            127.75 |
| m3.large   | 2015-06-11    | xx.xxx.x.xxx         | key3       | database1          | running |            0.133 |             97.09 |
| c3.2xlarge | 2016-02-09    | xx.xxx.x.xxx         | key2       | database2          | running |            0.42  |            306.6  |
| c3.2xlarge | 2016-02-11    | xx.xxx.x.xx          | key2       | database3          | running |            0.42  |            306.6  |
| c3.2xlarge | 2016-02-11    | xx.xxx.x.xx          | key3       | loadbalancer1      | running |            0.42  |            306.6  |
| m3.medium  | 2016-06-08    | xx.xxx.x.xx          | key3       | loadbalancer2      | running |            0.067 |             48.91 |
| m2.4xlarge | 2016-07-18    | xx.xxx.x.xxx         | key4       | backup-database    | running |            0.98  |            715.4  |
| m3.xlarge  | 2016-08-09    | xx.xxx.x.xxx         | key3       | backup-webserver   | running |            0.266 |            194.18 |

Total amount per month: $2,167.37
Time taken:  0:00:09.387928
```


# Dependencies

- python3
- boto3 (pip install boto3)
- tabulate (pip install tabulate)

# Configuraiton

Before you can begin using Boto 3, you should set up authentication credentials. Credentials for your AWS account can be found in the [IAM Console](https://console.aws.amazon.com/iam/home). You can create or use an existing user. Go to manage access keys and generate a new set of keys.

If you have the [AWS CLI](http://aws.amazon.com/cli/) installed, then you can use it to configure your credentials file:
`aws configure`

Alternatively, you can create the credential file yourself. By default, its location is at ~/.aws/credentials:

```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

You may also want to set a default region. This can be done in the configuration file. By default, its location is at ~/.aws/config:

```
[default]
region=us-east-1
```
