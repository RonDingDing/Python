def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
    if space_before >= 0:
        end = space_before
    else:
        space_after = text.rfind(' ', max_len)
        if space_after >= 0:
            end = space_after
    if end is None: # 没找到空格
        end = len(text)
    return text[:end].rstrip()



print(clip.__defaults__)
#(80,)
print(clip.__code__) # doctest: +ELLIPSIS
#<code object clip at 0x...>
print(clip.__code__.co_varnames)
#('text', 'max_len', 'end', 'space_before', 'space_after')
print(clip.__code__.co_argcount)
2
