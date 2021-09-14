<h1>Quizizz Spammer</h1>

<h5>How do i get set up?</h1>


<p><strong>1.</strong> Using the Windows PowerShell</p>


Inside the windows powershell type the following commands line by line.

```
git clone https://github.com/M3Horizun/Quizizz-Flooder quizizz-flooder # <- Must have git installed
######
cd quizizz-flooder
######
notepad config.json # <- In here you edit the options to your preference.
######
python3 -m pip install -r requirements.txt
######
```

<p><strong>1.2</strong> Edit the pin, amount_of_bots & maximum-minutes to your preference</p>


<p>Once finished save the file and run the following command in the same powershell windows</p>

```
python3 main.py
```