# easyAES

easyAES is just a [pyAES](https://github.com/ricmoo/pyaes/) wrapper.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install easyAES.

```bash
pip install easyAES
```

## Usage

```python
import easyAES

# Initilazes and gives a key to the AES class.
myAES = AES("password123")

# Encrypts a string and base64 encodes it.
crypter.encrypt("this a test")

# Decrypts a base64 encoded and crypted string.
crypter.decrypt("HvdQ/axD0T9zQQO9Q5Ch1jsIDZqdxLzZZD7Xtj3nzCY=")
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
Original code from [here](https://github.com/PaburoTC/AES/).
[MIT](https://choosealicense.com/licenses/mit/)
