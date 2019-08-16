import arrow

from .models import Event, Organization, TimelineEntity, User


DATE_FORMAT = 'YYYY-MM-DD'


def init_entities(user: User):
    aliah_date = arrow.get(user.aliah_date, DATE_FORMAT)

    # first_basket = Event.objects.create(
    #     user=user,
    #     name='First basket',
    #     description='Fist payment of integration basket, in cash',
    #     date=aliah_date.format(DATE_FORMAT),
    # )
    # first_basket.save()

    # shift to 10'th of next month
    payment_date = aliah_date.shift(months=1)
    payment_date = payment_date.shift(days=-payment_date.date().day + 10)

    # add 6 events
    for i in range(1, 7):
        basket_payment = Event.objects.create(
            user=user,
            name=f'Integration basket №{i}',
            description=f'Payment of integration basket, {i}/6',
            date=payment_date.format(DATE_FORMAT),
            organization=Organization.objects.get(name='Ministry of Aliyah and Integration')
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
            'name': 'Meet with integration curator',
            'description': 'todo...',
            'end_date': None,
            'type': 's',
            'organization': Organization.objects.get(name='Ministry of Aliyah and Integration')
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
        {
            'name': 'Harnona tax discount available',
            'description': 'todo...',
            'end_date': arrow.get(user.aliah_date).shift(years=2).format(DATE_FORMAT),
            'type': 'r',
            'organization': Organization.objects.get(name='Local city hall')
        },
        {
            'name': 'Real estate purchasing tax discount available',
            'description': 'todo...',
            'end_date': arrow.get(user.aliah_date).shift(years=7).format(DATE_FORMAT),
            'type': 'r',
            'organization': Organization.objects.get(name='Ministry of Construction and Housing')
        },
        {
            'name': '5 month of studying in ulpan',
            'description': 'todo...',
            'end_date': arrow.get(user.aliah_date).shift(months=18).format(DATE_FORMAT),
            'type': 'r',
            'organization': Organization.objects.get(name='Ministry of Aliyah and Integration')
        },
    ]

    for entity in entities:
        entity = TimelineEntity.objects.create(
            user=user,
            name=entity['name'],
            description=entity['description'],
            entity_type=entity['type'],
            start_date=user.aliah_date,
            end_date=entity['end_date'],
            organization=entity['organization']
        )
        entity.save()


def init_driving_license(user: User, more_then_5_yars_exp: bool):
    organization = Organization.objects.get(name='Ministry of Transport and Road Safety')

    # right to use old dr license for 1 year
    entity = TimelineEntity.objects.create(
        user=user,
        name='Available to use foreign driveng license',
        description='......',  # todo
        entity_type='r',
        start_date=user.aliah_date,
        end_date=arrow.get(user.aliah_date).shift(years=1).format(DATE_FORMAT),
        organization=organization
    )
    entity.save()

    if not more_then_5_yars_exp:
        entity = TimelineEntity.objects.create(
            user=user,
            name='Pass the driving exam without theoretical part',
            description='......',  # todo
            entity_type='r',
            start_date=user.aliah_date,
            organization=organization
        )
        entity.save()
    else:
        entity = TimelineEntity.objects.create(
            user=user,
            name='Receive the driving license without exam',
            description='......',  # todo
            entity_type='r',
            start_date=user.aliah_date,
            organization=organization
        )
        entity.save()

