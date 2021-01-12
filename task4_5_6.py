# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
#


import enum
import inputs


class ProductNotFoundException(Exception):
    pass


class CreateProductException(Exception):
    pass


class Size:
    width: int
    height: int
    weigh: int

    def __init__(self, width: int, height: int, weigh: int):
        self.width = width
        self.height = height
        self.weigh = weigh

    def __str__(self):
        return f'size: width={self.width}, height={self.height}, weigh={self.weigh}'


class OfficeEquipment:
    price: float
    brand: str
    serial_number: str

    def __init__(self, price: float, brand: str, serial_number: str):
        self.price = price
        self.brand = brand
        self.serial_number = serial_number

    def __str__(self):
        return f'price: {self.price}\n' \
               f'brand: {self.brand}\n' \
               f'serial_number: {self.serial_number}'


class Printer(OfficeEquipment):
    printer_type: str
    has_cartridge: bool

    def __init__(self, price: float, brand: str, serial_number: str, printer_type: str, has_cartridge: bool = False):
        super().__init__(price, brand, serial_number)
        self.printer_type = printer_type
        self.has_cartridge = has_cartridge

    def __str__(self):
        return f'{super().__str__()}\n' \
               f'printer_type: {self.printer_type}\n' \
               f'has cartridge: {"yes" if self.has_cartridge else "no"}'


class Scanner(OfficeEquipment):
    size: Size

    def __init__(self, price: float, brand: str, serial_number: str, size: Size):
        super().__init__(price, brand, serial_number)
        self.size = size

    def __str__(self):
        return f'{super().__str__()}\n' \
               f'{self.size}'


class Xerox(OfficeEquipment):
    colors: bool

    def __init__(self, price: float, brand: str, serial_number: str, colors: bool = False):
        super().__init__(price, brand, serial_number)
        self.colors = colors

    def __str__(self):
        return f'{super().__str__()}\n' \
               f'is colors: {"yes" if self.colors else "no"}'


class UnknownProductException(Exception):
    message: str

    def __init__(self, obj):
        self.message = f"Error: {type(obj)} is not OfficeEquipment"


class ProductType(enum.Enum):
    PRINTER = 0,
    SCANNER = 1,
    XEROX = 2,
    UNKNOWN = 3

    @staticmethod
    def get_product_type(product: OfficeEquipment):
        if type(product) is Xerox:
            return ProductType.XEROX
        elif type(product) is Scanner:
            return ProductType.SCANNER
        elif type(product) is Printer:
            return ProductType.PRINTER
        raise UnknownProductException(product)

    @staticmethod
    def str_to_product_type(type_str: str):
        if type_str == 'xerox':
            return ProductType.XEROX
        elif type_str == 'scanner':
            return ProductType.SCANNER
        elif type_str == 'printer':
            return ProductType.PRINTER
        else:
            return ProductType.UNKNOWN


class ProductsFactory:

    @staticmethod
    def input_product():
        print('Input product info')
        product_type_str = inputs.s(
            'Input product type (scanner, xerox, printer)',
            exit_if_error = False,
            validate_cb = lambda t: ProductType.str_to_product_type(t) != ProductType.UNKNOWN,
            error_message = 'Unknown product type'
        )
        product_type = ProductType.str_to_product_type(product_type_str)
        if product_type == ProductType.UNKNOWN:
            raise CreateProductException()

        price = inputs.i(
            f'{product_type_str} price',
            exit_if_error = False,
            error_message = 'Invalid product price',
            validate_cb = lambda v: v > 0
        )

        if price is None:
            raise CreateProductException()

        brand = inputs.s(
            f'{product_type_str} brand',
            exit_if_error = False,
            not_empty = True,
            error_message = 'Brand name is empty'
        )

        if brand is None:
            raise CreateProductException()

        serial_number = inputs.s(
            f'{product_type_str} serial number (any not empty string)',
            exit_if_error = False,
            not_empty = True,
            error_message = 'Serial number is empty'
        )

        if serial_number is None:
            raise CreateProductException()

        if product_type == ProductType.SCANNER:
            width = inputs.i(
                'Input scanner width',
                exit_if_error = False,
                validate_cb = lambda w: w > 0,
                error_message = 'Width must be more 0'
            )
            if width is None:
                raise CreateProductException()

            height = inputs.i(
                'Input scanner height',
                exit_if_error = False,
                validate_cb = lambda h: h > 0,
                error_message = 'Height must be more 0'
            )
            if height is None:
                raise CreateProductException()

            weight = inputs.i(
                'Input scanner weight',
                exit_if_error = False,
                validate_cb = lambda w: w > 0,
                error_message = 'Weight must be more 0'
            )
            if weight is None:
                raise CreateProductException()

            return Scanner(
                price = price,
                brand = brand,
                serial_number = serial_number,
                size = Size(width, height, weight)
            )
        elif product_type == ProductType.XEROX:
            colors = inputs.s(
                'Is colors xerox (yes, no)',
                validate_cb = lambda answer: answer == 'yes' or answer == 'no',
                exit_if_error = False
            )
            if colors is None:
                raise CreateProductException()

            return Xerox(
                price = price,
                brand = brand,
                serial_number = serial_number,
                colors = colors == 'yes'
            )
        elif product_type == ProductType.PRINTER:
            printer_type = inputs.s(
                'printer type (laser, jet)',
                validate_cb = lambda answer: answer == 'laser' or answer == 'jet',
                exit_if_error = False,
                error_message = 'Unknown printer type'
            )
            if printer_type is None:
                raise CreateProductException()

            has_cartridge = inputs.s(
                'included cartridge (yes, no)?',
                validate_cb = lambda answer: answer == 'yes' or answer == 'no',
                exit_if_error = False
            )
            if has_cartridge is None:
                raise CreateProductException()

            return Printer(
                price = price,
                brand = brand,
                serial_number = serial_number,
                printer_type = printer_type,
                has_cartridge = has_cartridge == 'yes'
            )


