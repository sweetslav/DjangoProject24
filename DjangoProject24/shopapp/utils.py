from faker import Faker
from shopapp.models import Client, Product, Order
import logging
fake = Faker()

logger = logging.getLogger('shopapp')


def create_fake_client():
    """Создать фальшивого клиента."""
    try:
        client = Client.objects.create(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number(),
            address=fake.address(),
        )
        logger.info(f"Created new client: {client}")
        return client
    except Exception as e:
        logger.error(f"Error creating fake client: {e}")
        return None


def create_fake_product():
    """Создать фальшивый продукт."""
    try:
        product = Product.objects.create(
            name=fake.word(),
            description=fake.text(),
            price=fake.random_int(min=1, max=10_000),
            quantity=fake.random_int(min=1, max=100),
        )
        logger.info(f"Created new product: {product}")
        return product
    except Exception as e:
        logger.error(f"Error creating fake product: {e}")
        return None


def create_fake_order(num_products=1):
    """Создать фальшивый заказ."""
    try:
        client = create_fake_client()

        total = 0
        products = []
        for _ in range(num_products):
            product = create_fake_product()
            if product:
                products.append(product)
                total += product.price

        status = fake.random_element(elements=('pending', 'processed', 'shipped', 'cancelled'))

        order = Order.objects.create(
            client=client,
            total=total,
            status=status,
        )

        order.products.add(*products)

        logger.info(f"Created new order: {order}")
        return order
    except Exception as e:
        logger.error(f"Error creating fake order: {e}")
        return None


def create_fake_orders(num_orders=5, num_products_per_order=3):
    """Создать функцию, генерирующую 5 заказов, внутри этих заказов по три товара. Каждый заказ у нового клиента."""
    try:
        for _ in range(num_orders):
            client = create_fake_client()

            total = 0
            products = []
            for _ in range(num_products_per_order):
                product = create_fake_product()
                if product:
                    products.append(product)
                    total += product.price

            status = fake.random_element(elements=('pending', 'processed', 'shipped', 'cancelled'))

            order = Order.objects.create(
                client=client,
                total=total,
                status=status,
            )

            order.products.add(*products)

            logger.info(f"Created new order: {order}")
    except Exception as e:
        logger.error(f"Error creating fake orders: {e}")
