matuda_scores = {"network":60, "database":80, "security":50}
asagi_scores = {"network":80, "database":75, "security":92}
menber_scores = {
    "松田":matuda_scores,
    "浅木":asagi_scores
}
# print(menber_scores)
print(menber_scores["松田"]["security"])
print(matuda_scores["security"])