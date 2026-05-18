"""
Torz Logic Engine - Torzní logika pro AI etiku a rezonanci
==========================================================

Implementace torzní logiky a MAJAK-CORE protokolu podle Grok navrhu.
Umožňuje měření "hustoty transformace" a aktivaci "Protokolu Proč?"

Principy:
- 1 + 1 + Impuls = 3 (emergentní synergie)
- ρ_T (hustota transformace) jako metrika rezonance
- Tahač vs Strkač paradigma
- Etika Vyslance jako navigační rámec
"""

from .core import TorzImpulse, MajakEngine
from .metrics import ResonanceMetrics
from .protocols import MajakProtocol

__version__ = "0.1.0"
__author__ = "Martin Beran (Chytrý Opravář) & AI Consortium"

__all__ = [
    "TorzImpulse",
    "MajakEngine", 
    "ResonanceMetrics",
    "MajakProtocol"
]
