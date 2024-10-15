import mlflow
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_model():
    X, y = make_classification(n_samples=1000, n_features=4, n_classes=2, random_state=42)
    X_train, x_test, y_train, t_test = train_test_split(X, y, test_size=0.2, random_state=42)
    with mlflow.start_run():
        model = LogisticRegression(random_state=42)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        mlflow.log_param("model_type", "LogisticRegression")
        mlflow.log_metric("accuracy", accuracy)

        mlflow.sklearn.log_model(model, "model")

        print(f"Model trained and logged wuth MLFlow. Accuracy: {accuracy:.2f}")
        
if __name__ == "__main__":
    train_model()