asset=int(input('Enter the total amount of your shopping :- '))
black_fri=(asset*8)/100
prime = input('Are you a prime member ? :-')
if prime.lower()=='yes':
    prime_id=int(input('Enter your prime_id :- '))
    if (3456000<=prime_id<=3460000):
        discount_p=(asset*15)/100
        print('Order cost after 15% discount for prime memeber is',asset-discount_p)
        print('Order cost after 8% discount of black friday is',asset-black_fri)
        print('total payable amount after all discount is',asset-discount_p-black_fri)
    else:
        raise TypeError('Enter a valid prime member id')
elif prime.lower()=='no':
    print('Order cost after 8% discount of black friday is',asset-black_fri)