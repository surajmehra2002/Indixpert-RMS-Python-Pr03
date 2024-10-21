# import json
# from datetime import datetime

# class Invoice:
#     GST_RATE = 0.18  # Example GST rate of 18%

#     def __init__(self, order, customer_name):
#         self.order = order
#         self.customer_name = customer_name
#         self.date = datetime.now()
#         self.subtotal = self.calculate_subtotal()
#         self.gst = self.calculate_gst()
#         self.total_amount = self.subtotal + self.gst

#     def calculate_subtotal(self):
#         subtotal = sum(item['price'] * item['quantity'] for item in self.order['items'])
#         return subtotal

#     def calculate_gst(self):
#         return self.subtotal * self.GST_RATE

#     def generate_invoice(self):
#         invoice_data = {
#             'customer_name': self.customer_name,
#             'date': self.date.strftime("%Y-%m-%d %H:%M:%S"),
#             'items': self.order['items'],
#             'subtotal': self.subtotal,
#             'gst': self.gst,
#             'total_amount': self.total_amount
#         }

#         invoice_file = f"invoice_{self.order['order_id']}.json"
#         with open(f"data/invoices/{invoice_file}", 'w') as f:
#             json.dump(invoice_data, f, indent=4)

#         print(f"Invoice generated and saved as {invoice_file}")
#         return invoice_data
