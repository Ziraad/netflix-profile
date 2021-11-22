from django.contrib.auth.models import User
from django.db import models
from account.models import Profile


class Product(models.Model):
    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصول'

    name = models.CharField('نام محصول', max_length=100)
    price = models.IntegerField('قیمت محصول')

    def __str__(self):
        return self.name


class Customer(models.Model):
    class Meta:
        verbose_name = 'خریدار'
        verbose_name_plural = 'خریدار'

    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='خریدار')

    def __str__(self):
        return self.user.username


class Order(models.Model):
    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد خرید'

    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='خریدار', null=True)
    presenter = models.ForeignKey(Profile, on_delete=models.PROTECT, related_name='order', verbose_name='معرف')
    product = models.ManyToManyField(Product, related_name='orders', null=True, blank=True)
    amount = models.PositiveIntegerField('تعداد', default=1)
    total_price = models.PositiveIntegerField('جمع کل', null=True, blank=True)

    def __str__(self):
        return self.customer.user.username

    @staticmethod
    def initiate(customer, presenter):
        print('in initial')
        try:
            order = Order.objects.filter(customer=customer)
            print('order', order)
            if order.exists():
                print('order exist')
                try:
                    get_order = Order.objects.get(customer=customer)
                    return get_order
                except:
                    new_order = Order()
                    new_order.customer = customer
                    new_order.presenter = presenter
                    new_order.save()
                    return new_order

            else:
                print('no order')
                new_order = Order()
                new_order.customer = customer
                new_order.presenter = presenter
                new_order.save()
                return new_order

        except Exception as e:
            raise Exception(e)

    def add_product(self, product):
        try:
            order = Order.initiate(customer=self.customer, presenter=self.presenter)
            print('order: ', order)
            product1 = Product.objects.filter(name=product)
            print('product exist')
            assert product1.exists(), "Product not found."
            product1 = product1.get(name=product)
            print('product: ', product1)
            order.product.add(product1)
            order.save()

        except Exception as e:
            raise Exception(e)