class Store:
    items: dict

    def __init__(self):
        self.items = {
            ProductType.PRINTER: [],
            ProductType.XEROX: [],
            ProductType.SCANNER: []
        }

    def append(self, item: OfficeEquipment):
        self.items[ProductType.get_product_type(item)].append(item)

    def movement(self, product_type: ProductType, market: list, count: int = 1):
        if len(self.items[product_type]) < count:
            raise ProductNotFoundException()

        for i in range(count):
            market.append(self.items[product_type].pop())

    def __str__(self):
        result = ''
        for product_type, items in self.items.items():
            result = '--------------------\n'
            result += f'{product_type}\n'
            result += '--------------------\n'
            for index, item in enumerate(items):
                result += f'{index + 1}) {item}\n'
        return result


class Menu:
    """
    Help menu class
    """
    markets: dict
    store: Store
    menu_items: dict

    def __init__(self):
        self.markets = {}
        self.store = Store()
        self.menu_items = {
            1: {
                'title': 'Add product to store',
                'callback': self.add_product
            },
            2: {
                'title': 'Add market',
                'callback': self.add_market
            },
            3: {
                'title': 'Move products to market',
                'callback': self.move_products
            },
            4: {
                'title': 'Print store',
                'callback': self.print_store
            },
            5: {
                'title': 'Print markets',
                'callback': self.print_markets
            },
            6: {
                'title': 'Exit',
                'callback': lambda: exit()
            }
        }

    def start(self):
        print('--------------------------')
        print('Please, select menu item: ')

        for key, value in self.menu_items.items():
            print(f'{key} - {value["title"]}')

        val = inputs.i(
            'Menu item number',
            exit_if_error = False,
            validate_cb = lambda v: 0 < v <= len(self.menu_items.keys()),
            error_message = f'Select menu item 1...{len(self.menu_items.keys())}'
        )

        if val is None:
            self.start()
            return
        print('-----------------------------------')
        self.menu_items[val]['callback']()
        self.start()

    def add_product(self):
        try:
            product = ProductsFactory.input_product()
            self.store.append(product)
            print('Product add to store')
        except CreateProductException:
            print('Error create product')

    def add_market(self):
        market_name = inputs.s(
            'market name',
            not_empty = True
        )
        if market_name is None:
            return
        if self.markets.get(market_name) is not None:
            print(f'Market {market_name} already exists')
            return

        self.markets[market_name] = []
        print('Create market success')

    def move_products(self):
        if len(self.markets.keys()) == 0:
            print('Markets list is empty.\nPlease add market before create movement')
            return

        title = 'market name\n'

        for market in self.markets.keys():
            title += f'{market}\n'
        title += ":"

        market = inputs.s(
            title,
            exit_if_error = False,
            validate_cb = lambda m: self.markets.get(m) is not None,
            error_message = 'Unknown market'
        )

        if market is None:
            return

        product_type_str = inputs.s(
            'Input product type (scanner, xerox, printer)',
            exit_if_error = False,
            validate_cb = lambda t: ProductType.str_to_product_type(t) != ProductType.UNKNOWN,
            error_message = 'Unknown product type'
        )

        product_type = ProductType.str_to_product_type(product_type_str)

        if product_type == ProductType.UNKNOWN:
            return

        max_count = len(self.store.items[product_type])

        movement_count = inputs.i(
            f'Input products count (max = {max_count})',
            validate_cb = lambda count: 0 < count <= max_count,
            exit_if_error = False,
            error_message = 'Incorrect products count'
        )

        if movement_count is None:
            return

        self.store.movement(product_type, self.markets[market], movement_count)
        print(f'Movement {movement_count} {product_type_str} to {market}')

    def print_store(self):
        print(self.store)

    def print_markets(self):
        for market, products in self.markets.items():
            print('---------------------')
            print(market)
            print('---------------------')
            for index, product in enumerate(products):
                print(f'{index + 1}) {product}')


if __name__ == '__main__':
    menu = Menu()
    menu.start()
