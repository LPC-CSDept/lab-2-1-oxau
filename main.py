def main():
   ##################################################
   # Comlete your code here
   ##################################################
    original_price = float(input('Original price of the item: '))
    rate = float(input('Discount rate: '))

    discount_amount = int(original_price * rate / 100)

    print ('Original Price: ' + str(original_price))
    print ('Discount_amount: ' + str(discount_amount))
    print ('the final price: ' + str(original_price - original_price * rate / 100))
    pass


if __name__ == '__main__':
    main()
