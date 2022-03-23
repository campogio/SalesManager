import datetime
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar
import datetime as dt
import dateutil.parser
import json

currentresults = []

store_names = ['Steam', 'Skinport', 'Dmarket', 'BUFF163', 'Skinbaron', 'Bitskins', 'Skinwallet', 'Skinbid',
               'Customer Sale']

inventory_id = 0
sale_id = 0
inventory = {}
total_sales = {}
yearly_sales = {}
monthly_sales = {}
daily_sales = {}

with open('inventory_id.json') as file:
    data = json.load(file)
    inventory_id = data

with open('sales_id.json') as file:
    data = json.load(file)
    sale_id = data

# id_file = open('inventory_id.json')

#databuff_file = open('../data.json')

#databuff = json.load(databuff_file)

#databuff_file.close()

item_names_file = open('itemNames.json')

item_names = json.load(item_names_file)

# item_names =['Test1',"Abram","Bertold","Niggur","gurna"]

item_names_file.close()


def is_this_year(date):
    if is_this_month(date):
        return True
    else:
        item_date = dateutil.parser.isoparse(date).date()
        if item_date.year == datetime.date.today().year:
            return True
        else:
            return False


def is_this_month(date):
    if is_this_day(date):
        return True
    else:
        item_date = dateutil.parser.isoparse(date).date()
        if item_date.month == datetime.date.today().month and item_date.year == datetime.date.today().year:
            return True
        else:
            return False


def is_this_day(date):
    item_date = dateutil.parser.isoparse(date).date()

    if datetime.date.today() == item_date:
        return True
    else:
        return False


def save_inventory():
    with open('inventory.json', 'w') as inv:
        json.dump(inventory, inv)

def save_total_sales():
    with open('total_sales.json', 'w') as sales:
        json.dump(total_sales, sales)


def save_inventory_id():
    with open('inventory_id.json', 'w') as fileid:
        json.dump(inventory_id, fileid)

def save_sales_id():
    with open('sales_id.json', 'w') as fileid:
        json.dump(sale_id, fileid)


def configure_sales_table(table):
    table['columns'] = (
        'id', 'name', 'paid', 'got', 'quantity', 'gainpercent', 'buydate', 'selldate', 'bought_at', 'sold_at')
    table.column("#0", width=0, stretch=NO)
    table.column("id", anchor=CENTER, width=80)
    table.column("name", anchor=CENTER, width=240)
    table.column("paid", anchor=CENTER, width=80)
    table.column("got", anchor=CENTER, width=80)
    table.column("quantity", anchor=CENTER, width=80)
    table.column("gainpercent", anchor=CENTER, width=80)
    table.column("buydate", anchor=CENTER, width=80)
    table.column("selldate", anchor=CENTER, width=80)
    table.column("bought_at", anchor=CENTER, width=80)
    table.column("sold_at", anchor=CENTER, width=80)

    table.heading("#0", text="", anchor=CENTER)
    table.heading("id", text="ID", anchor=CENTER)
    table.heading("name", text="Name", anchor=CENTER)
    table.heading("paid", text="Bought For", anchor=CENTER)
    table.heading("got", text="Sold For", anchor=CENTER)
    table.heading("quantity", text="Quantity", anchor=CENTER)
    table.heading("gainpercent", text="% Increase", anchor=CENTER)
    table.heading("buydate", text="Buy Date", anchor=CENTER)
    table.heading("selldate", text="Sell Date", anchor=CENTER)
    table.heading("bought_at", text="Purchased From", anchor=CENTER)
    table.heading("sold_at", text="Sold to", anchor=CENTER)


def load_inventory():
    global inventory

    with open('inventory.json') as inv:
        inventory = json.load(inv)

    for item in inventory:
        name = inventory[item]['name']
        paid = inventory[item]['paid']
        expected = inventory[item]['expected']
        quantity = inventory[item]['quantity']
        date = inventory[item]['date']
        tradelockdate = inventory[item]['tradelockdate']
        store = inventory[item]['store']
        notes = inventory[item]['notes']

        inventory_table.insert(parent='', index='end',
                               values=(item, name, paid, expected, quantity, date, tradelockdate, store, notes))

