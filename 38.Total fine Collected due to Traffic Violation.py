'''If the Date is EVEN then the vehicles with EVEN registration number
is allowed to travel ,and Fine amount is collected from each
ODD registration numbered Vehicles and VICE VERSA'''


def total_fine_collected(vehicle_reg_nos,date,fine_amount):
    odd_count=even_count=0
    for i in vehicle_reg_nos:
            if i%2!=0:
                odd_count+=1
            else:
                even_count+=1
    return odd_count*fine_amount if date%2==0 else even_count*fine_amount

vehicle_reg_nos=list(map(int,input('Enter the vehicles registration number:').split()))

date=int(input('Enter the date:'))

fine_amount=int(input('Enter the fine amount:'))

print(f'The total fine amount collected is '
      f'RS.{total_fine_collected(vehicle_reg_nos, date, fine_amount)}')

