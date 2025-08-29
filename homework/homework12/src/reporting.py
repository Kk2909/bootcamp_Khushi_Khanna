# helpers for Stage 12 reporting
def fmt_int(x):
    try: return f'{int(round(x)):,}'
    except: return str(x)
