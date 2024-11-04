def restock_inventory(available_items, inventory_records, current_day):
    '''
***********COMPLETE THIS FUNCTION***********
This function is responsible for updating the stock/restock for a given day.
---------------
Function Input:
---------------
available_items: (integer) Available Tshirts from the previous day.
inventory_records: (List) A list of inventory records until the previous day. Each row contains (day, sales, restocked items, available items)
current_day: (integer) Day number which you want to add as the current day. 

----------------
Function Output:
----------------
available_items:(integer) This function returns this integer which updates the available items at the current day.


The function will also update the inventory_records (For restocking) for a given current day. It will also return "available_items".
    '''
    restocked_items = 0
    sales = 0
    if (available_items < 2000 and current_day%7==0):
        restocked_items = 2000 - available_items
        #day,sales,restocked_items,available_items
        inventory_records.append(current_day)
        inventory_records.append(sales)
        inventory_records.append(restocked_items)
        if available_items + restocked_items == 2000:
            available_items = 2000
            inventory_records.append(available_items)
        else:
            raise ValueError("Available items + restocked items is not equal to 2000")
        
    return available_items
