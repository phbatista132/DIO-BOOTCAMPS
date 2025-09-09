import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score


y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

cm = confusion_matrix(y_true, y_pred)
VP, FN, FP, VN = cm[1,1], cm[1,0], cm[0,1], cm[0,0]

metricas = {
    "Acurácia": accuracy_score(y_true, y_pred),
    "Precisão": precision_score(y_true, y_pred),
    "Sensibilidade (Recall)": recall_score(y_true, y_pred),
    "F1-Score": f1_score(y_true, y_pred)
}
df_metricas = pd.DataFrame(metricas, index=["Valor"])


print(df_metricas)


fig, ax = plt.subplots()
ax.matshow(cm, cmap=plt.cm.Blues, alpha=0.7)
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(x=j, y=i, s=cm[i, j], va='center', ha='center')

plt.xlabel('Previsto')
plt.ylabel('Real')
plt.title('Matriz de Confusão')
plt.show()