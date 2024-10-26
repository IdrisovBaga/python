def introspection_info(obj):
    slovar = {}
    slovar['type'] = type(obj).__name__
    slovar['attributes'] =  [x for x in dir(obj) if not callable(getattr(obj, x))]
    slovar['methods'] = [x for x in dir(obj) if callable(getattr(obj, x))]
    slovar['module'] = introspection_info.__module__
    return (slovar)
number_info = introspection_info(42)
print(number_info)