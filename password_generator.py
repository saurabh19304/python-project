"""Password generator CLI

Features:
- choose length
- include uppercase, lowercase, digits, symbols
- uses `secrets` for cryptographically secure randomness
- copies to clipboard when `pyperclip` is installed
"""
import secrets
import string


def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    pool = ""
    if use_lower:
        pool += string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_digits:
        pool += string.digits
    if use_symbols:
        pool += "!@#$%^&*()-_=+[]{};:,.<>?/"
    if not pool:
        raise ValueError("At least one character set must be selected")
    return "".join(secrets.choice(pool) for _ in range(length))


def main():
    print("Password Generator")
    try:
        length = int(input("Length (8-64) [12]: ") or 12)
    except ValueError:
        print("Invalid length, using 12")
        length = 12
    length = max(1, min(64, length))

    def ask(prompt, default=True):
        r = input(f"{prompt} [{'Y' if default else 'y'}/{'n' if default else 'N'}]: ").strip().lower()
        if r == "":
            return default
        return r[0] == "y"

    use_lower = ask("Include lowercase", True)
    use_upper = ask("Include uppercase", True)
    use_digits = ask("Include digits", True)
    use_symbols = ask("Include symbols", False)

    pwd = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
    print("\nGenerated password:\n", pwd)

    try:
        import pyperclip

        try:
            pyperclip.copy(pwd)
            print("(Copied to clipboard)")
        except Exception:
            print("(pyperclip present but failed to copy)")
    except Exception:
        print("(pyperclip not installed — install with: pip install pyperclip)")


if __name__ == "__main__":
    main()
