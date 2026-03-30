# part3_api_files.py
# Product Explorer & Error-Resilient Logger

import requests
from datetime import datetime

# -------------------- LOGGER FUNCTION --------------------

def log_error(function_name, error_type, message):
    """Logs error with timestamp into file"""
    with open("error_log.txt", "a", encoding="utf-8") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{time}] ERROR in {function_name}: {error_type} — {message}\n")


# -------------------- TASK 1: FILE I/O --------------------

# Write file
try:
    with open("python_notes.txt", "w", encoding="utf-8") as f:
        f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
        f.write("Topic 2: Lists are ordered and mutable.\n")
        f.write("Topic 3: Dictionaries store key-value pairs.\n")
        f.write("Topic 4: Loops automate repetitive tasks.\n")
        f.write("Topic 5: Exception handling prevents crashes.\n")
    print("File written successfully.")
except Exception as e:
    log_error("file_write", "Exception", str(e))

# Append
try:
    with open("python_notes.txt", "a", encoding="utf-8") as f:
        f.write("Topic 6: Functions help reuse code.\n")
        f.write("Topic 7: APIs allow communication between systems.\n")
    print("Lines appended.")
except Exception as e:
    log_error("file_append", "Exception", str(e))

# Read file
try:
    with open("python_notes.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("\n--- FILE CONTENT ---")
    for i, line in enumerate(lines, 1):
        print(f"{i}. {line.strip()}")

    print("Total lines:", len(lines))

    # Keyword search
    keyword = input("Enter keyword to search: ").lower()
    found = False

    for line in lines:
        if keyword in line.lower():
            print(line.strip())
            found = True

    if not found:
        print("No matching lines found.")

except Exception as e:
    log_error("file_read", "Exception", str(e))


# -------------------- TASK 2: API --------------------

BASE_URL = "https://dummyjson.com/products"

def fetch_products():
    try:
        response = requests.get(f"{BASE_URL}?limit=20", timeout=5)
        data = response.json()

        print("\n--- PRODUCTS ---")
        for p in data["products"]:
            print(f"{p['id']} | {p['title'][:25]:25} | {p['category']} | ${p['price']} | {p['rating']}")

        return data["products"]

    except requests.exceptions.ConnectionError:
        print("Connection failed.")
        log_error("fetch_products", "ConnectionError", "No connection")
    except requests.exceptions.Timeout:
        print("Request timed out.")
        log_error("fetch_products", "Timeout", "Server slow")
    except Exception as e:
        print(e)
        log_error("fetch_products", "Exception", str(e))


products = fetch_products()

# Filter & sort
if products:
    filtered = [p for p in products if p["rating"] >= 4.5]
    filtered.sort(key=lambda x: x["price"], reverse=True)

    print("\n--- FILTERED PRODUCTS ---")
    for p in filtered:
        print(p["title"], p["price"])


# Category search
try:
    res = requests.get(f"{BASE_URL}/category/laptops", timeout=5)
    data = res.json()

    print("\n--- LAPTOPS ---")
    for p in data["products"]:
        print(p["title"], "-", p["price"])

except Exception as e:
    log_error("category_search", "Exception", str(e))


# POST request
try:
    new_product = {
        "title": "My Custom Product",
        "price": 999,
        "category": "electronics",
        "description": "Created via API"
    }

    res = requests.post(f"{BASE_URL}/add", json=new_product)
    print("\nPOST Response:", res.json())

except Exception as e:
    log_error("post_request", "Exception", str(e))


# -------------------- TASK 3 --------------------

# Safe divide
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))


# Safe file read
def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")


print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))


# Input validation loop
while True:
    user = input("\nEnter product ID (1–100) or 'quit': ")

    if user.lower() == "quit":
        break

    if not user.isdigit():
        print("Invalid input")
        continue

    pid = int(user)

    if pid < 1 or pid > 100:
        print("Out of range")
        continue

    try:
        res = requests.get(f"{BASE_URL}/{pid}", timeout=5)

        if res.status_code == 404:
            print("Product not found.")
            log_error("lookup_product", "HTTPError", f"404 for ID {pid}")
        else:
            data = res.json()
            print(data["title"], "-", data["price"])

    except Exception as e:
        log_error("lookup_product", "Exception", str(e))


# -------------------- TASK 4 --------------------

# Trigger connection error intentionally
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except Exception as e:
    log_error("test_connection", "ConnectionError", str(e))

# Trigger 404 manually
try:
    res = requests.get(f"{BASE_URL}/999")
    if res.status_code != 200:
        log_error("test_404", "HTTPError", "Product ID 999 not found")
except Exception as e:
    log_error("test_404", "Exception", str(e))

# Print log file
print("\n--- ERROR LOG ---")
try:
    with open("error_log.txt", "r") as f:
        print(f.read())
except:
    print("No logs yet.")
