def _init_(self, value):
    self.value = value
    self.left = None
    self.right = None

def add(left, right):
    return left + right

def minus(left, right):
    return left - right

def mult(left, right):
    return left * right

def div(left, right):
    if right == 0:
        raise ValueError("Pembagian dengan nol tidak diperbolehkan.")
    return left / right

def kryptonia(node):
    if isinstance(node, tuple):
        left, operator, right = node
        if operator == '+':
            return add(kryptonia(left), kryptonia(right))
        elif operator == '-':
            return minus(kryptonia(left), kryptonia(right))
        elif operator == '*':
            return mult(kryptonia(left), kryptonia(right))
        elif operator == '/':
            return div(kryptonia(left), kryptonia(right))
    else:
        return node  # Ini adalah angka dalam ekspresi

def tree(expression_tree):
    return kryptonia(expression_tree)

# Ekspresi pohon
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi ekspresi pohon dan cetak hasilnya
result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi:", result)
