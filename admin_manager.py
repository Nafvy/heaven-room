import json

DATA_FILE = "data.json"

def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def show_list(data_type):
    data = load_data()
    print(f"\n=== {data_type.upper()} LIST ===")
    for i, item in enumerate(data[data_type], 1):
        print(f"{i}. {item['name']} - {item['role']}")
    print("")

def add_item(data_type):
    name = input(f"Masukkan nama {data_type[:-1]}: ")
    role = input(f"Masukkan role {data_type[:-1]}: ")
    data = load_data()
    data[data_type].append({"name": name, "role": role})
    save_data(data)
    print(f"{data_type[:-1].capitalize()} '{name}' berhasil ditambahkan.\n")

def remove_item(data_type):
    show_list(data_type)
    index = int(input(f"Masukkan nomor {data_type[:-1]} yang ingin dihapus: "))
    data = load_data()
    if 1 <= index <= len(data[data_type]):
        removed = data[data_type].pop(index-1)
        save_data(data)
        print(f"{data_type[:-1].capitalize()} '{removed['name']}' berhasil dihapus.\n")
    else:
        print("Nomor tidak valid.\n")

def main():
    while True:
        print("=== ADMIN & PARTNER MANAGER ===")
        print("1. Lihat Admin")
        print("2. Lihat Partner")
        print("3. Tambah Admin")
        print("4. Tambah Partner")
        print("5. Hapus Admin")
        print("6. Hapus Partner")
        print("7. Keluar")
        choice = input("Pilih menu: ")
        
        if choice == "1":
            show_list("admins")
        elif choice == "2":
            show_list("partners")
        elif choice == "3":
            add_item("admins")
        elif choice == "4":
            add_item("partners")
        elif choice == "5":
            remove_item("admins")
        elif choice == "6":
            remove_item("partners")
        elif choice == "7":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()
