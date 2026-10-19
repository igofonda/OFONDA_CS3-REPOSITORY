#Dependency
class PaymentGateway:
    def process(self, amount):
        print(f"Gateway approved charge of ${amount}.")

class ShoppingCartProcessor:
    
    def checkout(self, gateway, total):
        print("Initiating checkout...")
        gateway.process(total)


if __name__ == "__main__":
    processor = ShoppingCartProcessor()
    stripe = PaymentGateway()
    processor.checkout(stripe, 99.99)
