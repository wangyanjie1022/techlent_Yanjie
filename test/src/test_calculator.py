from app.src.calculator import calculator

cal = calculator()

def test_add():
    assert cal.add(1,1) == 2
    assert cal.add(1,2) == 3
