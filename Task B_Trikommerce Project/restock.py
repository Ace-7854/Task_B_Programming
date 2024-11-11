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

    if (current_day%7==0 and current_day != 0): # if day is the seventh day and not 0
        restocked_items = 2000 # restocked items is equal to 2000
        restocked_items -= available_items # restocked items is the equivilent to 2000 - available items which gives us the items required for restock
        sales = 0 # no sales are done on seventh day
        available_items = 2000 # as of restock, availble units become 2000 
        #day,sales,restocked_items,available_items
        inventory_records.append([current_day, sales, restocked_items,available_items])# a record of inventory for x day
    elif(current_day == 0): # if the current day is 0, we fully restock
        restocked_items = 2000 # we fully stocked
        available_items = 2000 # available items is the maximum stock
        sales = 0 # no sales committed
        #day,sales,restocked_items,available_items
        inventory_records.append([current_day,sales,restocked_items,available_items]) # a record of inventory for x day
        
    return available_items
