def emp(id,name,company,*address):
    print("Id : {}".format(id))
    print("Name : {}".format(name))
    print("Company : {}".format(company))
    # print("Address : {}".format(address))
    for i,addr in enumerate(address):
        print("Address {} : {}".format(i+1,addr))

emp(101,'Ram','TCS','Delhi','Pune','Mumbai')
emp(102,'Shyam','TCS','Pune','Mumbai')
emp(103,'Ram','IBM','Delhi','Pune','Mumbai','Noida')