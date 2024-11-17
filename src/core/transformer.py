
# Define a transformer to convert parse trees to a more usable format
class DomainForgeTransformer(Transformer):
    def start(self, rules):
        return {'rules': rules}

    def rule(self, items):
        result = {}
        for item in items:
            result.update(item)
        return result

    def quantifier(self, q):
        return {'quantifier': q[0]}

    def entity(self, e):
        symbol, identifier = e
        return {'entity': {'symbol': symbol, 'name': identifier}}

    def relationship(self, r):
        return {'relationship': r[0]}

    def modal_operator(self, m):
        return {'modal_operator': m[0]}

    def qualifier(self, items):
        relationship = items[0]
        entity = items[1]
        return {'qualifier': {'relationship': relationship, 'entity': entity}}

    def qualifiers(self, qs):
        return {'qualifiers': qs}

    def condition(self, c):
        return {'condition': c[0]}

    def expression(self, items):
        entity1, relationship, entity2 = items
        return {'expression': {'entity1': entity1, 'relationship': relationship, 'entity2': entity2}}

    def IDENTIFIER(self, token):
        return str(token)

    def ENTITY_SYMBOL(self, token):
        return str(token)

    def RELATIONSHIP_SYMBOL(self, token):
        return str(token)

    def INT(self, token):
        return int(token)

    def __default__(self, data, children, meta):
        return {data: children}

# Example usage
if __name__ == '__main__':
    domainforge_code = '''
    ALL: #Employee ! > &Supervisor - %Experienced | #Employee - %FullTime
    #Order > [ #OrderItem ]
    #OrderItem > #Product & %Quantity & $Price
    '''

    tree = domainforge_parser.parse(domainforge_code)
    transformer = DomainForgeTransformer()
    result = transformer.transform(tree)
    print(result)