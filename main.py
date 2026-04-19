import traceback
import sys

def main():
    try:
        x = 1 / 0
    except Exception as e:
        with open("xato.txt", "w") as f:
            traceback.print_exc(file=f)

if __name__ == "__main__":
    main()
```

Bunda, `try-except` bloki yordamida xato yuz beradigan kodni yozamiz. Xato paytida, `traceback.print_exc()` funksiyasi to‘liq stackni faylga yozadi. `with open("xato.txt", "w") as f:` qismi esa faylni ochib, unda xato stackini yozish uchun foydalanadi.
