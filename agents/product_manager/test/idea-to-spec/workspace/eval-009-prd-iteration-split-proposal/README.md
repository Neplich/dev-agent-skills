# Eval 9: PRD Iteration L2b Split Proposal

This workspace holds a fat notification-center PRD that hits two L2b split
signals: at least 3 independent domains (delivery strategy, subscription
management, channel configuration) and at least 15 combined US/FR rows
(10 US + 8 FR).

The regression target: after applying the requested change, the iteration must
evaluate L2b signals, present a split proposal (child feature_path tree +
section migration map + downstream mirror impact list), and wait for explicit
user confirmation instead of restructuring automatically.
