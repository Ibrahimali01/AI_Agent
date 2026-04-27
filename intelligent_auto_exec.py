import re

def auto_correct(code):
    # Close open parentheses
    open_parens = code.count('(')
    close_parens = code.count(')')
    missing_close = open_parens - close_parens
    
    if missing_close > 0:
        code += ')' * missing_close
    
    # Keyword typo corrections
    keywords = {
        'deff': 'def',
        'dein': 'def',
        'retun': 'return',
        'retrun': 'return',
        'prnit': 'print',
        'pirnt': 'print',
        'impor': 'import',
        'fromm': 'from',
        'cllass': 'class',
        'iff': 'if',
        'elsse': 'else',
        'whille': 'while',
        'forr': 'for',
        'inn': 'in',
        'Truee': 'True',
        'Falsee': 'False',
        'Nonee': 'None',
        'andd': 'and',
        'orr': 'or',
        'nott': 'not',
        'raisse': 'raise',
        'exsept': 'except',
        'finnally': 'finally',
        'wirth': 'with',
        'asass': 'as',
        'lambdaa': 'lambda',
        'globala': 'global',
        'nonlocala': 'nonlocal',
        'asser': 'assert',
        'passs': 'pass',
        'continuee': 'continue',
        'brea': 'break',
        'delte': 'del',
        'inport': 'import',
        'form': 'from',
        'ture': 'True',
        'flase': 'False',
        'nul': 'None'
    }
    
    for wrong, correct in keywords.items():
        code = re.sub(rf'\\b{wrong}\\b', correct, code)
    
    return code
