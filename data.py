from datasets import load_dataset

cola_dataset = load_dataset("glue", "cola")
print(cola_dataset)

train_dataset = cola_dataset["train"]
print(train_dataset[0])
