# AWS-Bedrock

This project uses a Python virtual environment to manage dependencies. Follow the instructions below based on your operating system to set up the environment.

---

## 🛠️ Setup Instructions

### ✅ Prerequisites

- Python 3.12 or later
- `pip` installed

---

## 💻 On Ubuntu / Linux

### 1. Install required system package (if not already installed)

```bash
sudo apt update
sudo apt install python3.12-venv -y
````

### 2. Create and activate the virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

---

## 🪟 On Windows (PowerShell)

### 1. Create the virtual environment

```powershell
python -m venv .venv
```

### 2. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate
```

> ❗ If you get a script execution error, run:
>
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
> ```

### 3. Install Python dependencies

```powershell
pip install -r requirements.txt
```

---

## 🧪 To verify the environment

After activation, run:

```bash
python --version
pip list
```

---

## 🚫 Deactivating the Virtual Environment

When you're done working:

```bash
deactivate
```

