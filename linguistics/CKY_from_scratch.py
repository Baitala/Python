#Doing CKY/CYK algorithm from scratch.
from nltk.tree import Tree

def cky(in_tokens, in_grammar_rules):
    """Cocke–Younger–Kasami algorithm (alternatively called CYK, or CKY)
    is a parsing algorithm for context-free grammars, named after its inventors,
    John Cocke, Daniel Younger and Tadao Kasami. It employs bottom-up parsing and dynamic programming."""

    def get_cells(input_tokens, input_grammar_rules):
        """Generates cells for CKY algorithm."""
        def apply_rules(rule):
            try:
                return input_grammar_rules[rule]
            except:
                return None

        cells = { (1, x+1): [] for x in range(len(input_tokens)) }
        # print(cells)
        for ind, word in enumerate(input_tokens):
            rule = apply_rules(word)
            for variant in rule:
                cells[1, ind+1].append((variant, (word)))

        length = len(input_tokens)

        for l in range(2, length+1):
            for s in range(1, length - l + 2):
                for p in range(1, l):
                    if (p, s) in cells.keys() and (l-p, s+p) in cells.keys():
                        t1 = cells[p, s]
                        t2 = cells[l-p, s+p]

                        for pos1, _ in t1:
                            for pos2, _ in t2:
                                rules = apply_rules(pos1 + ' ' + pos2)
                                # print(rules)
                                if rules:
                                    if (l, s) not in cells.keys():
                                        cells[l, s] = []

                                    for rule in rules:
                                        cells[l, s].append(
                                            (
                                            rule, (pos1, pos2)
                                            )
                                        )
        return cells

    def get_trees():
        """Generates list of all trees for CKY algorithm."""
        return

    cells = get_cells(in_tokens, in_grammar_rules)
    print(cells)
    return get_trees()

if __name__ == "__main__":
    #Defining input
    sentence = "I like dogs and cats"
    grammar_rules = {
        'I': ['NP'],
        'like': ['V', 'PREP'],
        'like': ['V'],
        'dogs': ['NN'],
        'cats': ['NN'],
        'and': ['CONJ'],
        'NP VP': ['S'],
        'V NP': ['VP'],
        'V NN': ['VP'],
        'NN NP': ['NP'],
        'CONJ NN': ['NP'],
        'VP NP': ['S'],
    }

    tokens = sentence.split() #AKA words
    trees = cky(tokens, grammar_rules)
    for tree in trees:
        parsetree = Tree.fromstring(tree)
        parsetree.pretty_print()
