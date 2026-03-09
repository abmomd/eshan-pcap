# ☁️ Smart Cloud Storage System – Advanced Exception Handling Challenge

You are hired to design a **Smart Cloud Storage System** for a SaaS company.

Users can upload, download, and delete files.  
The system must validate operations, enforce storage limits, and handle failures professionally.

Your implementation must use:

- Custom exception classes
- Exception inheritance
- Structured exception data
- `.args`
- Multiple `except` blocks
- `else`
- `finally`
- Optional exception chaining
- Defensive programming practices

---

# 🎯 System Requirements

---

## 🔹 1️⃣ Create Custom Exceptions

Create the following exception classes:

### 1. `InvalidFileNameError`
- Inherit from `ValueError`
- Raised if:
  - Filename is empty
  - Filename contains invalid characters
  - Filename exceeds allowed length

---

### 2. `StorageLimitExceededError`
- Inherit from `Exception`
- Must store:
  - total storage limit
  - current usage
  - attempted file size
- Pass a meaningful message to the base `Exception` class

---

### 3. `FileAlreadyExistsError`
- Inherit from `Exception`
- Raised if uploading a file that already exists
- Must store the filename

---

### 4. `FileNotFoundInStorageError`
- Inherit from `FileNotFoundError`
- Raised when downloading or deleting a non-existing file

---

### 5. `UnauthorizedAccessError`
- Inherit from `PermissionError`
- Raised when user tries to access another user’s file

---

## 🔹 2️⃣ Create Class: `CloudStorageAccount`

The class must contain:

### Instance Variables:
- `username`
- `storage_limit` (in MB)
- `used_storage`
- `files` (dictionary → filename : size_in_MB)

---

## 🔹 3️⃣ Required Methods

### 🔸 `upload_file(filename, size)`

Must:

- Raise `InvalidFileNameError` if filename invalid
- Raise `ValueError` if size ≤ 0
- Raise `FileAlreadyExistsError` if file exists
- Raise `StorageLimitExceededError` if upload exceeds storage limit
- Otherwise:
  - Add file to dictionary
  - Update used_storage
  - Return success message

---

### 🔸 `download_file(filename)`

Must:

- Raise `FileNotFoundInStorageError` if file not found
- Otherwise return confirmation message

---

### 🔸 `delete_file(filename)`

Must:

- Raise `FileNotFoundInStorageError` if file not found
- Otherwise:
  - Remove file
  - Update used_storage
  - Return confirmation

---

## 🔹 4️⃣ Create Function: `process_operation(account, operation, *args)`

This function must:

- Print operation details
- Use `try` block to perform:
  - upload
  - download
  - delete

Include the following exception handling:

- Catch `InvalidFileNameError`
- Catch `StorageLimitExceededError`
  - Print `.args`
  - Print stored limit and attempted size
- Catch `FileAlreadyExistsError`
- Catch `FileNotFoundInStorageError`
- Catch `UnauthorizedAccessError`
- Catch generic `ValueError`
- Catch unexpected exceptions

Use:

- `else` → Print success confirmation
- `finally` → Print:
  ```
  Operation session ended.
  ```

---

## 🔹 5️⃣ Testing Scenario

Create:

```
account = CloudStorageAccount("Alice", 100)   # 100 MB limit
```

Then test:

```
process_operation(account, "upload", "file1.txt", 40)
process_operation(account, "upload", "file1.txt", 10)
process_operation(account, "upload", "bigfile.zip", 80)
process_operation(account, "upload", "", 10)
process_operation(account, "download", "file1.txt")
process_operation(account, "delete", "unknown.txt")
```

---

# 🎯 What This Assignment Tests

- Advanced exception design
- Exception hierarchy modeling
- Structured exception data
- `.args`
- Defensive programming
- Resource validation logic
- Production-style error handling
- try–except–else–finally control flow
- Real-world system modeling

Design this like a real cloud storage backend used in production.