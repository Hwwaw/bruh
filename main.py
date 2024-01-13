result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a должно быть равно или больше b")
        if b > 100:
            raise IndexError("b должно быть равно или меньше 100")
        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except Exception as e:
        print(f"Какая-то ошибка я хз: {e}")

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)