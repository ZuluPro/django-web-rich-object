import factory
from factory import fuzzy

WRO_TYPES = (
    'article',
    'website',
    'video',
    'image',
    'application'
)
WRO_SUBTYPES = {
    'article': ('html',),
    'website': ('html',),
    'video': ('html', 'mp4',),
    'image': ('png', 'jpeg', 'gif'),
    'application': ('pdf',),
}


def laze_subtype(wro):
    if wro.type not in WRO_SUBTYPES:
        return 'website'
    subtypes = WRO_SUBTYPES[wro.type]
    return fuzzy.FuzzyChoice(subtypes).fuzz()


class WebRichObjectFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('sentence')
    type = fuzzy.FuzzyChoice(WRO_TYPES)
    subtype = factory.LazyAttribute(laze_subtype)

    image = factory.Faker('image_url')
    base_url = factory.Faker('uri')
    url = factory.LazyAttribute(lambda w: w.base_url)

    site_name = factory.Faker('company')
    description = factory.Faker('sentence', nb_words=25)
    site_name = factory.Faker('name')
    author = factory.Faker('name')

    created_time = factory.Faker('date_time_between', start_date='-30d', end_date='-20d')
    published_time = factory.Faker('date_time_between', start_date='-20d', end_date='-10d')
    modified_time = factory.Faker('date_time_between', start_date='-10d', end_date='now')

    create_at = factory.Faker('date_time_between', start_date='-20d', end_date='-10d')
    updated_at = factory.Faker('date_time_between', start_date='-10d', end_date='now')

    class Meta:
        model = 'dj_web_rich_object.WebRichObject'
