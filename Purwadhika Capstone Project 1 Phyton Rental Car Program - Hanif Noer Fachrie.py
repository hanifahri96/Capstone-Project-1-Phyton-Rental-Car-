#Capstone Project Modul 1 Phyton - Hanif Noer Fachrie
#Judul: Program Rental Mobil "Hanif Car Rental Services"

#List Data Kendaraan Mobil Rental


booking_list = [ 
    {
        "booking_id": 1,
        "name": "Paul",
        "rental_date": "24 Jan 2024",
        "rental_duration": 5,
        "vehicle_name":"Nissan Xtrail",
        "rental_price":750000,
        "isDone" : False   
    },
    {
        "booking_id": 2,
        "name": "Liam",
        "rental_date": "21 Jan 2024",
        "rental_duration": 4,
        "vehicle_name":"Hyundai Ionic",
        "rental_price":600000,
        "isDone" : False
    },
    {
        "booking_id": 3,
        "name": "Neil",
        "rental_date": "12 Feb 2024",
        "rental_duration": 4,
        "vehicle_name":"Toyota Rush",
        "rental_price":600000,
        "isDone" : False
    },
    {
        "booking_id": 4,
        "name": "Toni",
        "rental_date": "15 Jan 2024",
        "rental_duration": 3,
        "vehicle_name":"Nissan Juke",
        "rental_price":450000,
        "isDone" : False
    },
    {
        "booking_id": 5,
        "name": "Ivy",
        "rental_date": "11 Feb 2024",
        "rental_duration": 2,
        "vehicle_name":"Toyota Agya",
        "rental_price":300000,
        "isDone" : False
    }
]
#Fitur Fungsi yang terdapat pada Program Rental Mobil "Hanif Car Rental Services"
# 1. Melihat list booking data existing rental mobil (Fitur Read)
# 2. Menambah data list booking pada rental mobil (Fitur Add)
# 3. Mengedit atau megupdate data list booking existing pada rental mobil based on ID booking existing (Fitur Update)
# 4. Menghapus data list booking pada rental mobil (Fitur Delete)
# 5. Keluar dari Main Menu Program Rental Mobil (Exit)


def menu():
    isActive = True

    while isActive:
        print("""
-----------------------------------------------
        WELCOME TO HANIF CAR RENTAL SERVICES  
-----------------------------------------------
1. Melihat list booking data existing rental mobil
2. Menambah data list booking pada rental mobil
3. Mengedit atau megupdate data list booking existing pada rental mobil based on ID booking existing
4. Menghapus data list booking pada rental mobil 
5. Keluar dari Main Menu Program Rental Mobil (Exit)
""")
        input_menu = input("select your desire menu: ")
        if input_menu == "1": 
            read()
        elif input_menu == "2":
            add()
        elif input_menu == "3":
            update()
        elif input_menu == "4":
            delete()
        elif input_menu == "5":
            isActive = False
            print("sampai jumpa kembali")
            
            exit()
        else:
            print("input invalid")


def read ():
    while True: 
        print('''
----------------------------------------
        HANIF CAR RENTAL SERVICES  
----------------------------------------
        1. View Data Booking Exiting Rental Mobil
        2. Kembali ke Main Menu
              ''')
        input_read = int(input("Masukkan  Pilihan 1-2:"))

        if input_read == 1 :
            print('Data Rental Mobil\n')
            print('booking_id\t| name \t| rental_date\t| rental_duration\t| vehicle_name \t\t| rental_price')
            for i in range (len(booking_list)):
                print('{} \t\t{} \t {} \t {} \t\t\t {} \t\t {} '.format (booking_list[i]["booking_id"], booking_list[i]["name"],  booking_list[i]["rental_date"],  booking_list[i]['rental_duration'],  booking_list[i]['vehicle_name'],  booking_list[i]['rental_price']))
        elif input_read == 2 :
            break
        else:
            print ('------- Pilihan tidak ditemukan---------')

def add():
    while True: 
        print('''
----------------------------------------
         HANIF CAR RENTAL SERVICES
----------------------------------------
        1. Menambahkan Data Booking Rental Mobil
        2. Kembali ke Main Menu
              ''')
        input_add = int(input("Masukkan  Pilihan 1-2:"))

        if input_add == 1 :

            input_name = input("your name: ")
            input_rental_date = input("rental date: ")
            input_rental_duration = input("rental duration: ")
            input_vehicle_name = input("vehicle name: ")
            price = int(input_rental_duration) * 150000

            new_customer = {
                "booking_id": booking_list[-1]["booking_id"]+1,
                "name": input_name,
                "rental_date": input_rental_date,
                "rental_duration": int(input_rental_duration),
                "vehicle_name": input_vehicle_name,
                "rental_price" : price,
                "status" : False
            }
            booking_list.append(new_customer)

        elif input_add == 2 :
            break
        else:
            print ('------- Pilihan tidak ditemukan---------')


def update():
     while True: 
        print('''
----------------------------------------
         HANIF CAR RENTAL SERVICES
----------------------------------------
        1. Mengupdate Data Booking Existing Rental Mobil
        2. Kembali ke Main Menu
              ''')   
        input_update = int(input("Masukkan  Pilihan 1-2:"))
        if input_update == 1 :

            input_booking_id = input("booking_id: ")
        
            booking_idx = None
            for i in range(len(booking_list)):
                if booking_list[i]["booking_id"] == int(input_booking_id):
                    booking_idx = i

                    input_name = input("your name: ")
                    input_rental_date = input("rental date: ")
                    input_rental_duration = input("rental duration: ")
                    input_vehicle_name = input("vehicle name: ")
                    price = int(input_rental_duration) * 150000

                    booking_list[booking_idx]["name"] = input_name
                    booking_list[booking_idx]["rental_date"] = input_rental_date
                    booking_list[booking_idx]["rental_duration"] = int(input_rental_duration)
                    booking_list[booking_idx]["vehicle_name"] = input_vehicle_name
                    booking_list[booking_idx]["rental_price"] = price

            if booking_idx == None:
                print("car rental booking not found")
                
        elif input_update == 2:
                break
        else:
                print ('------- Pilihan tidak ditemukan---------')
                    
def delete ():
        while True: 
            print('''
 ----------------------------------------
         HANIF CAR RENTAL SERVICES
 ----------------------------------------
         1. Menghapuskan Data Booking Existing Rental Mobil
         2. Kembali ke Main Menu
                ''')   
            
            input_delete = int(input("Masukkan  Pilihan 1-2:"))
            
            if input_delete == 1 :
                input_booking_id = input("booking_id: ")

                delete_index = None

                for i in range(len(booking_list)):
                    if booking_list[i]["booking_id"] == int(input_booking_id):
                        delete_index = i

                if delete_index == None:
                    print("car rental booking not found")
                else:
                     del booking_list[delete_index]
                     
            elif input_delete == 2:
                    break
            else:
                    print ('------- Pilihan tidak ditemukan---------')

menu()   