# RemoteCMD


RemoteCMD is a Flask based web application that allows users to define custom commands via a web interface and execute those commands by accessing specific URLs.
The Main aim of this was to allow for triggering commands via sticker NFC tags to cross reference written notes with Digital notes (in my case obsidian) yes its a very weird edge case but one I find extremely useful. Beyond this it's extremely powerful in that any command can be run remotely via URL that the flask server is running on. 

> [!WARNING]
>
> **This application has no authentication protocols in place and as such is not advised to be used in a commercial environment - (This feature will be added in the future)**
> 
> 

## Features

- **Add Custom Commands:** Users can add new custom commands by specifying a URL and the required shell command.
- **Edit and Delete Commands:** Existing custom commands can be edited or deleted through the admin interface.
- **Execute Commands:** Custom commands can be triggered by accessing the associated URL, and the command output is returned as JSON.

## Installation

1. Clone the repository:

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python flaskcmd.py
   ```

2. Access the admin interface at `http://localhost:5000/admin` to manage custom commands. or  server IP e.g. http://yourserverIP:5000/admin

3. Add, edit, or delete custom commands as needed.

![image](https://github.com/syntacticallysound/Remote-CMD/assets/109209434/7ee137f9-2622-419d-9200-191fe3817c8d)


5. Trigger custom commands by accessing URLs corresponding to the defined commands from anywhere on your network either directly through the browser or get command on any device. If it is needed for remote triggering I recommend implementing a VPN such as tail scale 

7. Using the above as an example accessing anywhere on your network http://192.168.1.208/uninst will run appwiz.cpl via the command line which on windows will open your add and remove programs

### Obsidian Bookmarks

Open obsidian right click on any file and select copy obsidian URL this will give you something like 

![image](https://github.com/syntacticallysound/Remote-CMD/assets/109209434/98e2fc92-1e78-4982-a46e-b98e246675d1)


`obsidian://open?vault=Personal%20Knowledge%20Base&file=Programming%2FScript%20Implmentations%2FRemoteCMD`

in the URL field give it a path e.g.  page and paste the obsidian shortcut into the command field preceded by the word start then press update 

`start obsidian://open?vault=Personal%20Knowledge%20Base&file=Programming%2FScript%20Implmentations%2FRemoteCMD`

![image](https://github.com/syntacticallysound/Remote-CMD/assets/109209434/1dcce33a-a338-45e8-9d11-0180284b5965)


it will then add to the command list as seen below

![image](https://github.com/syntacticallysound/Remote-CMD/assets/109209434/4b0151e8-f679-4788-a5be-883d0401a077)


now the added command can be accessed from http://192.168.1.208/page will run the obsidian url opening obsidian to the specific page 

#### Web URLs 

To add the ability to trigger opening specific web URL e.g. YouTube 

**Windows**

`start www.yoururlhere.com`   

**Linux**

`$ xdg-open TARGETED_WEB_URL`

Mac

`open https://google.com`
`
This will open the URL in your default browser

### Configuring NFC Tags to work with RemoteCMD (IOS)


- Open iOS Shortcuts App

- Go to the Automation tab

- Create a new automation by tapping the ➕ icon

- Choose NFC

- Scan your NFC tag,  give it a name and click OK

- Select your run preference Run after confirmation or Run immediately

- Select Next

- Tap the ➕ icon

- Select New Blank Automation

- Select Add Action and search for URL

- Select Get Contents of URL ( This will trigger the URL without opening the browser)

- Enter the URL, in our example above it would be http://192.168.1.208/page

- click done

***Now when you scan your NFC card or sticker it will trigger the URL in the background performing the desired function on the flask server***

> [!NOTE]
> Android users will follow a similar procedure using a third party app such as macrodroid instructions will be created in the future 


## Project Structure

- **`flaskcmd.py`:** Python code for the Flask application, defining routes and database models.
- **`templates/admin.html`:** HTML template for the admin interface, allowing users to manage custom commands.
- **`custom_commands.db`:** SQLite database file storing custom commands.

## Dependencies

- Flask: Web framework for Python.
- Flask-SQLAlchemy: Flask extension for working with SQLAlchemy ORM.
- subprocess: Module for spawning new processes and executing shell commands.


