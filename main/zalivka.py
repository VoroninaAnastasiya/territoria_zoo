import datetime

products = [
    {
        "name": 'FRESH STEP CAT LITTER CLAY EXTREME – Фреш Степ наполнитель..',
        "price": 15,
        "description": 'Fresh Step® Extreme - премиальный впитывающий наполнитель для кошачьего туалета, который производится из высококачественной светло-серой глины эксклюзивно для Fresh Step®.',
        "image_preview": '',
        "brand_id": 5,
        "category_id": 5,
        "sales_id": 4,
        "top_product": 0,
    },
    {
        "name": 'FURMINATOR SHORT HAIR LARGE CAT M/L Фурминатор для короткошерстных кошек..',
        "price": 100,
        "description": 'Фурминатор для шерсти со сменным ножом — это прекрасная альтернатива щеткам и пуходеркам для животных. Благодаря своей особой конструкции, инструмент хорошо удаляет отмерший подшерсток, в то время как здоровая шерсть проскальзывает между зубцами расчески.',
        "image_preview": '',
        "brand_id": 4,
        "category_id": 4,
        "sales_id": 4,
        "top_product": 0,
    },
{
        "name": 'Консервы ROYAL CANIN STERILISED для взрослых кастрированных котов..',
        "price": 25,
        "description": 'Высокий уровень содержания белков в ROYAL CANIN® адаптирован для поддержания мышечной массы вашего питомца. Кроме того, продукт обогащен L-карнитином – веществом, стимулирующим метаболизм жиров',
        "image_preview": '',
        "brand_id": 1,
        "category_id": 1,
        "sales_id": 5,
        "top_product": 1,
    },
{
        "name": 'Корм Chappi для взрослых собак всех пород, говядина по-домашнему..',
        "price": 50,
        "description": 'Chappi для взрослых собак всех пород (Говядина по-домашнему) - это полнорационный сухой корм для взрослых собак всех пород.',
        "image_preview": '',
        "brand_id": 3,
        "category_id": 2,
        "sales_id": 5,
        "top_product": 0,
    },
{
        "name": 'Лакомство For Friends, кабаносы для собак из говядины',
        "price": 12,
        "description": '',
        "image_preview": '',
        "brand_id": 2,
        "category_id": 3,
        "sales_id": 5,
        "top_product": 0,
    },
{
        "name": 'Корм Royal Canin для привередливых взрослых собак мелких пород до 10 кг',
        "price": 30,
        "description": 'Необходимо обеспечить собаке полноценный рацион, не потакая ее желаниям, когда она просит лакомств и отказывается от основного корма. Этого можно достичь при помощи здорового и сбалансированного питания, от которого не сможет отказаться даже самая привередливая собака.',
        "image_preview": '',
        "brand_id": 1,
        "category_id": 1,
        "sales_id": 5,
        "top_product": 1,
    },
]

category = [
    {"name": 'корма для кошек'},
    {"name": 'корма для собак'},
    {"name": 'лакомства для собак'},
    {"name": 'уход для шерсти'},
    {"name": 'наполнители'},
]

sales = [
    {
        "sales_name": "скидка 10%",
        "percent": 10,
        "image": "",
        "start_date": datetime.datetime.now(),
        "finish_date": datetime.datetime.now(),
    },
    {
        "sales_name": "скидка 20%",
        "percent": 20,
        "image": "",
        "start_date": datetime.datetime.now(),
        "finish_date": datetime.datetime.now(),
    }
]

product_image = [
    {
        "product": 0,
        "image": "",
    }
]

brands = [
    {
        "name": "Royal Canin",
        "image": "",
    },
    {
        "name": "For Friends",
        "image": "",
    },
    {
        "name": "Chappy",
        "image": "",
    },
    {
        "name": "Beeztees Profur",
        "image": "",
    },
    {
        "name": "Fresh Step",
        "image": "",
    },
]

ProductCount = [
    {
        "product": 0,
        "value": 0,
        "unit": "",

    }
]

articles = [
    {
        'title': '', 'image': '', 'description': '', 'animal_id': None, 'read_time': '', 'date': None
    }
]

reviews = [
    {'title': '', 'owner': '', 'description': '', 'email': '', 'pet': ''}

]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'terdb',
        'USER': 'teruser',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '',
    }
}

import psycopg2
conn = psycopg2.connect(dbname='terdb', user='teruser', password='admin', host='localhost', )


with conn.cursor() as curs:
    curs.execute('INSERT INTO main_animal(name, image) VALUES(%s, %s)', ("test", "animals/bird.jpg"))
conn.close()


# def fulling_db():
#     for brand_data in brands:
#         fulling_brands = Brand(**brand_data) # распаковка словаря на основании модели
#         fulling_brands.save()
#
#     for sale in sales:
#         fulling_sale = Sales(**sale)
#         fulling_sale.save()
#
#     for cat_prod in category:
#         fulling_cat_products = CategoryProduct(**cat_prod)
#         fulling_cat_products.save()
#
#     for product in products:
#         Product(**product).save()