def load_sales():
    #TODO
    # -RUN TROUGH GLOBAL SALES
    # -CHECK FOREACH TO PUT IN DAYLY,MONTHLY,YEARLY
    global  total_sales
    global  yearly_sales
    global  monthly_sales
    global  daily_sales

    with open('total_sales.json') as sales:
        total_sales = json.load(sales)

    for item in total_sales:

        name= total_sales[item]['name']
        buyprice= total_sales[item]['buyprice']
        sellprice= total_sales[item]['sellprice']
        quantity= total_sales[item]['quantity']
        gainpercent= total_sales[item]['gainpercent']
        buydate= total_sales[item]['buydate']
        selldate= total_sales[item]['selldate']
        fromstore= total_sales[item]['fromstore']
        tostore= total_sales[item]['tostore']

        totalsales_table.insert(parent='',index=END,values=(item,name,buyprice,sellprice,quantity,gainpercent,
                                                            buydate,selldate,fromstore,tostore))

        if is_this_year(selldate):
            yearly_sales[item]= total_sales[item]
            monthly_sales[item]= total_sales[item]
            daily_sales[item]= total_sales[item]
            yearlysales_table.insert(parent='',index=END,values=(item,name,buyprice,sellprice,quantity,gainpercent,
                                                            buydate,selldate,fromstore,tostore))
            monthlysales_table.insert(parent='', index=END,values=(item, name, buyprice, sellprice, quantity, gainpercent,
                                                            buydate, selldate, fromstore, tostore))
            dailysales_table.insert(parent='', index=END,values=(item, name, buyprice, sellprice, quantity, gainpercent,
                                                            buydate, selldate, fromstore, tostore))
        elif is_this_month(selldate):
            monthly_sales[item] = total_sales[item]
            daily_sales[item] = total_sales[item]
            monthlysales_table.insert(parent='', index=END,values=(item, name, buyprice, sellprice, quantity, gainpercent,
                                                buydate, selldate, fromstore, tostore))
            dailysales_table.insert(parent='', index=END,values=(item, name, buyprice, sellprice, quantity, gainpercent,
                                                buydate, selldate, fromstore, tostore))
        elif is_this_day(selldate):
            daily_sales[item] = total_sales[item]
            dailysales_table.insert(parent='', index=END,values=(item, name, buyprice, sellprice, quantity, gainpercent,
                                                buydate, selldate, fromstore, tostore))

def purchasecurrent():
    global inventory_id
    global inventory

    name = purchase_name_entry.get()
    paid = paid_entry.get()
    expected = expected_entry.get()
    quantity = quantity_entry.get()
    tradelock = tradelock_entry.get()
    store = purchasestore_combobox.get()
    notes = notes_entry.get()
    date = calendar_date.selection_get()

    if name == '' or paid == '' or expected == '' or quantity == '' or store == '':
        print("Invalid Data")
    else:

        if tradelock == '':
            tradelock = 0
        else:
            tradelock = int(tradelock)


        tradelockdate = date

        date = tradelockdate.isoformat()

        tradelockdate = tradelockdate + datetime.timedelta(days=int(tradelock))

        tradelockdate = tradelockdate.isoformat()

        inventory[str(inventory_id)] = {'name': name, 'paid': paid, 'expected': expected, 'quantity': quantity,
                                        'date': date, 'tradelockdate': tradelockdate, 'store': store, 'notes': notes}
        inventory_table.insert(parent='', index='end', iid=inventory_id, values=(
            str(inventory_id), name, paid, expected, quantity, date, tradelockdate, store, notes))
        inventory_id += 1

        save_inventory()
        save_inventory_id()


def change_storage_inv():
    # TODO
    # -GET COMBOBOX INFO
    # -CHANGE ITEM INFO IN INVENTORY AND TABLE
    # -UPDATE INVENTORY

    pass


