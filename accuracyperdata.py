from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# After making predictions
predictions = model.predict(df)
accuracy = accuracy_score(y_true, predictions)
precision = precision_score(y_true, predictions)
recall = recall_score(y_true, predictions)
f1 = f1_score(y_true, predictions)

# Log the metrics
logger.info(f"Accuracy: {accuracy}")
logger.info(f"Precision: {precision}")
logger.info(f"Recall: {recall}")
logger.info(f"F1 Score: {f1}")
