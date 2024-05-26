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
        # Obtiene la ruta del directorio actual
        current_dir = os.getcwd()
        
        # Navega al directorio del repositorio (si no estás allí)
        os.chdir("~/doncom/.dcprograms/rocket")
        
        # Actualiza las referencias locales a las ramas remotas
        subprocess.run(["git", "fetch"], check=True)

        # Mensaje de confirmación y explicación de consecuencias
        print(f"{COLOR_YELLOW}Atención: Esta acción sobrescribirá tus cambios locales con los cambios del repositorio remoto.{COLOR_RESET}")
        print("Esto puede resultar en la pérdida de trabajo no guardado.")

        confirmation1 = input("¿Estás seguro de continuar? (yes/no): ").strip().lower()

        if confirmation1 == "yes":
            confirmation2 = input("Por favor, confirma de nuevo. Escribe 'yes' para continuar: ").strip().lower()
            if confirmation2 == "yes":
                # Fusiona los cambios del repositorio remoto y sobrescribe los locales
                subprocess.run(["git", "reset", "--hard", "origin/main"], check=True)
                print(f"{COLOR_GREEN}Fusión exitosa sin confirmación del usuario.{COLOR_RESET}")
            else:
                print("Fusión cancelada. Confirmación no válida.")
        else:
            print("Fusión cancelada por el usuario.")

        # Vuelve al directorio original
        os.chdir(current_dir)

    except subprocess.CalledProcessError as e:
        print(f"{COLOR_YELLOW}Error al forzar la fusión: {e.stderr}{COLOR_RESET}")
    

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
