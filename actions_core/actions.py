import arrow

from .models import Event, Organization, TimelineEntity, User, TIMELINE_ENTITY_TYPES


DATE_FORMAT = 'YYYY-MM-DD'


def init_integration_basket(user: User):
    aliah_date = arrow.get(user.aliah_date, DATE_FORMAT)

    first_basket = Event.objects.create(
        user=user,
        name='First basket',
        description='Fist payment of integration basket, in cash',
        date=aliah_date.format(DATE_FORMAT)
    )
    first_basket.save()

    # shift to 10'th of next month
    payment_date = aliah_date.shift(months=1)
    payment_date = payment_date.shift(days=-payment_date.date().day + 10)

    # add 6 events
    for i in range(1, 7):
        print(payment_date.format(DATE_FORMAT))
        basket_payment = Event.objects.create(
            user=user,
            name=f'Integration basken №{i}',
            description=f'Payment of integration basket, {i}/6',
            date=payment_date.format(DATE_FORMAT)
        )
        basket_payment.save()
        payment_date = payment_date.shift(months=1)


def init_bank_suggestion(user: User):
    entities = [
        {
            'name': 'Create bank account',
            'description': 'todo...',
            'end_date': None,
            'type': 's',
            'organization': None
        },
        {
            'name': 'Register at medical insurance',
            'description': 'todo...',
            'end_date': None,
            'type': 's',
            'organization': None
        },
        {
            'name': 'Order a biometryc ID',
            'description': 'todo...',
            'end_date': arrow.get(user.aliah_date).shift(months=3).format(DATE_FORMAT),
            'type': 's',
            'organization': Organization.objects.get(name='Ministry of Aliyah and Integration')
        },
    ]

    for entity in entities:
        event = TimelineEntity.objects.create(
            user=user,
            name=entity['name'],
            description=entity['description'],
            entity_type=entity['type'],
            start_date=user.aliah_date,
            end_date=entity['end_date'],
            is_complited=False,
            organization=entity['organization']
        )
        event.save()

