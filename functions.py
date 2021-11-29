from sklearn.metrics import accuracy_score, recall_score, f1_score, roc_auc_score, precision_score


def metrics(y_test, predictions):
    """
    Takes the test labels and a model's predictions
    of the labels and prints the accuracy, recall, f1, and roc auc score.
    :param y_test: True labels
    :param predictions: Predicted Labels
    :return: Dictionary of scores for accuracy, recall, f2, and roc auc.
    """
    results = {
        'Accuracy': accuracy_score(y_test, predictions),
        'Precision': precision_score(y_test, predictions),
        'Recall': recall_score(y_test, predictions),
        'F1': f1_score(y_test, predictions),
        'ROCAUC': roc_auc_score(y_test, predictions)

    }
    print(f"Accuracy: {results['Accuracy']:.2f}")
    print(f"Precision: {results['Precision']:.2f}")
    print(f"Recall: {results['Recall']:.2f}")
    print(f"F1: {results['F1']:.2f}")
    print(f"ROC AUC: {results['ROCAUC']:.2f}")

    return results


def improvement(results1, results2):
    """
    prints whether your new model has improved or gotten worse, and by how much, for each metric.

    :param results1: Metrics from previous model
    :param results2: Metrics from new model
    :return: None
    """
    for items in results1:
        change = results2[items] - results1[items]
        if change < 0:
            print(f"{items:<15} {change:.2f}")
        else:
            print(f"{items:<15} +{change:.2f}")
