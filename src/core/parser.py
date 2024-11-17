# domainforge_parser.py

from lark import Lark, Transformer, v_args

# Load the grammar from the 'domainforge_grammar.lark' file
domainforge_grammar = r"""
%import common.WORD
%import common.INT
%import common.WS
%import common.NEWLINE
%ignore WS
%ignore NEWLINE

start: rule+

rule: quantifier? entity modal_operator? relationship entity qualifiers? condition?

quantifier: "ALL:" | "EXISTS:" | INT ":" 

entity: ENTITY_SYMBOL IDENTIFIER

relationship: RELATIONSHIP_SYMBOL

modal_operator: "!" | "~" | "?"

qualifiers: qualifier+

qualifier: relationship entity

condition: "|" expression

expression: entity relationship entity

ENTITY_SYMBOL: ("#" | "%" | "@" | "&" | "^" | "$" | "*")
RELATIONSHIP_SYMBOL: ("::" | ">" | "-" | "=>" | "/" | "->" | "||" | "++>" | "-->" | "<~>" | "<->")

IDENTIFIER: /[a-zA-Z_][a-zA-Z0-9_]*/

%declare INT
"""

# Initialize the parser
domainforge_parser = Lark(domainforge_grammar, parser='lalr', start='start')

