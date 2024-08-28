def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

# inner_function() - 3.Вызовите функцию inner_function внутри функции test_function Ошибка

test_function()