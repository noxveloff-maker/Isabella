import re
import json

class ToolParser:
    """Parse les tool_calls du LLM dans les formats <tool_call>...</tool_call> ou <nom>...</nom>."""

    # Accepte les tags <controle_lancer>, <fichiers_lister>, etc. (mais PAS <tool_call>)
    PATTERN = re.compile(r'<([a-zA-Z_][a-zA-Z0-9_]*)>\s*(\{.*?\})\s*</\1>', re.DOTALL)
    # Fallback : <tool_call> standard (exclut tool_call du pattern generique)
    PATTERN_TOOL_CALL = re.compile(r'<tool_call>\s*(\{.*?\})\s*</tool_call>', re.DOTALL)

    @classmethod
    def extraire(cls, texte):
        """Extrait les tool_calls d'un texte. Retourne (texte_sans_tool_calls, liste_d_actions)."""
        actions = []
        texte_propre = texte

        # Cherche les tags generiques <nom>...</nom> (sauf <tool_call>)
        for match in cls.PATTERN.finditer(texte):
            tag_name = match.group(1)
            if tag_name == "tool_call":
                continue  # Deja geré par le fallback
            try:
                action = json.loads(match.group(2))
                actions.append(action)
                texte_propre = texte_propre.replace(match.group(0), "")
            except json.JSONDecodeError:
                continue

        # Fallback : <tool_call> standard
        for match in cls.PATTERN_TOOL_CALL.finditer(texte):
            try:
                action = json.loads(match.group(1))
                actions.append(action)
                texte_propre = texte_propre.replace(match.group(0), "")
            except json.JSONDecodeError:
                continue

        return texte_propre.strip(), actions

    @classmethod
    def a_tool_calls(cls, texte):
        """Verifie si le texte contient des tool_calls."""
        return cls.PATTERN.search(texte) is not None or cls.PATTERN_TOOL_CALL.search(texte) is not None

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
