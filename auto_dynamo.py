import boto3
import sys

class user_table():
    def __init__(self, table):
        self.table = boto3.resource('dynamodb').Table(table)
        client = boto3.client('dynamodb')
        existing_tables = client.list_tables()['TableNames']

    def indexer(self, index_num):
        counter = 0
        indexes = {}
        while counter < index_num:
            new_key = input("Enter index name: ")
            indexes[new_key] = ""
            counter += 1
        return indexes

    def add_items(self, indexes, numItems):
        counter = 0
        while counter < numItems:
            for i in indexes:
                indexes[i] = input(f"Enter {i}: ")
            self.table.put_item(Item=indexes)
            print(indexes)
            counter += 1

def main_menu():
    main_table=input("What table do you want to use: ")
    table=user_table(main_table)
    indexes = int(input("How many indexes do the table have: "))
    indexed = table.indexer(indexes)
    print(type(indexed))
    items = int(input("How many items do you want to add: "))
    table.add_items(indexed, items)

if __name__ == "__main__":
    main_menu()
