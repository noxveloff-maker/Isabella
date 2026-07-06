import re
import json

class ToolParser:
    """Parse les tool_calls du LLM dans le format <tool_call>...</tool_call>."""

    PATTERN = re.compile(r'<tool_call>\s*(\{.*?\})\s*</tool_call>', re.DOTALL)

    @classmethod
    def extraire(cls, texte):
        """Extrait les tool_calls d'un texte. Retourne (texte_sans_tool_calls, liste_d_actions)."""
        actions = []
        texte_propre = texte

        for match in cls.PATTERN.finditer(texte):
            try:
                action = json.loads(match.group(1))
                actions.append(action)
                # Retire le tool_call du texte
                texte_propre = texte_propre.replace(match.group(0), "")
            except json.JSONDecodeError:
                continue

        return texte_propre.strip(), actions

    @classmethod
    def a_tool_calls(cls, texte):
        """Verifie si le texte contient des tool_calls."""
        return cls.PATTERN.search(texte) is not None

if __name__ == "__main__":
    # Test
    texte = """Je vais lister les fichiers pour toi.
<tool_call>
{"action": "lister", "module": "fichiers", "parametres": {"chemin": "."}}
</tool_call>
Et voici le resultat."""
    propre, actions = ToolParser.extraire(texte)
    print("Texte propre :", propre)
    print("Actions :", actions)
