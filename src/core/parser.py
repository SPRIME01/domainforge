from lark import Lark
import os

# Determine the path to the grammar file
grammar_path = os.path.join(os.path.dirname(__file__), '..', 'domainforge', 'grammar', 'domainforge_grammar.lark')

# Load the grammar from the 'domainforge_grammar.lark' file
with open(grammar_path, 'r') as grammar_file:
    domainforge_grammar = grammar_file.read()

domainforge_parser = Lark(domainforge_grammar, parser='earley', start='start')