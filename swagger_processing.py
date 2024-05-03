from swagger_parser import SwaggerParser

# condensed format (all operations in line with the path) 
def operations_per_path(specification):
    base = specification['basePath']
    paths = specification['paths']
    ops = []
    for p in paths:
        methods = paths[p].keys()
        temp = f"{'|'.join(methods).upper()} {base}{p}" #  methods are keys inside a single path-dict
        if "/pet" in temp:
            ops.append(temp)
    return ops

parser = SwaggerParser(swagger_path='swagger.json')  # Init with file
spec = parser.specification

print("Operations in swagger (resource-URIs with their HTTP-methods):")
paths = operations_per_path(spec)
print("\n".join(paths))