from imports import *
from constants import *
from defs import *

def ask_user_info():
    given_name = input("Nombre: ")
    sn = input("Apellido: ")
    user_password = input("Contraseña: ")

    while True:
        login_shell_input = input("¿Puede tener terminal? (yes/no): ").strip().lower()
        if login_shell_input == "yes":
            login_shell = "/bin/bash"
            break
        elif login_shell_input == "no":
            login_shell = "/bin/false"
            break
        else:
            print("Entrada inválida. Por favor, escriba 'yes' o 'no'.")

    uid = generate_username(given_name, sn)
    uid_number = get_next_uid()
    cn = f"{given_name} {sn}"
    display_name = cn
    home_directory = f"/home/{uid}"

    ldif_entry = create_ldif_entry(uid, sn, given_name, cn, display_name, uid_number, GID_NUMBER, user_password, login_shell, home_directory)
    save_ldif_file(ldif_entry, uid)

    return uid

def git_pull():
    try:
        result = subprocess.run(["git", "pull"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(f"{COLOR_GREEN}{result.stdout}{COLOR_RESET}")
    except subprocess.CalledProcessError as e:
        if "Your local changes to the following files would be overwritten by merge" in e.stderr:
            print(f"{COLOR_YELLOW}You have edited the folder. If you want to continue, we are going to force the changes so your changes will be deleted. Do you want to update knowing that you will lose your changes? (yes/no){COLOR_RESET}")
            choice = input().strip().lower()
            if choice == "yes":
                try:
                    subprocess.run(["git", "reset", "--hard"], check=True)
                    subprocess.run(["git", "pull"], check=True)
                    print(f"{COLOR_GREEN}Changes have been forced and repository updated.{COLOR_RESET}")
                except subprocess.CalledProcessError as inner_e:
                    print(f"{COLOR_YELLOW}Failed to update the repository: {inner_e}{COLOR_RESET}")
            else:
                print(f"{COLOR_YELLOW}Update canceled by user.{COLOR_RESET}")
        else:
            print(f"{COLOR_YELLOW}Failed to pull changes: {e.stderr}{COLOR_RESET}")
    

def main():
    parser = argparse.ArgumentParser(description="Rocket user management tool.")
    parser.add_argument("-u", "--update", action="store_true", help="Update the repository before running.")
    args = parser.parse_args()

    if args.update:
        git_pull()
        sys.exit()
    while True:
        uid = ask_user_info()
        print(f"{COLOR_GREEN}Archivo LDIF generado correctamente: {uid}.ldif{COLOR_RESET}")
        more_users = input("¿Desea agregar otro usuario? (yes/no): ").strip().lower()
        if more_users != "yes":
            break

if __name__ == "__main__":
    main()
