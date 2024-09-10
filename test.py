from Main.Engine.Effects import damage


def test_effects():
    effects = damage()
    assert effects is not None
    assert effects.effects == []
    assert effects.get_effects() == []
