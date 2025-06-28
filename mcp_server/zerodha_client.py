from kiteconnect import KiteConnect

class ZerodhaClient:
    _instance = None

    def __new__(cls, api_key, api_secret):
        if cls._instance is None:
            cls._instance = super(ZerodhaClient, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, api_key, api_secret):
        if self._initialized:
            return  # already initialized

        self.api_key = api_key
        self.api_secret = api_secret
        self.kite = KiteConnect(api_key=self.api_key)
        self.access_token = self.load_access_token()

        if self.access_token:
            self.kite.set_access_token(self.access_token)
        else:
            print("⚠️ No access token found.")

        self._initialized = True

    def load_access_token(self):
        try:
            request_token = "tXuaz6uT5L6LfHtsrIl16N1ApVGD5Swj" # manually update everyday
            data = self.kite.generate_session(request_token, api_secret=self.api_secret)
            print(self.api_secret)
            print(request_token)
            return data["access_token"]
        except Exception as e:
            print(f"⚠️ Access token load failed with the following error - {e}")
            return None

    def place_order(self, transaction_type, tradingsymbol, quantity, price=None):
        try:
            print(f"Trying to {transaction_type} {quantity} x {tradingsymbol}")
            order_id = self.kite.place_order(
                variety=self.kite.VARIETY_REGULAR,
                exchange=self.kite.EXCHANGE_NSE,
                tradingsymbol=tradingsymbol,
                transaction_type=transaction_type,
                quantity=quantity,
                product=self.kite.PRODUCT_MIS,
                order_type=self.kite.ORDER_TYPE_MARKET if price is None else self.kite.ORDER_TYPE_LIMIT,
                price=price,
                validity=self.kite.VALIDITY_DAY,
            )
            print(f"✅ Order placed successfully. Order ID: {order_id}")
            return order_id
        except Exception as e:
            print("❌ Error placing order:", str(e))
            return None
