# Valores de la matriz de confusión
TP = 40 # True Positives
TN = 30 # True Negatives
FP = 20 # False Positives
FN = 10 # False Negatives

# Cálculo de Accuracy
accuracy = (TP + TN) / (TP + TN + FP + FN)

# Cálculo de Precision
precision = TP / (TP + FP) if (TP + FP) > 0 else 0

# Cálculo de Recall
recall = TP / (TP + FN) if (TP + FN) > 0 else 0

# Cálculo de F1-Measure
f1_measure = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

# Imprimir resultados
print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Measure: {f1_measure:.2f}")