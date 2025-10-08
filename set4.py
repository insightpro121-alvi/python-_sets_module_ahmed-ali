# Given label sets
train_labels = {'cat', 'dog', 'horse', 'goat'}
val_labels = {'cat', 'dog', 'sheep'}
test_labels = {'cat', 'dog', 'horse', 'cow'}

print("Train labels:", train_labels)
print("Validation labels:", val_labels)
print("Test labels:", test_labels)

common_labels = train_labels & val_labels & test_labels
print("Labels present in all splits:", common_labels)

missing_in_val=train_labels-val_labels
missing_in_test=train_labels-test_labels
print("label in train but mussing in val:",missing_in_val)
print("label in train but misiing in test:",missing_in_test)

is_subset=test_labels.issubset(train_labels)
print("Are all test labels in train labels?", is_subset)

if not is_subset:
    unseen_in_test=test_labels-train_labels
    print("unseen test labels:",unseen_in_test)
