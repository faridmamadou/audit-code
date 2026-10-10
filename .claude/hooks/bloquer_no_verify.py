#!/usr/bin/env python3
# Hook Claude Code — cours "Auditer son code avant de pousser"
# Bloque toute commande git qui contourne les hooks de sécurité.
# Doc : https://code.claude.com/docs/en/agent-sdk/hooks
#
# Installation : référencer ce fichier dans .claude/settings.json

import json
import re
import sys

commande = json.load(sys.stdin).get("tool_input", {}).get("command", "")

if re.search(r"\bgit\b.*(--no-verify|\s-n\b)", commande):
    print(
        "Bloqué : les hooks de sécurité sont obligatoires. "
        "Corrige les erreurs signalées par pre-commit au lieu de les contourner.",
        file=sys.stderr,
    )
    sys.exit(2)
