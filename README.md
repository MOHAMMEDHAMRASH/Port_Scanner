# Port Scanner

This Python script allows you to perform port scanning on a specified target host.

## Usage

1. Make sure you have Python installed on your system.

2. Clone the repository to your local machine.

```bash
git clone https://github.com/<username>/<repository>.git
```

3. Navigate to the directory where the script is located.

```bash
cd <repository>
```

4. Run the script.

```bash
python port_scanner.py
```

5. Follow the prompts to enter the target IP/Domain and select the scan mode.

- Select 1 for scanning ports 1 to 1024.
- Select 2 for scanning ports 1 to 65535.
- Select 3 for custom port range scanning.
- Select 4 to exit the program.

If you choose custom port range scanning, you will be prompted to enter the starting and ending port numbers.

## Example

```bash
Enter Your IP/Domain: <target_IP>
Select your scan type:
[*] Select 1 for 1 to 1024 port scanning
[*] Select 2 for 1 to 65535 port scanning
[*] Select 3 for custom port scanning
[*] Select 4 to exit

[+] Select any option: 1
```

## Disclaimer

This tool is provided for educational and informational purposes only. Use responsibly and only on systems you have permission to scan. Unauthorized port scanning can be against the law and may result in legal consequences.

## Credits

Coded by [HAMRASH](https://github.com/HAMRASH)

## License

This project is licensed under the [MIT License](LICENSE).
