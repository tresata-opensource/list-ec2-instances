#!/usr/bin/env python

import argparse
import boto3
from tabulate import tabulate
import ec2_pricing
import datetime
import operator


def list_instances(price):
    ec2 = boto3.resource('ec2')

    instances = [i for i in ec2.instances.all()]
    temp_list = []
    list_of_instances = []
    unique_instance_types = [i.instance_type for i in instances]
    list_of_instances1 = (list(set(unique_instance_types)))
    if price:
        print ("-" * 40)
        print ("Please wait, getting ec2-instances")
        print ("-" * 40)
        price_per_instance = ec2_pricing.pricing(list_of_instances1)
    total = 0.0

    for instance in instances:
        if price:
            pricing = price_per_instance[instance.instance_type]
            pricing_per_month = float(pricing) * 730
            total = total + float(pricing_per_month)
            temp_list.extend([instance.instance_type,
                             instance.launch_time.strftime('%-Y-%m-%d'),
                             instance.private_ip_address,
                             instance.key_name, instance.tags[0]['Value'],
                             instance.state['Name'],
                             pricing, pricing_per_month])
        else:
            temp_list.extend([instance.instance_type,
                             instance.launch_time.strftime('%-Y-%m-%d'),
                             instance.private_ip_address,
                             instance.key_name, instance.tags[0]['Value'],
                             instance.state['Name']])
        list_of_instances.append(temp_list)
        temp_list = []

    list_of_instances = sorted(list_of_instances, key=operator.itemgetter(1))
    print (tabulate(list_of_instances,
           headers=["Type", "Launch Time",
                    "Private IP Address", "Key Name",
                    "Tag", "State", "Price per hour",
                    "Price per month"], tablefmt="orgtbl"))
    if price:
        print ("\nTotal amount per month:", ('${:,.2f}'.format(total)))


def main():
    parser = argparse.ArgumentParser(description="List EC2 instances")
    parser.add_argument("-price", "-p", action="store_true",
                        default=False,
                        help="Pass this if you want the prices to be included")
    args = parser.parse_args()
    # Start time for listing of instances
    start_time = datetime.datetime.now()
    list_instances(args.price)
    end_time = datetime.datetime.now()
    print ("Time taken: ", end_time-start_time)

if __name__ == "__main__":
    main()
