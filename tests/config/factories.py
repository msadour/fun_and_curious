import factory
from factory.faker import faker

from app.core.game.models import Category, Question

fake = faker.Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    """Class CategoryFactory."""

    label = factory.LazyFunction(fake.word)

    class Meta:
        """class Meta."""

        model = Category


class QuestionFactory(factory.django.DjangoModelFactory):
    """Class QuestionFactory."""

    @factory.lazy_attribute
    def label(self):
        return " ".join(fake.words()) + "?"

    class Meta:
        """class Meta."""

        model = Question
