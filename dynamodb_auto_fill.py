"""
Dillon Ramsey
AWS DynamoDB Auto Fill application
This app lets a user add a specified number of items to an existing DynamoDB table
as well as the attributes the items have.
"""
import boto3

def indexer(index_num):
    counter = 0
    indexes = {}
    while counter < index_num:
        new_key = input("Enter index name: ")
        indexes[new_key] = ""
        counter += 1
    return indexes

def add_items(numItems, table, indexes):
    counter = 0
    while counter < numItems:
        for i in indexes:
            indexes[i] = input(f"Enter {i}: ")
        table.put_item(Item=indexes)
        print(indexes)
        counter += 1

def main():
    user_table = input("Enter the table you want to add to: ")
    table = boto3.resource('dynamodb').Table(user_table)
    index_num = int(input("How many indexs will these items have?: "))
    indexes = indexer(index_num)
    items = int(input("How many items do you want to add: "))
    add_items(items, table, indexes)

if __name__=="__main__":
    main()