def sell_item():

    sale_window = Toplevel(window)

    item_values = inventory_table.item(inventory_table.focus(), 'values')

    sale_window.title("Sale Configuration")

    # sale_window.geometry("400x600")

    sale_name_label = Label(sale_window, text=item_values[1])
    sale_name_label.grid(column=0, row=0, pady=(10, 0), columnspan=2)

    sale_paid_label = Label(sale_window, text='Paid:')
    sale_paid_label.grid(column=0, row=1, pady=(10, 0))

    sale_paid_entry = Entry(sale_window, justify='center')
    sale_paid_entry.grid(column=1, row=1, pady=(10, 0))
    sale_paid_entry.delete(0, END)
    sale_paid_entry.insert(0, item_values[2])

    sale_got_label = Label(sale_window, text='Got:')
    sale_got_label.grid(column=0, row=2, pady=(10, 0))

    sale_got_entry = Entry(sale_window, justify='center')
    sale_got_entry.grid(column=1, row=2, pady=(10, 0))
    sale_got_entry.delete(0, END)
    sale_got_entry.insert(0, item_values[3])

    sale_quantity_label = Label(sale_window, text='Quantity:')
    sale_quantity_label.grid(column=0, row=3, pady=(10, 0))

    sale_quantity_entry = Entry(sale_window, justify='center')
    sale_quantity_entry.grid(column=1, row=3, pady=(10, 0))
    sale_quantity_entry.delete(0, END)
    sale_quantity_entry.insert(0, item_values[4])

    sale_soldat_label = Label(sale_window, text='Sold at:')
    sale_soldat_label.grid(column=0, row=4, pady=(10, 0))

    sale_soldat_combobox = ttk.Combobox(sale_window, values=store_names)
    sale_soldat_combobox.grid(column=1, row=4, pady=(10, 0))
    sale_soldat_combobox.delete(0, END)
    sale_soldat_combobox.insert(0, item_values[7])

    sale_calendar_label = Label(sale_window, text='Sale Date').grid(column=3, row=0, pady=(10, 0))
    sale_calendar_date = Calendar(sale_window, date_pattern='dd/mm/yy')
    sale_calendar_date.grid(column=3, row=1, pady=(10, 10), padx=(0, 10), rowspan=5)

    sale_confirm_button = Button(sale_window, text='Confirm Sale', command=lambda:
    finalize_sale(item_values[0], item_values[1], sale_paid_entry.get(), sale_got_entry.get(),
                  sale_quantity_entry.get(), item_values[5], sale_calendar_date.selection_get().isoformat(), item_values[7],
                  sale_soldat_combobox.get(),item_values[4], sale_window))
    sale_confirm_button.grid(column=0, row=5, pady=(10, 0), columnspan=2)


def finalize_sale(id, name, buyprice, sellprice, quantity, buydate, selldate, fromstore, tostore,oldquantity, salewindow):


    global total_sales
    global sale_id

    old_item_values = inventory_table.item(inventory_table.focus(), 'values')


    percentgain = ((float(sellprice) / float(buyprice)) - 1) * 100
    percentgain = round(percentgain, 2)

    total_sales[sale_id] = {'name': name, 'buyprice': buyprice,
                       'sellprice': sellprice, 'quantity': quantity, 'gainpercent': str(percentgain),
                       'buydate': buydate, 'selldate': selldate, 'fromstore': fromstore, 'tostore': tostore}

    item_values = [sale_id,name,buyprice,sellprice,quantity,str(percentgain),buydate,selldate,fromstore,tostore]


    if is_this_day(selldate):
        daily_sales[sale_id] = total_sales[sale_id]
        monthly_sales[sale_id] = total_sales[sale_id]
        yearly_sales[sale_id] = total_sales[sale_id]
        dailysales_table.insert(parent='', index=END,values=item_values)
        monthlysales_table.insert(parent='', index=END,values=item_values)
        yearlysales_table.insert(parent='', index=END,values=item_values)

    elif is_this_month(selldate):
        monthly_sales[sale_id] = total_sales[sale_id]
        yearly_sales[sale_id] = total_sales[sale_id]
        monthlysales_table.insert(parent='', index=END,values=item_values)
        yearlysales_table.insert(parent='', index=END,values=item_values)

    elif is_this_year(selldate):
        yearly_sales[sale_id] = total_sales[sale_id]
        yearlysales_table.insert(parent='', index=END,values=item_values)

    totalsales_table.insert(parent='', index=END,values=item_values)

    sale_id= sale_id+1
    save_sales_id()

    if int(quantity) == int(oldquantity):
        remove_from_inv()
    else:
        inventory_selected = inventory_table.focus()
        newquantity = int(oldquantity)-int(quantity)
        inventory[str(id)] = {'name': name, 'paid': buyprice, 'expected': old_item_values[3], 'quantity': str(newquantity),
                              'date': old_item_values[5], 'tradelockdate': old_item_values[6], 'store': old_item_values[7], 'notes': old_item_values[8]}
        inventory_table.item(inventory_selected,
                             values= (str(id),name,buyprice,old_item_values[3],str(newquantity),old_item_values[5],
                                      old_item_values[6],old_item_values[7],old_item_values[8]))
        save_inventory()

    save_total_sales()

    salewindow.destroy()


