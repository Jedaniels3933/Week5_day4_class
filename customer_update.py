from db_connection import connect_db, Error

def update_customer_phone():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            customer_id = input("Enter the customer ID: ")
            phone = input("Enter the new phone number: ")

            phone_update  = ( phone , customer_id)

            query = "UPDATE customer SET phone = %s WHERE id = %s"

            cursor.execute(query, phone_update) 
            conn.commit()
            print("Phone number updated successfully")
        except Error as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
if __name__ == '__main__':
    update_customer_phone() 


            

