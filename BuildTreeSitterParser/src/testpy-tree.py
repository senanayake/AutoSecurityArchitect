from tree_sitter import Language
from tree_sitter import Parser

Language.build_library(
            # Store the library in the `build` directory
                "build/my-languages.so",
                    # Include one or more languages
                        ["tree-sitter-python"],
                        )


PY_LANGUAGE = Language("build/my-languages.so", "python")

parser = Parser()
parser.set_language(PY_LANGUAGE)

tree = parser.parse(
            bytes(
                  """
                def foo():
                    if bar:
                        baz()
                  """,
                    "utf8",
                 )
            )
print(tree.root_node)