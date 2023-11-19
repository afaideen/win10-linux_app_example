import stripe

# Set your secret key
stripe.api_key = 'sk_test_51JbIe3GcwwiaDhfhhA1OxYirj1Vjos5IQAaG1D9lpv8kRcYr3Ygn5DpglO7rALkQRSq1uHZKgNE6cfIeV4no5vPE00kxB39PpJ'

# Create a new customer
new_customer = stripe.Customer.create(
    email="customer@example.com",
    name="John Doe",
    description="A new customer"
)

print(new_customer)  # Just an example to show the customer details

coupon = None
params = {
            'source': 'token_whatever',
            'email': 'afaideen@gmail.com',
            'plan': 'gold plans'
        }

if coupon:
    params['coupon'] = coupon
new_customer1 = stripe.Customer.create(**params)
print(new_customer1)  # Just an example to show the customer details
