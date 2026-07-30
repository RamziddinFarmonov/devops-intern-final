import mlflow
import random

# Point MLflow at the server we just started
mlflow.set_tracking_uri("http://localhost:5001")
mlflow.set_experiment("devops-intern-demo")

with mlflow.start_run(run_name="dummy-run"):
    # Fake hyperparameters
    learning_rate = 0.01
    epochs = 10
    batch_size = 32

    mlflow.log_param("learning_rate", learning_rate)
    mlflow.log_param("epochs", epochs)
    mlflow.log_param("batch_size", batch_size)

    # Fake metrics (simulating a training loop)
    for epoch in range(1, epochs + 1):
        accuracy = 0.5 + (epoch / epochs) * 0.4 + random.uniform(-0.02, 0.02)
        loss = 1.0 - (epoch / epochs) * 0.8 + random.uniform(-0.02, 0.02)
        mlflow.log_metric("accuracy", accuracy, step=epoch)
        mlflow.log_metric("loss", loss, step=epoch)

    print("Dummy experiment logged to MLflow successfully!")
