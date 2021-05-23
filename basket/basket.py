class Basket():
    """
        A base Basket class, providing some default behaviors that
        can be inherited or overrided, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get("basket_session_key")
        if "basket_session_key" not in request.session:
            basket = self.session["basket_session_key"] = {}
        self.basket = basket

    def add(self, product, product_qty):
        """
        Adding and updating the users basket session data
        """
        product_id = product.id

        if product_id not in self.basket: # checks if product is in the basket session
            self.basket[product_id] = {"price": str(product.price), "qty": int(product_qty)}
        self.session.modified = True # tells django we've modified the session

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item["qty"] for item in self.basket.values())
