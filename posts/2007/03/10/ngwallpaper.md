I started using Google Code project hosting for the **ngwallpaper** project. This Python script fetches the wallpaper of the day from the National Geographic website and sets it as your desktop wallpaper.

It currently works on Windows by leveraging Python Windows Extensions (using the `SETDESKTOPWALLPAPER` attribute from a Windows API call).

Future improvements include:
1. Making it platform-agnostic (support for Windows, Linux, and Mac).
2. Refactoring the code for better structure.
3. Implementing the program as a service or scheduled task.
4. Fixing the issue where the wallpaper resets after a few hours on Windows.
