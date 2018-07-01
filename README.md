# Anonymous_chaser

To use this application, Plurk API 2.0 and Chrome driver is needed.

Plurk API 2.0 sign up: https://www.plurk.com/PlurkApp/register

Chrome driver: http://chromedriver.chromium.org/downloads

You also need a Plurk account to be the hound, better sign up for a new one.

Usage:

```
$pip install -r requirements.txt
```

```
$python hounds.py
```

or

```
$python kitty.py
```

reset blacklist:

```
$python reset.py
```

>Noted that the hound **only** finds post from someone's(master) friend.
>And the kitty finds post from your following.
>if the post doesn't appear in master's channel or from your following, this App won't work anymore.
>
>Enjoy until Plurk fix this configuration:)
