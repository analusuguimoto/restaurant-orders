from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    vaca_atolada = Dish("vaca_atolada", 40.90)
    vaca_atolada_2 = Dish("vaca_atolada", 40.90)
    carbonara = Dish("carbonara", 53.20)

    assert carbonara.price == 53.20
    assert carbonara.name == "carbonara"
    assert vaca_atolada == vaca_atolada_2

    assert hash(vaca_atolada) != hash(carbonara)
    assert hash(vaca_atolada) == hash(vaca_atolada_2)
    assert repr(carbonara) == "Dish('carbonara', R$53.20)"

    carbonara.add_ingredient_dependency(Ingredient("farinha"), 3)
    carbonara.add_ingredient_dependency(Ingredient("ovo"), 4)
    carbonara.add_ingredient_dependency(Ingredient("bacon"), 1)

    assert carbonara.get_ingredients() == {
        Ingredient("farinha"),
        Ingredient("ovo"),
        Ingredient("bacon"),
    }

    assert carbonara.get_restrictions() == {
        Restriction.GLUTEN,
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("carbonara", "valor")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("carbonara", 0)
