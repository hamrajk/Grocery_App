from sql_connection import get_sql_connection #importing our sql connection function

#this is a function to query database, and capture the info we need
def get_all_products(connection):

    cursor = connection.cursor() #cursor is used to execute mysql database queries through python

    query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name FROM gs.products inner join gs.uom on products.uom_id=uom.uom_id;")

    cursor.execute(query) #executing query using the cursor class

    response = [] # we will pass in the query results into a dictionary
                
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'uom_id': uom_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name
            }
        )

    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into products "
            "(name, uom_id, price_per_unit)"
            " values (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()
    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products WHERE product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

if __name__ == '__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 10))