def remove_from_inv():
    global inventory

    item_id = inventory_table.item(inventory_table.focus(), 'values')[0]

    del inventory[item_id]

    inventory_table.focus_set()

    inventory_table.delete(inventory_table.focus())

    save_inventory()


def filter_entries(event):
    results = []
    global currentresults

    item_listbox.delete(0, END)

    try:
        to_filter = purchase_var.get().lower()

        filters = str(to_filter).split()
        for name in item_names:
            name_caseIns = name.lower()
            if all(filt in name_caseIns for filt in filters):
                results.append(name)

        currentresults = results.copy()
        item_listbox.insert(0, *currentresults)
        results.clear()
    except Exception as e:
        print(e)


def select_filter(event):
    purchase_name_entry.delete(0, END)
    purchase_name_entry.insert(0, item_listbox.selection_get())


# declare the window
window = Tk()
# set window title
window.title("SalesManager")
# set window width and height
window.configure(width=800, height=600)
# set window background color
window.configure(bg='lightgray')

ext_control = ttk.Notebook(window)

######### MAIN TAB CONTROL #############

inv_tab = ttk.Frame(ext_control)
ext_control.add(inv_tab, text='Inventory')

sales_tab = ttk.Frame(ext_control)
ext_control.add(sales_tab, text='Sales')

ext_control.pack(expand=1, fill="both")

inv_tabs = ttk.Notebook(inv_tab)
addpurchase_tab = ttk.Frame(inv_tabs)
currentinv_tab = ttk.Frame(inv_tabs)

inv_tabs.add(addpurchase_tab, text='Add Purchase')
inv_tabs.add(currentinv_tab, text='Current Inventory')

inv_tabs.pack(expand=1, fill="both")

sale_tabs = ttk.Notebook(sales_tab)
dailysales_tab = ttk.Frame(sale_tabs)
monthlysales_tab = ttk.Frame(sale_tabs)
yearlysales_tab = ttk.Frame(sale_tabs)
totalsales_tab = ttk.Frame(sale_tabs)

sale_tabs.add(dailysales_tab, text='Daily')
sale_tabs.add(monthlysales_tab, text='Monthly')
sale_tabs.add(yearlysales_tab, text='Yearly')
sale_tabs.add(totalsales_tab, text='Total')

sale_tabs.pack(expand=1, fill='both')

########## ADD PURCHASE TAB ###########

purchase_var = StringVar(window)
purchase_name_label = Label(addpurchase_tab, text='Item Name').grid(column=0, row=0)
purchase_name_entry = Entry(addpurchase_tab, textvariable=purchase_var, width=60)
purchase_name_entry.grid(column=1, row=0, columnspan=2)
purchase_name_entry.bind('<KeyRelease>', filter_entries)

item_listbox = Listbox(addpurchase_tab, width=80)
item_listbox.grid(column=0, row=1, columnspan=3)
item_listbox.bind('<Double-1>', select_filter)

paid_label = Label(addpurchase_tab, text='Paid(Euro)', width=10).grid(column=0, row=2)
paid_entry = Entry(addpurchase_tab, width=20, justify='center')
paid_entry.grid(column=1, row=2)

expected_label = Label(addpurchase_tab, text='Expected(Euro)').grid(column=0, row=3)
expected_entry = Entry(addpurchase_tab, justify='center')
expected_entry.grid(column=1, row=3)

quantity_label = Label(addpurchase_tab, text='Quantity').grid(column=0, row=4)
quantity_entry = Entry(addpurchase_tab, justify='center')
quantity_entry.insert(0, '1')
quantity_entry.grid(column=1, row=4)

tradelock_label = Label(addpurchase_tab, text='Tradelock(in days)').grid(column=0, row=5)
tradelock_entry = Entry(addpurchase_tab, width=20, justify='center')
tradelock_entry.grid(column=1, row=5)

purchasestore_label = Label(addpurchase_tab, text='Purchase Store').grid(column=0, row=6)
purchasestore_combobox = ttk.Combobox(addpurchase_tab, width=17, values=store_names)
purchasestore_combobox.grid(column=1, row=6)

