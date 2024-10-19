from billing_system.invoice import Invoice

class Billing:
    def __init__(self, order, customer_name):
        self.order = order
        self.customer_name = customer_name

    def complete_order(self):
        # Generate the invoice when the order is finalized
        invoice = Invoice(self.order, self.customer_name)
        invoice_data = invoice.generate_invoice()

        # Print summary
        print(f"Order completed. Total: {invoice_data['total_amount']}, including GST: {invoice_data['gst']}")
