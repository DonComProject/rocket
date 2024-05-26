Sure, here's the README translated into English:

---

# Rocket

## Description
Rocket is a command-line tool (CLI) designed to simplify the creation and management of users in a Unix-like system. It allows generating LDIF (LDAP Data Interchange Format) files that can then be used for user creation on an LDAP server.

## Features
- Generation of users with basic information.
- Creation of LDIF files with user information.
- Customization of parameters such as password, login shell, and more.

## Requirements
- Python 3 installed on the system.
- Administrator access to execute some functions.

## Installation
1. Clone the Rocket repository from GitHub:
    ```bash
    git clone https://github.com/DonComProject/arenita && cd arenita/src/programs/rocket
    ```
2. Run the `rocket_setup.sh` script to set up the environment:
    ```bash
    chmod u+x rocket_setup.sh && ./rocket_setup.sh
    ```

## Usage
Once installed and configured, you can use Rocket by executing the `rocket` command followed by the desired options. For example:
```bash
rocket
```
This command will start the creation of a new user, following the instructions provided by the tool.

## Contribution
Contributions are welcome! If you wish to improve Rocket or report any issues, feel free to open an issue or send a pull request on the GitHub repository.

## License
This project is licensed under the MIT License. For more information, see the LICENSE file.

---

Feel free to adjust the README according to the specific needs of the project and your team's conventions.
