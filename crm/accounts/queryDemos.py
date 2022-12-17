from crm.accounts.models import Customer
from crm.accounts.models import Order
from crm.accounts.models import Product
# Return all customers from customer table
customers = Customer.objects.all()

# Return first customer
firstCustomer = Customer.objects.first()

# Return last customer
lastCustomer = Customer.objects.last()

# Return single customer by name
customerByName = Customer.objects.get(name='Quinn Le')

# Return single customer by id
customerByID = Customer.objects.get(id='1')

# Return all orders related to customer (firstCustomer)
firstCustomer.order.set_all()

# Return order customer name
order = Order.objects.first()
parentName = order.customer.name

# Return products from products table with value "Out Door"
products = Product.objects.filter(category='Outdoor')

# Sort objects by ID
leastToGreatest = Product.objects.all().order_by('id')
greatestToLeast = Product.objects.all().order_by('-id')