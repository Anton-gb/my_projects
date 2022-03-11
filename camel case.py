# def to_camel_case(text: str):
#     res = ''
#     case = []
#     for i in text.split('-'):
#         for j in i.split('_'):
#             case.append(j)
#     for i, v in enumerate(case):
#         if i != 0:
#             res += v.capitalize()
#         else:
#             res += v
#     return res

def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])


print(to_camel_case('woei-ekdkd_edkm'))
