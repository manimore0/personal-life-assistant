from db import initialize_db

def main():
    print("=== STARTING APP ===")
    initialize_db()
    print("Personal Life Assistant CLI")

if __name__ == "__main__":
    main()