## Run selenium chrome driver on ubuntu server

I needed to run a script to update the DNS records for my site on amen.pt. Since they don't have an API, I chose to create a selenium script using c# as it has a WAY easier setup than Java (never tried any other lang).

- First install dotnet on the machine, my project was made using .NET7
  ```
  sudo snap install dotnet-sdk --channel=7.0 --classic
  ```
This installs dotnet under the command name `dotnet-sdk.dotnet` so any command for dotnet must use this and not just dotnet, unless you make an `alias` which I didn;t because I already had another dotnet sdk version installed and I couldn't be bothered
- Since the google-chrome packages aren't available by default, we need to add it to the sources list
  ```
  wget https://dl-ssl.google.com/linux/linux_signing_key.pub
  sudo apt-key add linux_signing_key.pub
  rm linux_signing_key.pub
  sudo bash -c "echo ' deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list"
  sudo apt-get update
  ```
- Then get the google-chrome package
  ```
  sudo apt install google-chrome
  ```
  This installs the package, but if you try to run your code, it won't work as it looks for a display that you don't have. Trying running the command `google-chrome` would return something like this
  ```
  martinho@martinho:~/UpdateDNSAmen.pt/UpdateAmenDNSSelenium$ google-chrome
  [15226:15226:1201/224949.193881:ERROR:ozone_platform_x11.cc(239)] Missing X server or $DISPLAY
  [15226:15226:1201/224949.193914:ERROR:env.cc(255)] The platform failed to initialize.  Exiting.
  ```
- In order to be able to run, I've [found on the internet](https://stackoverflow.com/a/61043049) the `xvfb` package, it'll install a bunch of dependencies too.
  ```
  sudo apt-get install -y xorg xvfb gtk2-engines-pixbuf
  ```
  From what I understand, this package implements the X11 protocol server, without actually displaying the data out, allowing GUI apps to be ran but not allowing any input from the GUI.
  Then run this command to Make sure that Xvfb starts every time the box/vm is booted
  ```
  Xvfb -ac :99 -screen 0 1280x1024x16 &
  ```
  Output:
  ```
  export DISPLAY=:99
  [1] 16360
  ```
- After that, everything should be running. Now build and run the visual studio project
  ```
  dotnet-sdk.dotnet build UpdateAmenDNSSelenium.csproj

  dotnet-sdk.dotnet run UpdateAmenDNSSelenium.csproj
  ```
  With this, you also do not need to add the launch argument `--headless=new`, as Xvfb handles it. This was very cool as the login page of the website used ReCaptcha3 which blocks Selenium scripts if the headless argument is present!
