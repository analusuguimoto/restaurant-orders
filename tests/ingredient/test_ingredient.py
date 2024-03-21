from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    first_ingredient = Ingredient("camarão")
    second_ingredient = Ingredient("manteiga")
    third_ingredient = Ingredient("camarão")

    assert third_ingredient.name == "camarão"
    assert first_ingredient.name == third_ingredient.name
    assert second_ingredient.name != third_ingredient.name

    assert (first_ingredient == third_ingredient) is True
    assert (first_ingredient == second_ingredient) is False

    assert hash(first_ingredient) == hash(third_ingredient)
    assert hash(first_ingredient) != hash(second_ingredient)

    assert repr(first_ingredient) == "Ingredient('camarão')"
    assert (first_ingredient.restrictions) == {
        Restriction.ANIMAL_MEAT,
        Restriction.SEAFOOD,
        Restriction.ANIMAL_DERIVED,
    }
