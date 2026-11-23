# ================================
# GROCERY BILLING QUEUE
# ================================

print("=== Grocery Billing Queue ===\n")

# ---------- PART 1: the five counters ----------
# YOUR CODE HERE
# Three counters for the price bands: low_price_items, medium_price_items,
# high_price_items — all start at 0.
# Two more for the day: customers_served and total_sales — both start at 0.
# Also make a variable  billing = True  to control the outer loop.
lowpriceitems = 0
medpriceitems = 0
highpriceitems = 0
customersserved = 0
totalsale = 0
billing = True

# ---------- PART 2: the OUTER while loop — one customer per repeat ----------
# YOUR CODE HERE
# while billing:
#     ask for the customer's name
#     ask how many items they are buying, wrapped in int()
while billing:
    input ('enter your name: ')
    icount = int(input('How many items are you getting?: '))
# ---------- PART 3: continue on a bad item count ----------
# YOUR CODE HERE
# Still inside the outer loop, before anything else happens:
# if the item count is 0 or less, print a message and use continue
    if icount <= 0:
        print ('Buy something next time will ya?')
        continue
# ---------- PART 4: the INNER while loop — one item per repeat ----------
# YOUR CODE HERE
# Set customer_total = 0 and item_number = 1 first.
# Then:  while item_number <= item_count:
#            ask for item name, price, quantity
#            (price and quantity wrapped in int())
    customertot = 0
    itemnum = 1    
    while itemnum <= icount:
        iname = input('enter item name: ')
        iprice = int(input('enter item price: '))
        iquant = int(input('enter item quantity: '))


# ---------- PART 5: item total and price band ----------
# YOUR CODE HERE
# Inside the inner loop:
#   if price or quantity is 0 or less -> print a message and continue
#   item_total = price * quantity
#   print the line:    item_name: quantity x price = item_total
#   add item_total to customer_total
#   add quantity to the right band:  under 50 = low, 50 to 100 = medium, over 100 = high
#   add 1 to item_number      <- forget this and the loop never ends
        if iprice + iquant <= 0:
            print ('we sell no items like that')
            continue
        itemtot = iprice * iquant
        print (iname,':',iquant,'* $',iprice,'=',itemtot)
        customertot += itemtot
        if itemtot < 5:
            lowpriceitems += 1
        elif itemtot <= 15:
             medpriceitems +=1
        else:
            highpriceitems += 1
        itemnum += 1
        
# ---------- PART 6: finish the customer, ask about the next ----------
# YOUR CODE HERE
# Back out in the outer loop, after the inner loop has finished:
#   add 1 to customers_served, add customer_total to total_sales
#   print the customer's total
#   ask "Next customer? (yes/no): "
    customersserved += 1
    totalsale += customertot 
    next = input('next customer (yes/no) ').lower()
    if next == 'no':
        billing = False
# ---------- PART 7: the NESTED for report ----------
# YOUR CODE HERE
# After the outer loop has ended:
#   an outer for loop over the three bands
#   an inner for loop printing one * per item in that band, using end=""
# Then print customers_served and total_sales
print ('high price items:')
for i in range(highpriceitems):
        highpriceitems -= 1
        if highpriceitems == 1:
             print ('* ',end='')
        else:
             print ('* ')
print ('medium price items:')
for i in range(medpriceitems):
        medpriceitems -= 1
        if medpriceitems == 1:
             print ('* ',end='')
        else:
             print ('* ')

print ('low price items:')
for i in range(lowpriceitems):
        lowpriceitems -= 1
        if lowpriceitems == 1:
             print ('* ',end='')
        else:
             print ('* ')

print ('customers served:',customersserved)
print ('total sales: $',totalsale)