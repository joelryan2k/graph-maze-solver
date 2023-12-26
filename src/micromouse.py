import typing

def convert_micro_mouse(lines: typing.List[str]):
    result: typing.List[str] = []

    for line in lines:
        foo = line[::2] \
            .replace(' ', '  ') \
            .replace('o', ' #') \
            .replace('-', ' #') \
            .replace('|', ' #') \
            .replace('S', ' S') \
            .replace('G', ' E')
        
        result.append(foo)

    return result