notes_label = Label(addpurchase_tab, text='Notes(Float etc.)').grid(column=0, row=7)
notes_entry = Entry(addpurchase_tab, width=49)
notes_entry.grid(column=1, row=7, columnspan=2)

purchase_confirm = Button(addpurchase_tab, text='Confirm Purchase', command=purchasecurrent)
purchase_confirm.grid(column=2, row=3)

calendar_label = Label(addpurchase_tab, text='Purchase Date').grid(column=3, row=0)
calendar_date = Calendar(addpurchase_tab, date_pattern='dd/mm/yy')
calendar_date.grid(column=3, row=1)

############# END ADD PURCHASE TAB ################


############ START INVENTORY TAB ##################
inventory_table = ttk.Treeview(currentinv_tab)
inventory_table['columns'] = ('id', 'name', 'paid', 'expected', 'quantity', 'buydate', 'tradelock', 'storage', 'notes')
inventory_table.column("#0", width=0, stretch=NO)
inventory_table.column("id", anchor=CENTER, width=80)
inventory_table.column("name", anchor=CENTER, width=240)
inventory_table.column("paid", anchor=CENTER, width=80)
inventory_table.column("expected", anchor=CENTER, width=80)
inventory_table.column("quantity", anchor=CENTER, width=80)
inventory_table.column("buydate", anchor=CENTER, width=80)
inventory_table.column("tradelock", anchor=CENTER, width=80)
inventory_table.column("storage", anchor=CENTER, width=80)
inventory_table.column("notes", anchor=CENTER, width=80)

inventory_table.heading("#0", text="", anchor=CENTER)
inventory_table.heading("id", text="ID", anchor=CENTER)
inventory_table.heading("name", text="Name", anchor=CENTER)
inventory_table.heading("paid", text="Paid", anchor=CENTER)
inventory_table.heading("expected", text="Expected", anchor=CENTER)
inventory_table.heading("quantity", text="Quantity", anchor=CENTER)
inventory_table.heading("buydate", text="Purchase Date", anchor=CENTER)
inventory_table.heading("tradelock", text="Tradelock", anchor=CENTER)
inventory_table.heading("storage", text="Stored at", anchor=CENTER)
inventory_table.heading("notes", text="Notes", anchor=CENTER)

inventory_table.grid(column=0, row=0, columnspan=6)

change_tradelock_entry = Entry(currentinv_tab, width=50, justify='center')
change_tradelock_entry.grid(column=0, row=1)

change_tradelock_button = Button(currentinv_tab, text='Add tradelock(days)')
change_tradelock_button.grid(column=1, row=1)

changestorage_combobox = ttk.Combobox(currentinv_tab, width=47, values=store_names)
changestorage_combobox.grid(column=0, row=2, pady=(20, 0))

changestorage_button = Button(currentinv_tab, text='Change Storage', command=change_storage_inv)
changestorage_button.grid(column=1, row=2, pady=(20, 0))

sale_button = Button(currentinv_tab, text='Sell Item', command=sell_item)
sale_button.grid(column=4, row=3, pady=(20, 0))

removefrominv_button = Button(currentinv_tab, text='Remove Item(Unregister)', command=remove_from_inv)
removefrominv_button.grid(column=0, row=3, pady=(20, 0))

load_inventory()

################ END INVENTORY TAB ##################

################ TOTAL SALES TAB ####################

totalsales_table = ttk.Treeview(totalsales_tab)
configure_sales_table(totalsales_table)

totalsales_table.pack()

################ YEARLY SALES TAB ####################

yearlysales_table = ttk.Treeview(yearlysales_tab)
configure_sales_table(yearlysales_table)

yearlysales_table.pack()

################ MONTHLY SALES TAB ####################

monthlysales_table = ttk.Treeview(monthlysales_tab)
configure_sales_table(monthlysales_table)

monthlysales_table.pack()

################# DAILY SALES TAB ######################

dailysales_table = ttk.Treeview(dailysales_tab)
configure_sales_table(dailysales_table)

dailysales_table.pack()

load_sales()

mainloop()

# TODO
#   -SAVE INVENTORY BACK TO FILE
#   -SAVE INVENTORY ID BACK TO FILE
#   -SAVE SALES BACK TO FILE


save_inventory()
save_inventory_id()
save_total_sales()
